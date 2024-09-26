"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""

def main():
  
    #asks the user for two numbers and stores them in their corresponding variables
    num1: int = int(input("Enter a number: "))
    num2: int = int(input("Enter another number: "))
    #adds the two numbers together
    total: int = num1 + num2
    total2: int = num1 - num2
    total3: int = num1 * num2
    total4: int = num1 / num2
    total5: int = num1 ** num2
    total6: int = num1 // num2
    total7: int = num1 % num2

    #prints the result
    print(f"{num1} + {num2} = {total}")
    print(f"{num1} - {num2} = {total2}")
    print(f"{num1} * {num2} = {total3}")
    print(f"{num1} / {num2} = {total4}")
    print(f"{num1} ** {num2} = {total5}")
    print(f"{num1} // {num2} = {total6}")
    print(f"{num1} % {num2} = {total7}")

if __name__ == "__main__":
  main()
