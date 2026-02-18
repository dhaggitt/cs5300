import numpy as np

# This function calculates the median, mean
# and standard deviation of an np array
def calc_stats(numbers: np.array):
    n_median = np.median(numbers)
    n_mean = np.mean(numbers)
    n_std = np.std(numbers)
    return {"Standard Deviation": round(n_std, 3), 
        "Mean": round(n_mean, 3), 
        "Median": round(n_median, 3)}

# Main declared for debugging
def main():
    eg_numbers = np.array([[42, 7, 85, 23, 61],
        [14, 78, 42, 92, 8],
        [23, 19, 47, 63, 42]])
    print(eg_numbers)
    print("Mean =", round(np.mean(eg_numbers), 3))
    print("Median =", round(np.median(eg_numbers), 3))
    print("Standard Deviation =", round(np.std(eg_numbers), 3))
    print(calc_stats(eg_numbers))
    

if __name__ == "__main__":
    main()