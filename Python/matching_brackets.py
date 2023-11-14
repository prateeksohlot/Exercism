def is_paired(input_string):
    '''
    It finds brackets are paired or not in the string.
    :param input_string: string
    :return: boolean
    '''
       
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in bracket_map.values():
            # If it's an opening bracket, push it onto the stack.
            stack.append(char)
        elif char in bracket_map:
            # If it's a closing bracket, check if the top of the stack is the corresponding opening bracket.
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    # If the stack is empty, all brackets were matched and properly nested.
    return not stack

print(is_paired('({)}'))
print(is_paired('({})'))
print(is_paired('({[]})'))