with open('word2.txt','r') as f:
    data=f.read()
    data=data.replace(".","")
    data=data.replace("(","")
    data=data.replace(")","")
    data=data.replace(",","")
    data=data.replace("!","")
    data=data.replace(":","")
    data=data.replace("’","")
    data=data.replace("‘","")
    data=data.replace("–"," ")
    data=data.replace(";","")
    data=data.replace('”','')
    data=data.replace("-"," ")
    data=data.replace('“','')
    data=data.replace('…',' ')
    with open('word2.txt','w') as f:
        f.truncate()
        f.write(data)
with open('word2.txt','r') as f:
    for line in f:
        for word in line.split():
            sum=0
            l=len(word)
            letters=list(word)
            for i in range(0,l):
                if letters[i]=="f" or letters[i]=="c" or letters[i]=="r" or letters[i]=="k" or letters[i]=="F" or letters[i]=="C" or letters[i]=="R" or letters[i]=="K":
                    sum=sum+1        
            if sum>(l-sum):
                print(word,"/","Bad Word")
            elif sum<=(l-sum):
                print(word,"/","Good Word") 
f.close()
