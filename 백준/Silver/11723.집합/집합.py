import sys
input=sys.stdin.readline
S=[]

for _ in range(int(input().rstrip())):
    command=list(input().rstrip().split())
    
    if len(command)==1:
        if command[0]=='all':
            S=[x for x in range(1,21)]
        else:
            S=[]

    else:
        command[1]=int(command[1])
        
        if command[0]=='add' and command[1] not in S:
            S.append(command[1])
        elif command[0]=='remove' and command[1] in S:
            S.remove(command[1])
        elif command[0]=='check' and command[1] in S:
            print(1)
        elif command[0]=='check' and command[1] not in S:
            print(0)
        elif command[0]=='toggle' and command[1] in S:
            S.remove(command[1])
        elif command[0]=='toggle' and command[1] not in S:
            S.append(command[1])