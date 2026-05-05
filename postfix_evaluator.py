#create a evaluator for postfix expression
from stack import Stack

class PostfixEvaluator:
    
    def evaluate(self, expression):
        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if token.isdigit() or self._is_float(token):
                stack.push(float(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.push(a + b)
                elif token == '-':
                    stack.push(a - b)
                elif token == '*':
                    stack.push(a * b)
                elif token == '/':
                    stack.push(a / b)
                else:
                    raise Exception(f"Invalid operator: {token}")

        result = stack.pop()
        return int(result) if result.is_integer() else result

    def _is_float(self, s):
        try:
            float(s)
            return True
        except:
            return False
