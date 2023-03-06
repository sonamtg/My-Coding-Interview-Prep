'''Question 1.3:- URLify, replacing all spacees in a string with %20'''

def urlify(str1, len):
    newstr1 = ""
    count = 0
    for i in range(len):
        if str1[i] == ' ':
            newstr1 += '%'
            newstr1 += '2'
            newstr1 += '0'
        else:
            newstr1 += str1[i]
    
    return newstr1

def main():
    print(urlify("Mr John Smith", 13))

if __name__ == "__main__":
    main()