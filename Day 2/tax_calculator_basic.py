# This program is used to calculate tax to be paid by the user, but it has only basic functionalities.

# Inputs
base_income : float = float(input("Enter your annual base income: "))
TAX_RATE : int = 10

# Calculations
tax_amount : float = base_income * TAX_RATE / 100

# Display
print("=" * 40)
print("Income tax calculator")
print("=" * 40)
print(f"Base Income:          ${base_income}")
print(f"Tax Rate:             {TAX_RATE}%")
print("-" * 40)
print(f"Tax Amount:           ${tax_amount}")
print("=" * 40)

# Now create another tax calculator which should take into account tax slabs, e.g. slab_1 = 0%, slab_2 = 12% and so on.