class Queue:
    def __init__(self):
        self.__items = []


    def insert_item(self, item):
        self.__items.append(item)

    def delete(self):
        if not self.is_empty():
            return self.__items.pop(0)
        else:
            raise IndexError("delete from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.__items[0]
        return None

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def size(self) -> int:
        return len(self.__items)

    def __str__(self):
        return str(self.__items)


my_quee = Queue()

my_quee.insert_item(1)
my_quee.insert_item(4)
my_quee.insert_item(5)
my_quee.insert_item(6)
print(my_quee)
print(my_quee.peek())
print(my_quee.size())
my_quee.insert_item(6)
print(my_quee)
print(my_quee.peek())
print(my_quee.size())
print(my_quee.delete())

print(my_quee)