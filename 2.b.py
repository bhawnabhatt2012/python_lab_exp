index = 0
string = input("Enter the string: ")
substring = input("Enter the substring: ")
if substring in string:
    print(substring," is present in ",string)
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        print(substring, ' found at', index)
        index += len(substring)
    print('No. of occurences of',substring,': ',string.count(substring))
else:
    print(substring," is not present in ",string)