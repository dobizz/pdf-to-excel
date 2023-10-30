import pytest


@pytest.fixture
def invalid_page() -> str:
    return "Blank Page"


@pytest.fixture
def valid_page() -> str:
    text = "Some company text\nPO Nbr PO Date Inv Nbr Inv Date Rcv Date Rcv Wgt Net Net List Allow List Variance Qty Billed Claim Example\nDivision: 096 SV Item#: 001904102 UPC: 79249301625 Desc: 1111796   BLOCK WHITENER 4/1 Pack: 1 Size: 4    GA\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 40.55 36.86 40.55 0.00 36.86 3.69 251 926.19\nSub Total = 926.19\nDivision: 096 SV Item#: 001904108 UPC: 79249300176 Desc: 1114159   SUPER SOAK CONCENT Pack: 1 Size: 3    GA\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 72.78 66.15 72.78 0.00 66.15 6.63 40 265.20\nSub Total = 265.20\nDivision: 096 SV Item#: 001904109 UPC: 79249302315 Desc: 1114111   KAY STNLSS CLNER P Pack: 1 Size: 6    QT\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 36.19 32.84 36.19 0.00 32.84 3.35 8 26.80\nSub Total = 26.80\nDivision: 096 SV Item#: 001904128 UPC: 79249301628 Desc: 1112027   CLEAN IN PLACE OVE Pack: 1 Size: 2.5  GA\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 61.29 55.72 61.29 0.00 55.72 5.57 7 38.99\nSub Total = 38.99\nDivision: 096 SV Item#: 001904149 UPC: 02546917781 Desc: 6117781   OASIS 146 MULTI QU Pack: 4 Size: 1    CT\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 44.96 40.87 44.96 0.00 40.87 4.09 36 147.24\nSub Total = 147.24\nDivision: 096 SV Item#: 001904157 UPC: 79249302359 Desc: 1110313   WHITEOUT POWER FOA Pack: 4 Size: 1    CT\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 78.43 71.30 78.43 0.00 71.30 7.13 144 1,026.72\nSub Total = 1,026.72\nPage 1"  # noqa
    return text


@pytest.fixture
def valid_invoice_page() -> str:
    text = "UNFI\n11840 VALLEY VIEW RD\nEDEN PRAIRIE, MN 55344\nInvoice to Vendor\nBILL TO: 6273247 SV Barcode: 0009848418\nECOLAB Audit Period: 2022-1\nPO BOX 70343 Claim: 99P1236001\nCHICAGO IL 60673-0343 Date: 2/16/2023\nClaim Amount $ 11,267.48\nClaim Code 911.0\nDescription WRONG PRICE PER PO\nRegion GM/HBA\nCategory 12 GEN MDSE/HBC\n¶CLMK001383061236001)Ä\nCLMK001383061236001\nAccount Number Division Name Amount Div No.\n099921-962108-991  BWS 11,267.48 096\nTotal = $ 11,267.48\nComments\nSupporting Schedule and Documentation are attached.\nAddress Inquiries through ePASS application on \nSVHarbor.com\nAll access to ePASS is assigned to the appropriate user by the vendor or broker SVHarbor \nAdministrator.  \nContact the administrator to obtain a user name and password.  To find out whom the \nadministrator is, or request access to ePASS, e-mail merchandisingservices@unfi.com \nrequesting access to ePASS."  # noqa
    return text
