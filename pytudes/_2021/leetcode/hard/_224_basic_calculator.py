"""https://leetcode.com/problems/basic-calculator/


Constraints:
    - 1 ≤ s.length ≤ 3 * 10^5
    - s consists of digits, '+', '-', '(', ')', and ' '
    - s represents a valid expression

Examples:
    >>> Solution().calculate("0")
    0

"""

from pytudes._2021.leetcode.medium._150__evaluate_reverse_polish_notation import (
    eval_RPN,
)


class Solution:
    def calculate(self, s: str) -> int:
        return calculate_via_rpn(s)


def calculate_via_rpn(expression: str) -> int:
    """Return the evaluation of the given infix arithmetic expression

    Args:
        expression: A valid infix arithmetic expression containing only numbers from R
        and symbols in '+', '-', '(', ')', and ' '

    Examples:
        >>> calculate_via_rpn("1 + 1")
        2
        >>> calculate_via_rpn(" 2-1 + 2 ")
        3
        >>> calculate_via_rpn("(1+(4+5+2)-3)+(6+8)")
        23

    See Also:
        - https://leetcode.com/problems/basic-calculator/discuss/414898/infix-to-postfix-a-general-approach-to-similar-questions

    """

    def move_greater_or_equal_precedence_operators_in_curr_scope_to_rpn_stack() -> None:
        """Moves intermediate stack operators with precedence < `token` to RPN stack"""
        while intermediate_operator_tokens:
            last_operator = intermediate_operator_tokens[-1]
            if operator_precedence[token] >= operator_precedence[last_operator]:
                rpn_tokens.append(intermediate_operator_tokens.pop())
            else:
                if last_operator == "(":  # Current scope is now empty
                    # Discard open parenthesis belonging to current scope which no
                    # longer contains operators
                    intermediate_operator_tokens.pop()
                break

    # Precedence table which enables operator partial ordering
    operator_precedence = {
        # "^": 1,
        # "√": 1,
        "*": 2,
        "/": 2,
        "+": 3,
        "-": 3,
        "(": float("inf"),
        ")": -float("inf"),
    }  # https://en.wikipedia.org/wiki/Order_of_operations

    num = None  # None means no number is parsed
    intermediate_operator_tokens, rpn_tokens = [], []
    for i, token in enumerate(expression):

        # Build number from multi-digit strings
        if token.isdigit():
            if num is None:
                num = 0
            num = num * 10 + int(token)

        # Add built number to RPN stack
        if token in operator_precedence or i == len(expression) - 1:
            if num is not None:
                rpn_tokens.append(str(num))
            num = None

        # Update operators in intermediate stack/Move to RPN stack
        if token in operator_precedence:
            if token != "(":
                move_greater_or_equal_precedence_operators_in_curr_scope_to_rpn_stack()
            if token != ")":
                intermediate_operator_tokens.append(token)

    rpn_tokens += reversed(intermediate_operator_tokens)
    return eval_RPN(rpn_tokens)
