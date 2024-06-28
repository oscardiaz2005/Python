def calculate_common_salary_discounted(common_salary, miss_days):
    return common_salary - (common_salary * (miss_days / 30))

def calculate_overtime(total_hours, money_per_hour):
    return total_hours * money_per_hour

def calculate_total_salary(common_salary_discounted_day, total_of_daytime, total_of_night, total_of_holidays, total_of_sunday):
    return common_salary_discounted_day + total_of_daytime + total_of_night + total_of_holidays + total_of_sunday

def calculate_discounts(total_salary):
    health_discount = total_salary * 0.04
    pension_discount = total_salary * 0.04
    return health_discount, pension_discount

def calculate_total_salary_discounted(total_salary, health_discount, pension_discount):
    return total_salary - health_discount - pension_discount
