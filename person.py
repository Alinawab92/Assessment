class Person:
    def __init__(self, name, email):
        self.email = email
        self.name = name

    def check_in(self):   
        return f"{self.name} is checked IN"
    
    def check_out(self):   
        return f"{self.name} is checked OUT"
