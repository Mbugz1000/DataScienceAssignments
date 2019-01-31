import math

class MathProb:
    x = 0
    y = 0
    
    def start(self):
        #Using loop and try-except-else to do a number type check
        while True:
            try:
                self.x = int(input("Enter first number: "))
            except ValueError:
                print("Kindly enter an integer")
                continue
            else:
                break
            
        while True:
            try:
                self.y = int(input("Enter second number: "))
            except ValueError:
                print("Kindly enter an integer")
                continue
            else:
                break
        
        print("{0} raised to {1} is {2}".format(self.x,self.y,self.x**self.y))
        print("Log of {0} is {1}".format(self.x,math.log(self.x)))
        
        
obj = MathProb()
obj.start()