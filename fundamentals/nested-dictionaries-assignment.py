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
# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x[1][0] += 5
print(x)
# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)
# 3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
# 4. Change the value 20 in z to 30
z[0]["y"] += 10
print(z)


# This one was very difficult for me
students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for x in range(0, len(list)):
        output = ""
        for key,val in list[x].items():
            output += f" {key} = {val},"
        print(output)
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(firstName, list):
    for x in range(0, len(list)):

        for key,val in list[x].items():
            if key == firstName:
                print(val)
iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)




dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key,val in some_dict.items():
        print("===================")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
printInfo(dojo)



# I found this assignment to be extremely difficult 