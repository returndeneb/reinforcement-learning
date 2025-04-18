import sys

def is_balanced(line):
    stack = []
    brackets = {')': '(', ']': '['}
    
    for char in line:
        if char in "([":  # 여는 괄호는 스택에 추가
            stack.append(char)
        elif char in ")]":  # 닫는 괄호가 나오면 스택 확인
            if not stack or stack[-1] != brackets[char]:
                return "no"
            stack.pop()
    
    return "yes" if not stack else "no"

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()  # 개행 문자 제거
        if line == ".":
            break
        print(is_balanced(line))
