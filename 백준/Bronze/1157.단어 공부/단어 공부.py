word=(input())
word=list(word.upper())
cnt_list=[word.count(chr(x)) for x in range(65,91)]
w_max=max(cnt_list)
if cnt_list.count(w_max)==1:
    print(chr(cnt_list.index(w_max)+65))
else:
    print('?')