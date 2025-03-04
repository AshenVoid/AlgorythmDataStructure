class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def stack_pop(self):
        if not self.isEmpty():
            return self.__items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.__items[-1]
        return None

    def isEmpty(self) -> bool:
        return len(self.__items) == 0

    def size(self) -> int:
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

def are_parenthesis_valid(string: str) -> bool:
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in pairs.values():       #yeet na stack když open
            stack.push(char)
        elif char in pairs:     #když close
            if stack.isEmpty() or stack.stack_pop() != pairs[char]:      #validace contentu a kontrola výstřelu (y)
                return False
    return stack.isEmpty()      #když true my gucci

'''
input = "())"  #False
input0 = "({})" #True
input1 = "({({}[])[]})" #True
input2 = "({({}[])[})" #False
# ------------------------ Level 2 -------------------
input3 = "(8*5{8({3+8}-[5-8])+[9*0]})" #True
input4 = "(8*5{8({3+8-[5-8])+[9*0]})" #False
input5 = "(8*5{8(3+8}-[5-8])+[9*0]})" #False
'''

inputs = [
    "())",  # False
    "({})", # True
    "({({}[])[]})", # True
    "({({}[])[})", # False
    "(8*5{8({3+8}-[5-8])+[9*0]})", # True
    "(8*5{8({3+8-[5-8])+[9*0]})", # False
    "(8*5{8(3+8}-[5-8])+[9*0]})" # False
]

for inp in inputs:
    print(f"{inp}: {are_parenthesis_valid(inp)}")