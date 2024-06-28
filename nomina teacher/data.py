from funtions.operations import *


common_salary=int(input("enter your common salary "))
overtime_hours=int(input("enter your  day overtime hours worked "))
overtime_night=int(input("enter your  night overtime hours worked "))
overtime_holidays=int(input("enter your holidays overtime hours worked "))
overtime_sundays=int(input("enter your  sunday overtime hours worked "))
dont_worked_days=int(input("enter your dont worked days "))

total_salary=salary_overtime_hours(common_salary,overtime_hours,overtime_night,overtime_holidays,overtime_sundays)
discount_day=discuount_days_dontworked(common_salary,dont_worked_days)
totalearn=total_salary-discount_day
discount_social_security=socialsecurity(totalearn)

total_salary_with_discount=totalearn-discount_social_security

print(total_salary_with_discount)
