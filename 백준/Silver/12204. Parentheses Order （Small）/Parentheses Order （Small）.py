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

def generate_par_seq(seq: list, mx_len, open_par_count):
    if len(seq) == mx_len:
        # if check(seq):
        if open_par_count == 0:
            par_seq_lst.append(''.join(seq))
        return
    # for par in "()":
    generate_par_seq(seq + ['('], mx_len, open_par_count + 1)

    if open_par_count > 0:
        generate_par_seq(seq + [')'], mx_len, open_par_count - 1)

t = int(input())
for tn in range(1, t+1):
    n, k = map(int, input().split())
    par_seq_lst = []
    generate_par_seq([], n*2, 0)
    
    print(f"Case #{tn}: ", end="")
    if k > len(par_seq_lst):
        print("Doesn't Exist!")
    else:
        print(par_seq_lst[k-1])