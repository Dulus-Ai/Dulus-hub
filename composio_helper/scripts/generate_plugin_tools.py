"""Generate completed plugin_tool.py files for Dulus-hub Composio plugins."""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "plugins" / "composio_notion"))
from composio_plugin.tool_generator import generate_plugin_tool_py
from composio_plugin.session_manager import list_tools

NOTION_SLUGS = [
    "NOTION_ADD_MULTIPLE_PAGE_CONTENT",
    "NOTION_ADD_PAGE_CONTENT",
    "NOTION_APPEND_BLOCK_CHILDREN",
    "NOTION_ARCHIVE_NOTION_PAGE",
    "NOTION_CREATE_COMMENT",
    "NOTION_CREATE_DATABASE",
    "NOTION_CREATE_NOTION_PAGE",
    "NOTION_DELETE_BLOCK",
    "NOTION_DUPLICATE_PAGE",
    "NOTION_FETCH_BLOCK_CONTENTS",
    "NOTION_FETCH_BLOCK_METADATA",
    "NOTION_FETCH_COMMENTS",
    "NOTION_FETCH_DATA",
    "NOTION_FETCH_DATABASE",
    "NOTION_FETCH_ROW",
    "NOTION_GET_ABOUT_ME",
    "NOTION_GET_ABOUT_USER",
    "NOTION_GET_PAGE_PROPERTY_ACTION",
    "NOTION_INSERT_ROW_DATABASE",
    "NOTION_LIST_USERS",
    "NOTION_QUERY_DATABASE",
    "NOTION_RETRIEVE_COMMENT",
    "NOTION_RETRIEVE_DATABASE_PROPERTY",
    "NOTION_SEARCH_NOTION_PAGE",
    "NOTION_UPDATE_BLOCK",
    "NOTION_UPDATE_PAGE",
    "NOTION_UPDATE_ROW_DATABASE",
    "NOTION_UPDATE_SCHEMA_DATABASE",
]

HUBSPOT_SLUGS = [
    # Core CRM
    "HUBSPOT_CREATE_CONTACT",
    "HUBSPOT_CREATE_COMPANY",
    "HUBSPOT_CREATE_DEAL",
    "HUBSPOT_CREATE_TICKET",
    "HUBSPOT_CREATE_PRODUCT",
    "HUBSPOT_CREATE_EMAIL",
    # Read
    "HUBSPOT_FETCH_CONTACT_DETAILS_BY_ID",
    "HUBSPOT_HUBSPOT_READ_CONTACT",
    "HUBSPOT_HUBSPOT_GET_COMPANY",
    "HUBSPOT_HUBSPOT_GET_DEAL",
    "HUBSPOT_GET_TICKET",
    "HUBSPOT_GET_PRODUCT",
    # List
    "HUBSPOT_LIST_CONTACTS_PAGE",
    "HUBSPOT_HUBSPOT_LIST_CONTACTS",
    "HUBSPOT_HUBSPOT_LIST_COMPANIES",
    "HUBSPOT_HUBSPOT_LIST_DEALS",
    "HUBSPOT_LIST_TICKETS",
    "HUBSPOT_GET_PRODUCTS",
    # Search
    "HUBSPOT_HUBSPOT_SEARCH_COMPANIES",
    "HUBSPOT_HUBSPOT_SEARCH_DEALS",
    "HUBSPOT_CUSTOMIZABLE_CONTACTS_PAGE_RETRIEVAL",
    # Update
    "HUBSPOT_HUBSPOT_UPDATE_CONTACT",
    "HUBSPOT_HUBSPOT_UPDATE_COMPANY",
    "HUBSPOT_HUBSPOT_UPDATE_DEAL",
    "HUBSPOT_PARTIALLY_UPDATE_TICKET_BY_ID",
    # Archive
    "HUBSPOT_ARCHIVE_CONTACT_BY_ID",
    "HUBSPOT_ARCHIVE_COMPANY",
    "HUBSPOT_HUBSPOT_ARCHIVE_DEALS",
    "HUBSPOT_ARCHIVE_TICKET",
    "HUBSPOT_ARCHIVE_PRODUCT",
    # Batch
    "HUBSPOT_CREATE_BATCH_OF_CONTACTS",
    "HUBSPOT_CREATE_A_BATCH_OF_COMPANIES",
    "HUBSPOT_CREATE_BATCH_OF_DEALS",
    "HUBSPOT_CREATE_BATCH_OF_TICKET",
    # Merge
    "HUBSPOT_MERGE_TWO_CONTACTS_OF_SAME_TYPE",
    "HUBSPOT_MERGE_TWO_COMPANIES_OF_SAME_TYPE",
    "HUBSPOT_MERGE_TWO_DEALS_OF_SAME_TYPE",
    # Workflows
    "HUBSPOT_GET_ALL_WORKFLOWS",
    "HUBSPOT_GET_WORKFLOW_BY_ID",
    "HUBSPOT_CREATE_WORKFLOW",
    "HUBSPOT_DELETE_WORKFLOW",
    # Campaigns
    "HUBSPOT_CAMPAIGN_SEARCH",
    "HUBSPOT_GET_CAMPAIGN",
]


def build_tool_defs(toolkit: str, wanted_slugs: list[str]) -> list[dict]:
    all_tools = {t["slug"]: t for t in list_tools(toolkit)}
    defs = []
    missing = []
    for slug in wanted_slugs:
        t = all_tools.get(slug)
        if not t:
            missing.append(slug)
            continue
        schema = t.get("input_schema") or {}
        defs.append({
            "slug": slug,
            "description": t.get("description", f"Execute {slug}"),
            "schema": schema,
        })
    return defs, missing


def generate_for_plugin(plugin_name: str, toolkit: str, wanted_slugs: list[str]):
    plugin_dir = ROOT / "plugins" / plugin_name
    output_path = plugin_dir / "plugin_tool.py"
    defs, missing = build_tool_defs(toolkit, wanted_slugs)
    generate_plugin_tool_py(defs, output_path)
    print(f"{plugin_name}: wrote {len(defs)} tools to {output_path}")
    if missing:
        print(f"{plugin_name}: missing {len(missing)} slugs: {missing}")
    return defs, missing


if __name__ == "__main__":
    generate_for_plugin("composio_notion", "notion", NOTION_SLUGS)
    generate_for_plugin("composio_hubspot", "hubspot", HUBSPOT_SLUGS)
