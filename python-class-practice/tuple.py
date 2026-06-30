# ----------------- tuple -------------------------
# Defination and property of tuple.
# creation of tuple.
# indexing and slicing.
# Traversing
# In-built methods
# tuple comprehension (count(),index())
# Assignment and class Activity.

#---------------- Defination and property of tuple.
# 1.tuple is a data structure in python used to store 
# multiple data of different types with comma(,) in round braces.
# 2.Immutable
# 3.Support indexing slicing and oredered.

# ----------- creation of tuple.
# t1,t2,t3=(50,40,"dev")
# print(type(t3))
# print(t1)
# print(t2)
# print(t3)

# indexing and slicing.
# marks_tuple=(50,55,69,34,89)
# print(marks_tuple[-1])
# print(marks_tuple[::-1])

# mutability ❌
# marks_tuple=(50,55,69,34,89)
# marks_tuple[2]=500
# print(marks_tuple)

# Traversing
# 1.Waf to ectract all number greater than 55, marks_tuple=(50,55,69,34,89)
# def tuple_fun(m):
#     new_value=[]
#     for i in m:
#         if i>=55:
#             new_value.append(i)
#     return new_value
# marks_tuple=(50,55,69,34,89)
# res=tuple_fun(marks_tuple)
# print(res)

# 2.Waf to sum of indices of tuple, 
# marks_tuple=(50,55,69,34,89)
# s=0
# for i in range(len(marks_tuple)):
#     s+=i
# print(s)


from custom_mod import check_odd_even,rev_str

print(check_odd_even(10))

print(rev_str("aman"))

