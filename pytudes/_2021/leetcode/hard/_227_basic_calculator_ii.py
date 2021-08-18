"""https://leetcode.com/problems/basic-calculator/


Constraints:
    - 1 ≤ s.length ≤ 3 * 10^5
    - s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    - s represents a valid expression.
    - All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
    - The answer is guaranteed to fit in a 32-bit integer.

Examples:
    >>> Solution().calculate("")
    0

"""


class Solution:
    def calculate(self, s: str) -> int:
        return calculate(s)


def calculate(expression: str) -> int:
    """Return the evaluation of the given infix arithmetic expression

    Note: integer division should truncate toward zero.

    Args:
        expression: A valid infix arithmetic expression containing only digits and
        operators in '+', '-', '*', '/', and ' '.

    Examples:
        >>> calculate("3+2*2")
        7
        >>> calculate(" 3/2 ")
        1
        >>> calculate(" 3+5 / 2 ")
        5

    """
    # Arithmetic operator symbol to function map
    operator_functions = {
        # Interpret '+', '-' operators as signs, deferring evaluation to stack summation
        "+": lambda x: x,
        "-": lambda x: -x,
        # Perform '*', '/' against last stored number to respect operator precedence
        "*": lambda x: operand_stack.pop() * x,
        "/": lambda x: int(operand_stack.pop() / x),  # truncate towards 0
    }  # Note: implicit exception raising for invalid operator keys

    # DS's/res
    operand_stack = []
    curr_num, last_operator = 0, "+"  # Turing machine tape start state
    for i, token in enumerate(expression):

        # Build number from multi-digit strings
        if token.isdigit():
            curr_num = curr_num * 10 + int(token)

        if token in operator_functions or i == len(expression) - 1:
            # Evaluate the currently stored number, possibly against a previous stack entry
            operand_stack.append(operator_functions[last_operator](curr_num))

            # Turing machine tape state update:
            # reset `curr_num` since it has just been evaluated and
            # track token for future evaluation
            curr_num, last_operator = 0, token

    return sum(operand_stack)


def calculate_separate_operator_conditionals(expression: str) -> int:
    """Return the evaluation of the given infix arithmetic expression

    Note: integer division should truncate toward zero.

    Args:
        expression: A valid infix arithmetic expression containing only digits and
        operators in '+', '-', '*', '/', and ' '.

    Examples:
        >>> calculate_separate_operator_conditionals("3+2*2")
        7
        >>> calculate_separate_operator_conditionals(" 3/2 ")
        1
        >>> calculate_separate_operator_conditionals(" 3+5 / 2 ")
        5

    """

    operators = {"+", "-", "*", "/"}
    # DS's/res
    operand_stack = []
    curr_num, last_operator = 0, "+"  # Turing machine tape start state
    for i, token in enumerate(expression):

        # Build number from multi-digit strings
        if token.isdigit():
            curr_num = curr_num * 10 + int(token)

        if token in operators or i == len(expression) - 1:
            # Evaluate the currently stored number, possibly against a previous stack entry

            # Interpret '+', '-' operators as signs, deferring evaluation to stack summation
            if last_operator == "+":
                new_operand = curr_num
            elif last_operator == "-":
                new_operand = -curr_num

            # Perform '*', '/' against last stored number to respect operator precedence
            elif last_operator == "*":
                new_operand = operand_stack.pop() * curr_num
            else:  # last_operator == "/"
                new_operand = int(operand_stack.pop() / curr_num)  # truncate towards 0

            operand_stack.append(new_operand)

            # Turing machine tape state update:
            # reset `curr_num` since it has just been evaluated and
            # track token for future evaluation
            curr_num, last_operator = 0, token

    return sum(operand_stack)
