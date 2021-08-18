def hello():
    filename=input("enter file name: ")
    count=0
    file=open(filename,"r")
    countl=0
    for i in file:
        words=i.split()
        count=count+len(words)
        countl=countl+1

    
    print (count,countl)

hello()