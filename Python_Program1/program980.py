class Arithematic:
    
    # Constructor
    def __init__(self,A = 0, B = 0):
        self.No1 = A                    # Chararcteristics
        self.No2 = B                    # Chararcteristics
        
    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Subtraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

def main(): 
    aobj = Arithematic()
    
    Ret = aobj.Addition()
    
    print("Addition is : ",Ret)
    
    Ret = aobj.Subtraction()
    print("Subtraction is : ",Ret)
    
main()