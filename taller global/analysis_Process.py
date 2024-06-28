import json

Data_Analysis = ["DATE         BEHAVIOR      MODPOINT HIGHT-LOW"]
goes_up_times=0
drops_times=0
stable_times=0
highest_price=-100000000000000000
lowest_price=10000000000000000000
date_lowest_prices=""    
date_highest_prices=""    

with open("GLOBANT.csv", "r") as file:
    DataGlobant = file.readlines()

    for line in DataGlobant[1:]:
        data_line = line.split(",")
        date = data_line[0]
        open_price = float(data_line[1])
        high = float(data_line[2])
        low = float(data_line[3])
        close = float(data_line[4])

        if close - open_price > 0:
            behavior = "GOES UP"
            goes_up_times+=1
        elif close - open_price < 0:
            behavior = "DROPS  "
            drops_times+=1
        else:
            behavior = "STABLE"
            stable_times+=1
        midpoint = (high - low) / 2

        if low<lowest_price:
            lowest_price=low
            date_lowest_prices=date
        if high>highest_price:
            highest_price=high
            date_highest_prices=date    

        Data_Analysis.append(f"{date}   {behavior}       {midpoint}")


with open("analysis_file.csv", "w") as file:
    for line in Data_Analysis:
        file.write(line + "\n")

datails={
    "date_lowest_prices":date_lowest_prices,
    "lowest_price":lowest_price,
    "date_highest":date_highest_prices,
    "highest_price":highest_price,
    "goes_up_times":goes_up_times,
    "drops_times":drops_times,
    "stable times":stable_times
}        

datajson="details.json"

with open ("details.json","w") as file:
    json.dump(datails,file,indent=4)


        


