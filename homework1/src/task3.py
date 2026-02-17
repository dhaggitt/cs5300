# This function checks if a number is
# positive, negative, or zero
def check_sign(int x):
    sign = ""
    if (x < 0):
        sign = "negative"
    elif (x > 0):
        sign = "positive"
    else:
        sign = "zero"
    return sign

# Main declared for debugging
def main():
    variables = [5, -5, 0, 1, -1]
    for x in variables:
        print(x, " is ", check_sign(x))

if __name__ == "__main__":
    main()