# To print length of a string
# print(len(input("What is your name ?")))

#name = input("What are you doing?")
#print(name)

#name1 = "You are playing and " +name
#print(name1)

#length = len(name1)

#print(length)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)