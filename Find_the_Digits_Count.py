number=int(input())
digit_count=0
while number>0:
    number=number//10
    digit_count+=1
print(digit_count)