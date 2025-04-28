class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def call(self,number):
        print(f"Calling {number} from {self.brand} {self.model}")
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"
    
    # Inheritance
    class SmartphoneWithCamera(Smartphone):
        def __init__(self, brand, model, price, camera_megapixels):
            super().__init__(brand, model, price)
            self.camera_megapixels = camera_megapixels
        def take_photo(self):
            print(f"Taking a photo with {self.camera_megapixels} MP camera")
        def __str__(self):
            return f"{super().__str__()} with {self.camera_megapixels} MP camera"

# Example usage
if __name__ == "__main__":
    # Create a smartphone object
    phone = Smartphone("Apple", "iPhone 10", 999)
    print(phone)
    phone.call("123-456-7890")
    
    # Create a smartphone with camera object
    camera_phone = Smartphone.SmartphoneWithCamera("Samsung", "Galaxy S21", 799, 108)
    print(camera_phone)
    camera_phone.take_photo()

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving "

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())