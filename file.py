# open('file_path', 'mode')
# close()

"""File handling in Python is the process of working with files stored on your computer's permanent storage. The primary function for this is open(), 
which takes the filename and mode as parameters and returns a file object. """

# # Modes :
# 'r'  -> reading moding
# 'w'  -> writting mode
# 'a' -> append mode 
# 'x' -> create file

# 't' --> text file 
# 'b' --> binary file

# By default 'rt'  (reading text file)
# 'r' --> if file does not exist it will give error 
# 'w' --> if file does not exist so it will create file. overwrite if content is there.
# 'a' --> if file does not exist so it will create file. content will be added.
# 'x' --> if file exist it will give error 
# '+' -->

# file = open("abc.txt",'r')
# # print(file.read())
# # print(file.readline())
# # print(file.readline())
# print(file.readlines())  # [\n]
# # file.close()

# file = open('xyz.txt','rt') # error

file = open('xyz.txt','w')
file.write("Hello opening a file in writting mode for first time.")
file.close()

# file2 = open("xyz.txt")
# print(file2.read())
# file.close()

# with open("xyz.txt",'w+') as f :
#     f = f.write("Now this time content will be overwrite......")
    

# with open('xyz.txt','a') as file :
#     f = file.write("\n This time using append mode so content will be added at the end....")



# # with open('xyz.txt','x') as file2:
# #     pass

# # fil23 = open("123.txt", 'x')

import os 
file = "xyz.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print("file path not found !!")