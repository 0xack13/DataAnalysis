# We need to import the necessary modules.
import json
import csv
from pprint import pprint
#Now, we define a dictionary to store the result
typePokemon = {}
#Open and load the ii file.
with open("pokemon.json") as f:
    data = json.loads(f.read())

#Fill the typePokemon dictionary with sum of pokemon by type
    for line in data:
        if line["type"] not in typePokemon:
            typePokemon[line["type"]] = 1
        else:
            typePokemon[line["type"]]=typePokemon.get(line["type"])+1

#Open in a write mode the sumPokemon.csv file 
with open("sumPokemon.csv", "w") as a:
    w = csv.writer(a)

#Sort the dictionary by number of pokemon
#writes the result (type and amount) into the csv file
    for key, value in sorted(typePokemon.items(),
    key=lambda x: x[1]):
        w.writerow([key,str(value)])
    
 #finally, we use "pretty print" to print the dictionary   
    pprint(typePokemon)