# given an integer, this code attempts to convert it into a string, and if 
# the input is not an integer, it throws an exception

x = input("integer: ")
try:
    print(int(x))	

except:
	print("could not convert str to int", x)
