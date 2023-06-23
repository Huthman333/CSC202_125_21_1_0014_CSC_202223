#DAY  9
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected."
    "function""A piece of code that you can easily call over and over again."
}
programming_dictionary["loop"] = "The action of doing something over and over again."
empty_dictionary = {}
#programming_dictionary = {}
#print(programming_dictionary)
programming_dictionary["Bug"] = "A moth in you computer."
#print(programming_dictionary)
#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    print(student_grades)
#Nesting
capitals = {
    "France":"Paris",
    "Germany":"Berlin",
},
#nesting a list in a dictionary
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"],"total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hambury"],"total_visits": 15},
}
travel_log = [
    {
        "country": "France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":9
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin","Hambury","Stutt"],
        "total_visits": 5
    },
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
add_new_country("nigeria",2,["moscom","america"])
print(travel_log)
