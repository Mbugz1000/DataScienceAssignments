class HouseHunt:
  
    def __init__(self,portion_down_payment = 0.25,r = 0.04):
        self.portion_down_payment = portion_down_payment
        self.r = r
        

    def userInput(self):
        print("House Hunting Savings Calculator!!!")
        total_cost = int(input("What is the total cost of your dream home? "))
        annual_salary = int(input("What is your annual salary? "))
        portion_saved = float(input("What portion of your salary do you save(In %)? "))/100
        return total_cost, annual_salary, portion_saved

    def calculateMonths(self):
        total_cost, annual_salary, portion_saved = self.userInput()
        savings = annual_salary/12*portion_saved
        down_payment = self.portion_down_payment*total_cost
        months = 0
        current_savings = 0
        
        while current_savings < down_payment:
            #Same as current_savings = Current_savings + Interest + Savings
            current_savings += current_savings*(self.r)/12 + savings
            months += 1
        
        return months

    #Gives us the results
    def results(self):
        months = self.calculateMonths()
        print("-----------------------------------------------------------------")
        if months > 12:
            temp = int(months/12)
            temp1 = months - temp*12
            print("\nThe time necessary to save for the Down Payment is {0} years and {1} months".format(temp, temp1))
        else:
            temp = months
            print("\nThe time necessary to save for the Down Payment is {0} months".format(temp))
        
obj = HouseHunt()
obj.results()