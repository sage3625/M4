#Modifies the infix expression to a postfix expression using the stack
from stack import Stack

class InfixToPostfixConverter:
        precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    def convert(self, expression):
        stack = Stack()
        output = []
        tokens = expression.split()

        for token in tokens:
            if token.isalnum():
                output.append(token)

            elif token == '(':
                stack.push(token)

            elif token == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()  # remove '('

            else:  # operator
                while (not stack.is_empty() and
                       stack.peek() != '(' and
                       self.precedence[stack.peek()] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.push(token)

        while not stack.is_empty():
            output.append(stack.pop())

        return " ".join(output)
