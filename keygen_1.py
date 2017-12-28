import hashlib
import binascii
import getpass

max_iter = 100000

def blocking_func(block, size_t):
    for i in range(0, len(block), size_t):
         yield block[i: i + size_t]

    
''' The function generate_tuples generates two keys and XOR them 
    to produce the final key.
'''
def generate_tuples_1(H, W, password):
    height = H
    width = W

    minm = min(height, width)
    
    # Reversing the string password
    rev_password = ""
    for i in password:
        rev_password = i + rev_password

    enc_password = rev_password.encode('utf-8')
    hash_str = hashlib.sha1(enc_password).hexdigest()

    salt_1 = hash_str[0:20]
    salt_2 = hash_str[20:]

    key_1_t = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_1.encode('utf-8'), max_iter)
    temp_1 = binascii.hexlify(key_1_t)
    key_1 = temp_1.decode('utf-8')

    key_2_t = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_2.encode('utf-8'), max_iter)
    temp_2 = binascii.hexlify(key_2_t)
    key_2 = temp_2.decode('utf-8')

    list1 = list(blocking_func(key_1, 4))
    list2 = list(blocking_func(key_2, 4))

    num_list_1 = []
    num_list_2 = []

    num_list_1.append([int(i, 16) for i in list1])
    num_list_2.append([int(i, 16) for i in list2])
    num_list_1 = num_list_1[0]
    num_list_2 = num_list_2[0]

    final_key = []

    final_key.append([(num_list_1[i] ^ num_list_2[i]) % minm for i in range(len(num_list_1))])

    final_key = final_key[0] 

    keytupl1 = final_key[0:4]
    keytupl2 = final_key[4:8]
    keytupl3 = final_key[8:12]
    keytupl4 = final_key[12:]

    return (keytupl1, keytupl2, keytupl3, keytupl4)
