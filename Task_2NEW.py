class Stack:
    def __init__(self):
        self.__items = []

    def showItems(self):
        print(self.__items)

    def isEmpty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)

    def pop(self):
        return self.__items.pop()


def parenthesesChecker(par_string: str, par_start, par_end):
    stack = Stack()
    balanced = True
    index = 0

    while index < len(par_string) and balanced:
        stack.showItems()
        par = par_string[index]
        print(par)
        if par == par_start:
            stack.push(par)
        elif par == par_end:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()

        index += 1

    if not stack.isEmpty():
        balanced = False
    stack.showItems()

    return balanced

str = '(()({})[]())'
checks = [["(", ")"], ["{", "}"], ["[", "]"]]

for check in checks:
    balanced = parenthesesChecker(str, check[0], check[1])
    if balanced == False:
        break

print(balanced)