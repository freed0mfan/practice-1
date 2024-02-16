length_sm = float(input('Расстояние в сантиметрах: '))
length_inch = length_sm / 2.54
length_ft = length_inch / 12
length_yrd = length_ft / 3
length_ml = length_yrd / 1760
print(f'{length_yrd} ярдов\n{length_ml} мили\n{length_ft} футов\n{length_inch} дюймов\n')
