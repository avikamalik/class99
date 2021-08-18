info=input ("write a few lines about yourself: ")
charactercount=0
wordcount=1

for i in info:
    charactercount+=1
    if (i==" "):
        wordcount+=1
        charactercount-=1

print ("character count: ", charactercount)
print ("word count: ", wordcount)