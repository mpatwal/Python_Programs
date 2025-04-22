def is_balanced(string):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0


string = input("Enter a string with parentheses: ")

if is_balanced(string):
    print("The string has balanced parentheses.")
else:
    print("The string does NOT have balanced parentheses.")
