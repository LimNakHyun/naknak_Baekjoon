def bracket(x):
    y=[]
    for i in range(len(x)):
        if x[i]=='(':y.append(x[i])
        elif x[i]==')':
            if '(' in y:y.pop()
            else:return False
    if '(' in y:return False
    return True

for _ in range(int(input())):
    print('YES') if bracket(list(input()))==True else print('NO')