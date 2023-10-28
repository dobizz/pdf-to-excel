import glob
import time
from pathlib import Path

from pdf2excel.tasks import process_pdf


def main():
    paths = [Path(file) for file in glob.glob("*.pdf")]
    print(f"Found ({len(paths)}) files: {paths}")
    input("\n<Press ENTER to continue>\n")
    for path in paths:
        process_pdf(path)


if __name__ == "__main__":
    t0 = time.perf_counter()
    main()
    t1 = time.perf_counter()
    print(f"\nDone in {t1 - t0:0.3f} seconds")
