# Time and Memory complexity = O(n) 

def isValid(str):
    # creating a stack to store the opening parenthesis
    stack = []
    # hashmap to check whether the closing matches the opening parenthesis
    matching = {"]" : "[", ")" : "(", "}" : "{"}
    
    for c in str:
        if c in matching:
            if stack and stack[-1] == matching[c]:
                stack.pop()
            
            else:
                return False
            
        else:
            stack.append(c)
            
    return True if not stack else False

def main():
    print(isValid("({{}})"))
    print(isValid("}({{}})"))
    print(isValid("{}({{}})"))
    print(isValid("{}[]({{}}){(})"))


    
if __name__ == "__main__":
    main()