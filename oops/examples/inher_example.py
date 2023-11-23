#Inheritance

# class Parent:
#     def house(self):
#         return 'house'
    
#     def money(self):
#         return "money"
    
#     def car(self):
#         return "car"
    
#     def jewel(self):
#         return "jewel"
    
# class Child(Parent):
#     def education(self):
#         return "education"
    
# child = Child()
# child_asset = child.education(),child.car(),child.jewel(),child.house(),child.money()
# print(child_asset)

# # parent = Parent()
# # parent_assets = [
# #     parent.car(),
# #     parent.house(),
# #     parent.jewel(),
# #     parent.money()
# # ]
# # print(parent_assets)
'---------------------------------------------------------------------------------------------------------------'
# multiple inheritance -needs multiple parent classes
class Father:
    def house(self):
        return 'house'
    
    def money(self):
        return "money"
    
    def company(self):
        return "builder"
    
class Mother:

    def car(self):
        return "car"
    
    def jewel(self):
        return "jewel"
    
    def company(self):
        return "fashion design"
    

class Child(Father,Mother):
    def education(self):
        return "education"
    
# child = Child()
# child_asset = child.education(),child.car(),child.house(),child.jewel(),child.money(),child.company()
# print(child_asset)

'--------------------------------------------------------------------------------------------'
#Multilevel
class Grand_Father:
    def house(self):
        return 'house'
    
    def money(self):
        return "money"
    
    def company(self):
        return "builder"
    
class Parent(Grand_Father):

    def car(self):
        return "car"
    
    def jewel(self):
        return "jewel"
    
    def company(self):
        return "fashion design"
    

class Child(Parent):
    def education(self):
        return "education"
    
# child = Child()
# child_asset = child.education(),child.car(),child.house(),child.jewel(),child.money(),child.company()
# print(child_asset)
'------------------------------------------------------------------------------------------'

#Hierachial - Needs multiple classes

class GrandParent:

    def house(self):
        return 'house'
    
    def land(self):
        return "land"
    
    def money(self):
        return "money"

class ParentSibling1(GrandParent):

    def company(self):
        return "builder"
    
    def factory(self):
        return "factory"
    
class ParentSibling2(GrandParent):

    def car(self):
        return "car"
    
class Child1(ParentSibling1):

    def education(self):
        return "education"
    
class Child2(ParentSibling2):

    def education(self):
        return "education"

# child1 = Child1()
# child1_assets = child1.education(),child1.house(),child1.land(),child1.money(),child1.company(),child1.factory()
# print(child1_assets)

# child2 = Child2()
# child2_assets = child2.education(),child2.house(),child2.land(),child2.money(),child2.car()
# print(child2_assets)

'------------------------------------------------------------------------------'
#Hybrid 

class GrandParent:

    def house(self):
        return 'house'
    

class ParentSibling1(GrandParent):

    def company(self):
        return "builder"
    
    def factory(self):
        return "factory"
    
class ParentSibling1(GrandParent):

    def company(self):
        return "builder"
    
    def factory(self):
        return "factory"
    
class ParentSibling2(GrandParent):

    def car(self):
        return "car"
    
class Child1(ParentSibling1):

    def education(self):
        return "education"
    
class Child2(ParentSibling1,ParentSibling2):

    def hobby(self):
        return "bookd reading"
    
child2 = Child2()
child2_asserts = child2.hobby(),child2.car(),child2.factory(),child2.company(),child2.house()
print(child2_asserts)

child1 = Child1()
child1_asserts = child1.education(),child1.company(),child1.factory(),child1.house()
print(child1_asserts)

    