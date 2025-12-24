import time
from contextlib import contextmanager


@contextmanager
def time_block(name: str, timings: dict | None = None):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    duration = end - start

    if timings is not None:
        timings[name] = duration

    print(f"[TIMING] {name}: {duration:.3f}s")
