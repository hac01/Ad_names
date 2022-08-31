#Simple python code to convert names 
#for ex frank castle output :- f.castle fcastle etc....

first_name=input("Put Your first Name\n")
last_name=input("Put Your last name \n ")

first_name_list=[]
last_name_list=[]

for i in first_name:
    first_name_list.append(i)

for i in last_name:
    last_name_list.append(i)

last_name_list_joined=''
for i in last_name_list:
    last_name_list_joined+=i

first_name_list_joined=''
for i in first_name_list:
    first_name_list_joined+=i

#fcastle
def first_char_lastname():
    f_name=first_name_list[0]
    print(f_name+last_name_list_joined)

#f.castle
def first_char_dot_lastname():
    f_name=first_name_list[0]
    print(f_name+"."+last_name_list_joined)

#frank.castle
def firstname_dot_lastname():
    print(first_name_list_joined+"."+last_name_list_joined)

#frankcastle
def name():
    print(first_name_list_joined+last_name_list_joined)



def final():
    print("Here are some possible names")
    print("Made "+"\u2764\uFE0F"+"  Hac10101")
    first_char_lastname()

    first_char_dot_lastname()

    firstname_dot_lastname()

    name()

final()
