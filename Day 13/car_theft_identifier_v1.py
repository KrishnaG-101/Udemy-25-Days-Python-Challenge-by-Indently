# Simple car theft identifier program, check whether a car object initialized is reported stolen or not.

class Car:
    def __init__(self, license_plate : str) -> None:
        if len(license_plate) != 6:
            raise ValueError("Invalid License Plate")
        
        self.license_plate : str = license_plate.upper()
    
    
class StolenCarRegistry:
    def __init__(self) -> None:
        self.stolen_plates : set[str] = set()
        self.stolen_cars_count : int = 0
    
    def add_stolen_plates(self, *plates : str) -> None:
        for plate in plates:
            self.stolen_plates.add(plate.upper())
        
        self.stolen_cars_count = len(self.stolen_plates)
    
    def remove_stolen_plates(self, *plates : str) -> None:
        for plate in plates:
            self.stolen_plates.remove(plate.upper())
        
        self.stolen_cars_count = len(self.stolen_plates)
    
    def is_stolen(self, plate : str) -> bool:
        return (plate.upper() in self.stolen_plates)
    
    def display_stolen_plates(self) -> None:
        print("Stolen Plates:")
        for plate in self.stolen_plates:
            print(f"  {plate}")
    
    def display_stolen_count(self) -> None:
        print(f"Total number of stolen cars: {self.stolen_cars_count}")
    

def main() -> None:
    registry : StolenCarRegistry = StolenCarRegistry()
    
    registry.add_stolen_plates("ABC123", "xyz288", "zzz383", "cal205")
    
    print("Welcome to car theft identifier.")
    while True:
        car_plate_input : str = input("Enter License Plate number: ")
        car : Car = Car(car_plate_input)
        if registry.is_stolen(car.license_plate):
            print(f"❌ The car with {car.license_plate} is: REPORTED STOLEN!")
        else:
            print(f"✅ The car with {car.license_plate} is: OK")


if __name__ == "__main__":
    main()