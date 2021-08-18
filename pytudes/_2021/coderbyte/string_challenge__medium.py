"""https://coderbyte.com/information/String%20Expression

Description:
    - For this challenge you will convert a string of written numbers to an
    actual number.

"""
import operator
import re


def StringChallenge(strParam: str) -> str:
    """Returns the evaluation of the arithmetic expression in a given string

    Args:
      strParam:
        the input string containing the given arithmetic expression. Concretely, strParam
        contains the written out version of the numbers 0-9 and the words "minus" or "plus".

    Returns:
      The string representation of the arithmetic evaluation of strParam using the written
      out version of the numbers 0-9. If a negative number was produced, the number is
      prefixed by the word "negative".

    Examples:
      >>> # 10 + 8 =>
      >>> StringChallenge("onezeropluseight")
      'oneeight'
      >>> # 18

      >>> # 1 - 11 =>
      >>> StringChallenge("oneminusoneone")
      'negativeonezero'
      >>> # -10

      >>> # 46 - 22 + 10 =>
      >>> StringChallenge("foursixminustwotwoplusonezero")
      'threefour'
      >>> # 34

      >>> # Empty string (degenerate case)
      >>> StringChallenge("")
      'zero'
      >>> # 0

    """
    if not strParam:
        return "zero"

    word_to_digit_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    arithmetic_operations = {
        "+": operator.add,
        "-": operator.sub,
    }

    strParam = strParam.lower()

    for digit_word, digit_str in word_to_digit_map.items():
        strParam = re.sub(digit_word, digit_str, strParam)

    for operator_word, operator_symbol in {"plus": "+", "minus": "-"}.items():
        strParam = re.sub(
            operator_word, f" {operator_symbol} ", strParam
        )  # add whitespace

    infix_expression_components = strParam.split()
    # Since only addition and subtraction are defined and we are using infix notation,
    # incrementally build up result using pre-defined arithmetic operation functions.
    while len(infix_expression_components) > 1:
        left_operand, operation, right_operand = infix_expression_components[:3]
        result = arithmetic_operations[operation](int(left_operand), int(right_operand))
        infix_expression_components[2] = result  # store last result
        infix_expression_components = infix_expression_components[
            2:
        ]  # truncate away used operator & operand

    evaluation_str = str(infix_expression_components[-1])
    for word, symbol in {**word_to_digit_map, "negative": "-"}.items():
        evaluation_str = re.sub(symbol, word, evaluation_str)

    return evaluation_str


# keep this function call here
# print(StringChallenge(input()))
