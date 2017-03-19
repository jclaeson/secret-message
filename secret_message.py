#initial version
import os
import numpy as np
import numpy.random as npr

def encode_message(file_list):
  rand_array = np.array(npr.randint(321, 1868, 400))
  counter = 0
  for file_name in file_list:
      os.rename(file_name, str(rand_array[counter])+file_name)
      counter += 1

def decode_message(file_list):
  for file_name in file_list:
    os.rename(file_name, file_name.translate(None, "0123456789"))
  os.chdir(r"../")

print("Welcome to the secret message!")
print("Select an option:")
print("[1] Decode message")
print("[2] Encode message")
selection = raw_input("Enter your choice: ")

file_list = os.listdir(r"message")
os.chdir(r"message")

if int(selection) == 1:
  decode_message(file_list)
elif int(selection) == 2:
  encode_message(file_list)
else:
  print("Invalid selection! Bye")
  os.chdir(r"../")
  exit()

os.chdir(r"../")
