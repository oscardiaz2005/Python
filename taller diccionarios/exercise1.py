from procesos.procesos_exercise1 import meets_requirements
n = int(input("Enter the number of bicycles to register: \n"))

records = []

for i in range(1, n + 1):
    print(f"\nEnter the data for bicycle number {i}:")
    pedal_ground_distance = int(input("Pedal ground distance: "))
    crank_length = int(input("Crank length: "))
    saddle_length = int(input("Saddle length: "))
    handlebar_length = int(input("Handlebar length: "))
    price = int(input("Price: "))

    bicycle_record = {
        "pedal_ground_distance": pedal_ground_distance,
        "crank_length": crank_length,
        "saddle_length": saddle_length,
        "handlebar_length": handlebar_length,
        "price": price
    }
    records.append(bicycle_record)



record_meets_requirements = False
print("\nBicycles meeting the criteria of the regulations:") 
for record in records:
    if meets_requirements(record):
        print(f"${record['price']}")
        record_meets_requirements = True
if not record_meets_requirements:
    print("<NOT AVAILABLE> No bicycles were found that meet the criteria of the regulations.")


