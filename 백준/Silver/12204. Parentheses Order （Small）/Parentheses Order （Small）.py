import sys
input = sys.stdin.readline

def check(seq: list):
    st = []
    for par in seq:
        if par == '(':
            st.append(par)
        else:
            if len(st) == 0:
                return False
            st.pop()
    return len(st) == 0

def generate_par_seq(seq: list, mx_len):
    if len(seq) == mx_len:
        if check(seq):
            par_seq_lst.append(''.join(seq))
        return
    for par in "()":
        generate_par_seq(seq + [par], mx_len)

t = int(input())
for tn in range(1, t+1):
    n, k = map(int, input().split())
    par_seq_lst = []
    generate_par_seq([], n*2)
    
    print(f"Case #{tn}: ", end="")
    if k > len(par_seq_lst):
        print("Doesn't Exist!")
    else:
        print(par_seq_lst[k-1])