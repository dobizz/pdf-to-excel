import pytest


@pytest.fixture
def invalid_page() -> str:
    return "Blank Page"


@pytest.fixture
def valid_page() -> str:
    text = "Some company text\nPO Nbr PO Date Inv Nbr Inv Date Rcv Date Rcv Wgt Net Net List Allow List Variance Qty Billed Claim Example\nDivision: 096 SV Item#: 001904102 UPC: 79249301625 Desc: 1111796   BLOCK WHITENER 4/1 Pack: 1 Size: 4    GA\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 40.55 36.86 40.55 0.00 36.86 3.69 251 926.19\nSub Total = 926.19\nDivision: 096 SV Item#: 001904108 UPC: 79249300176 Desc: 1114159   SUPER SOAK CONCENT Pack: 1 Size: 3    GA\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 72.78 66.15 72.78 0.00 66.15 6.63 40 265.20\nSub Total = 265.20\nDivision: 096 SV Item#: 001904109 UPC: 79249302315 Desc: 1114111   KAY STNLSS CLNER P Pack: 1 Size: 6    QT\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 36.19 32.84 36.19 0.00 32.84 3.35 8 26.80\nSub Total = 26.80\nDivision: 096 SV Item#: 001904128 UPC: 79249301628 Desc: 1112027   CLEAN IN PLACE OVE Pack: 1 Size: 2.5  GA\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 61.29 55.72 61.29 0.00 55.72 5.57 7 38.99\nSub Total = 38.99\nDivision: 096 SV Item#: 001904149 UPC: 02546917781 Desc: 6117781   OASIS 146 MULTI QU Pack: 4 Size: 1    CT\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 44.96 40.87 44.96 0.00 40.87 4.09 36 147.24\nSub Total = 147.24\nDivision: 096 SV Item#: 001904157 UPC: 79249302359 Desc: 1110313   WHITEOUT POWER FOA Pack: 4 Size: 1    CT\n0096409525 6/20/2022 6270198588 6/29/2022 7/11/2022 31002.210 78.43 71.30 78.43 0.00 71.30 7.13 144 1,026.72\nSub Total = 1,026.72\nPage 1"  # noqa
    return text
