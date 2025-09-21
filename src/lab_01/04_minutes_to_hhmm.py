"""minutes = int(input())

print(f'{minutes//60%24}:{minutes%60 if minutes%60 > 9 else '0' + str(minutes%60)}')"""
min = int(input())
minutes = min % 60
hours = min // 60
print(f"{hours}:{minutes:02d}")