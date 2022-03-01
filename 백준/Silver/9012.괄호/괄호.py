def bracket_fuction(bracket):
    res=[]
    for i in range(len(bracket)):
        if bracket[i]=='(':
            res.append(bracket[i])
        elif bracket[i]==')':
            if '(' in res:
                res.pop()
            else:
                return False
    if '(' in res:
        return False
    return True

n=int(input())
for i in range(n):
    print('YES') if bracket_fuction(input())==True else print('NO')