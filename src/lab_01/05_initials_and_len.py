string = input()
table = list(string.split())
f_char = string.find(table[0][0])
print(f'ФИО: {string}', f'Инициалы: {table[0][0]+table[1][0]+table[2][0]}', f'Длина (символов): {len((string.strip())[f_char:])}', sep='\n')