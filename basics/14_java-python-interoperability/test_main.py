from unittest.mock import patch 
from io import StringIO 
from contextlib import redirect_stdout 
import main

expected = [
    "Growth requires consistency.",
    "Calmness creates awareness.",
    "Curiosity drives learning.",
    "Perseverance creates progress.",
    "Presence requires attention.",
    "Invalid number input"
]

for number in range(6):
    output = StringIO()

    with patch("builtins.input", return_value=str(number)):
        with redirect_stdout(output):
            main.main()

    result = output.getvalue().strip()
    assert result == expected[number], f"Failed for input {number}"

print("All tests passed.")

