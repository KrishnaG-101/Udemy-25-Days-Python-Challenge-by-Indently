# This is a program to simulate a slot machine in python.

import time
import random

class SlotMachine:
    def __init__(self, credits : int) -> None:
        self.credits : int = credits
        assert credits > 0, "Credits can't be 0 or less."
        self.symbols : dict[str, int] = {"🍊" : 1, "🍒" : 2, "🍇" : 3, "🍋" : 4}
    
    def update_credits(self, amount : int) -> None:
        self.credits += amount
    
    def calculate_rewards(self, bet : int, config : list[str]) -> int:
        initial : str = config[0]
        winnings : list[int] = list()
        
        for symbol in config:
            if symbol == initial:
                winnings.append(self.symbols[symbol])
            else:
                break
        
        if len(winnings) == 1:
            return 0
        else:
            return sum(winnings) * bet
    
    def spin(self, bet : int) -> None:
        # Checking if the bet amount is correct.
        if bet <= 0:
            print("\nBet must be greater than 0.")
            return None
        
        # Checking if the bet amount is not more than credits.
        if self.credits >= bet:
            self.update_credits(-bet)
        else:
            print("\nNot enough credits...")
            return None
        
        print()
        
        result : list[str] = list()
        for _ in range(4):
            time.sleep(0.3)
            slot_landed : str = random.choice(list(self.symbols))
            result.append(slot_landed)
            # Flush = True ensures quick printing, ensuring the difference in print timings.
            print(slot_landed, end="", flush=True)
        
        print("\n")
        
        # Calculating reward and updating the 
        reward : int = self.calculate_rewards(bet, result)
        self.update_credits(reward)
        print(f"Reward: {reward}")
        
        if self.credits == 0:
            print("No credits left.")
            print("Game Over!\n")
            return None
        else:
            print(f"Credits Remaining: {self.credits}\n")
        
        print("-" * 30)
        return None
        
    def play(self) -> None:
        print(f"\nStarting Credits: {self.credits}")
        print("-" * 30)
        while self.credits > 0:
            try:
                bet : int = int(input("\nBet: "))
                self.spin(bet)
            except ValueError as error:
                print(f"\n{error}\nEnter a valid bet amount.")
    
def main() -> None:
    slot : SlotMachine = SlotMachine(credits=200)
    slot.play()

if __name__ == "__main__":
    main()