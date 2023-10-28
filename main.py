import glob
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import pandas as pd
import pdfplumber


@dataclass
class Row:
    PO_Nbr: str
    PO_Data: datetime
    Inv_Nbr: str
    Rcv_Date: datetime
    Rcv_Wgt: float
    Paid_Net: float
    PO_Net: float
    Paid_List: float
    Frt_Allow: int


# regex patterns
core_pat = re.compile(
    r"Claim\s+Example\s+(.*?)\s+(?:Page \d+|Total for)",
    re.DOTALL,
)

head_pat = re.compile(
    r"Division:\s*(?P<division>\d+)\s*"
    r"SV Item#:\s*(?P<sv_item_no>\d+)\s*"
    r"UPC:\s*(?P<upc>\d+)\s*"
    r"Desc:\s*(?P<desc>.+)\s*"
    r"Pack:\s*(?P<pack>\d+)\s*"
    r"Size:\s*(?P<size>[0-9.,]+)\s*"
    r"(?P<example>\w+)"
)

entry_pat = re.compile(
    r"(?P<po_nbr>\d+)\s*"
    r"(?P<po_date>\d{1,2}/\d{1,2}/\d{2,4})\s*"
    r"(?P<inv_nbr>\d+)\s*"
    r"(?P<inv_date>\d{1,2}/\d{1,2}/\d{2,4})\s*"
    r"(?P<rcv_date>\d{1,2}/\d{1,2}/\d{2,4})\s*"
    r"(?P<rcv_wgt>[0-9.,]+)\s*"
    r"(?P<paid_net>[0-9.,]+)\s*"
    r"(?P<po_net>[0-9.,]+)\s*"
    r"(?P<paid_list>[0-9.,]+)\s*"
    r"(?P<frt_allow>[0-9.,]+)\s*"
    r"(?P<po_list>[0-9.,]+)\s*"
    r"(?P<po_paid_variance>[0-9.,]+)\s*"
    r"(?P<rcv_qty>\d+)\s*?"
    r"(?P<prior_billed>[0-9.,]*)\s*?"
    r"(?P<claim>[0-9.,]+)\s*"
)


def process_pdf(path: Path):
    print(f"Processing file {path}")

    # extract lines
    with pdfplumber.open(path) as pdf:
        all_lines = []
        for page in pdf.pages:
            text = page.extract_text(keep_blank_chars=True)
            core = re.search(core_pat, text)
            if not core:
                continue
            core = core.group(1)
            lines = core.split("\n")
            all_lines.extend(lines)

    # build groups
    heads = []
    entries = []
    for line in all_lines:
        head_search = head_pat.search(line)
        entry_search = entry_pat.search(line)
        if head_search:
            head = head_search.groupdict()
            heads.append(head)
        if entry_search:
            entry = entry_search.groupdict()
            entries.append(entry)

    # write output
    df1 = pd.DataFrame(heads)
    df2 = pd.DataFrame(entries)
    df1.to_excel(
        path.stem + "_extraction_1_.xlsx",
        index=False,
        header=[
            "Division",
            "SV_Item",
            "UPC",
            "Desc",
            "Pack",
            "Size",
            "Example",
        ],
    )
    df2.to_excel(
        path.stem + "_extraction_2_.xlsx",
        index=False,
        header=[
            "PO_Nbr",
            "PO_Date",
            "Inv_Nbr",
            "Inv_Date",
            "Rcv_Date",
            "Rcv_Wgt",
            "Paid_Net",
            "PO_Net",
            "Paid_List",
            "Frt_Allow",
            "PO_List",
            "PO_Paid_Variance",
            "Rcv_Qty",
            "Prior_Billed",
            "Claim",
        ],
    )


def main():
    paths = [Path(file) for file in glob.glob("*/*.pdf", recursive=True)]
    print(f"Found ({len(paths)}) files: {paths}")
    input("\n<Press ENTER to continue>\n")
    for path in paths:
        process_pdf(path)


if __name__ == "__main__":
    t0 = time.perf_counter()
    main()
    t1 = time.perf_counter()
    print(f"\nDone in {t1 - t0:0.3f} seconds")
