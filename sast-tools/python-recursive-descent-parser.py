# Example recursive decent parse. 
# Can be used as a guide for writing SAST tools

# Uses the following math example from cratecode
# https://cratecode.com/info/python-recursive-descent-parser

#expression -> term + expression | term - expression | term
#term -> factor * term | factor / term | factor
#factor -> ( expression ) | number


import re

class RecursiveDescentParser():
    """
    Recursive Descent Parser class
    """
    
    def tokenize(self, expression):
        """ 
        Function to tokenize 
        the input from the user.
        """
        token_pattern = r"(\d+|[()+\-*/])"
        tokens = re.findall(token_pattern, expression)
        return tokens 

    def parse_factor(self, tokens):
        """
        Parse the factors as defined in the example
        comments at the start of the file:

        factor -> ( expression ) | number
        """    
        token = tokens.pop(0)
        if token == "(":
            result = self.parse_expression(tokens)
            tokens = tokens.pop(0)
            return result
        else:
            return float(token)

    def parse_term(self, tokens):
        """
        Parse the terms as defined in the example
        comments at the start of the file:

        term -> factor * term | factor / term | factor
        """
        left = self.parse_factor(tokens)
        while tokens and tokens[0] in ["*", "/"]:
            op = tokens.pop(0)
            right = self.parse_factor(tokens)
            if op == "*":
                left *= right
            else:
                left /= right
        return left

    def parse_expression(self, tokens):
        """
        Parse the expression as defined in the example
        comments at the start of the file:

        expression -> term + expression | term - expression | term
        """
        left = self.parse_term(tokens)
        while tokens and tokens[0] in ["+", "-"]:
            op = tokens.pop(0)
            right = self.parse_term(tokens)
            if op == "+":
                left += right
            else:
                left -= right
        return left

    def evaluate_expression(self, expression):
        """
        Evaluate the expression by tokenizing it
        and then parsing it.
        """
        tokens = self.tokenize(expression)
        result = self.parse_expression(tokens)
        return result

    def main(self):
        """
        Main function to run the program.
        """
        expression = input("Enter an expression: ")
        result = self.evaluate_expression(expression)
        print(result)

if __name__ == "__main__":
    new_parser = RecursiveDescentParser()
    new_parser.main()
        

