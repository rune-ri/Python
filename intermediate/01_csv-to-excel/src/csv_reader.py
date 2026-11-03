# i am learning as i go so this may take a while.
# there is a builtin handling for csv in python apparently. i think it was always there 
#   but i was not allowed to use it in the uni work

import csv 

def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    # i understood everything except what newline means and is for.
    # open is just opne,
    # r is for reading the file.
    # utf is for formatting of value 
    # apparently keeping newline as empty string is crucial to avoid empty lines.
        reader = csv.DictReader(file, delimiter=";")
        # usually the case is csv.reader. most likely DictReader is differnet in utility.
        # list(reader) turns it into list of lists. since reader teraties through lines and list 
        #   turns that lines and splits it basedon differnet strings presetn.
        return list(reader)


