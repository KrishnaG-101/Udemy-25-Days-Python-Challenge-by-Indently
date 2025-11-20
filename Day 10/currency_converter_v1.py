# This file contains program for currency conversion, using conversion rate through a json file.

from typing import Any
import json


def load_conversion_rates() -> dict[str, float] | None:
    try:
        with open("currencies.json", "r") as file:
            currencies : dict[str, float] = json.load(file)
        return currencies
    except FileNotFoundError as error:
        print(f"The file cannot be found in your working directory.\n{error}")
        return None
    except json.JSONDecodeError as error:
        print(f"The file contains invalid JSON format.\n{error}")
        return None
    
def convert(currency: str = "USD", amount : float = 1) -> dict[str, float]:
    conversion_rates : dict[str, float] | None = load_conversion_rates()
    converted_amounts : dict[str, float] = dict()
    
    if conversion_rates:
        # Converting the amount to USD if it is not.
        if currency in conversion_rates.keys():
            base_amount : float = amount / conversion_rates[currency]
            
            for ticker, exchange_rate in conversion_rates.items():
                if ticker == currency:
                    continue
                converted_amounts.setdefault(ticker, (exchange_rate * base_amount))

        else:
            raise ValueError(f"The currency ticker does not exist in the table: '{currency}'")
        
    return converted_amounts

def display_converted_table(converted_table : dict[str, float] | Any) -> None:
    if converted_table:
        print("Converted Amounts:")
        print("{")
        
        for ticker, amount in converted_table.items():
            print(f"  = {amount:>10.2f}  {ticker}")
        
        print("}")
        return None
    else:
        print("The table could not be printed, due to wrong input or some error.\n")
        return None

def instructions() -> None:
    print("Welcome to currency converter, please read the following instructions and adhere to them.")
    print("1. Type the amount and currency in this format \"10 INR\" in order to convert the currency.")
    print("2. Type LIST to list all available currencies or EXIT to exit the program.")

def main() -> None:
    instructions()
    while True:
        user_input : str = input("\nEnter a command or the amount & currency in the correct format for conversion: ").upper().strip()
        
        if user_input.lower() == "exit":
            print("\nThank you for using the program.\n")
            break
        elif user_input.lower() == "list":
            # Currently it prints the currency tickers with their exchange rate w.r.t. USD, but we can change it to display only tickers.
            display_converted_table(load_conversion_rates())
        else:
            try:
                currency_input : str = user_input[-3:]
                amount_input : float = float(user_input[:-3])
                display_converted_table(convert(currency=currency_input, amount=amount_input))
            except (ValueError, IndexError) as error:
                print(f"\n{error}\nPlease enter the amount and currency ticker in correct format.")
                
    return None
        

if __name__ == "__main__":
    main()


# The code lacks annotation and function definitions (doc string)
# Things to fix, change the display to encorporate the entered amount with its currency, make LIST correct to only display the currency tickers, annotate the file.