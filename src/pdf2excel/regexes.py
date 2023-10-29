import re

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
    r"(?P<inv_nbr>\w+)\s*"
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

invoice_page_pat = re.compile(
    r"BILL TO:\s*(?P<bill_to>\w+)\s*"
    r"SV Barcode:\s*(?P<sv_barcode>\w+)\s*"
    r"(?P<vendor_name>.*)\s* Audit Period:\s*(?P<audit_period>[0-9-]+)\s*"
    r"(?P<address_1>.*)\s*Claim:\s*(?P<claim_no>\w+)\s*"
    r"(?P<address_2>.*)\s*Date:\s(?P<claim_date>\d{1,2}/\d{1,2}/\d{2,4})\s*"
    r"Claim Amount\s*\$\s*(?P<claim_amount>[0-9.,]+)\s*"
    r"Claim Code\s*(?P<claim_code>[a-zA-Z0-9.]+)\s*"
    r"Description\s*(?P<description>.*)\s*"
    r"Region\s*(?P<region>.*)\s*"
    r"Category\s*(?P<category>.*)"
)
