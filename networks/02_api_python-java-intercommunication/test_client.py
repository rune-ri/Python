# DO NOT RUN THIS CODE WITH LARGE INPUT, THE TIME COMPLEXITY IS HIGH.

from unittest.mock import patch 
from contextlib import redirect_stdout
from io import StringIO
import client
import sys
from itertools import product


# now this is gonna be normal exhaustive check code.
# basically i will set a limit and then use that limit
#   to exhausitvley check all differnet variations from 0 to that number.

# i am also thinking of feeding the input through terminal
# i have found that we can use sys import for this

limit = int(sys.argv[1])
tuples = product(range(limit+1), repeat=2)
# i have used product before so i know how to do this, i think.

for a, b in tuples:
    output = StringIO()

    with patch("builtins.input", side_effect=[str(a), str(b)]):
        with redirect_stdout(output):
            client.main()

    result = output.getvalue().strip()
    # i have been using strip for a while withotu understnading its functionality, 
    # now i should actually see what it does.
    # strip removes extra whitespaces. is this just a precaution?

    assert result == str(a+b), (
        f"Failed: ({a}, {b}), expected {a + b}, got {result}"
    )
    print(f"{a} + {b} = {a+b} | {result}")

print("All tests Passed")
