import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=False)

ROOT_DIR = Path(__file__).parent.parent

BASE_URL: str = os.getenv("BASE_URL", "https://demoqa.com")
BROWSER: str = os.getenv("BROWSER", "chromium")
HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
SLOW_MO: int = int(os.getenv("SLOW_MO", "0"))

# "on_failure" | "always" | "off"
TRACE_MODE: str = os.getenv("TRACE_MODE", "on_failure")

BOOKSTORE_USERNAME: str = os.getenv("BOOKSTORE_USERNAME", "")
BOOKSTORE_PASSWORD: str = os.getenv("BOOKSTORE_PASSWORD", "")

ARTIFACTS_DIR = ROOT_DIR / "artifacts"
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
TRACES_DIR = ARTIFACTS_DIR / "traces"
LOGS_DIR = ROOT_DIR / "logs"
REPORTS_DIR = ROOT_DIR / "reports"

for _d in (SCREENSHOTS_DIR, TRACES_DIR, LOGS_DIR, REPORTS_DIR):
    _d.mkdir(parents=True, exist_ok=True)
