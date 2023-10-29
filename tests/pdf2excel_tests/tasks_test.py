import os
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import pytest

from pdf2excel.tasks import process_invoice_page, process_pdf

filename = "__test__.pdf"


@pytest.fixture
def setup_test_pdf():
    path = Path(filename)
    path.write_bytes(b"%PDF")
    yield
    os.remove(filename)


@pytest.mark.usefixtures("setup_test_pdf")
class TestProcessPDF:
    def test_process_pdf(self, valid_page, invalid_page):
        mock_invalid_page = Mock()
        mock_invalid_page.extract_text.return_value = invalid_page
        mock_valid_page = Mock()
        mock_valid_page.extract_text.return_value = valid_page
        mock_context = MagicMock()
        mock_pdf = Mock()
        mock_context.__enter__.return_value = mock_pdf
        mock_pdf.pages = [
            mock_invalid_page,
            mock_valid_page,
        ]
        with patch("pdfplumber.open", return_value=mock_context), patch(
            "pandas.DataFrame.to_excel", return_value=None
        ):
            process_pdf(path=Path("__test__.pdf"))

    def test_process_invoice_page(self, valid_invoice_page, invalid_page):
        assert process_invoice_page(valid_invoice_page)
        assert process_invoice_page(invalid_page) == {}
