import re
class Stack:
    def __init__(self) :
        self.items = []
    def push(self, item) :
        self.items.append(item)

    def pop(self):
        return self.items.pop()

s1=Stack();


# print(re.split("([^0-9])", "123+456*"))
def evalPostfix(expr):
    tokenList = re.split("([^0-9])", expr)
    stack = Stack()
    for token in tokenList:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

print(evalPostfix ("56 47 + 2 *"))