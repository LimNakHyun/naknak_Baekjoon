import sys
input=sys.stdin.readline

def prime_index(x):
    index_list=[1 for _ in range(x+1)]

    for i in range(2,int(x**0.5)+1):
        if index_list[i]:j=2
        while i*j<=x:
            index_list[i*j]=0
            j=j+1
    return index_list

numbers=[int(input()) for _ in range(int(input()))]
max_num_p_index=prime_index(max(numbers))

for number in numbers:
    count=0
    for i in range(2,(number//2)+1):
        if max_num_p_index[i] and max_num_p_index[number-i]:count=count+1
    print(count)