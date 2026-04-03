import time
from pipeline import run_pipeline

def performance_test(lines):
    start = time.time()
    run_pipeline(lines)
    end = time.time()

    print("Processing Time:", end - start, "seconds")