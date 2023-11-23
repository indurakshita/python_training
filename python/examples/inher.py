"""
# single inheritance
class dad():
	def phone(self):
		print("dad's phone")
class son(dad):
	def laptop(self):
		print("son's laptop")
ram=son()
ram.phone()
ram.laptop()

 #multiple inheritance
class dad():
	def phone(self):
		print("dad's phone")
class mom():
    def sweet(self):
        print("mom's sweet")
class son(dad,mom):
	def laptop(self):
		print("son's laptop")
ram=son()
ram.phone()
ram.laptop()

ram.sweet()

#multilevel inheritance

class grandpa():
    def phone(self):
        print("grandpa phone")
class dad(grandpa):
    def money(self):
        print("dad's money")
class son(dad):
    def laptop(self):
        print("son's laptop")
        
ram=son()
ram.laptop()
ram.money()
d1=dad()
d1.phone()
ram.phone()
"""

#hierarchical inheritance

class dad():
    def money(self):
        print("dad's money")
class son1(dad):
     pass
class son2(dad):
    pass
class son3(dad):
    pass
s2=son2()
s2.money()