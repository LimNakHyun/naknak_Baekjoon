numbr=int(input())
students=list(map(int,input().split()))
main,sub=map(int,input().split())

result=0

for student in students:
    student=student-main
    result=result+1
    if student>0:
        result=result+(student//sub)
        student=student%sub
        if student>0:
            result=result+1
print(result)