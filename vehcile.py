class Vehicle:
    def __init__(self, vehicle_type, model):
        self.vehicle_type = vehicle_type
        self.model = model

    def get_vehicle_type(self):
        return f"Your vehicle type is: {self.vehicle_type} and model number is: {self.model}"
    
# Example usage
if __name__ == "__main__":
    r1 = Vehicle("Hybrid", 2024)
    print(r1.get_vehicle_type())
