a,b,c=map(int,input().split())
d = b**2 - 4*a*c
if d < 0:
    print('d < 0')
elif d == 0:
    print(-b / (2*a))
else:
    print((-b - d**0.5) / (2*a), (-b + d**0.5) / (2*a))