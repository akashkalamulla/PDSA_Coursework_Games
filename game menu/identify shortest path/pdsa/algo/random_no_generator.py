import random

# Generate 45 random numbers between 5 and 50
random_numbers = [random.randint(5, 50) for _ in range(45)]

#print(random_numbers)
# Generate a random letter between A and J
random_letter = chr(random.randint(ord('A'), ord('J')))


names = ["AJ", "BJ", "CJ", "DJ", "EJ",  # Add as many names as needed
         "FJ", "GJ", "HJ", "IJ", "AI",
         "BI", "CI", "DI", "EI", "FI",
         "GI", "HI", "AH", "BH", "CH",
         "DH", "EH", "FH", "GH", "AG",
         "BG", "CG", "DG", "EG", "FG",
         "AF", "BF", "CF", "DF", "EF",
         "AE", "BE", "CE", "DE", "AD",
         "BD", "CD", "AC", "BC", "AB"]

# Generating a 2D array where each sub-array contains a name and a random number
random_numbers_with_names = [[names[i], random_numbers[i]] for i in range(45)]

# Example of accessing the first name and number
#print(random_numbers_with_names[0])  # Output might be: ['John', 23]

#for name, number in random_numbers_with_names:
#    print(f"{name},{number}")




