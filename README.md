# DemoQA Test Automation Framework

End-to-end test automation suite for [demoqa.com](https://demoqa.com) built with Python, Pytest, and Playwright.

## Tech stack

| Tool | Version |
|---|---|
| Python | 3.11+ |
| playwright | 1.44.0 |
| pytest | 8.2.2 |
| pytest-xdist | 3.5.0 (parallel) |
| pytest-html | 4.1.1 (reports) |
| pytest-rerunfailures | 14.0 (flaky retries) |

## Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install the package and all dependencies
pip install -e ".[dev]"

# Install the Playwright browser
playwright install chromium
```

Copy `.env.example` to `.env` and adjust as needed:

```bash
cp .env.example .env
```

## Running tests

```bash
# All tests, single process
pytest

# All tests, parallel (auto-detect CPU count)
pytest -n auto

# By marker
pytest -m smoke
pytest -m "elements and not regression"
pytest -m bookstore

# Headed mode (override .env)
HEADLESS=false pytest -m smoke
```

## Markers

| Marker | Scope |
|---|---|
| `smoke` | Quick framework sanity checks |
| `regression` | Full data-driven regression suite |
| `elements` | Elements section |
| `forms` | Forms section |
| `alerts` | Alerts, Frame & Windows section |
| `widgets` | Widgets section |
| `interactions` | Interactions section |
| `bookstore` | Book Store Application + API |

## Dual logging

Every test run produces two types of output simultaneously.

### 1. Custom step logs (txt)

One directory per run under `logs/run_YYYYMMDD_HHMMSS/`.
Each test gets its own `.txt` file with ISO-8601 timestamped lines:

```
2026-05-14 10:32:01.123 | INFO | STEP | Open Practice Form page
2026-05-14 10:32:02.456 | INFO | STEP | Fill first name with "John"
2026-05-14 10:32:03.789 | INFO | PASS | Confirmation modal displayed expected name
```

Step logs also record failure details and the paths of any screenshots or traces saved.

### 2. Playwright tracing

Traces are saved to `artifacts/traces/<test_name>.zip` on failure by default.
Control this with the `TRACE_MODE` environment variable:

- `on_failure` (default) — save trace only when a test fails
- `always` — save trace for every test
- `off` — disable tracing

**Opening a trace:**

```bash
playwright show-trace artifacts/traces/<test_name>.zip
```

### Verbose API logs

To enable Playwright's low-level API request/response logging:

```bash
DEBUG=pw:api pytest -m smoke
```

## Reports

After a run, open `reports/report.html` in a browser for the self-contained pytest-html report.
Screenshots of failed tests are embedded in the report.

## Project structure

```
├── config/          # Settings loaded from .env
├── core/            # BasePage, StepLogger, ad-blocker
├── pages/           # Page Object Model (mirrors DemoQA sections)
├── tests/           # Test files (mirrors pages/ structure)
├── test_data/       # Data factories and datasets
├── reports/         # pytest-html output (gitignored)
├── logs/            # Per-run step logs (gitignored)
└── artifacts/       # Screenshots, traces (gitignored)
```

## Book Store — first-run note

The Book Store tests create a throw-away user via the DemoQA Account API.
On the very first run the user is created automatically.
If you want to pin credentials across runs, set `BOOKSTORE_USERNAME` and
`BOOKSTORE_PASSWORD` in `.env` (observe DemoQA's password policy:
8+ chars, at least one uppercase letter, one digit, one special character).
