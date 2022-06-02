import sys
input=sys.stdin.readline
n,m=map(int,input().strip().split())

pokemons={}

for i in range(n):
    pokemons[i+1]=input().strip()

snomekop={v:k for k,v in pokemons.items()}

for _ in range(m):
    temp=input().strip()
    print(pokemons.get(int(temp))) if ord(temp[0])<60 else print(snomekop.get(temp))