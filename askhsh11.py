print('Δώστε 6 αριθμούς!(Τυχόν δεκαδικοί αριθμοί να χρησιμοποιούν τον χαρακτήρα "." για την διάκριση του δεκαδικού από το ακέραιο μέρος)')
x1=input()
x2=input()
x3=input()
x4=input()
x5=input()
x6=input()
s=0
with open('list.txt','r') as f:
    for line in f:
        if s!=4:
            s=0
            l=list(line.split(","))
            l[3]=l[3].replace("\n","")
            if x1==l[0] or x2==l[0] or x3==l[0] or x4==l[0] or x5==l[0] or x6==l[0]:
                s=s+1
                l[0]=""
            if x1==l[1] or x2==l[1] or x3==l[1] or x4==l[1] or x5==l[1] or x6==l[1]:
                s=s+1
                l[1]=""
            if x1==l[2] or x2==l[2] or x3==l[2] or x4==l[2] or x5==l[2] or x6==l[2]:
                s=s+1
                l[2]=""
            if x1==l[3] or x2==l[3] or x3==l[3] or x4==l[3] or x5==l[3] or x6==l[3]:
                s=s+1
                l[3]=""                    
if s==4:
    print('Υπάρχει διαθέσιμη 4τράδα από αυτούς τους 6 αριθμούς!')
else:
    print('Δεν υπάρχει διαθέσιμη 4τράδα από αυτούς τους 6 αριθμούς!')
f.close()    
                
