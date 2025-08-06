# Must implement .read(), .join(), .remove(), iterate through the remove list, 
# convert a string to a list, and use with open() as file: with "w" and "r" and "a"

import re
from IP_address_list import ip_address_list
# The lsit that will hold the final list of IP addresses that are allowed to access specific content
import_file = "allow_list.txt"

ip_address_list(import_file)


# IP addresses that are not safe and can't be allowed tp access specific information
# remove_list = ["192.168.97.142", "192.168.97.108", "192.168.97.219", "192.168.97.173", "192.168.97.201", "192.168.97.125", "192.168.97.187", "192.168.97.156", "192.168.97.198", "192.168.97.165", "192.168.97.117", "192.168.97.133", "192.168.97.203", "192.168.97.149", "192.168.97.184"]
remove_list = ["192.168.97.142",
    "192.168.97.108",
    "192.168.97.173",
    "192.168.97.125",
    "192.168.97.198",
    "192.168.97.117",
    "192.168.97.184"
]

with open(import_file, "r") as file:
    text = file.read()
# Chekcing to see if the import_file was actually read and copied onto the text vartiable
# print(text)

# Creating the text string to a list using .split() and storing it in new_list variable
new_list = text.split()
# iterates through remove_list and stores its values in the ip Variable
# then checks if ip is in the new_list variable.  If so, remove that value from new_list
for ip in remove_list:
    if ip in new_list:
        new_list.remove(ip)

# Could also do this:
# for ip in new_list:
#     print(ip, "\n")
#     if ip in remove_list:
#         print(" removed" ,ip, "from the list\n")
#         new_list.remove(ip)
#     else:
#         print("THE IP ADDRESS IS SAFE")



# Now convert the new_list list to a string with "\n".join() and store it in updated_list with it being separated with new lines
updated_list = "\n".join(new_list)

# If you want to separate with commas on a straight line, use this:
# updated_list = ", ".join(new_list)


# Now we use with open(import_file, "w") as file: to change the content of the original wich is import file 
# with the updated_list varibale
with open(import_file, "w") as file:
    file.write(updated_list)

# now we check the to see if the orginal file was change by using
# with open() and using the "r" as a parameter 

with open(import_file, "r") as file:
    text = file.read()

print(text)