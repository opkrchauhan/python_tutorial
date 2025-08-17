# Tuple Operations

s = "Omprakash"
#s[0]= 'o'  # This will raise an error because strings are immutable in Python
print(s)

a = ('O', 'm', 'p', 'r', 'a', 'k', 'a', 's')
# a[0]='c'
print(a)  
print(a[0])  # Accessing the first element of the tuple
print(a[1:4])
print(a[1:]) 
print(a[:4])
print(a.index('m'))
print(a.count('a'))
# print(a.append('h'))
print(a + ('h','c'))  # Concatenating 
print(len(a))
print(a * 2)
print(max(a))
print(min(a))
# sorted(a)
# print(sum(a))