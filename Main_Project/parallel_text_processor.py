from concurrent.futures import ProcessPoolExecutor
from module.scorer import process_batch

def parallel_process(lines, workers=4, batch_size=5000):
    batches = [lines[i:i+batch_size] for i in range(0, len(lines), batch_size)]
    results = []

    with ProcessPoolExecutor(max_workers=workers) as executor:
        output = executor.map(process_batch, batches)

    for r in output:
        results.extend(r)

    return results