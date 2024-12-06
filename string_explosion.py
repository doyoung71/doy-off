def string_explosion(original, bomb):
    stack = []
    bomb_length = len(bomb)

    for char in original:
        stack.append(char)
        if len(stack) >= bomb_length and ''.join(stack[-bomb_length:]) == bomb:
            for _ in range(bomb_length):
                stack.pop()

    return ''.join(stack) if stack else "FRULA"

if __name__ == "__main__":
    original_string = input().strip()
    bomb_string = input().strip()
    result = string_explosion(original_string, bomb_string)
    print(result)
