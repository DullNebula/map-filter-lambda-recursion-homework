#Exercise #1
#Filter out all of the empty strings from the list below

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

stripped_places = [s.strip() for s in places]
filtered_places = list(filter(None, stripped_places))
print(filtered_places)

#Exercise #2
#Write an anonymous function that sorts this list by the last name...

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author = sorted(author, key = lambda x : x.split()[-1].lower())
print(author)


#Exercise #3
#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

places = list(map(lambda x: (x[0], (9/5)*x[1] + 32), places))

print(places)

#Exercise #4
#Write a recursion function to perform the fibonacci sequence up to the number passed in.

def the_Fibonacci(x):
   if x <= 1:
       return x
   else:
       return(the_Fibonacci(x-1) + the_Fibonacci(x-2))
fibterms = 10

if fibterms <= 0:
    print("Can't input negative numbers") 
else:
   print("Fibonacci sequence:")
   for i in range(fibterms):
       print(the_Fibonacci(i))