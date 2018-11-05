# def fbi(n:int):
# 	if n == 1 or n == 0:
# 		return 1
# 	return fbi(n-1) + fbi(n-2)


# def fbi_sl(n):
# 	for i in range(n):
# 		yield fbi(i)

# def pri(n):
# 	for _ in range(n):
# 		print(next(fbi_sl(n)))
# # fbi_sl(10)
# pri(10)


# def jc(n):
# 	if n==1:
# 		return 1
# 	return n*jc(n-1)

# print(jc(6))

def fbi():
	'''使用生成器编写斐波那契数列'''
	res = 1
	idx = 1
	while True:
		yield res
		yield idx
		res += idx
		idx += res
t = fbi()
for _ in range(10):
	print(next(t))



