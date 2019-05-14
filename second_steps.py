# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database["GEOS"] = 2000
sat_database["worldview"] = 0.31
                
                


# 2) print out all satellite names contained in the dictionary [2P]


print("I have the following satellites in my database:")

print(sat_database.keys())


# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

y = input("Wich satellites resolution you would like to know?")


# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

if y == "METEOSAT":
    
    print("There are informations about the recomendet satallite in sat_database")
    
elif y == "LANDSAT":
    
    print("There are informations about the recomendet satallite in sat_database")
    
elif y == "MODIS":
    
    print("There are informations about the recomendet satallite in sat_database")
    
elif y == "GEOS":
    
    print("There are informations about the recomendet satallite in sat_database")
    
elif y == "worldview":
    
    print("There are informations about the recomendet satallite in sat_database")
    
else: 
    
    print("There are no informations about the recomendet satallite in sat_database")


# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 


if y =="METEOSAT":
    
    print("The resolution of 'METEOSAT' is", sat_database[y], "meters." )
    
if y =="LANDSAT":
    
    print("The resolution of 'LANDSAT' is", sat_database[y], "meters." )
    
elif y =="MODIS":
    
    print("The resolution of 'MODIS' is", sat_database[y], "meters." )
    
elif y =="GEOS":
    
    print("The resolution of 'GEOS' is", sat_database[y], "meters." )
    
elif y =="worldview":
    
    print("The resolution of 'worldview' is", sat_database[y], "meters." )

    
