class CarWash:
    def __init__(self, wash_price):
        self.wash_price = wash_price

    def perform_wash(self):
        if self.wash_price == 100:
            return "Rs.100 for soap only"
        elif self.wash_price == 200:
            return "Rs.200 for soap and polish"
        elif self.wash_price == 500:
            return "Rs.500 for soap, polish, and inner clean"
        else:
            return "Invalid amount"

class SoapOnly(CarWash):
    def __init__(self, wash_price):
        super().__init__(wash_price)

    def apply_basic_service(self):
        if self.wash_price == 100:
            return "Applying soap only wash"
        else:
            return "Invalid amount"

class ExtraService(CarWash):
    def __init__(self, wash_price):
        super().__init__(wash_price)

    def apply_extra_service(self):
        if self.wash_price == 200:
            return "Applying soap and polish wash"
        else:
            return "Invalid amount"

class LuxuryService(CarWash):
    def __init__(self, wash_price):
        super().__init__(wash_price)

    def apply_luxury_service(self):
        if self.wash_price == 500:
            return "Applying soap, polish, and inner clean wash"
        else:
            return "Invalid amount"

# Example usage
if __name__ == "__main__":
    # For price
    p1 = CarWash(100)
    print(p1.perform_wash())
