def calculate_average_age_by_name(data_list):
    ages_by_name = {}
    count_by_name = {}
    
    for element in data_list:
        name = element[0]
        age = element[1]
        
        if name in ages_by_name:
            ages_by_name[name] += age
            count_by_name[name] += 1
        else:
            ages_by_name[name] = age
            count_by_name[name] = 1
    
    average_age_by_name = {}
    for name, total_age in ages_by_name.items():
        count = count_by_name[name]
        average_age = total_age / count
        average_age_by_name[name] = average_age
    
    return average_age_by_name
