def IS_palindrom(str):
    org_string= str.lower()

    rev_str = str[::-1]

    if org_string == rev_str:
        print("The given sting is palindrome ", org_string ,"=", rev_str)

    else:
        print("The given string is not a palindrom ", org_string,"!=",rev_str)


print("Palindrom checker ")
str = input("Enter the word to find palindrom  : ")
IS_palindrom(str)

