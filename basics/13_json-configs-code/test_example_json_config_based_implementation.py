from json_config_based_implementation import config_imp

tests = [
    {
        "name": "Square with negatives allowed",
        "input": [-3, -2, -1, 0, 1, 2, 3],
        "config": {
            "operation": "square",
            "limit": 10,
            "allow_negatives": True
        },
        "expected": [9, 4, 1, 0, 1, 4, 9]
    },
    {
        "name": "Cube with negatives disallowed",
        "input": [-3, -2, -1, 0, 1, 2, 3],
        "config": {
            "operation": "cube",
            "limit": 50,
            "allow_negatives": False
        },
        "expected": [0, 1, 8, 27]
    },
    {
        "name": "Double with boundary filtering",
        "input": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        "config": {
            "operation": "double",
            "limit": 10,
            "allow_negatives": True
        },
        "expected": [-8, -6, -4, -2, 0, 2, 4, 6, 8]
    },
    {
        "name": "Empty input",
        "input": [],
        "config": {
            "operation": "square",
            "limit": 10,
            "allow_negatives": True
        },
        "expected": []
    },
    {
        "name": "All results rejected",
        "input": [1, 2, 3],
        "config": {
            "operation": "square",
            "limit": 1,
            "allow_negatives": True
        },
        "expected": []
    }
]
# from what i see here for an example based testing, it is a step by step procedure.
# 1. define test case, as done above.
# 2. execute test case
# 3. assert and check 
# 4. print test result. 

for test in tests:
    actual_copy, actual_inplace = config_imp(test["input"].copy(), test["config"])
    assert actual_copy == test["expected"], (
        f'{test["name"]}: list comprehension failed'
    )
    
    assert actual_inplace == test["expected"], (
        f'{test["name"]}: in-place filtering failed'
    )

    assert actual_copy == actual_inplace, (
        f'{test["name"]}: filtering implementations differ'
    )
    print(f'PASS: {test["name"]}')
print("\nAll example-based tests passed!")
