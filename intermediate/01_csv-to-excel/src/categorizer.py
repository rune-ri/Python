# identify whether transaction is credit or debit.
# identify counterpart that is known.
# use configs

def categorize_transaction(transactions, config):
    counterparties = config["counterparties"]

    categorized = []
    # this is wehre we store the output.

    for transaction in transactions:
        transaction = transaction.copy()

        # we first need to determine the transaction direction.
        # we know this by multiple fields already.
        # 1. credit debit.
        # 2. true false with is_income
        transaction["Category"] = (
                "Income" if transaction["is_income"] else "Outgoing"
        )
        # this is the best part of python, we can create these english type sentences.

        # now we need to work with the counterparty.
        transaction["Counterparty name"] = None
        # new column

        for name, account_numbers in counterparties.items():
            # i need to learn whta items does. 
            if transaction["Counterparty"] in account_numbers:
                transaction["Counterparty name"] = name
                # easy to understand mostly.
                break

        categorized.append(transaction)

    return categorized
