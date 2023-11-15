https://replit.com/join/ytcvzpieft-diego-adieladie 
#Salary
"""
Salary. File name as: Salary - tuition.
Objective. Algorithm to calculate the salary of “n” salespeople.
Each salary is made up of a base salary and a sales commission.
    Total Salary = Base salary + sales commission
The sales commission is calculated by taking a percentage of the sales made, according to the following table:
    Sales Commission percentage
    Less than 3,500 7%
    3,500 – 7,000 10%
    Greater than 7000 15%
The algorithm must ask as input: if there is another seller (yes/no response), the name of each seller, the base salary of each one and the total sales made per seller. Tip: use the lower function to validate yes and no.
The output must have the seller's name and their total salary
"""

counter = 0
seller = input("Is there any seller? (yes/no)")
while seller == "yes":
  counter += 1
  print("number of sallers attended:", counter)
  name_s = input("What is the name of the seller?")
  base_salary = int(input("what is your base salary?"))
  sales = int(input("How many sales did you did?"))
  if sales < 3500:
    Commision_percentage = 0.07

  elif sales >= 3500 and sales <= 7000:
    Commision_percentage = 0.1

  elif sales >= 7000:
    Commision_percentage = 0.15 

  final_sales_comission = float(base_salary) * float(Commision_percentage) / 100
  total_salary = float(base_salary) + float(final_sales_comission)
  print("The total salary of", name_s, "is:", float(total_salary))
  seller = input("Is there any seller? (yes/no)")
