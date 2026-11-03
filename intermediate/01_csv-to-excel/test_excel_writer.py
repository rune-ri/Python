from src.csv_reader import read_csv
from src.transaction_processor import process_transaction
from src.categorizer import categorize_transaction
from src.excel_writer import write_excel

import json
import tempfile
from pathlib import Path
# this is one of the most important lib, i should learn it someitme

from openpyxl import load_workbook
# nearly made a mistake of importing Workbook instead of this.

# now real code. 
# this part is completely ai, i was tired.
# Load transactions
transactions = read_csv("input/Statements.csv")
transactions = process_transaction(transactions)

# Load configuration
with open("config/categories.json", "r", encoding="utf-8") as file:
    config = json.load(file)

# Categorize transactions
categorized = categorize_transaction(transactions, config)


# Generate and test Excel workbook
with tempfile.TemporaryDirectory() as temp_dir:
    file_path = Path(temp_dir) / "test.xlsx"

    write_excel(categorized, file_path)

    # Check file creation
    assert file_path.exists()

    # Open generated workbook
    workbook = load_workbook(file_path)
    
    # Check worksheets
    assert workbook.sheetnames == [
        "All Transactions",
        "Income",
        "Outgoing"
    ]

    all_sheet = workbook["All Transactions"]
    income_sheet = workbook["Income"]
    outgoing_sheet = workbook["Outgoing"]

    # Check transaction counts (subtract header row)
    assert all_sheet.max_row == len(categorized) + 1

    income_count = sum(
        transaction["Category"] == "Income"
        for transaction in categorized
    )

    outgoing_count = sum(
        transaction["Category"] == "Outgoing"
        for transaction in categorized
    )

    assert income_sheet.max_row == income_count + 1
    assert outgoing_sheet.max_row == outgoing_count + 1

    print("All Excel writer tests passed!")

    workbook.close()

