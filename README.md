# The Office — Org Chart

![GitHub last commit](https://img.shields.io/github/last-commit/chrisandrews1012/the-office-org-chart)
![GitHub repo size](https://img.shields.io/github/repo-size/chrisandrews1012/the-office-org-chart)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Stack](https://img.shields.io/badge/stack-Streamlit%20%7C%20SQLAlchemy%20%7C%20NetworkX%20%7C%20PostgreSQL-blue)

A Dunder Mifflin org chart builder with real database constraints, graph export, and full CRUD.

## Problem Statement

Managing a multi-tier organizational hierarchy isn't just a CRUD problem. The challenge is enforcing structural rules (executives have no supervisors, managers report to executives, employees report to managers) while handling edge cases like cascading deletes, subordinate reassignment, and preventing orphaned records. The goal was to build something that gets these constraints right at every layer.

## Approach

The hierarchy is modeled as three SQLAlchemy ORM tables (`SQLExecutive`, `SQLManager`, `SQLEmployee`) with foreign key relationships enforcing the reporting structure. Pydantic validates all input at the boundary before it touches the database. A custom decorator centralizes error handling and session rollback across every database operation.

NetworkX represents the org structure as a directed graph built directly from SQL query results, the same pattern used in dependency resolution and graph neural network pipelines. The graph can be exported as Cytoscape JSON for external visualization.

Streamlit ties it together as a multi-page app with full CRUD across all three employee tiers. A separate `build.py` script handles database initialization using bulk inserts in the correct dependency order.

## Results

| Tier | Reports To | Can Have Subordinates |
|---|---|---|
| Executive | | Managers |
| Manager | Executive | Employees |
| Employee | Manager | |

The app supports add, update, and delete for all three tiers, with optional subordinate reassignment on delete and live graph construction exportable to Cytoscape.

## How to Run

```bash
git clone https://github.com/chrisandrews1012/the-office-org-chart.git
cd the-office-org-chart
uv sync
cp .template.env .env  # fill in your database credentials
```

```bash
docker compose up -d
uv run python build.py rebuild
uv run streamlit run app.py
```

> **Note:** The Docker Compose network setup is currently being refined. Start the Streamlit app manually in a separate terminal for now.

**Tests**

```bash
uv run pytest tests/ -v --cov
```

## File Structure

```
the-office-org-chart/
├── app.py
├── build.py
├── docker-compose.yml
├── pyproject.toml
├── data/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   └── raw/
├── models/
├── notebooks/
├── reports/
│   └── figures/
├── src/
│   └── officegraph/
│       ├── config/
│       ├── handler/
│       ├── models/
│       ├── pages/
│       ├── ui/
│       └── utilities/
└── tests/
```

## License

This project is licensed under the [MIT License](LICENSE).
