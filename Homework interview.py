from collections import deque


class Stack:

    #1 задание
    def __init__(self, my_stack):
        self.stack = my_stack

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, element):
        self.stack.appendleft(element)

    def pop(self):
        return self.stack.popleft()

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    # 2 задание
    def bracket_balance(self, bracket_list):
        self.stack.clear()
        for bracket in bracket_list:
            if bracket in ["(", "[", "{"]:
                self.push(bracket)
            else:
                if self.isEmpty() is True:
                    return print("Несбалансировано")
                left_bracket = self.pop()
                if left_bracket == "(":
                    if bracket != ")":
                        return print("Несбалансировано")
                if left_bracket == "[":
                    if bracket != "]":
                        return print("Несбалансировано")
                if left_bracket == "{":
                    if bracket != "}":
                        return print("Несбалансировано")
        if self.isEmpty() is False:
            return print("Несбалансировано")
        return print("Cбалансировано")


if __name__ == "__main__":
    run = Stack(my_stack=deque([['o', 'p', 'q'], 'abc', 2, 3, 'a']))
    run.isEmpty()
    run.push("qwerty")
    run.pop()
    run.peek()
    run.size()
    run.bracket_balance("[([])((([[[]]])))]{()}")
