n=int(input("enter first digit : "))
m=int(input("enter second digit : "))
o=int(input("enter third digit : "))
digit=[n,m,o]
for i in digit:
    for j in digit:
        for k in digit:
            if i!=j and j!=k and k!=i:
                print(i,j,k)


 

