''' Question 1.1
Is Unique:- Implement an algorithm to deetermine if a string has all unique characters.'''

# using a hash table first
# Time complexity - O(n)
# Space complexity - O(n)

def isUnique(str):
    table = {}
    
    for i in range(len(str)):
        if str[i] in table:
            return False
        
        # we reach here only if the letter is unique or appearing for the 1st time
        table[str[i]] = 1
    
    return True

def main():
    print(isUnique("Sonam"))
    print(isUnique("Sonam Gurung"))
    print(isUnique("repeated"))
    print(isUnique("acdeghuopy"))

if __name__ == "__main__":
    main()