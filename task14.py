year = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']

winter = ('Грудень', 'Січень', 'Лютий')
spr = year[2:5]
summ = year[5:8]
autumn = year[8:11]

full = (winter, tuple(spr), tuple(summ), tuple(autumn))
print(full)