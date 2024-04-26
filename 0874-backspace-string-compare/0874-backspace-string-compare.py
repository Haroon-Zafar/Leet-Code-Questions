class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first_string = s
        second_string = t
        first_stack = []
        second_stack = []
        for string in first_string:
            if string == "#":
                first_stack = first_stack[0:len(first_stack)-1]
            else:
                first_stack.append(string)
        print(first_stack)
        for string in second_string:
            if string == "#":
                second_stack = second_stack[0:len(second_stack)-1]
            else:
                second_stack.append(string)
        return(first_stack == second_stack)