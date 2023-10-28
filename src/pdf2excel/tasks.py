import logging
import re
from pathlib import Path

import pandas as pd
import pdfplumber

from pdf2excel.regexes import core_pat, entry_pat, head_pat


def process_pdf(path: Path) -> None:
    """
    Run extraction on PDF file in path

    Args:
        path (Path): path to PDF file
    """
    logging.info(f"Processing file {path}")

    # extract lines from pdf
    with pdfplumber.open(path) as pdf:
        all_lines = []
        for page in pdf.pages:
            text = page.extract_text(keep_blank_chars=True)
            # skip page if does not match core pattern
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
        # use regex to search line for data
        head_search = head_pat.search(line)
        entry_search = entry_pat.search(line)
        # save data from line (if found) to respective group
        if head_search:
            head = head_search.groupdict()
            heads.append(head)
        if entry_search:
            entry = entry_search.groupdict()
            entries.append(entry)

    # write output to excel file(s)
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
