import pdfplumber
import sys
from pathlib import Path

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/extract_fund_text.py data/factsheet.pdf")
        return

    pdf_path = sys.argv[1]
    raw_text = extract_text(pdf_path)

    output_path = Path("data/fund_data.txt")
    output_path.write_text(raw_text, encoding="utf-8")

    print(raw_text)
    print("\nText saved to data/fund_data.txt")

if __name__ == "__main__":
    main()