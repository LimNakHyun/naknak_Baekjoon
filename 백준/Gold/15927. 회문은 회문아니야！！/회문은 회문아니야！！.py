string=input()
print(len(string)) if string!=string[::-1] else print(-1) if string.count(string[0])==len(string) else print(len(string)-1)