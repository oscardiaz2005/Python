def salary_overtime_hours(commom_salary,overtime_day,overtime_night,holidays,sunday):
   vohd=(commom_salary/240*1.25)*overtime_day 
   vohn=(commom_salary/240*1.35)*overtime_night 
   vohh=(commom_salary/240*1.75)*holidays 
   vohs=(commom_salary/240*2)*sunday 
   return(commom_salary+vohd+vohn+vohh+vohs)

def discuount_days_dontworked(common_salary,days_dontworked):
   vddw=common_salary/30*days_dontworked
   return vddw

def socialsecurity(totalearn):
   ss=totalearn*0.08
   return ss
