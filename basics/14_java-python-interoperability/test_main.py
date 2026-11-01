from unittest.mock import patch 
from io import StringIO 
from contextlib import redirect_stdout 

# unit test is needed to do this unit test, 
# need patch to take over the input command.
# string io is needed to create a buffer to hold the input or output whatever.
# context lib if for redirecting the output received to stirng io.

# first we import main.
import main

# next we need to define results expected. its easy fo rnow since its limited.
expected = [
    "Growth requires consistency.",
    "Calmness creates awareness.",
    "Curiosity drives learning.",
    "Perseverance creates progress.",
    "Presence requires attention.",
    "Invalid number input"
]

for number in range(6):
    # first we create place to hold the output that would be needed.
    output = StringIO()

    # then we create the method to run the inputs.
    with patch("builtins.input", return_value=str(number)):
        with redirect_stdout(output):
            main.main()

    result = output.getvalue().strip()
    assert result == expected[number], f"Failed for input {number}"

print("All tests passed.")

# This is exhaustive testing method of taking over input. creating output space, redurecting to output to output space
# then you call the main method from the main.py. and then you just get the value stored, check its equality and then 
# just print whatever is needed.
