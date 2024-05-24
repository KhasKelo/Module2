import random

random_number = random.randint(3, 20)
print(random_number)


number_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 16, 17, 18, 19, 20][2:random_number]
new_arr = []
for i in number_arr:
    if random_number % i == 0:
        new_arr.append(i)
#print(new_arr)

password = []
passd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 16, 17, 18, 19, 20]

for i in new_arr:
   for j in passd:
       for k in passd:
           if i == j + k:
            password.append(j)
            password.append(k)
#print(password)

portdin = []
rut = []
for i in password:
    rut.append(i)
    if len(rut) == 2:
        portdin.append(rut)
        rut = []

#print(portdin)

for i in portdin:
   if i[0] == i[1]:
       portdin.remove([i[0],i[1]])
#print(portdin)


right_password = sorted(portdin)


def fiku(l):
    n = []
    for i in l:
        if i not in n and sorted(i) not in n:
            n.append(i)
    return n



result = fiku(right_password)
ff=[]

for i in result:
    ff+=i


print(''.join(map(str,ff)))



























