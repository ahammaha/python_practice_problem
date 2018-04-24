from random import randint

class Generators_example():
	def __init__(self):
		pass

	def gensquares(self,no):
		for i in range(1,no+1):
			yield i*i

	def gen_random_nos(self,lower,upper,no):
		for i in range(no):
			yield randint(lower,upper)

	def convert_str_to_iterator(self,str_val):
		return iter(str_val)


if __name__=='__main__':
	gen=Generators_example()

	print("SQUARE NUMBERS : ")
	#print square of the numbers in the given range
	for i in gen.gensquares(int(input("Enter a number : "))):
		print(i)

	#print n random numbers
	print("RANDOM NUMBERS : ")
	lower_bound=int(input("Enter a lower bound : "))
	upper_bound=int(input("Enter a upper bound : "))
	no_of_randno_to_gen=int(input("No of random numbers to be generated : "))
	for i in gen.gen_random_nos(lower_bound,upper_bound,no_of_randno_to_gen):
		print(i)

	#convert string to iterator
	iter_str = gen.convert_str_to_iterator(input("Enter a string : "))
	print(next(iter_str))
	for char in gen.convert_str_to_iterator(input("Enter a string : ")):
		print(char,end=" ")