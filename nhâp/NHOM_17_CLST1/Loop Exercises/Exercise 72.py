string = input("Enter a string: ")
palindrome=True
left=0
right=len(string)-1
while left < right:
    if string[left] != string[right]:
        palindrome = False
        break
    left = left + 1
    right = right - 1
if palindrome==True:
    print(string,"is a palindrome.")
else:
    print(string,"is not a palindrome.")