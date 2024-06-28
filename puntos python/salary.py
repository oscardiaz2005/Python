from salaryFunctions import *

common_salary = int(input("How much money do you earn with your common salary? "))
miss_days = int(input("How many days did you miss this month? "))
daytime_overtime = int(input("How many hours of daytime overtime did you work? "))
night_overtime = int(input("How many hours of night overtime did you work? "))
holiday_hours = int(input("How many holiday hours did you work? "))
sunday_hours = int(input("How many Sunday hours did you work? "))

hours_worked = 30 * 8

money_for_hour = common_salary / hours_worked
money_for_daytime = money_for_hour * 1.25
money_for_night = money_for_hour * 1.35
money_for_holidays = money_for_hour * 1.75
money_for_sunday = money_for_hour * 2

common_salary_discounted_day = calculate_common_salary_discounted(common_salary, miss_days)
total_of_daytime = calculate_overtime(daytime_overtime, money_for_daytime)
total_of_night = calculate_overtime(night_overtime, money_for_night)
total_of_holidays = calculate_overtime(holiday_hours, money_for_holidays)
total_of_sunday = calculate_overtime(sunday_hours, money_for_sunday)

total_salary = calculate_total_salary(common_salary_discounted_day, total_of_daytime, total_of_night, total_of_holidays, total_of_sunday)

health_discount, pension_discount = calculate_discounts(total_salary)
total_salary_discounted = calculate_total_salary_discounted(total_salary, health_discount, pension_discount)

print(f'Your common salary is: {common_salary}, but you missed {miss_days} day(s), so your common salary this month is {common_salary_discounted_day}.')
print(f'You earned {total_of_daytime} for your daytime overtime, {total_of_night} for your night overtime, {total_of_holidays} for your holiday hours, and {total_of_sunday} for your Sunday hours.')
print(f'In total, you earned: {total_salary}')

print(f'Health discount: {health_discount}')
print(f'Pension discount: {pension_discount}')

print(f'Your total salary after health and pension deductions is: {total_salary_discounted}')
