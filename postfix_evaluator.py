#create a evaluator for postfix expression
from stack import Stack

class PostfixEvaluator:
    """Evaluates postfix expressions using a stack."""

    def evaluate(self, expression):
        stack = Stack()
