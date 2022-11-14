
class Stack:
    def __init__(self):
        self.__items = []

    def showItems(self):
        print(self.__items)

    def isEmpty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def push_first(self, item):
        self.__items.insert(0, item)

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)

    def pop(self):
        return self.__items.pop()

    def get_from_stack(self, value):
        for i in range(len(self.__items)):
            if value == self.__items[i]:
                self.__items.pop(i)
                return value

        raise ValueError ("There is a missing element in the stack")

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("chjghf")
stack.push("d")
stack.showItems()
print(stack.get_from_stack("bfreg"))
stack.showItems()

