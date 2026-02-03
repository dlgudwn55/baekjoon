n = int(input())
a, b, c, d, e, f = map(int, input().split())
# print(max(a))

if n == 1:
    print(sum([a, b, c, d, e, f]) - max([a, b, c, d, e, f]))
else:
    one_face_count = (n-2)*(n-1)*4+(n-2)*(n-2)
    two_face_count = (n-1)*4+(n-2)*4
    three_face_count = 4
    # print(one_face_count + two_face_count + three_face_count)
    ans = one_face_count * min(a, b, c, d, e, f)
    ans += two_face_count * min(a+b, a+c, a+d, a+e, b+c, b+d, b+f, c+e, c+f, d+e, d+f, e+f)
    ans += three_face_count * min(a+c+e, a+d+e, a+b+c, a+b+d, f+b+d, f+b+c, f+e+c, f+e+d)
    print(ans)