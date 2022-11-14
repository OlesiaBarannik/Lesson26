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


def parenthesesChecker(par_string: str):
    stack = Stack()
    stack2 = Stack()

    balanced = True
    i = 0

    while i < len(par_string) and balanced:
        stack.showItems()
        par = par_string[i]
        print(par)

        if par == "(" :
            stack.push(par)
        elif par == "{" :
            stack2.push(par)
        else:
            if par == ")":
                if stack.isEmpty():
                    balanced = False
                else:
                    stack.pop()
            elif par == "}":
                if stack2.isEmpty():
                    balanced = False
                else:
                    stack2.pop()

        i += 1

    if not stack.isEmpty() or not stack2.isEmpty():
        balanced = False
    stack.showItems()
    stack2.showItems()
    print(balanced)

parenthesesChecker('(({}{}})()())')