from datetime import datetime
from decimal import Decimal
# we use decimal because it allows there to be no floating point errors
# for financila data, this distinction is crucial since money is being compared and handled.

def process_transaction(transactions):
    processed = []
    for transaction in transactions:
        transaction = transaction.copy()
        # then we normalize each of hte transaction from list of transactions.
        # 1. we need to take ddates and times and make it approapriate format.
        # 2. we need to take the monney values and turn them into proper international 
        #   structure ie replace , with . and . with ""
        transaction["Date"] = datetime.strptime(transaction["Date"], "%Y%m%d").date()
        # this should take date remove extra and then turn it into date time format with ymd .
        # i think this should also remove the time aspect since it is not required.
        
        transaction["Amount (EUR)"] = Decimal(transaction["Amount (EUR)"].replace(".", "").replace(",", "."))
        # the order of replace is important coz otherwise everyting would go to ""
        transaction["Resulting balance"] = Decimal(transaction["Resulting balance"].replace(".", "").replace(",", "."))

        # just add to the list.
        processed.append(transaction)

    return processed
