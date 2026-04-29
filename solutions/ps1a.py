annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))

portion_down_payment = 0.25
current_saving = 0
r = 0.04

months = 0

while current_saving < (total_cost * 0.25):
  month_saving = (annual_salary / 12) * portion_saved
  current_saving += month_saving + (current_saving * r / 12)
  months += 1

print("Number of months: ", months)
