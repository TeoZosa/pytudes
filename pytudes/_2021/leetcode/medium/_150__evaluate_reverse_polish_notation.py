"""https://leetcode.com/problems/evaluate-reverse-polish-notation/

Constraints:
    - 1 ≤ tokens.length ≤ 104
    - tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in
    the range [-200, 200].

Examples:
    >>> Solution().evalRPN(["1","1","+"])
    2

See Also:
    - https://cs.stackexchange.com/questions/16575/does-reverse-polish-notation-have-an-ll-grammar

"""

import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        return eval_RPN(tokens)


def eval_RPN(tokens: list[str]) -> int:
    """Returns the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or
    another expression. Note that division between two integers should truncate
    toward zero. It is guaranteed that the given RPN expression is always
    valid. That means the expression would always evaluate to a result, and
    there will not be any division by zero operation.

    Let L be the language of all arithmetic expressions written in Reverse
    Polish Notation, containing only binary operators.
        Σ(𝐿)={𝑛,𝑜}, n := number, o := operator.

    There exists an LL grammar G : L(G) = L
        𝐺=({𝐸,𝑆,𝑅},{𝑛,𝑜},𝑃,𝐸), with productions:
            𝐸→𝑛 | 𝑆𝑅
            𝑆→𝑛𝐸𝑜
            𝑅→𝐸𝑜𝑅 | 𝜖

    Args:
        tokens: sequence of operators and operands in reverse polish notation

    Examples:
        >>> eval_RPN(["2","1","+","3","*"])
        9
        >>> # ((2 + 1) * 3)
        >>> # = 3 * 3
        >>> # = 9
        >>> eval_RPN(["4","13","5","/","+"])
        6
        >>> # (4 + (13 / 5))
        >>> # = 4 + 2
        >>> # = 6
        >>> eval_RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        22
        >>> # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        >>> # = ((10 * (6 / (12 * -11))) + 17) + 5
        >>> # = ((10 * (6 / -132)) + 17) + 5
        >>> # = ((10 * 0) + 17) + 5
        >>> # = (0 + 17) + 5
        >>> # = 17 + 5
        >>> # = 22
        >>> eval_RPN(["1","1","-"])
        0
        >>> eval_RPN([""])
        Traceback (most recent call last):
        ...
        ValueError: invalid literal for int() with base 10: ''
        >>> eval_RPN(["^"])
        Traceback (most recent call last):
        ...
        ValueError: invalid literal for int() with base 10: '^'

    """
    arithmetic_operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    operand_stack = []
    for token in tokens:
        if operator_fn := arithmetic_operations.get(token):
            right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
            new_operand = operator_fn(left_operand, right_operand)
        else:
            new_operand = token
        operand_stack.append(int(new_operand))

    return operand_stack.pop()


def eval_RPN_robust(tokens: list[str]) -> int:
    """Returns the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or
    another expression. Note that division between two integers should truncate
    toward zero. It is guaranteed that the given RPN expression is always
    valid. That means the expression would always evaluate to a result, and
    there will not be any division by zero operation.

    Let L be the language of all arithmetic expressions written in Reverse
    Polish Notation, containing only binary operators.
        Σ(𝐿)={𝑛,𝑜}, n := number, o := operator.

    There exists an LL grammar G : L(G) = L
        𝐺=({𝐸,𝑆,𝑅},{𝑛,𝑜},𝑃,𝐸), with productions:
            𝐸→𝑛 | 𝑆𝑅
            𝑆→𝑛𝐸𝑜
            𝑅→𝐸𝑜𝑅 | 𝜖

    Args:
        tokens: sequence of operators and operands in reverse polish notation

    Examples:
        >>> eval_RPN_robust(["2","1","+","3","*"])
        9
        >>> # ((2 + 1) * 3)
        >>> # = 3 * 3
        >>> # = 9
        >>> eval_RPN_robust(["4","13","5","/","+"])
        6
        >>> # (4 + (13 / 5))
        >>> # = 4 + 2
        >>> # = 6
        >>> eval_RPN_robust(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        22
        >>> # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        >>> # = ((10 * (6 / (12 * -11))) + 17) + 5
        >>> # = ((10 * (6 / -132)) + 17) + 5
        >>> # = ((10 * 0) + 17) + 5
        >>> # = (0 + 17) + 5
        >>> # = 17 + 5
        >>> # = 22
        >>> eval_RPN_robust(["1","1","-"])
        0
        >>> eval_RPN_robust([""])
        0
        >>> eval_RPN_robust(["^"])
        Traceback (most recent call last):
        ...
        ValueError: Invalid token: ^


    """
    ## INITIALIZE VARS ##
    # DS's/res
    arithmetic_operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    # Evaluate RPN expression
    operand_stack = []
    for token in tokens:
        if not token:
            continue

        if operator_fn := arithmetic_operations.get(token):
            right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
            new_operand = operator_fn(left_operand, right_operand)
        elif token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
            new_operand = token
        else:
            raise ValueError(f"Invalid token: {token}")

        operand_stack.append(int(new_operand))

    return operand_stack.pop() if operand_stack else 0


def eval_RPN_classic(tokens: list[str]) -> int:
    """Returns the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or
    another expression. Note that division between two integers should truncate
    toward zero. It is guaranteed that the given RPN expression is always
    valid. That means the expression would always evaluate to a result, and
    there will not be any division by zero operation.

    Let L be the language of all arithmetic expressions written in Reverse
    Polish Notation, containing only binary operators.
        Σ(𝐿)={𝑛,𝑜}, n := number, o := operator.

    There exists an LL grammar G : L(G) = L
        𝐺=({𝐸,𝑆,𝑅},{𝑛,𝑜},𝑃,𝐸), with productions:
            𝐸→𝑛 | 𝑆𝑅
            𝑆→𝑛𝐸𝑜
            𝑅→𝐸𝑜𝑅 | 𝜖

    Args:
        tokens: sequence of operators and operands in reverse polish notation

    Examples:
        >>> eval_RPN_classic(["2","1","+","3","*"])
        9
        >>> # ((2 + 1) * 3) = 9
        >>> eval_RPN_classic(["4","13","5","/","+"])
        6
        >>> # (4 + (13 / 5)) = 6
        >>> eval_RPN_classic(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        22
        >>> # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        >>> # = ((10 * (6 / (12 * -11))) + 17) + 5
        >>> # = ((10 * (6 / -132)) + 17) + 5
        >>> # = ((10 * 0) + 17) + 5
        >>> # = (0 + 17) + 5
        >>> # = 17 + 5
        >>> # = 22
        >>> eval_RPN_classic(["1","1","-"])
        0
        >>> eval_RPN_classic([""])
        Traceback (most recent call last):
        ...
        ValueError: invalid literal for int() with base 10: ''
        >>> eval_RPN_classic(["^"])
        Traceback (most recent call last):
        ...
        ValueError: invalid literal for int() with base 10: '^'

    """
    arithmetic_operators = {"+", "-", "*", "/"}
    operand_stack = []

    for token in tokens:
        if token in arithmetic_operators:
            right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
            if token == "+":
                new_operand = left_operand + right_operand
            elif token == "-":
                new_operand = left_operand - right_operand
            elif token == "*":
                new_operand = left_operand * right_operand
            else:  # token == "/"
                # Integer division is truncated toward zero.
                new_operand = int(left_operand / right_operand)
        else:
            new_operand = int(token)
        operand_stack.append(new_operand)

    return operand_stack.pop()
