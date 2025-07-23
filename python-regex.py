import re

my_text = "my name is varma i am from  vijayawada. i born and brough up in vijayawada"

# a = re.findall("vijayawada",my_text)

# print(a)



# a = re.split("born",my_text)

# print(a)


#its replacing the serached string
# a = re.sub("vijayawada","guntur",my_text)

# print(a)

# a = re.search("vijayawada",my_text)

# print(a)


a = re.search("a",my_text)

print(a.group)