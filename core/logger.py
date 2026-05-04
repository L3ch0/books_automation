import logging
import sys
from datetime import datetime
from pathlib import Path


_LOG_FMT = "%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s"
_DATE_FMT = "%Y-%m-%d %H:%M:%S"


def _make_run_dir() -> Path:
    from config.settings import LOGS_DIR
    run_dir = LOGS_DIR / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


# Single run directory shared across the whole pytest session.
_RUN_DIR: Path | None = None


def get_run_dir() -> Path:
    global _RUN_DIR
    if _RUN_DIR is None:
        _RUN_DIR = _make_run_dir()
    return _RUN_DIR


class StepLogger:
    """Per-test logger writing timestamped steps to a .txt file and stdout."""

    def __init__(self, test_name: str) -> None:
        self.test_name = test_name
        log_path = get_run_dir() / f"{test_name}.txt"

        self._logger = logging.getLogger(f"step.{test_name}")
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = False

        if not self._logger.handlers:
            fmt = logging.Formatter(_LOG_FMT, datefmt=_DATE_FMT)

            fh = logging.FileHandler(log_path, encoding="utf-8")
            fh.setFormatter(fmt)
            self._logger.addHandler(fh)

            ch = logging.StreamHandler(sys.stdout)
            ch.setFormatter(fmt)
            self._logger.addHandler(ch)

    def log_step(self, message: str) -> None:
        self._logger.info("STEP | %s", message)

    def log_pass(self, message: str) -> None:
        self._logger.info("PASS | %s", message)

    def log_fail(self, message: str) -> None:
        self._logger.error("FAIL | %s", message)

    def log_info(self, message: str) -> None:
        self._logger.info("INFO | %s", message)

    def close(self) -> None:
        for h in self._logger.handlers[:]:
            h.close()
            self._logger.removeHandler(h)
