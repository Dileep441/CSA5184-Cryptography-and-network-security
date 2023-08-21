import math

def calculate_possible_keys():
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Note: 'J' is omitted
    num_letters = len(alphabet)
    possible_keys = math.factorial(num_letters)
    return possible_keys

def main():
    possible_keys = calculate_possible_keys()
    power_of_2 = math.log2(possible_keys)
    
    print("Number of possible keys:", possible_keys)
    print("Approximate power of 2:", power_of_2)

if __name__ == "__main__":
    main()
