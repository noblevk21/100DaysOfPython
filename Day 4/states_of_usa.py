states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Adding Pandora to the states of America
states_of_america.append("Pandora")

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#entending with another list
print("\n After extending:\n")
states_of_america.extend(dirty_dozen)

#inserting mango
states_of_america.insert(20, "Mangoes")
print(states_of_america)

#sorting the list
states_of_america.sort()

print("\n After sorting: \n")
print(states_of_america)

#sorting the list in reverse order
states_of_america.sort(reverse=True)

print("\n After sorting in reverse: \n")
print(states_of_america)