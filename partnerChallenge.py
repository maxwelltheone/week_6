#Partner activity

school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"

#Find the student who is making an A and upgrade it to an A +
school["class"]["students"]["student1"] = "A+"

print(school)

#Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
product_inventory["warehouse1"]["quantities"][1]

#Sum up all the quantities in the warehouse

quantity1 = product_inventory["warehouse1"]["quantities"]

quantity2 = product_inventory["warehouse2"]["quantities"]

print(sum(quantity1)+ sum(quantity2))

# Elpancho17 (Original Host)
# Maxwell (My copy of our work)