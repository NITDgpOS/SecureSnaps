import hashlib
import getpass

def max_val(ht, wdth):
    return max(ht, wdth)

def yield_chunks(block, iterate_size):
    for i in range(0, len(block), iterate_size):
        yield block[i: i + iterate_size]

def get_string_hash(psswd):
    # Encode the string into a byte array
    psswd_encoded = psswd.encode('utf-8')
    # Generate hash value
    hash_psswd = hashlib.sha256(psswd_encoded)
    hashvalue = hash_psswd.hexdigest()
    return hashvalue

def generate_tuples(H, W, pwd):
    height = H
    width = W
    password_hashed = get_string_hash(pwd)
    hash_lst = list(yield_chunks(password_hashed, 4))
    # print (hash_lst)
    mod = max_val(height, width)
    finval = []
    # Since we want our values to be less than the height or width of the image
    finval.append([(int(i, 16)) % mod for i in hash_lst])
    finval = finval[0]
    keytupl1 = finval[0:4]
    keytupl2 = finval[4:8]
    keytupl3 = finval[8:12]
    keytupl4 = finval[12:]

    return (keytupl1, keytupl2, keytupl3, keytupl4)
