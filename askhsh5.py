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
            l=len(word)
            letters=list(word)
            if l>3:
                word.replace(letters[0],"")
                word=word+letters[0]+"ay"
            print(word)
f.close()
