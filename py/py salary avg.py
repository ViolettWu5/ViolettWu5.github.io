def avg(data):
    sum = 0
    for i in range(0, len(data['employees'])):
        sum += data['employees'][i]['salary']
    return sum/len(data['employees'])
salary = avg({
    "count":3,
    "employees":
        [
            {"name":"John","salary":30000},
            {"name":"Bob","salary":60000},
            {"name":"Jenny","salary":50000}
        ]
})
print(salary)
