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


my_stack = Stack()
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.peek())  # 5
print(my_stack.size())  # 3
my_stack.push(6)
print(my_stack.peek())  # 6
print(my_stack.size())  # 4
print(my_stack.stack_pop())  # 6
print(my_stack)  # [3, 4, 5]