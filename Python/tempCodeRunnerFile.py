openList = ["[", "{", "("]
# closeList = ["]", "}", ")"]


# def balance(myStr):
#     stack = []
#     for i in myStr:
#         if i in openList:
#             stack.append(i)
#         elif i in closeList:
#             pos = closeList.index(i)
#             if stack and (openList[pos] == stack[-1]):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"