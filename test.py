kelipatan_5 = 'Backend'
kelipatan_3 = 'Frontend'
N =50
for i in range(N+1):
    if i % 3 == 0:
        i = kelipatan_3
    elif i % 5 == 0:
        i = kelipatan_5
    print(str(i))