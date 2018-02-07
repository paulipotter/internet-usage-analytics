output_file = open('cities.csv', 'w')
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
    for line in input_file:
        lin = ""
        num = int(line[:2].lstrip('0'))
        if num in cities.keys():
            lin += str(num)
            lin += ","
            lin += cities[num]
            lin += "\n"
            print(lin)
            output_file.write(lin)

input_file.close()
output_file.close()

