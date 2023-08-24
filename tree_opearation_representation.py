import re


class operator:
    def __init__(self,op,l,r):
        self.op=op
        self.l=l
        self.r=r
        self.result=int(eval(self.l+self.op+self.r))

    def representation(self):
        print(str(self.l)+" "*(len(str(self.result)))+str(self.r))
        print(" "*(len(str(self.l))-1)+"\\"+self.op.center((len(str(self.result)))," ")+"/")
        print(" "*len(str(self.l))+str(self.result))
 
def extracter(s,ind):
    z=""
    for i in range(ind-1,-1,-1):
        if s[i].isdigit():
            z+=s[i]
        else:
            break
    z=z[::-1]
    p=""
    for i in range(ind+1,len(s)):
        if s[i].isdigit():
            p+=s[i]
        else:
            break
    return (z,p) 
    



def splitter(s):
    l=[]
    while '*' in s:
        x=s.index('*')
        l.append((('*'),extracter(s,x)))
        s=s[:x]+'~'+s[x+1:]
    while '/' in s:
        x=s.index('/')
        l.append((('/'),extracter(s,x)))
        s=s[:x]+'~'+s[x+1:]
    while '+' in s:
        x=s.index('+')
        l.append((('+'),extracter(s,x)))
        s=s[:x]+'~'+s[x+1:]
    while '-' in s:
        x=s.index('-')
        l.append((('-'),extracter(s,x)))
        s=s[:x]+'~'+s[x+1:]
 
    return l





def valid_operation(s):
    """
    Split input by operators
    check if first and last elements are operands. not operators
    """
    pattern=r"^[0-9][0-9+\-*/]*[0-9]$"
    if re.match(pattern,s):
        cond=True
        for i in splitter(s):
            if i[1][0].isdigit() and i[1][1].isdigit():
                pass
            else:
                cond=False
    else:
        cond=False
    return cond



def main():
    s=input()
    if valid_operation(s):
        print("VALID")
    else:
        print("INVALID")
    l=[]
    for i in splitter(s):
        l.append(operator(i[0],i[1][0],i[1][1]))
    for i in l:
        i.representation()

if __name__=="__main__":
    main()
