# i have found that there are 3 types of testing,
# 1. exhaustive testing when finite domain.
# 2. exampe based testing for selected input and expected outupt.
# 3. property testing for testing general property 

from hypothesis import given, strategies as st 
# hypothesis is property based testing library for python.
# hypothesis allows testign some behaviour by automatically generating inputs 
# hypothesis is library
# given is function in it 
# strategies is a module 
#   a strategy dfeines how to geenrate values of certain kind.
#   st.integers() makes integers.

@given(
    # @given takes strategy as arguments to create inputs for test functions.
    users=st.lists(st.dictionaries(
        keys=st.text(),
        values=st.integers()
    )),
    new_entry=st.dictionaries(
        keys=st.text(),
        values=st.integers()
    )
)
def test_append_properties(users, new_entry):
    original_users = users.copy()

    # Perform the operation
    users.append(new_entry)

    # Property 1: Length increases by exactly one
    assert len(users) == len(original_users) + 1

    # Property 2: Existing entries are preserved
    assert users[:-1] == original_users
