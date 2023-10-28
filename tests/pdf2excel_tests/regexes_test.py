from pdf2excel.regexes import core_pat, entry_pat, head_pat


def test_core_pat(valid_page, invalid_page):
    assert core_pat.search(valid_page)
    assert core_pat.search(invalid_page) is None


def test_entry_pat(valid_page, invalid_page):
    assert entry_pat.search(valid_page)
    assert entry_pat.search(invalid_page) is None


def test_head_pat(valid_page, invalid_page):
    assert head_pat.search(valid_page)
    assert head_pat.search(invalid_page) is None
