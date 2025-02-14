x = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

x['divorced'] = True

married_status = ''
divorced_status = ''
children_status = ''
car_status = ''

del x['children']

if x['married'] == True:
    married_status = 'You are married.'
else:
    married_status = 'You are not married.'

if x['divorced'] == True:
    married_status = 'You were married.'
    divorced_status = 'and you are divorced now, hang in there buddy!'
else:
    divorced_status = 'God bless your marriage.'

if 'children' in x:
    children_status = 'We hope ' + f'{x['children'][0]} ' + 'and ' + f'{x['children'][1]}' + ' are doing well.'
else:
    children_status = 'Who needs children?'

if x['cars']:
    number_of_cars = 'You have ' + str(len(x['cars'])) + ' cars. '
    car_status = number_of_cars + 'Great to see you have ' + f'{x["cars"][0]["model"]}' + ' and ' + f'{x["cars"][1]["model"]}' 
else:
    car_status = 'You broke bitch.'

print('Your name is ', f'{x['name']},', 'You are ', f'{x['age']} years old.',  married_status, divorced_status, children_status, 'We do not care about your pets.', car_status)
print()
print(list(x.keys()))
print()
print(list(x.values()))
print()
print(list(x.items()))