class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        prev_operator = "+"
        curr_num = 0
        s.split("+")
        operators = set(["+","/","*","-"])
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                curr_num = (curr_num * 10) + int(char)
            if char in operators or i == len(s)-1:
                if prev_operator == None:
                    stack.append(curr_num)
                elif prev_operator == "+":
                    stack.append(curr_num)
                elif prev_operator == "-":
                    stack.append(-curr_num)
                elif prev_operator == "*":
                    lastVal = stack.pop()
                    res = lastVal * curr_num
                    stack.append(res)
                else:
                    lastVal = stack.pop()
                    res = int(lastVal / curr_num)
                    stack.append(res)

                curr_num = 0
                prev_operator = char
        
        return sum(stack)

                



  
