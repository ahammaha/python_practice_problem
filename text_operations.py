class String_text_operations():
	input_str = ''
	
	def __init__(self,input_str):
		self.input_str = input_str

	def check_if_palindrome(self):
		if self.input_str==self.reverse_str():
			return "Palindrome"
		else:
			return "Not a Palindrome"

	def count_vowels(self):
		count = {'a':0,'e':0,'i':0,'o':0,'u':0}
		for char in self.input_str.lower():
			if char in count.keys():
				count[char]+=1
		return count
	def reverse_str(self):
		return self.input_str[::-1]

	def count_word(self):
		return len(self.input_str.split(" "))

if __name__=='__main__':
	obj = String_text_operations(input("Enter a string : "))
	print("Reverse string : "+obj.reverse_str())
	print("Vowel count : "+str(obj.count_vowels()))
	print(obj.check_if_palindrome())
	print("No of words : "+str(obj.count_word()))