n = int(input())
participants = [input() for i in range(n)]
ochn = 0
distant = 0
for i in participants:
    info = list(i.split())
    info[2] = int(info[2])
    info[3] = bool(info[3])
    if info[3] == True:
        ochn += 1
    else:
        distant += 1

print(ochn, distant)