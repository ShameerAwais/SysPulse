## Branching Strategy

- `main`: Stable production-ready code
- `dev`: Integration branch
- `feature/*`: One feature per branch (e.g., `feature/metrics-endpoint`)

## Workflow

1. Create feature branch from `dev`
2. Push code and open a Pull Request (PR) into `dev`
3. PR must pass CI and be reviewed before merge

## Code Style

- Python: Follow PEP8 (use flake8)
- Bash: Use shellcheck for scripts
