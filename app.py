import glob
import logging
import sys
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

from pdf2excel import __version__
from pdf2excel.tasks import process_1


def main(directory: str):
    logging.info(f"pdf2excel v{__version__}")
    try:
        # search for pdf files in current directory
        logging.info(f"Searching for *.pdf files in {directory}")
        files = [Path(file) for file in glob.glob("*.pdf")]
        file_count = len(files)
        for file in files:
            logging.info(file.name)
        logging.info(f"Found ({file_count}) files to process")

        # prompt user to continue as files might be too many
        input("\n[Press ENTER to continue]\n")

        t0 = time.perf_counter()
        process_1(files=files)
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
    # create tk instance and hide root panel
    root = tk.Tk()
    root.withdraw()
    # prompt user for directory to search for files
    directory = filedialog.askdirectory(
        title="Select dir to search for PDF files",
    )
    # run main routine
    main(directory=directory)
