import glob
import logging
import sys
import time
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tkinter import filedialog

import pandas as pd

from pdf2excel import __version__
from pdf2excel.tasks import process_pdf


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

        # run tasks in parallel using max of 8 threads
        t0 = time.perf_counter()
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = pool.map(process_pdf, files)
        invoice_data = list(results)
        # generate output for invoices
        df = pd.DataFrame(invoice_data)
        df.to_excel(
            "invoice_summary.xlsx",
            index=False,
            columns=[
                "bill_to",
                "vendor_name",
                "address",
                "sv_barcode",
                "audit_period",
                "claim_no",
                "claim_date",
                "claim_amount",
                "claim_code",
                "description",
                "region",
                "category",
            ],
            header=[
                "Bill_To",
                "Vendor_Name",
                "Address",
                "SV_Barcode",
                "Audit_Period",
                "Claim_No",
                "Claim_Date",
                "Claim_Amount",
                "Claim_Code",
                "Description",
                "Region",
                "Category",
            ],
        )
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
