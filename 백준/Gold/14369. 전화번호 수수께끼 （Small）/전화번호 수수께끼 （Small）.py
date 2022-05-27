for i in range(int(input())):
    s=list(input())
    a=[]
    while s:
        while 'Z' in s:
            s.remove('Z')
            s.remove('E')
            s.remove('R')
            s.remove('O')
            a.append(0)
        while 'W' in s:
            s.remove('T')
            s.remove('W')
            s.remove('O')
            a.append(2)
        while 'X' in s:
            s.remove('S')
            s.remove('I')
            s.remove('X')
            a.append(6)
        while 'U' in s:
            s.remove('F')
            s.remove('O')
            s.remove('U')
            s.remove('R')
            a.append(4)
        while 'G' in s:
            s.remove('E')
            s.remove('I')
            s.remove('G')
            s.remove('H')
            s.remove('T')
            a.append(8)
        while 'O' in s:
            s.remove('O')
            s.remove('N')
            s.remove('E')
            a.append(1)
        while 'F' in s:
            s.remove('F')
            s.remove('I')
            s.remove('V')
            s.remove('E')
            a.append(5)
        while 'S' in s:
            s.remove('S')
            s.remove('E')
            s.remove('V')
            s.remove('E')
            s.remove('N')
            a.append(7)
        while 'R' in s:
            s.remove('T')
            s.remove('H')
            s.remove('R')
            s.remove('E')
            s.remove('E')
            a.append(3)
        while 'N' in s and 'I' in s:
            s.remove('N')
            s.remove('I')
            s.remove('N')
            s.remove('E')
            a.append(9)
    a.sort()
    print('Case #'+str(i+1)+': ',*a,sep='')