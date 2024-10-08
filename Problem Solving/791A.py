x,y = map(int,input().split())
year = 0
while(x <= y):
    year+=1
    x*=3
    y*=2
print(year)