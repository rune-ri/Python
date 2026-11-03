from openpyxl import Workbook

def write_excel(transactions, file_path):
    workbook = Workbook()
    # creates a workbook? i think so
    
    all_sheet = workbook.active
    # creates the main sheet i think.
    all_sheet.title = "All Transactions"
    # first sheet name

    income_sheet = workbook.create_sheet("Income")
    outgoing_sheet = workbook.create_sheet("Outgoing")
    # this creates the ohter 2.
    
    headers = list(transactions[0].keys())
    # i know sheet turns series of strings into list.
    # i dont know what transaction[0] rfers to though.
    # transaction 0 accesses the first dictionary in the list of transactions
    # also need to check what .keys does.
    # ah this is soo simpple, it accesses the keys of key value pair
    for sheet in (all_sheet, income_sheet, outgoing_sheet):
        sheet.append(headers)

    # but now we have headers 
    for transaction in transactions:
        row = list(transaction.values())
        all_sheet.append(row)

        if transaction["Category"] == "Income":
            income_sheet.append(row)

        elif transaction["Category"] == "Outgoing":
            outgoing_sheet.append(row)

    workbook.save(file_path)
