# Algorithm for Mobile Phone Subscription Billing 

1. Prompt the user to enter their subscription package (options: Green, Blue, Purple). 

2. Use lower () and strip () to convert the input to all lower case and remove any leading and trailing whitespace characters. 

3. Check if the package is valid, if not valid, repeat: 

   While package != “Green”, “Blue” or “Purple”: 

    - Output “Invalid package name. Please enter a valid package.” 

    - Prompt the user to input subscription data again 

4. Prompt the user to enter the amount of data used (in GB). 

5. Prompt the user to indicate if they have a coupon (yes/no). 

6. Initialize billing variables based on the selected package: 

7. If package is Green: 

   - Set base cost to $49.99 

   - Set included data to 2 GB 

   - Set additional data cost to $15/GB 

   If package is Blue: 

   - Set base cost to $70.00 

   - Set included data to 4 GB 

   - Set additional data cost to $10/GB 

   If package is Purple: 

    - Set base cost to $99.95 
   
    - Set included data to Unlimited 
   
    - Set additional data cost to $0/GB 

8. Calculate additional data charges: 

   If data used is greater than included data: 

   - Calculate additional data used: additional_data = data_used - included_data 

   - Calculate total cost: total_cost = base_cost + (additional_data * additional_data_cost) 

    Otherwise: 

   - Set total cost to base_cost 

9. Apply coupon discount (if applicable): 

   If package is Green and user has a coupon, and total cost is $75 or more: 

    - Subtract $20 from total cost. 

10. Display the total monthly bill for the selected package. 