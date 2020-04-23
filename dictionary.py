data = {
    'name' : 'Messi',
    'number' : '10',
    'position' : 'Striker',
}

print(data['name'])

#loop
for key, value in data.items():
    print(key + " - " + value)

nested_data = {
    1: {
        'name' : 'Suarez',
        'number' : '9',
    },
    2: {
        'name' : 'Griezmann',
        'number' : '17'
    }
}

print(nested_data[1])
