n=[]
for i in range(2):
    inputs=input()
    n=n+[inputs]
#print(n)
if(n[0]==n[1]):
    print("Please enter two different cities")
else:
    utt=[]
    utt=utt+[ "How far is "+n[0]+" from "+n[1] ]+["How far is "+n[1]+" from "+n[0]]+["How is the weather in "+n[0]]+["How is the weather in "+n[1]]
    print(utt)
