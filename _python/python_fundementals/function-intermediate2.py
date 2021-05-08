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
students[0]['last_name']='braynt'
x[1][0]=15
sports_directory['soccer'][0]='andres'
z[0]['y'] = 30

print(z)
print(x)
print(students)
print(sports_directory)

def iterateDictionary(list):
    for i in range(len(list)):
        for key, val in list[i].items():
            print(f"{key} - {val}")

        
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students) 


def iterateDictionary2(key_name, some_list):
    for i in range (len(students)):
        print(f"{key_name} {students[i][key_name]}")
        


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

def printInfo(some_dict):

    for key in some_dict.keys():
        print(f"{len(some_dict[key])}, {key}")
        for item in some_dict[key]:
            print(item)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

# 'locations' and 'instructors' are keys >> each dictionary must have a key >> so these are the keys.>> for the san jose ..etc the whole words are value for the key.