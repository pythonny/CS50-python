# Even if you haven’t studied physics (recently or ever!), you might have heard that
# , wherein
#  represents energy (measured in Joules),
#  represents mass (measured in kilograms), and
#  represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.


mass = int(input("M:"))
c = 300000000

result = mass * (c * c)

print(f"E: {result}") # cann make it {result:,} , but want to match the example answer

