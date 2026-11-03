from openpyxl import Workbook

def write_excel(transactions, file_path):
    workbook = Workbook()
    # creates a workbook? i think so
    
    all_sheet = workbook.active
    # creates the main sheet i think.
    all_sheet.title = "All Transactions"
    # first sheet name

    Income_sheet = workbook.create_sheet("Incoming")
    Outgoing_sheet = workbook.create_sheet("Outgoing")
    # this creates the ohter 2.
    
    headers = list(transactions[0].keys())
    # i know sheet turns series of strings into list.
    # i dont know what transaction[0] rfers to though.
    # also need to check what .keys does.

    # but now we have headers 
    for transaction in transactions:
        row = list(transaction.values())
        all_sheet.append(row)

        if transaction["Category"] == "Income":
            income_sheet.append(row)

        elif transaction["Category"] == "Outgoing":
            outgoing_sheet.append(row)

    workbook.save(file_path)
