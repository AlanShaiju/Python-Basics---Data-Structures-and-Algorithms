str1='abcd'
str2='bcad'
print(len(str1))
str1=list(str1)
str2=list(str2)
str1.sort()
str2.sort()
if str1==str2:
    print('Anagram')
else:
    print('Not Anagrams')