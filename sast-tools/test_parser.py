def test_parse_expression():
    # Test addition
    assert parse_expression(["2", "+", "3"]) == 5

    # Test subtraction
    assert parse_expression(["5", "-", "2"]) == 3

    # Test multiplication
    assert parse_expression(["2", "*", "4"]) == 8

    # Test division
    assert parse_expression(["10", "/", "2"]) == 5

    # Test complex expression
    assert parse_expression(["2", "*", "3", "+", "4", "/", "2"]) == 7

    # Test expression with parentheses
    assert parse_expression(["(", "2", "+", "3", ")", "*", "4"]) == 20

    # Test expression with multiple operators
    assert parse_expression(["2", "+", "3", "*", "4", "-", "5"]) == 9

    # Test expression with only one term
    assert parse_expression(["10"]) == 10

    print("All test cases passed!")

test_parse_expression()