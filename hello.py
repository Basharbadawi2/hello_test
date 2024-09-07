def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

num = 5
res = factorial(num)
print(f"the factorial of {num} is {res}.")
