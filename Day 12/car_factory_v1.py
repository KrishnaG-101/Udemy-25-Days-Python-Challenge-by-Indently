# Program for car factory, allows user to create, display, sell cars and save the earned amount.

from collections import Counter
from time import sleep


class Car:
    def __init__(self, brand : str, model : str, color : str, price : float) -> None:
        self.brand : str = brand
        self.model : str = model
        self.color : str = color
        self.price : float = price
    
    def drive(self, distance : int, speed : float) -> None:
        print(f"{self.brand} {self.model} started its journey....")
        
        for covered in range(1, distance + 1):
            sleep(60/speed)
            print(f"Distance Covered: {covered} KM")
        
        print(f"{self.brand} {self.model} completed its journey....")


def display_options() -> None:
    print("\nOptions:")
    print("0 => Display Options")
    print("1 => Check Inventory")
    print("2 => Create Cars")
    print("3 => Exit Program")

def display_inventory(cars : list[Car]) -> None:
    cars_details : list[tuple[str, str, str, float]] = [(car.brand, car.model, car.color, car.price) for car in cars]
    inventory_counter : Counter[tuple[str, str, str, float]] = (Counter(cars_details))
    
    print("-"*28)
    print("Inventory:")
    for (brand, model, color, price), count in inventory_counter.items():
        print(f"{brand} {model} [{color}] [\u20B9{price:,}]: {count} in stock")
    print("-"*28)

def create_cars() -> list[Car]:
    cars_list : list[Car] = list()
    print("\nCarefully enter details for the following:")
    try:
        brand : str = input("Enter Brand Name: ").lower().strip()
        model : str = input("Enter Model Name: ").lower().strip()
        color : str = input("Enter Color: ").lower().strip()
        price : float = float(input("Enter Car's Price: "))
        production : int = int(input("Enter number of Units to produce: "))
        for _ in range(production):
            cars_list.append(Car(brand, model, color, price))
    except ValueError as error:
        print(f"\n{error}. Enter details correctly in digits.")
    
    return cars_list

def main() -> None:
    # test_obj : Car = Car(brand="Toyota", model="Fortuner", color="White", price=50_00_000)
    # test_obj.drive(distance=10, speed=100)
    
    # list[Car]
    # display stock
    # extend using create_cars
    
    display_options()                        # Prints options to the terminal console
    
    cars_inventory : list[Car] = list()      # To represent the cars in inventory.
    
    while True:
        try:
            user_option_input : int = int(input("\nEnter your choice: "))
            match user_option_input:
                case 0:
                    display_options()
                case 1:
                    display_inventory(cars=cars_inventory)
                case 2:
                    cars_inventory.extend(create_cars())
                case 3:
                    print("\nThank you for using the program.")
                    return None
                case _:
                    raise ValueError("Input out of range")
                
        except ValueError as error:
            print(f"\n{error}. Please enter choice in digits and in range.")
    

if __name__ == "__main__":
    main()

# The task of create_cars() is too memory intensive, and unnecessarily redundant, replace that with a dictionary, and we won't need a counter as well.
# Have to add a function for selling cars
# Have to add functionality of maintaining a bank, cars sold would increase bank balance.