# -*- coding: utf-8 -*-
class GuessingGame:
    guess = 0
    guessNo = 0
    
    def displayAnswer(self,guess,guessNo):
        print("\nThe number in your head is %d" % guess )
        print("No of guesses: %d" % guessNo)
        
    def insertUpper(self):
        x = int(input("Enter the Upper limit: "))
        return x
        
    def start(self):
        low = 0
        epsilon = 0.5
        answer = ""
        v = True
        
        print("Welcome to the Guessing Game!!!")
        
        high = self.insertUpper()
        while high > 1000000:
            print("Number is too high, kindly enter the upper limit again.")
            high = self.insertUpper()
            
        print("Kindly answer these qns with a y or n")
        self.guess = (high)/2
        while abs(high - self.guess) > epsilon and v:
            answer = input("Is it %d? " % self.guess)
            if answer == "n":
                answer = input("Is it above %d? " % self.guess)
                if answer == "y":
                    low = self.guess
                elif answer == "n":
                    high = self.guess
                else:
                    break
            elif answer == "y":
                v = False
            else:
                break
                
            self.guess = (high-low)/2 + low
            self.guessNo += 1
                   
        self.displayAnswer(self.guess,self.guessNo)
                

game = GuessingGame()
game.start()