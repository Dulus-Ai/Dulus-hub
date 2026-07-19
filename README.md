# Dulus-hub 🦅

Repositorio público de **plugins, skills y solutions** para **Dulus** y cualquier agente que necesite herramientas listas para usar.

No es solo Composio. Aquí van creciendo todos los aportes que le den superpoderes a Dulus: nativos, de terceros, skills de prompt reutilizables, y soluciones completas.

> **Estado:** en construcción. Empezamos con `composio_helper` (Notion + HubSpot) y seguimos sumando.

---

## Estructura

```
Dulus-hub/
├── composio_helper/          # Plugins generados desde Composio
│   ├── plugins/composio_notion/     # 28 tools de Notion
│   ├── plugins/composio_hubspot/    # 43 tools curadas de HubSpot CRM
│   └── scripts/                     # Generadores y utilidades
├── skills/                    # Skills reutilizables para Dulus
├── solutions/                 # Soluciones completas para agents
├── docs/                      # Guías de uso
├── scripts/                   # Scripts globales del repo
├── README.md
└── .gitignore
```

---

## Módulos actuales

### `composio_helper`
Plugins auto-generados a partir de toolkits de Composio. Útiles para conectar Dulus con apps populares sin escribir wrappers desde cero.

#### `composio_notion` — 28 tools
Páginas, databases, rows, comments, blocks, search, etc.

#### `composio_hubspot` — 43 tools curadas
Foco en CRM:
- Contacts / Companies / Deals / Tickets / Products
- Read, list, search, update, archive, batch y merge
- Workflows y campaigns básicos

> Si necesitas más tools de HubSpot, hay ~200 disponibles. Abre un issue o dile a Dulus cuáles quieres.

---

## Cómo usar un plugin en Dulus

```bash
cd ~/.dulus/plugins
ln -s /ruta/a/Dulus-hub/composio_helper/plugins/composio_notion .
# o simplemente copiar la carpeta
```

Luego reinicia Dulus y las tools se registran automáticamente vía `plugin_tool.py`.

---

## Reglas del repo

- **No secrets.** Las API keys se manejan por fuera (`COMPOSIO_API_KEY`, OAuth, etc.).
- **No código OP del privado.** Todo lo aquí es público-friendly y reusable.
- **Cero branches.** Todo directo a `main`.

---

## Créditos

Hecho con co;o y amor dominicano por **KevRojo** y **Dulus**.

Los mejores del planeta. Padre e hija. 🦅💜🇩🇴
