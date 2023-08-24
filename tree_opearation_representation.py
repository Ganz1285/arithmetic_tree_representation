import re

high_precedence=[]
low_precedence=[]

class operator:
    def __init__(self,op,l,r):
        self.op=op
        self.l=l
        self.r=r
        self.result=None
        self.left=None
        self.right=None


    def representation(self):
        print(str(self.l)+" "*(len(str(self.result)))+str(self.r))
        print(" "*(len(str(self.l))-1)+"\\"+self.op.center((len(str(self.result)))," ")+"/")
        print(" "*len(str(self.l))+str(self.result))
 
    



def splitter(s):
    ext=""
    recent=None
    for i in range(len(s)):
        if s[i].isdigit():
            ext+=s[i]
        else:
            op=s[i]
            l=ext
            r=""
            for j in range(i+1,len(s)):
                if s[j].isdigit():r+=s[j]
                else:break
            root=operator(op,l,r)
            if not recent:
                recent=root
            else:
                root.left=recent
                recent.right=root
                recent=recent.right
            
            if op in "*/":high_precedence.append(root)
            else:low_precedence.append(root)
            ext=""

def valid_operation(s):
    """
    check if first and last elements are operands. not operators
    """
    pattern=r"^[0-9][0-9+\-*/]*[0-9]$"
    return re.match(pattern,s)

def parse():

    root=high_precedence[0] if high_precedence!=[] else low_precedence[0]
    pend=None
    if root.left:
        pend=root.left
    while root:
        print(root.l,root.op,root.r)
        root=root.right
    while pend.left:pend=pend.left    
    while pend:
        print(pend.l,pend.op,pend.r)
        pend=pend.right



def main():
    s=input()
    if valid_operation(s):
        print("VALID")
    else:
        print("INVALID")

    splitter(s)
    parse()



if __name__=="__main__":
    main()
