def is_valid_age(age):
    if 18 <= age <= 60:
       return "Valid"
    else:
        return"Invalid"

#Define test Cases

test_cases = [
    (18,"Valid"),
    (17,"Invalid"),
    (19,"Valid"),
    (59,"Valid"),
    (60,"Valid"),
    (61,"Invalid")
]

#Run test cases 

for i,(age,expected)in enumerate(test_cases):
    result = is_valid_age(age)
    assert result == expected, f"Test case {i+1} failed: age={age}, expected={expected}, got={result}"
    print(f"Test case {i+1} passed:age={age}, expected={expected}, got{result}")

print("All test cases passsed!")