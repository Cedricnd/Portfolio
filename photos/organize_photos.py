import os

# os.chdir('photos')
# originals = os.listdir()

# print(originals)

# def extract_place(filename):
#    first = filename.find("_")
#    partial = filename[first+1:]
#    second = partial.find("_")
#    return partial[:second]

# print(extract_place("2016-09-04_Berlin_08_25_50.jpg"))
# print(extract_place("2017-01-13_Yosemite_03_36_50.jpg"))

# Rewriting code with split function, two examples:

#def extract_place(filename):
#    return filename.split("_")[1]

# the split function breaks the file into three spots because of the "_", "2016-09-04" "Berlin" "08_25_50.jpg"
# and then we use the index to select "Berlin" since it is the "1" value at the index!


#print(extract_place("2016-09-04_Berlin_08_25_50.jpg"))
#print(extract_place("2017-01-13_Yosemite_03_36_50.jpg"))

# def extract_place(filename):
#    parts = filename.split("_") # Get a list containing all the parts
#    place_name = parts[1] # Use the index operator to select the second list item
#    return place_name
# the split function breaks the file into three spots because of the "_", "2016-09-04" "Berlin" "08_25_50.jpg"
# and then we use the index to select "Berlin" since it is the "1" value at the index!

# print(extract_place("2016-09-04_Berlin_08_25_50.jpg"))
# print(extract_place("2017-01-13_Yosemite_03_36_50.jpg"))

#os.chdir("photos")
#originals = os.listdir()
#places = []
#for filename in originals:
#    place = extract_place(filename)
#    places.append(place)
#print(places)

# This code grabs all of the files in the directory and extracts just their names to a list. Like below:
# ['Berlin', 'Berlin', 'Berlin', 'Yosemite', 'Kyoto', 'Berlin', 'Brooklyn', 'Yosemite', 'Firenze'
#, 'Cancun', 'Firenze', 'Brooklyn', 'Scotland', 'Scotland', 'Cancun', 'Kyoto', 'Kyoto', 'Scotland',
#  'Cancun', 'Cancun', 'Kyoto', 'Berlin', 'Oahu', 'Oahu', 'Firenze', 'Kyoto', 'Yosemite']

#def extract_place(filename):
#    return filename.split("_")[1]

#def make_place_directories(places):
#    for place in places:
#        os.mkdir(place)

#os.chdir("photos")
#originals = os.listdir()
#places = []
#for filename in originals:
#    place = extract_place(filename)
#    if place not in places:
#        places.append(place)

#make_place_directories(places)

#for photo in originals:
#        name = extract_place(photo)
#        os.rename(photo, os.path.join(name, photo))

# The above code will create the directories and move the picutres into the directions. It does not run a check
# for duplicates first though and it's tied to our user account from our computer.

# The code from below will work on any computer with any user:

def extract_place(filename):
    return filename.split("_")[1]

def make_place_directories(places):
    for place in places:
        os.mkdir(place)

def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    make_place_directories(places)

    for photo in originals:
        name = extract_place(photo)
        os.rename(photo, os.path.join(name, photo))

# To call code, we only have to use: 

#organize_photos("photo")

print("TEST!")