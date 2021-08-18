"""https://coderbyte.com/information/Reverse%20Polish%20Notation

"""

import operator


def MathChallenge(rpn_expression: str) -> int:
    """Returns the value of an arithmetic expression written in Reverse Polish notation

    Args:
      rpn_expression:
        The input string containing the Reverse Polish notation expression which to
        evaluate. rpn_expression is composed of only integers and the operators:
        +,-,* and /.

    Examples:
        >>> MathChallenge("1 1 + 1 + 1 +")
        4
        >>> # ((1 + 1) + 1) + 1
        >>> # = (2 + 1) + 1
        >>> # = 3 + 1
        >>> # = 4
        >>> MathChallenge("4 5 + 2 1 + *")
        27
        >>> # (4 + 5) * (2 + 1)
        >>> # = 9 * (2 + 1)
        >>> # = 9 * 3
        >>> # = 27
        >>> MathChallenge("2 12 + 7 / ")
        2
        >>> # (2 + 12) / 7
        >>> # = 14 / 7
        >>> # = 2
        >>> MathChallenge("1 1 - 1 + 1 +")
        2
        >>> # ((1 - 1) + 1) + 1
        >>> # = (0 + 1) + 1
        >>> # = 1 + 1
        >>> # = 2
        >>> MathChallenge("1 1 - +")
        Traceback (most recent call last):
        ...
        ValueError: Malformed RPN arithmetic expression: 1 1 - +; Stack had < 2 elements (≥2 expected)

    """

    arithmetic_operation = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda x, y: int(operator.truediv(x, y)),
    }

    curr_num = None
    operand_stack = []
    for token in rpn_expression:

        # Build number by parsing multi-digit string
        if token.isdigit():
            if curr_num is None:
                curr_num = 0
            curr_num = curr_num * 10 + int(token)

        # Add number from fully-parsed multi-digit string to operand stack
        elif token == " " and curr_num is not None:  # Operand/operator delimiter
            operand_stack.append(curr_num)
            curr_num = None

        # Evaluate operand stack items with the current operator
        elif token in arithmetic_operation:
            try:
                right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
            except IndexError as e:
                raise ValueError(
                    f"Malformed RPN arithmetic expression: {rpn_expression}; "
                    "Stack had < 2 elements (≥2 expected)"
                ) from e

            operand_stack.append(
                arithmetic_operation[token](left_operand, right_operand)
            )

    return operand_stack.pop() if operand_stack else 0


def MathChallenge_cases(rpn_expression: str) -> int:
    """Returns the value of an arithmetic expression written in Reverse Polish notation

    Args:
      rpn_expression:
        The input string containing the Reverse Polish notation expression which to
        evaluate. rpn_expression is composed of only integers and the operators:
        +,-,* and /.

    Examples:
        >>> MathChallenge_cases("1 1 + 1 + 1 +")
        4
        >>> # ((1 + 1) + 1) + 1
        >>> # = (2 + 1) + 1
        >>> # = 3 + 1
        >>> # = 4
        >>> MathChallenge_cases("4 5 + 2 1 + *")
        27
        >>> # (4 + 5) * (2 + 1)
        >>> # = 9 * (2 + 1)
        >>> # = 9 * 3
        >>> # = 27
        >>> MathChallenge_cases("2 12 + 7 / ")
        2
        >>> # (2 + 12) / 7
        >>> # = 14 / 7
        >>> # = 2
        >>> MathChallenge_cases("1 1 - 1 + 1 +")
        2
        >>> # ((1 - 1) + 1) + 1
        >>> # = (0 + 1) + 1
        >>> # = 1 + 1
        >>> # = 2
        >>> MathChallenge_cases("1 1 - +")
        Traceback (most recent call last):
        ...
        ValueError: Malformed RPN arithmetic expression: 1 1 - +; Stack had < 2 elements (≥2 expected)

    """

    arithmetic_operators = {"+", "-", "*", "/"}

    curr_num = None
    operand_stack = []
    for char in rpn_expression:

        # Build multi-digit string
        if char.isdigit():
            if curr_num is None:
                curr_num = 0
            curr_num = curr_num * 10 + int(char)

        elif (
            char == " " and curr_num is not None
        ):  # delimiter between operands & operators
            processed_token, curr_num = curr_num, None
            operand_stack.append(processed_token)

        elif char in arithmetic_operators:

            try:
                right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
            except IndexError as e:
                raise ValueError(
                    f"Malformed RPN arithmetic expression: {rpn_expression}; "
                    "Stack had < 2 elements (≥2 expected)"
                ) from e

            if char == "+":
                processed_token = left_operand + right_operand
            elif char == "-":
                processed_token = left_operand - right_operand
            elif char == "*":
                processed_token = left_operand * right_operand
            else:  # char == "/"
                processed_token = int(
                    left_operand / right_operand
                )  # truncate fractions
            operand_stack.append(processed_token)

    return operand_stack.pop() if operand_stack else 0


# # keep this function call here
# print(MathChallenge_cases(input()))
