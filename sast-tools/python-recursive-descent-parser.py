# Example recursive decent parse. 
# Can be used as a guide for writing SAST tools

# Uses the following math example from cratecode
# https://cratecode.com/info/python-recursive-descent-parser

#expression -> term + expression | term - expression | term
#term -> factor * term | factor / term | factor
#factor -> ( expression ) | number


import re

def tokenize(expression):
    """ 
    Function to tokenize 
    the input from the user.
    """
    token_pattern = r"(\d+|[()+\-*/])"
    tokens = re.findall(token_pattern, expression)
    return tokens 

def parse_factor(tokens):
    """
    Parse the factors as defined in the example
    comments at the start of the file:

    factor -> ( expression ) | number
    """    
    token = tokens.pop(0)
    if token == "(":
        result = parse_expression(tokens)
        tokens = tokens.pop(0)
        return result
    else:
        return float(token)

def parse_term(tokens):
    """
    Parse the terms as defined in the example
    comments at the start of the file:

    term -> factor * term | factor / term | factor
    """
    left = parse_factor(tokens)
    while tokens and tokens[0] in ["*", "/"]:
        op = tokens.pop(0)
        right = parse_factor(tokens)
        if op == "*":
            left *= right
        else:
            left /= right
    return left

def parse_expression(tokens):
    """
    Parse the expression as defined in the example
    comments at the start of the file:

    expression -> term + expression | term - expression | term
    """
    left = parse_term(tokens)
    while tokens and tokens[0] in ["+", "-"]:
        op = tokens.pop(0)
        right = parse_term(tokens)
        if op == "+":
            left += right
        else:
            left -= right
    return left

def evaluate_expression(expression):
    """
    Evaluate the expression by tokenizing it
    and then parsing it.
    """
    tokens = tokenize(expression)
    result = parse_expression(tokens)
    return result

def main():
    """
    Main function to run the program.
    """
    expression = input("Enter an expression: ")
    result = evaluate_expression(expression)
    print(result)

if __name__ == "__main__":
    main()
        

