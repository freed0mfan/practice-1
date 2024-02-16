dad_playlst = []
for i in range(5):
    dad_playlst.append(input(f'Введите {i + 1}-ю песню из плейлиста папы: '))
print('Плей-лист мамы: ')
for j in reversed(range(5)):
    print(dad_playlst[j])
