from person import Person

class Customer(Person):
    def __init__(self, name, email, membership_date):
        super().__init__(name, email)  # Initialize name and email using the Person class constructor
        self.membership_date = membership_date
    
    def payment_process(self, amount):
        self.amount = amount
        return f"{self.name}, your final amount is {self.amount}"
