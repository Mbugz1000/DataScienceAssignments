class BestSavingsRate(object):
    annual_salary = 0
    
    def __init__(self, portion_down_payment = 0.25, r = 0.04, semi_annual_raise = 0.07,total_cost = 100000000):
        self.portion_down_payment = portion_down_payment
        self.r = r
        self.semi_annual_raise = semi_annual_raise
        self.total_cost = total_cost
        
    def userInput(self):
        print("Best Savings Rate Calculator!!!")
        return int(input("What is your annual starting salary? "))
        
    #Portion saved will be our guess in the bisection search
    def calculateMonths(self, portion_saved, loops):
        
        if loops == 0:
            self.annual_salary = self.userInput()
        savings = self.annual_salary/12*portion_saved
        down_payment = self.portion_down_payment*self.total_cost
        months = 0
        current_savings = 0
        
        while months != 36:
            #Same as current_savings = Current_savings + Interest + Savings    
            current_savings += current_savings*(self.r)/12 + savings
            
            if months%6 == 0 and months!=0:
                #same as savings = savings + semi_annual_raise
                savings += savings*self.semi_annual_raise
                    
            months += 1
        
        return down_payment, current_savings

    #Gives us the results
    def results(self,method):
        portion_saved, guessNo, current_savings, down_payment = method
        print("_________________________________________________________________________________")
        if guessNo < 30:
            print("\nThe best saving rate to make the down payment is [{0:.2f} percent]".format(portion_saved))
            print("There were [{0} guesses] for savings of [Ksh {1:.2f}] (Down Payment: {2} )in [36 months]".format(guessNo, current_savings,down_payment))
        else:
            print("\nYour annual salary is insufficient to make the down payment in [36 months]")
       
        
        
class BisectionSearch:
    
    def __init__(self, guess = 0, guessNo = 0):
        #Same as the portion saved
        self.guess = guess
        self.guessNo = guessNo
        
    def start(self,saveingsRateObj):
        high = 10000
        low = 0
        epsilon = 100000
        guess = self.guess
        guessNo = self.guessNo
        down_payment = 100001
        current_savings = 0
        
        guess = (high)/2
        while abs(down_payment - current_savings) > epsilon and guessNo < 30:
            #Divide guessby 10000 so it can be a decimal rate for portion saved
            down_payment, current_savings = savingsRateObj.calculateMonths(guess/10000, guessNo)
            
            if current_savings < down_payment - epsilon:
                low = guess
            elif current_savings > down_payment + epsilon:
                high = guess
            
            guess = (high-low)/2 + low
            guessNo += 1
                   
        #Divide by 100 to get the Percentage
        return guess/100, guessNo, current_savings, down_payment
        
    
biSearchObj = BisectionSearch()
savingsRateObj = BestSavingsRate()
savingsRateObj.results(biSearchObj.start(savingsRateObj))

