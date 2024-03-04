numbers = list(map(int,input().split()))
sqrt_numbers = [i**2 for i in numbers]
print(sum(sqrt_numbers)%10)