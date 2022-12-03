import random
def password_generator(pw_len):
    data_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$^&**_"
    passwords_list = [] 
    for i in pw_len:
        password = '' 
        for j in range(i):
            nxt_ind = random.randrange(len(data_string))
            password = password + data_string[nxt_ind]
        passwords_list.append(password) 
    return passwords_list

print('HELLO, I AM A PASSWORD GENERATOR...............') 
n = int(input("Number of passwords to generate:"))
print('Generating',n,'PASSWORDS')
passwordLengths = []
print('Minimum length of password should be 6')
for i in range(n):
    length = int(input('Enter the length of password' + str(i+1) + ':'))
    if length<6:
        length = 6
        print(' ')
        print('NOTE==>Minimum length of password is 6!')
        print(' ')
    passwordLengths.append(length)

Password = password_generator(passwordLengths)
for i in range(n):
    print('Password',i+1,'=',Password[i])

