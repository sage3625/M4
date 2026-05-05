from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter
from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

# ------------------------------
# Postfix Evaluation
# ------------------------------
postfix_tests = [
    "5 3 +",
    "8 2 - 3 +",
    "5 3 8 * +",
    "6 2 / 3 +",
    "5 8 + 3 -",
    "5 3 + 8 *",
    "8 2 3 * + 6 -",
    "5 3 8 * + 2 /",
    "8 2 + 3 6 * -",
    "5 3 + 8 2 / -"
]

print("----- Postfix Evaluator -----")
pe = PostfixEvaluator()
for expr in postfix_tests:
    print(f"[{expr}] = {pe.evaluate(expr)}")

# ------------------------------
# Infix to Postfix Conversion
# ------------------------------
infix_tests = [
    "A + B",
    "A + B * C",
    "( A + B ) * C",
    "A * B + C / D",
    "( A + B ) * ( C - D )",
    "A + B * C - D / E",
    "A * ( B + C ) / D",
    "( A + B * C ) / ( D - E )",
    "A + ( B - C ) * D",
    "( A + B * ( C - D ) ) / E"
