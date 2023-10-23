#example 1 
#example of class with decorators , using the property in the old fashioned way WITHOUT @
# be sure to define all attributes in the constructor ( they oo not need to be referred to when calling the class ). In this example when creating an object from class BankAccount we only provide the name for the bank Account . The balance is set to 0 in the background and is not even referred to as an attribute at this stage 
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    # Write your code here

    def get_balance(self):
        return round(self._balance)
    
    #use the property to check the constraints (range , type )
    def set_balance(self, balance):
        # a cool way to check if a provided value is a number
        if type(balance) not in [int, float]:
            return
        # if the condition is met - EI the value is NOT an INT and NOT and Float - > return without making the balance as self._balance, nothing happens 
        
        if balance < 0 or balance >= 100000 :
            return
        # if the condition is met ( the value is too high or too low ) -> return without making the balance as self._balance , nothing happens 
        
        #none of the constraints apply, we can set the value of balance to our attribute _balance 
        self._balance = balance
    
    
    
    
# example 2 
# example of a class with decorators , using the @ syntax 


class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) not in [int, float]:
            return
        if balance < 0 or balance >= 100000 :
            return
        self._balance = balance
                