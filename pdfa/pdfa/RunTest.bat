@echo off
@echo Command-line samples for PDF/A Manager
@echo Copyright 2001-2025 Apryse Software Inc.
@echo.
@echo Example 1) Test a PDF file for PDF/A compliance:
pdfa --noxml "PDFTron PDFA Manager User Manual.pdf"
@echo.
@echo Example 2) Test PDF files for PDF/A compliance and generate an XML error report:
pdfa -o test_out/OUT1 --level B --subfolders *.pdf
@echo.
@echo Example 3) An example of PDF/A Conversion:
pdfa -c -z -o test_out/OUT2 *.pdf
@echo.
@echo Example 4) An example of PDF/A Conversion:
pdfa -c --noxml -o test_out/OUT3 --subfolders "PDFTron PDFA Manager User Manual.pdf" test_out/OUT2
@echo.