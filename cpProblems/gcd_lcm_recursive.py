class Solution14 :
    # self- connects the function to the object instance.
    def gcdRec(self,a,b):
        if a%b==0:
            return b
        return self.gcdRec(b,a%b)
        

    def lcm (self,a,b): 
        return (a*b)//self.gcdRec(a,b) #return int

