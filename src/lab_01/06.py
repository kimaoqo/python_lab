n = int(input())
participants = [input() for i in range(n)]
ochn = 0
distant = 0
for i in participants:
    info = list(i.split())
    if info[3] == 'False':
        info[3] = False
    else:
        info[3] = True
    if info[3] == True:
        ochn += 1
    else:
        distant += 1

print(ochn, distant)