from function import *

work_days = input("work_days ==> ")
ot_hours = input("ot_hours ==> ")
late_days = input("late_days ==> ")

try:
    work_days = int(work_days)
    ot_hours = int(ot_hours)
    late_days = int(late_days)
except ValueError:
    print("please input only integer upper")
    exit()


salary = calculate_salary(work_days, ot_hours, late_days)
print("salary ==> ", salary)
    
