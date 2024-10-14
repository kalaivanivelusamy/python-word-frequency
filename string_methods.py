def join_strings():
    join_str= "...".join(["This", "is", "joined","by","triple","dots"]) # a...b...c
    print(join_str)


def concatenate_String():
    str1 = "Hello"
    str2 = "World"
    str3 = str1 + str2
    print(str3)

#Test cases
#concatenate_String()
#expected: HelloWorld
print("---This is example of Concatenate String---")
concatenate_String()

#join_strings()
#expected: This...is...joined...by...triple...dots
print("---This is example of Join String---")
join_strings()