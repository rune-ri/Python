from src.csv_reader import read_csv
from src.transaction_processor import process_transaction
from src.categorizer import categorize_transaction

import json

# this is what is to be done either way.
transaction = read_csv("input/Statements.csv")
transaction = process_transaction(transaction)

# now the main part
with open("config/categories.json", "r", encoding="utf-8") as file:
    config = json.load(file)
# this has created a config variable that will hold hte configs to send to categorize_transactions

categorized = categorize_transaction(transaction, config)
for transaction in categorized[:3]:
    print(transaction)


