name = input("Enter your full name (First, Middle, Last): ")
first, middle, last = [part.strip().capitalize() for part in name.split(",")]

formatted = f"{last}, {first} {middle[0].upper()}."
print("Formatted Name:", formatted)
