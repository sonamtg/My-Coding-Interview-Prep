''' Question 1.2 Check Permutation:- Given two strings, write a method to decide if one is a 
permutation of the other'''

from tkinter.tix import ExFileSelectBox


def checkPermutation(str1, str2):
    # if they have different length, they are different
    if (len(str1) != len(str2)):
        return False
    
    table1 = {}
    for i in range(len(str1)):
        if (str1[i] in table1):
            table1[str1[i]] += 1
        else:
            table1[str1[i]] = 1
            
    table2 = {}
    for j in range(len(str2)):
        if (str2[j] in table2):
            table2[str2[j]] += 1
        else:
            table2[str2[j]] = 1
            
    if (table1 == table2):
        return True
    
    else:
        return False
    
def main():
    print(checkPermutation("sonam", "msano"))
    print(checkPermutation("sonam", "sano"))
    print(checkPermutation("sonam", "msanotg"))
    print(checkPermutation("sonam", "manos"))
  
if __name__ == "__main__":
    main()
            
            
        
    