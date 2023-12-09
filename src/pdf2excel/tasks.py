import logging
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import List

import pandas as pd
import pdfplumber

from pdf2excel.regexes import core_pat, entry_pat, head_pat, invoice_page_pat


def process_invoice_page(text: str) -> dict:
    """
    Process the invoce page and parse the needed data

    Args:
        text (str): text of invoce page

    Returns:
        dict: dictionary of field values
    """
    res = invoice_page_pat.search(text)
    if res is None:
        return {}
    data = res.groupdict()
    address = [
        data.pop("address_1"),
        data.pop("address_2"),
    ]
    address = " ".join(address).strip()
    data["address"] = address
    return data


def process_pdf(path: Path) -> dict:
    """
    Run extraction on PDF file in path

    Args:
        path (Path): path to PDF file

    Returns:
        dict: dictionary of field values found in first page.
    """
    logging.info(f"Processing file {path}")

    # extract lines from pdf
    with pdfplumber.open(path) as pdf:
        all_lines = []
        for idx, page in enumerate(pdf.pages):
            text = page.extract_text(keep_blank_chars=True)
            if idx == 0:
                invoice_data = process_invoice_page(text)
                continue
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
    return invoice_data


def process_1(files: List[Path], max_workers: int = 8) -> dict:
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
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

if __name__ == "__main__":
    deal_sheet_type = re.compile(
        r"Deal\s*Sheet\s*Type:\s*(?P<deal_sheet_type>\w*)"
    )
    path = Path("loms/99P6537373-LOMS.pdf")
    with pdfplumber.open(path) as pdf:
        all_lines = []
        for idx, page in enumerate(pdf.pages):
            text = page.extract_text(keep_blank_chars=True)
            res=deal_sheet_type.findall(text)
            if res:
                # dst=res.groupdict()
                # print(dst)
                print(res)
            breakpoint