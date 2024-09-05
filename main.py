from person import Person
from customer import Customer
from worker import Worker
from registration import Registration
from car_wash import CarWash, SoapOnly, ExtraService, LuxuryService

# Add data for the Customer class     
c1 = Customer("Alice", "alice@example.com", "12-12-2000")
print(c1.membership_date)
print(c1.payment_process(13000)) 

# Add data for Person class (check-in, check-out)    
c2 = Person("Ali", "bisma@gmail.com")
print(c2.check_out())

# Creating Worker objects with composition relation to Regist_Record
w1 = Worker("John Doe", "john.doe@example.com", 50000, "Engineer")
w2 = Worker("Jane Smith", "jane.smith@example.com", 55000, "Manager")
w3 = Worker("Abdullah", "abd@example.com", 550, "Technician")

# Display worker details and history
print(w3.display_details())  # Output worker details with current position

# Change position for w3 and add to history
w3.change_position("Supervisor")
w3.change_position("Manager")

# Show full position history for w3
print(w3.display_full_history())  # Output: Position History: Technician, Supervisor, Manager

# Example usage of Registration class
r1 = Registration("3:00", "5:00", "2nd time comes")
print(r1.update("10:00", "2:00", "4th time comes")) 
print(r1.get_details())

# Example usage of CarWash classes
p1 = CarWash(100)
print(p1.perform_wash())

p2 = SoapOnly(100)
print(p2.apply_basic_service())

p3 = ExtraService(200)
print(p3.apply_extra_service())

p4 = LuxuryService(500)
print(p4.apply_luxury_service())
