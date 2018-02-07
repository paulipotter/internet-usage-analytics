output_file = open('city_entry.csv', 'w')
output_file.write("city_id, city\n")

cities = {
    1: "ASUNCION",
    3: "LUQUE",
    4: "SAN LORENZO",
    5: "MARIANO ROQUE ALONSO",
    6: "NEMBY",
    7: "ITAGUA",
    8: "CORONEL OVIEDO",
    9: "VILLARICA",
    10: "CAACUPE",
    11: "CARAPEGUA",
    12: "CAAZAPA",
    13: "CIUDAD DEL ESTE",
    14: "MINGA GUAZU",
    15: "SANTA RITA",
    16: "HERNANDARIAS",
    18: "ENCARNACION",
    19: "CORONEL BOGADO",
    20: "HOHENAU"

}
with open('cities.txt') as input_file:
    print("open")
    i = 1
    for line in input_file:
        lin = ""
        num = int(line[:2].lstrip('0'))
        if num in cities.keys():
            lin += str(i)
            lin += ","
            lin += cities[num]
            lin += "\n"
            print(lin)
            output_file.write(lin)
            i += 1

input_file.close()
output_file.close()

output2_file = open('city.csv', 'w')

for key in cities.keys():
    li = str(key)
    li += ","
    li += cities[key]
    li += "\n"
    output2_file.write(li)

output2_file.close()

