# Program for car factory, allows user to create, display, sell cars and save the earned amount.

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
    print("2 => Check Bank")
    print("3 => Create Cars")
    print("4 => Sell Cars")
    print("5 => Exit Program")

def display_inventory(cars : dict[Car, int]) -> None:
    print("\nInventory:")
    print("-"*28)
    for car_object, count in cars.items():
        print(f"{car_object.brand.capitalize()} {car_object.model.capitalize()} [{car_object.color}] [\u20B9{car_object.price:,}]: {count} in stock")
    print("-"*28)

def create_cars(cars : dict[Car, int]) -> None:
    print("\nCarefully enter details for the following:")
    try:
        # Taking Inputs
        brand_input : str = input("Enter Brand Name: ").lower().strip()
        model_input : str = input("Enter Model Name: ").lower().strip()
        color_input : str = input("Enter Color: ").lower().strip()
        price_input : float = float(input("Enter Car's Price: "))
        production_input : int = int(input("Enter number of Units to produce: "))
        
        # check if same car already exists, if does then update the count, else create a new entry.
        for car in cars.keys():
            if (car.brand == brand_input and car.model == model_input and car.color == color_input and car.price == price_input):
                # Increases count if car already exists
                cars[car] += production_input
                break
        else:
            cars.setdefault(Car(brand_input, model_input, color_input, price_input), production_input)
        
        print(f"\n{production_input} {color_input} {brand_input} {model_input} cars created successfully.")
        
    except ValueError as error:
        # This will handle any errors that may occur while taking the inputs.
        print(f"\n{error}. Enter details correctly in digits.")
        
    return None
    
def sell_cars(cars : dict[Car, int]) -> float:
    # Check stock, if it has that many cars of that brand and model that can be sold
    # if yes then sell and add the amount earned to the bank else let the user know.
    sales : float = 0
    print("\nCarefully enter details for the following:")
    
    try:
        # Taking Inputs
        brand_input : str = input("Enter Brand Name: ").lower().strip()
        model_input : str = input("Enter Model Name: ").lower().strip()
        color_input : str = input("Enter Color: ").lower().strip()
        units_input : int = int(input("Enter number of Units to sell: "))
        
        for car_object, count in cars.items():
            # Checking if any of the car meets such details.
            if (car_object.brand == brand_input and car_object.model == model_input and car_object.color == color_input):
                # If car with such details is found, then we check if we have enough units to sell.
                if count >= units_input:
                    # If yes then we sell the units from the inventory and return the total amount earned.
                    cars[car_object] -= units_input
                    sales += units_input * car_object.price
                    print(f"\n{units_input} {color_input} {brand_input} {model_input} cars sold successfully. Profit: \u20B9{sales:,}")
                else:
                    # Else we let the user know that we do not have enough units.
                    print("\nNot enough units in the Inventory.")
                
                break
        else:
            # If no such car is found in the entire dictionary, then we print this.
            print("\nCar with such details is not found in the Inventory.")
        
    except ValueError as error:
        # This is to handle any error that may occur while taking input.
        print(f"\n{error}. Enter details correctly in digits.")
    
    return sales

def main() -> None:
    # test_obj : Car = Car(brand="Toyota", model="Fortuner", color="White", price=50_00_000)
    # test_obj.drive(distance=10, speed=100)
    
    # list[Car]
    # extend using create_cars
    # remove from list[Car] using sell_cars
    # stock
    # bank
    # counter
    
    display_options()                           # Prints options to the terminal console
    # Initializing Variables (Should be done with file.io to save the results)
    bank_balance : float = 0                    # To represent amount earned from selling cars.
    cars_inventory : dict[Car, int] =  dict()   # To represent the cars in inventory.
    
    while True:
        try:
            user_option_input : int = int(input("\nEnter your choice: "))
            match user_option_input:
                case 0:
                    display_options()
                case 1:
                    display_inventory(cars=cars_inventory)
                case 2:
                    print(f"\nBank Balance: \u20B9{bank_balance:,}")
                case 3:
                    create_cars(cars=cars_inventory)
                    
                case 4:
                    bank_balance += sell_cars(cars=cars_inventory)
                case 5:
                    # Add code to ask confirmation before exiting.
                    print(f"\nEOD Bank Balance: \u20B9{bank_balance:,}")
                    print("\nThank you for using the program.\n")
                    return None
                case _:
                    raise ValueError("Input out of range")
                    
        except ValueError as error:
            print(f"\n{error}. Please enter choice in digits and in range.")
    

if __name__ == "__main__":
    main()

# There are a lot of improvement require, also annotations and doc strings.