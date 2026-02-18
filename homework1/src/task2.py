# Returns a variable of type int
def return_integer():
    x = int(5)
    return x

# Returns a variable of type float
def return_float():
    y = float(6.125)
    return y

# Returns a variable of type string
def return_string():
    s = str("happylittlestring")
    return s

# Returns a variable of type bool
def return_bool():
    b = bool(True)
    return b

# Main declared to print function returns
def main():
    print("Integer = ", return_integer())
    print("Float = ", return_float())
    print("String = ", return_string())
    print("Boolean = ", return_bool())

if __name__ == "__main__":
    main()