# List
# List is a collection of Variables
from ipaddress import ip_address


l1 = [1,2,3,4,56] # Integer list
l2 = []             # Empty List
l3 = [1,1,1,1,2,3,4,"omkar","mixedlist"] # Mixed List
l3.append("sanjay pomendkar")  # Use to add at the End of the List
l2.insert(0,"omkar") # Use to inserrt at particular element
l3.remove(2)
print(l1)
print(l2)
print(l3)
print(l3[0])
print(len(l1))
print(l3.count(1))
# l1.reverse()
l1[::-1]
print(l1)


#Tuples
# A tuple is similar to a list except that it is fixed-length and immutable
ip_address = ('192.166.0.1',8080)
print(ip_address)

# Dictionaries
#  Key-Value Pair
family = {
    "First" : "Omkar",
    "Middle" : "Sanjay",
    "Last" : "Pomendkar"
}
print(family)

# Default Dictionaries
# Values which never Changed

India_States = {
    'India' : "Maharashtra",
    'India' : "Raigad",
    'India' : "Ratnagiri"

}
print(India_States)

# Set 
# Set is a collection of elements with no repeat Values
Names = {'omkar','surbhi','vedika'}
print(Names)

"""if name in Names:
    print(name)"""