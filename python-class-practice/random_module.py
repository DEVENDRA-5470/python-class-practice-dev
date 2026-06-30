import random
# emp_name=["aman","kamal","shivam","anshu"]
# res=random.choice(emp_name)
# print(res)

# emp_name=["aman","kamal","shivam","anshu"]
# w=[2,3,1,0]
# res=random.choices(emp_name,weights=w , k=4)
# print(res)

# res=random.random()*1000
# print(int(res))


# rand_int=random.randint(1,10)
# rand_range=random.randrange(1,10)
# print(rand_int)
# print(rand_range)


# user max attempt = 6
# each attempt random number generate
# random number generate sum
# fix_value = 150


# choice()
# choices()
# randint()
# randranage()

# sample()
# emp_name=["aman","kamal","shivam","anshu"]
# res=random.sample(emp_name ,k=2)
# print(res)

# shuffle()
# emp_name=["aman","kamal","shivam","anshu"]
# random.shuffle(emp_name)
# print(emp_name)

# Coupon code
# def generate_coupon():
#     a_to_z="abcdefghijklmnopqrstuvwxyz"
#     num="1234567890"

#     char=[random.choice(a_to_z).upper() for i in range(1,5)]
#     num=[random.choice(num) for i in range(1,5)]

#     print("".join(char+num))

# for i in range(1,10):
#     generate_coupon()

def generate_coupon():
   import string
   "".join(random.choices(string.ascii_uppercase ,k=4))
   +"".join(random.choices(string.digits ,k=4))

for i in range(10):
    generate_coupon()