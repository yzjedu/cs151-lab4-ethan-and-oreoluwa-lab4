# Programmers: Oreoluwa Adebusoye & Ethan D'Souza
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/09/2024
# Lab Assignment: 04
# Problem Statement:
# Problem Statement: Calculate the monthly bill for a mobile subscription based on user input.
# Purpose: To determine how much a customer owes based on their chosen package and data usage.
# Data In: Subscription package type, amount of data used, and coupon availability.
# Data Out: Total monthly bill for the selected package.
# Credits:

# Prompt for package name
package = input("Enter your subscription package (Green, Blue, Purple): ").lower().strip()

# Check for valid package
while package != "green" and package != "blue" and package != "purple":
    print("Invalid package name. Please enter a valid package.")
    package = input("Enter your subscription package (Green, Blue, Purple): ").lower().strip()

# Prompt for data usage
data_used = float(input("Enter the amount of data used (in GB): "))

# Prompt for coupon
coupon_input = input("Do you have a coupon? (yes/no): ").strip().lower()
has_coupon = coupon_input == "yes"

# Initialize variables for billing
if package == "green":
    base_cost = 49.99
    included_data = 2
    additional_data_cost = 15
elif package == "blue":
    base_cost = 70.00
    included_data = 4
    additional_data_cost = 10
elif package == "purple":
    base_cost = 99.95
    included_data = 100000000000000  # Unlimited data
    additional_data_cost = 0

# Calculate additional data charges
if data_used > included_data:
    additional_data = data_used - included_data
    total_cost = base_cost + (additional_data * additional_data_cost)
else:
    total_cost = base_cost

# Apply coupon discount if applicable for Green package
if package == "Green" and has_coupon and total_cost >= 75:
    total_cost -= 20

# Display the bill
print(f"Your total monthly bill for the {package} package is: ${total_cost:.2f}")
