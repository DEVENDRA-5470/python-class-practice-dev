import os
# print(os.listdir())
# print("Current folder :",os.getcwd())
# path=r"C:\Users\dev\OneDrive\Desktop"
# os.chdir(path)
# print("Current folder :",os.getcwd())
# with open("os.txt","w") as file:
#     print(f"File create at {os.getcwd()}")

# print(os.listdir())

# print(os.getcwd()) # current working dir
# print(os.listdir()) # listing all files and folder
# print(os.path.exists("xyz.txt"))
# C:\Users\dev\OneDrive\Desktop\git-for-118\python-class-practice\aman.txt

# emp_list=["aman","shivam","shubham","anshu","kamal","dev","xyz"]
# for i in emp_list:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#         with open(f"{i}.txt","w") as file:
#             print(f"{i}.txt File Created .✅")
#     else:
#         print(f"{i} - File Already Exits ✅")

# folder="Employee_Details"
# os.makedirs(folder)




path=r"C:/Users/dev/OneDrive/Desktop/git-for-118/Employee_Details"
os.chdir(path)
print(os.getcwd())
print(os.listdir())
os.path.join()

emp_list=["aman","shivam","shubham","anshu","kamal"]
for i in emp_list:
    with open(f"{i}.txt","w") as file:
        print(i , "Created")







