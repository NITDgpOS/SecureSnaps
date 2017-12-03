import hashlib, binascii, getpass

max_iter = 100000


def blocking_func(block, size_t):
    for i in range(0, len(block), size_t):
         yield block[i: i + size_t]

    
    
    ''' The function generate_tuples generates two keys and XOR them 
        to produce the final key.
    '''


def generate_tuples(h, w):
    
    height = h
    width = w

    minm = min(height, width)

    password = getpass.getpass()
    
    # print(password_e, password_e[0])
    # print(password, password[0], type(password))

    # Reversing the string password

    rev_password = ""
    for i in password:
        rev_password = i + rev_password

    # print(rev_password, rev_password[0], type(rev_password))

    enc_password = rev_password.encode('utf-8')
    hash_str = hashlib.sha1(enc_password).hexdigest()

    # print(hash_str, len(hash_str), hash_str[0], type(hash_str))

    

    salt_1 = hash_str[0:20]
    salt_2 = hash_str[20:]

    # print(salt_1, salt_2, len(salt_1), len(salt_2), salt_1[0], salt_2[0], type(salt_1), type(salt_2))

    key_1_t = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_1.encode('utf-8'), max_iter)
    temp_1 = binascii.hexlify(key_1_t)
    key_1 = temp_1.decode('utf-8')

    # print('Key 1 is :')
    # print(key_1, len(key_1), key_1[0], type(key_1))
    
    key_2_t = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_2.encode('utf-8'), max_iter)
    temp_2 = binascii.hexlify(key_2_t)
    key_2 = temp_2.decode('utf-8')

    # print('Key 2 is :')
    # print(key_2, len(key_2), key_2[0], type(key_2))

    list1 = list(blocking_func(key_1, 4))
    list2 = list(blocking_func(key_2, 4))

    # print('list 1 :')
    # print(list1, type(list1))
    # print('list 2 :')
    # print(list2, type(list2))

    num_list_1 = []
    num_list_2 = []

    num_list_1.append([int(i, 16) for i in list1])
    num_list_2.append([int(i, 16) for i in list2])
    num_list_1 = num_list_1[0]
    num_list_2 = num_list_2[0]

    # print('num list 1 : ')
    # print(num_list_1, type(num_list_1), num_list_1[0], len(num_list_1))
    # print('num list 2 : ')
    # print(num_list_2, type(num_list_2), num_list_2[0], len(num_list_2))

    final_key = []


    
    final_key.append([(num_list_1[i] ^ num_list_2[i]) % minm for i in range(len(num_list_1))])

    final_key = final_key[0] 

    # print('Final Key is : ')
    # print(final_key, len(final_key), final_key[0])

    keytupl1 = final_key[0:4]
    keytupl2 = final_key[4:8]
    keytupl3 = final_key[8:12]
    keytupl4 = final_key[12:]
    
    # print(keytupl1, keytupl2, keytupl3, keytupl4)

    return (keytupl1, keytupl2, keytupl3, keytupl4)
