# This file contains program for currency conversion, using conversion rate through a json file.

import json


def load_conversion_rates() -> dict[str, float] | None:
    """Function to load the currencies.json file into a dictionary variable in this file, so it can be used.

    Returns:
        dict[str, float] | None: stores the contents of currencies.json
    """
    
    try:
        with open("currencies.json", "r") as file:
            # loading the JSON into a dictionary, and returning it, if there is no error.
            currencies : dict[str, float] = json.load(file)
        return currencies
    except FileNotFoundError as Error:
        print(f"The file cannot be found in your working directory.\n{Error}")
        return None
    except json.JSONDecodeError as Error:
        print(f"The file contains invalid JSON format.\n{Error}")
        return None
    
def convert(exchange_rates : dict[str, float], currency: str = "USD", amount : float = 1) -> dict[str, float]:
    """Does all the conversion calculations using the exchange rate table provided and returns a table of converted amounts.

    Args:
        exchange_rates (dict[str, float]): the exchange rate table provided through the input.
        currency (str, optional): currency ticker for which conversions are to be done. Defaults to "USD".
        amount (float, optional): amount of money to be converted in other currencies. Defaults to 1.

    Raises:
        ValueError: If the currency ticker provided in the input does not exist in the table.

    Returns:
        dict[str, float]: table containing all the converted amounts and their respective currencies.
    """
    
    # Creating an empty dictionary to store the converted amounts and their respective tickers.
    converted_amounts : dict[str, float] = dict()
    
    if exchange_rates:
        # Converting the amount to USD if it is not.
        if currency in exchange_rates.keys():
            base_amount : float = amount / exchange_rates[currency]
            
            for ticker, exchange_rate in exchange_rates.items():
                if ticker == currency:
                    continue
                # Adding each currency ticker and its respective conversion using base amount.
                converted_amounts.setdefault(ticker, (exchange_rate * base_amount))
            
        else:
            raise ValueError(f"The currency ticker does not exist in the table: '{currency}'")
        
    return converted_amounts

def display_converted_table(converted_table : dict[str, float]) -> None:
    """Displays the converted table with currencies and amounts to the terminal.

    Args:
        converted_table (dict[str, float]): this table holds contents to be printed.

    Returns:
        None: The function display directly to the terminal, no need for a return value.
    """
    
    if converted_table:
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
    exchange_rate_table : dict[str, float] | None = load_conversion_rates()    # Loads the exchange rate table into a variable for use.
    
    if exchange_rate_table:
        instructions()                                                         # Initial instructions for the user are printed.
        
        while True:
            user_input : str = input("\nEnter a command or the amount & currency in the correct format for conversion: ").upper().strip()

            # Condition checking for input provided.
            if user_input == "EXIT":
                print("\nThank you for using the program.\n")
                break
            elif user_input == "LIST":
                # Prints the currencies tickers present in the table, in a list format.
                print(f"\nExchange currencies in the table:\n{list(exchange_rate_table.keys())}")
            else:
                try:
                    currency_input : str = user_input[-3:]
                    amount_input : float = float(user_input[:-3])
                    # Final display
                    print(f"\nConversion of {amount_input:.2f} {currency_input} to other currencies:")    # For printing the input amount and currency in a presentable format.
                    display_converted_table(convert(exchange_rate_table, currency=currency_input, amount=amount_input))    # This will print the output.
                except (ValueError, IndexError) as Error:
                    print(f"\n{Error}\nPlease enter the amount and currency ticker in correct format.")
                
    return None
        

if __name__ == "__main__":
    main()
    
# Good Work !