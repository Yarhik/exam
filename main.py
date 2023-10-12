
building_name = input("Enter the name of the building: ")
number_of_floors = int(input("Enter the number of floors: "))

floors = {}

for floor in range(1, number_of_floors + 1):
    number_of_apartments = int(input(f"Enter the number of apartments on floor {floor}: "))
    floors[floor] = {"number_of_apartments": number_of_apartments}

    for apartment in range(1, number_of_apartments + 1):
        number_of_rooms = int(input(f"Enter the number of rooms in apartment {apartment} on floor {floor}: "))
        number_of_beds = int(input(f"Enter the number of beds in apartment {apartment} on floor {floor}: "))
        number_of_tv_sets = int(input(f"Enter the number of TV sets in apartment {apartment} on floor {floor}: "))
        floors[floor][apartment] = {
            "number_of_rooms": number_of_rooms,
            "number_of_beds": number_of_beds,
            "number_of_tv_sets": number_of_tv_sets
        }

print(f"Building Name: {building_name}")
print(f"Number of Floors: {number_of_floors}")
for floor, floor_data in floors.items():
    print(f"Floor {floor}:")
    print(f"  Number of Apartments: {floor_data['number_of_apartments']}")
    for apartment, apartment_data in floor_data.items():
        if isinstance(apartment, int):
            print(f"  Apartment {apartment}:")
            print(f"    Number of Rooms: {apartment_data['number_of_rooms']}")
            print(f"    Number of Beds: {apartment_data['number_of_beds']}")
            print(f"    Number of TV Sets: {apartment_data['number_of_tv_sets']}")
