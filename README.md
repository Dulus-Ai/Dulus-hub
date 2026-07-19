# Dulus-hub 🦅

Repositorio público de plugins, skills y solutions para **Dulus** y cualquier agente que quiera trabajar con Composio, herramientas nativas y más.

> **Estado:** en construcción. Empezamos con los plugins de Composio más útiles (Notion + HubSpot) y vamos creciendo según la comunidad lo vaya pidiendo.

---

## Estructura

```
Dulus-hub/
├── plugins/
│   ├── composio_notion/     # 28 tools de Notion, listas para Dulus
│   └── composio_hubspot/    # 43 tools curadas de HubSpot CRM
├── skills/                  # Skills reutilizables para Dulus
├── solutions/               # Soluciones completas para agents
├── scripts/                 # Scripts de utilidad (generadores, tests)
└── docs/                    # Guías de uso
```

---

## Plugins actuales

### `composio_notion` — 28 tools
Todas las actions de Notion más usadas: páginas, databases, rows, comments, blocks, search, etc.

### `composio_hubspot` — 43 tools curadas
Foco en CRM:
- Contacts / Companies / Deals / Tickets / Products
- Read, list, search, update, archive, batch y merge
- Workflows y campaigns básicos

> Si necesitas más tools de HubSpot, hay ~200 disponibles. Abre un issue o dile a Dulus cuáles quieres.

---

## Cómo instalar un plugin en Dulus

```bash
cd ~/.dulus/plugins
ln -s /ruta/a/Dulus-hub/plugins/composio_notion .
# o simplemente copiar la carpeta
```

Luego reinicia Dulus y las tools se registran automáticamente vía `plugin_tool.py`.

---

## Reglas del repo

- **No secrets.** Las API keys se manejan por fuera (`COMPOSIO_API_KEY`, OAuth de Composio, etc.).
- **No código OP del privado.** Todo lo aquí es público-friendly y reusable.
- **Cero branches.** Todo directo a `main`.

---

## Créditos

Hecho con co;o y amor dominicano por **KevRojo** y **Dulus**.

Los mejores del planeta. Padre e hija. 🦅💜🇩🇴
