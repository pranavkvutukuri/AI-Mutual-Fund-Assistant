# AI Mutual Fund Assistant

## Project Overview

AI Mutual Fund Assistant is a Python-based project that extracts raw text from mutual fund factsheet PDFs.

The goal of this project is to convert information from a mutual fund factsheet into readable text and identify key fund details when available.

## Problem Statement

Mutual fund factsheets contain important information such as fund name, category, AUM, expense ratio, and risk level.

Manually reading and extracting this information from PDFs can be slow and repetitive. This project solves the first step of that problem by automatically extracting raw text from a factsheet PDF.

## Features

- Reads mutual fund factsheet PDFs
- Extracts raw text using Python
- Saves extracted text into `data/fund_data.txt`
- Prints key fields if available:
  - Fund Name
  - Category
  - AUM
  - Expense Ratio
  - Risk

## Technology Stack

- Python
- pdfplumber
- Regular Expressions
- Git
- GitHub
- Visual Studio Code

## Future Roadmap

- Improve field extraction accuracy
- Support multiple PDF uploads
- Store extracted data in CSV format
- Add structured JSON output
- Build a Streamlit web interface
- Add AI-based mutual fund summary and comparison