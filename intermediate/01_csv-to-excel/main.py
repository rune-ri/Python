import json

from src.categorizer import categorize_transaction
from src.csv_reader import read_csv
from src.excel_writer import write_excel
from src.transaction_processor import process_transaction


# read 
transactions = read_csv("input/Statements.csv")

# process.
transactions = process_transaction(transactions)

# load config 
with open("config/categories.json", "r", encoding="utf-8") as file:
    config = json.load(file)

# categorize
categorized = categorize_transaction(transactions, config)

# write 
write_excel(categorized, "output/transactions.xlsx")

print("Excel file generated successfully!")
# successfully written, need to check now
