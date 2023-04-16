def validate_input(work_days, ot_hours, late_days):
    if not all(isinstance(x, int) and x >= 0 for x in [work_days, ot_hours, late_days]):
        return "please input only integer upper 0"
    elif not 0 <= int(work_days) <= 30:
        return "work_days must be between 0 and 30"
    elif not 0 <= int(ot_hours) <= work_days*3:
        return "ot_hours must be between 0 and {}".format(work_days*3)
    elif not 0 <= int(late_days) <= work_days:
        return "late_days must be between 0 and {}".format(work_days)
    else:
        return True
    
    
def calculate_salary(work_days, ot_hours, late_days):
    if validate_input(work_days, ot_hours, late_days) is not True:
        return validate_input(work_days, ot_hours, late_days)
    else:
        basic_salary = work_days*340
        ot_salary = ot_hours*60
        late_salary = 1000 if work_days!=0 and late_days == 0 else 0
        total_salary = basic_salary + ot_salary + late_salary
        return total_salary
    