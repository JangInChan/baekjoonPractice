import sys

input = sys.stdin.readline
li = input().rstrip('\n')
stack = []
ans = ''
for i in li:
    if i.isupper():
        ans += i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
while stack:
    ans += stack.pop()
print(ans)