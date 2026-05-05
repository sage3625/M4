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
]

print("\n----- Infix to Postfix Converter -----")
conv = InfixToPostfixConverter()
for expr in infix_tests:
    print(f"[{expr}] -> [{conv.convert(expr)}]")

# ------------------------------
# Linked List Tests
# ------------------------------
print("\n----- Linked List Tests -----")
lst = SinglyLinkedList()
lst.build_list_forward([10, 20, 30, 40, 50])
print(lst)
lst.delete_first()
print(lst)
lst.delete_last()
print(lst)
lst.delete_value(30)
print(lst)

# ------------------------------
# Split Evens and Odds
# ------------------------------
print("\n----- Split Evens and Odds -----")
s = SplitEvensOdds()
s.build_list_forward([1,2,3,4,5,6,7,8,15,14,13,12,11,10,9])
print(s)

evens, odds = s.split_even_odd()
print(evens)
print(odds)
print(s)  # should be empty
