
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


def reverse_list(my_list):
    stack = Stack()

    # варіант 1
    # n = len(my_list) - 1
    # while n >= 0:
    #     stack.push(my_list[n])
    #     n -= 1


    # варіант 2
    for i in my_list:
        stack.push_first(i)

    stack.showItems()

reverse_list([22, 1, 7, 9, 0, 33])


