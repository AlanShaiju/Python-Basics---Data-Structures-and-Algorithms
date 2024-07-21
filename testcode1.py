#unique character length specified by 'k'
# k=3
# string='aabbbbcdcddeeff'
# i=0
# j=0
# unique_elements=[]
# unique_elements.append(string[i])
# maxlen=0
# setlen=0
# print(string[j])
# while len(unique_elements)<=k:
#     if string[i] not in unique_elements:
#         unique_elements.append(string[i])
#     if string[j]==string[i]:
#         j+=1
#         setlen+=1
#     else:
#         if string[j] not in unique_elements:
#             unique_elements.append(string[j])
#         j+=1
#         setlen+=1
#     if maxlen<setlen:
#         maxlen=setlen
#     if len(unique_elements)>k:
#         unique_elements.pop()
#         setlen=0
#         i+=1
#     if j>=len(string):
#         break
# print(maxlen)     

k = 3
string = 'aabbbbhdfsjjjjjjjnsdncsf'
i = 0
j = 0
unique_elements = set()  # Use a set to keep track of unique elements
char_count = {}  # Dictionary to keep count of characters in the current window
maxlen = 0
setlen = 0

while j < len(string):
    # Add the current character to the window
    if string[j] in char_count:
        char_count[string[j]] += 1
    else:
        char_count[string[j]] = 1
    
    unique_elements.add(string[j])
    
    # If the number of unique characters exceeds k, shrink the window from the left
    while len(unique_elements) > k:
        char_count[string[i]] -= 1
        if char_count[string[i]] == 0:
            unique_elements.remove(string[i])
        i += 1
        setlen -= 1
    
    setlen += 1
    maxlen = max(maxlen, setlen)
    j += 1

print(maxlen)