text = input("Enter text to analyze: ")
characters = len(text)
letters = 0
digits = 0
spaces = 0
uppercase_letters = 0
lowercase_letters = 0


for char in text:
    if char.isupper():
        uppercase_letters += 1
    elif char.islower():
        lowercase_letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
letters = uppercase_letters + lowercase_letters


print("=== TEXT ANALYSIS ===")
print(text)
print(f"Total characters: {characters}")
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Uppercase letters: {uppercase_letters}")
print(f"Lowercase letters: {lowercase_letters}")
