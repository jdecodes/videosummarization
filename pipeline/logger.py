import time
from contextlib import contextmanager
from datetime import datetime
from typing import Dict, Optional

class Logger:
    def __init__(self):
        self.timings: Dict[str, float] = {}

    def _timestamp(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    def info(self, message: str):
        print(f"[{self._timestamp()}] [INFO] {message}")

    def warn(self, message: str):
        print(f"[{self._timestamp()}] [WARN] {message}")

    def error(self, message: str):
        print(f"[{self._timestamp()}] [ERROR] {message}")

    @contextmanager
    def timed(self, name: str):
        self.info(f"START {name}")
        start = time.perf_counter()
        try:
            yield
        finally:
            duration = time.perf_counter() - start
            self.timings[name] = duration
            self.info(f"END {name} ({duration:.3f}s)")

    def dump_timings(self):
        self.info("=== PIPELINE TIMINGS ===")
        for name, duration in self.timings.items():
            self.info(f"{name:20s}: {duration:.3f}s")
