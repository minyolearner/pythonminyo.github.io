people = [
    {'name':'Momo','Group':'Twice','Genre':'KPOP','Company':'JYP International','Citizenship':'Japanese'},
    {'name':'Nayeon','Group':'Twice','Genre':'KPOP','Company':'JYP International','Citizenship':'South Korean'},
    {'name':'Jihyo','Group':'Twice','Genre':'KPOP','Company':'JYP International','Citizenship':'South Korean'},
    {'name':'Tyuzu','Group':'Twice','Genre':'KPOP','Company':'JYP International','Citizenship':'Taiwanese'}
]

# def f(person):
#     return person['name']

# people.sort(key=f)

# # people.sort().[name]

people.sort(key = lambda person:person['Citizenship'] )

print(people)