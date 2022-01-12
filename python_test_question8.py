d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
d3=dict()
#this for loop is used for taking common keys and printing the output
for i in d1.keys():
    for j in d2.keys():
        if(i==j):
            sum=d1[i]+d2[j]
            d3[i]=sum
#print(d3)
#this loop is used for remaining keys which is not common in both the dictionaries
d1keys=d1.keys()
d2keys=d2.keys()
for i in d2keys:
    if(i not in d3):
        d3[i]=d2[i]
for i in d1keys:
    if(i not in d3):
        d3[i]=d1[i]
print(d3)
