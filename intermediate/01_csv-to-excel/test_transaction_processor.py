from src.transaction_processor import process_transaction
from src.csv_reader import read_csv

transactions = read_csv("input/Statements.csv")

processed = process_transaction(transactions)

for transaction in processed[:3]:
    print(transaction)

print("\nData Types:")
print(type(processed[0]["Date"]))
print(type(processed[0]["Amount (EUR)"]))
print(type(processed[0]["Resulting balance"]))
