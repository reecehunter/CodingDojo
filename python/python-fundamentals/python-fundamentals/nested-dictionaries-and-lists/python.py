#
# Part 1
#
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"

#
# Part 2
#

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary(list):
    for i in range(len(list)):
        for key, value in list[i].items():
            print(f"{key} - {value}")

# iterate_dictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#
# Part 3
#

# given list of dictionaries and key name, print value
def iterate_dictionary2(list, key_name):
    for dict in list:
        print(dict[key_name])

# iterate_dictionary2(students, "first_name") 

#
# Part 4
#

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# some_dict is a dictionary of lists
def print_info(some_dict):
    for list in some_dict:
        locations = some_dict[list]
        print(f"{len(locations)} {list.upper()}")
        for location in locations:
            print(location)
        print(" ")

print_info(dojo)