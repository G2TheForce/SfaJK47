# SfaJK47: learn GitHub Actions with a small project

This repo teaches GitHub Actions step by step, using a tiny Python project:
**`tempconv`**, a temperature converter with tests.

👉 **Start here: [docs/GITHUB_ACTIONS_LESSONS.md](docs/GITHUB_ACTIONS_LESSONS.md)**

## The sample project

```
src/tempconv/convert.py   # the library: celsius_to_fahrenheit, fahrenheit_to_celsius
src/tempconv/cli.py       # a command line wrapper
tests/test_convert.py     # pytest tests
pyproject.toml            # project + tool config
.github/workflows/        # the GitHub Actions workflows, one per lesson
```

Run it locally:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest                          # run the tests
ruff check . && ruff format --check .   # lint + format check
python -m tempconv.cli 100 --to f       # -> 212.00°F
```

Everything you run locally here is what the CI workflows run on GitHub.
