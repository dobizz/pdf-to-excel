import glob
import logging
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from pdf2excel import __version__
from pdf2excel.tasks import process_pdf


def main():
    logging.info(f"pdf2excel v{__version__}")
    try:
        # search for pdf files in current directory
        logging.info("Searching for *.pdf files in current directory")
        files = [Path(file) for file in glob.glob("*.pdf")]
        file_count = len(files)
        for file in files:
            logging.info(file.name)
        logging.info(f"Found ({file_count}) files to process")

        # prompt user to continue as files might be too many
        input("\n[Press ENTER to continue]\n")

        # run tasks in parallel using max of 8 threads
        t0 = time.perf_counter()
        with ThreadPoolExecutor(max_workers=8) as pool:
            pool.map(process_pdf, files)
        t1 = time.perf_counter()

        # show metrics
        run_time = t1 - t0
        logging.info(
            f"Processed {file_count} files in {run_time:0.3f} seconds.",
        )

    except KeyboardInterrupt:
        logging.warning("Terminating with CTRL+C")

    except Exception as e:
        logging.error(f"Uncaught Exception {e}")

    finally:
        input("\n[Press ENTER to exit]")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",  # noqa
        datefmt="%d/%b/%Y %H:%M:%S",
        stream=sys.stdout,
    )
    main()
