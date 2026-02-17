import math

# This function calculate the discounted price of an item
# assuming the discount is expressed as a percentage
# and the currency should round to 2 decimal places
def calculate_discount(price: int | float, discount: int | float):
    converted_discount = 1.0 - (discount / 100)
    new_price = round(price * converted_discount, 2)
    return new_price

def main():
    prices = [10, 9999, 18.50, 100.001]
    discounts = [10, 25, 36.666, 100, 999]

    for p in prices:
        for d in discounts:
            print(p, "with a", d, "percent discount is", calculate_discount(p, d))

if __name__ == "__main__":
    main()