"""Session manager for Composio (composio 1.0 SDK — stateless, no sessions).

The old `Composio().create(user_id, toolkits, manage_connections)` session API
no longer exists. The 1.0 SDK is stateless: you call
`client.tools.execute(tool_slug, arguments=..., user_id=...)` per call. We keep a
thin `_Session` shim so existing callers (`get_or_create_session(...).execute(...)`)
keep working without a rewrite.
"""
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

_composio_client = None


def _load_api_key() -> str:
    """Composio key from env or Dulus config — DECRYPTED (config stores it enc:)."""
    key = os.environ.get("COMPOSIO_API_KEY", "").strip()
    if key:
        return key
    # Dulus config goes through load_config() which decrypts enc: values.
    try:
        from config import load_config
        k = (load_config().get("composio_api_key") or "").strip()
        if k and not k.startswith("enc:"):
            return k
    except Exception:
        pass
    for cfg_path in (Path.home() / ".dulus" / "config.json",
                     Path.home() / ".falcon" / "config.json"):
        if cfg_path.exists():
            try:
                k = (json.loads(cfg_path.read_text(encoding="utf-8")).get("composio_api_key") or "").strip()
                if k and not k.startswith("enc:"):
                    return k
            except Exception:
                pass
    return ""


def get_client():
    """Return the Composio HTTP client (has .tools, .toolkits, .connected_accounts)."""
    global _composio_client
    if _composio_client is not None:
        return _composio_client
    key = _load_api_key()
    if not key:
        raise RuntimeError("COMPOSIO_API_KEY not found. Run `/skill composio connect`.")
    os.environ["COMPOSIO_API_KEY"] = key
    from composio import Composio
    _composio_client = Composio(api_key=key).client
    return _composio_client


class _Session:
    """Stateless shim — the 1.0 SDK has no sessions; execute is per-call."""

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.session_id = user_id
        self.client = get_client()

    def execute(self, tool_slug: str, arguments: Optional[Dict[str, Any]] = None, **_kw):
        return self.client.tools.execute(
            tool_slug, arguments=arguments or {}, user_id=self.user_id
        )


def get_or_create_session(user_id: str, toolkits: List[str], connected_accounts=None):
    """Compat: returns a stateless session bound to user_id (toolkits unused now)."""
    return _Session(user_id)


def list_tools(toolkit_slug: str, limit: int = 200) -> List[Dict[str, Any]]:
    """List a toolkit's tools with their JSON-schema input parameters."""
    client = get_client()
    resp = client.tools.list(toolkit_slug=toolkit_slug, limit=str(limit))
    items = getattr(resp, "items", None)
    if items is None and isinstance(resp, dict):
        items = resp.get("items", [])
    out = []
    for t in items or []:
        d = t if isinstance(t, dict) else (t.model_dump() if hasattr(t, "model_dump") else {})
        out.append({
            "slug": d.get("slug") or d.get("name", ""),
            "name": d.get("name", ""),
            "description": d.get("description", ""),
            "input_schema": d.get("input_parameters") or d.get("input_schema") or {},
        })
    return [t for t in out if t["slug"]]


def list_accounts() -> List[Dict[str, Any]]:
    """List connected accounts (for status / which apps are authorized)."""
    client = get_client()
    try:
        accounts = client.connected_accounts.list()
        items = getattr(accounts, "items", accounts) or []
    except Exception:
        return []
    result = []
    for acc in items:
        d = acc if isinstance(acc, dict) else (acc.model_dump() if hasattr(acc, "model_dump") else {})
        tk = d.get("toolkit")
        result.append({
            "id": d.get("id", "N/A"),
            "toolkit": tk.get("slug", "N/A") if isinstance(tk, dict) else (tk or "N/A"),
            "status": d.get("status", "N/A"),
        })
    return result
