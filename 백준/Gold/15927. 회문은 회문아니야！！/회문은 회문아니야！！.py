string=input()

if string!=string[::-1]:
    print(len(string))
elif string.count(string[0])==len(string):
    print(-1)
else:
    print(len(string)-1)