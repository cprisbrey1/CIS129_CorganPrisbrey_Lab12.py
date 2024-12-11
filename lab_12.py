class Pet:
	def __init__(self, name=None, type=None, age=0):
		self.name = name
		self.type = type
		self.age = int(age)
	def set_name(self, name):
		self.name = name
	def set_type(self, type):
		self.type = type
	def set_age(self, age):
		self.age = int(age)
	def get_name(self):
		return self.name
	def get_type(self):
		return self.type
	def get_age(self):
		return self.age


def get_info(pet):
	pet.set_name(input("Enter your pet's name: \n"))
	pet.set_type(input("Enter your pet's type: \n"))
	pet.set_age(input("Enter your pet's age: \n"))

def display_info(pet):
	print(f"Your pet's name: {pet.get_name()}")
	print(f"Your pet's type: {pet.get_type()}")
	print(f"Your pet's age: {pet.get_age()}")

if __name__ == "__main__":
	cocofink = Pet()
	get_info(cocofink)
	display_info(cocofink)
