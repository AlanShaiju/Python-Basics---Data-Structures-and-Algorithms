#unique character length specified by 'k'
k=3
string='aabbbbcdcddeeff'
i=0
j=0
unique_elements=[]
unique_elements.append(string[i])
maxlen=0
setlen=0
print(string[j])
while len(unique_elements)<=k:
    if string[i] not in unique_elements:
        unique_elements.append(string[i])
    if string[j]==string[i]:
        j+=1
        setlen+=1
    else:
        if string[j] not in unique_elements:
            unique_elements.append(string[j])
        j+=1
        setlen+=1
    if maxlen<setlen:
        maxlen=setlen
    if len(unique_elements)>k:
        unique_elements.pop()
        setlen=0
        i+=1
    if j>=len(string):
        break
print(maxlen)     