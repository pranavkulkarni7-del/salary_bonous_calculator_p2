import sys

if len(sys.argv) != 2:
    print("Usage: python bonus_calculator.py <salary>")
else:
  salary = float(sys.argv[1])
  
    try:
        salary = float(sys.argv[1])
      
        if salary > 0:
            bonus = salary * 0.10
            total_salary = salary + bonus

            print("Bonus Amount: $", bonus)
            print("Total Salary after adding bonus: $", total_salary)
        else:
            print("Salary must be greater than 0.")

    except ValueError:
        print("Please enter a valid number for salary.")
