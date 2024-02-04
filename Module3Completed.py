Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #PART 1
>>> 
>>> Food_Charge = float(input("Enter the charge for the food: $"))
Enter the charge for the food: $85
>>> 
>>> #Tip and Sales Tax
>>> tip_percentage = 18
>>> tax_percentage = 7
>>> 
>>> #calculate tip and sales tax amount with food charge
>>> 
>>> Tip_amount = (tip_percentage / 100) * Food_Charge
>>> Tax_amount = (tax_percentage / 100) * Food_Charge
>>> 
>>> #calculate total price
>>> 
>>> Total_price = Food_Charge + Tip_amount + Tax_amount
>>> 
>>> #Display
>>> 
>>> print("\nAmount Details:")

Amount Details:
>>> print(f"Food_Charge]")
Food_Charge]
>>> print(f"Tip (18%) : ${Tip_amount}")
Tip (18%) : $15.299999999999999
>>> print(f" Tax (7%) : ${Tax_amount}")
 Tax (7%) : $5.95
>>> print(f"Total Price: ${Total_price}")
Total Price: $106.25
