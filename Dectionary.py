
Marks = { 'Abdelrahman' : 300 , 'Mohamed' : 290 , 'Omar' : 295 , 'Ali' : 292}

Tempreture = { 'Alexandria' : 'Twenty-Nine', 'Aswan' : 35 , 'Fayoum' : 'Fifteen'}

Approximating = { 0.999 : 'One' , 5.555 : 'Six' , 2.3654 : 'Two' }

print(Marks)

print(Marks.keys())

print(Marks.values())

Tempreture['Alexandria'] = 100

print(Tempreture)

print('Abdelrahman' in Marks)

print( 'Fifteen' in Tempreture.values())

print(Approximating.get(0.999))

print(Marks.get('Abdelrahman' , 600))

print(Marks.get('abdelrahman' , 600))

Tempreture['Luxor'] = 'Twenty-Three'

print(Tempreture)

del(Marks['Ali'])

print(Marks)

print(len(Tempreture))

Marks.clear()

print(Marks)

del(Approximating) # Delete All The Dictionary

Degrees = Tempreture.copy()

print(Degrees)

Degree = list(Degrees.keys())

print(Degree)

Degree = list(Degrees.values())

print(Degree)

Degree = list(Degrees.items())

print(Degree)

#---------------------------------------------------------------------------

Details = { 'ahmed' : ('96' , '25' , 'Egypt') , 'Bodi' : ('280' , '15' , 'Jordan') , 'Salma' : ('13' , '65' , 'Gepoti') }

print(Details.keys())

print(Details.values())

print(Details)

print(Details['ahmed'])

print(Details['Bodi'][1])