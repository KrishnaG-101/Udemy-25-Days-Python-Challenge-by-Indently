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
        print()
        for plate in plates:
            if plate in self.stolen_plates:
                print(f"License plate {plate} is already in the stolen car registry.")
            else:
                self.stolen_plates.add(plate.upper())
                print(f"License plate {plate} is added to stolen car registry.")
        
        self.stolen_cars_count = len(self.stolen_plates)
    
    def remove_stolen_plates(self, *plates : str) -> None:
        print()
        for plate in plates:
            if plate in self.stolen_plates:
                self.stolen_plates.remove(plate.upper())
                print(f"License plate {plate} is removed from stolen car registry.")
            else:
                print(f"License plate {plate} is not found in the stolen car registry.")
        
        self.stolen_cars_count = len(self.stolen_plates)
    
    def is_stolen(self, plate : str) -> bool:
        return (plate.upper() in self.stolen_plates)
    
    def display_stolen_plates(self) -> None:
        print("Stolen Plates:")
        for plate in self.stolen_plates:
            print(f"  {plate}")
    
    def display_stolen_count(self) -> None:
        print(f"Total number of stolen cars: {self.stolen_cars_count}")
    

def display_options() -> None:
    print("\nOptions:")
    print("0 => Display Options")
    print("1 => Check License Plate")
    print("2 => Report Stolen Plate")
    print("3 => Found Stolen Plate")
    print("4 => Display Stolen Plates")
    print("5 => Count Stolen Plates")
    print("6 => Exit Program")

def main() -> None:
    registry : StolenCarRegistry = StolenCarRegistry()
    
    registry.add_stolen_plates("ABC123", "xyz288", "zzz383", "cal205")
    
    print("Welcome to car theft identifier.")
    display_options()
    while True:
        try:
            user_choice_input : int = int(input("\nYou: "))
            
            match user_choice_input:
                case 0:
                    display_options()
                
                case 1:
                    car_plate_input : str = input("\nEnter License Plate number: ").strip()
                    car : Car = Car(car_plate_input)
                    if registry.is_stolen(car.license_plate):
                        print(f"\n❌ The car with {car.license_plate} is: REPORTED STOLEN!")
                    else:
                        print(f"\n✅ The car with {car.license_plate} is: OK")
                
                case 2:
                    stolen_plate_input : str = input("\nEnter Stolen License Plate number: ").strip()
                    registry.add_stolen_plates(Car(stolen_plate_input).license_plate)
                
                case 3:
                    found_plate_input : str = input("\nEnter Found License Plate number: ").strip()
                    registry.remove_stolen_plates(Car(found_plate_input).license_plate)
                
                case 4:
                    print()
                    registry.display_stolen_plates()
                
                case 5:
                    print()
                    registry.display_stolen_count()
                
                case 6:
                    print("\nThank you for using the program.\n")
                    return None

                case _:
                    raise ValueError("Input out of range")
            
        except ValueError as error:
            print(f"\n{error}. Please enter correct input.")
    

if __name__ == "__main__":
    main()
    
# annotation and doc strings are to be added.