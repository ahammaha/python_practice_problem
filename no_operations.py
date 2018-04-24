class No_operations():

	no = -1

	def __init__(self, no=1):
		self.no = no

	def fibonacci(self):
		a = 1
		b = 1
		for i in range(self.no):
			yield(a)
			a,b=b,a+b

	def factorial_using_loop(self):
		if self.no<0:
			return "Not a positive num"
		f = 1
		for i in range(1,self.no+1):
			f*=i
		return f

	def factorial_using_recursive(self, num=-1):
		if num == -1:
			num = self.no
		if num<0:
			return "Not a positive num"
		if num==0 or num==1:
			return 1
		return num*self.factorial_using_recursive(num-1)

	def check_if_happy_no(self, num):
		count=0
		while True:
			sum=0
			while num>=1:
				sum+=(num%10)**2
				num=int(num/10)
			if sum>1:
				num=sum
				count+=1
				if count==10:
					return False
			elif sum==1:
				return True

	def happy_numbers(self):
		#find first 10 happy number
		print("happy_numbers.......")
		count=0
		for i in range(1,50):
			if self.check_if_happy_no(i):
				yield(i)
				count+=1
				if count==10:
					break

if __name__ == '__main__':
	op=No_operations(int(input("Enter a number on which operation can be done : ")))
	print("fibonacci : "+str(list(op.fibonacci())))
	print("factorial_using_loop : "+str(op.factorial_using_loop()))
	print("factorial_using_recursive : "+str(op.factorial_using_recursive()))
	print("happy numbers : "+str(list(op.happy_numbers())))
	#print(op.check_if_happy_no(487))