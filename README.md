# SecureSnaps
Image encryption and Decryption based on private-key cryptography

## Directories:
```
SecureSnaps
---| Enc
---| Dec
---| Temp
```

## Documentation

### keygen.py
* `max_val(ht,wdth)` : returns max(ht,wdth)
* `get_string_hash()` : returns the hashvalue for the entered password
* `generate_tuples(H,W)` : generates a list of tuples recursively for the codec
* `yield_chunks(block, iterate_size)` : returns lists of varying size for the hash list

### encoder.py
Encodes the image at `image_path` as per the entered password


### decoder.py
Decodes the image at `image_path` as per the entered password

### utils.py
* `fucntion(x)` : The first function for generating tuples
* `function2(x)`: The second function for generating tuples
* `swap(ai,aj,bi,bj, image, arr)` : swaps two pixels `arr(ai,aj)` with `arr(bi, bj)`
* `efficiency(orig, enco, W, H)` : Finds the efficiency of the encryption by comparing the original image with encoded image, W and H are width ad height respectively
* `cascade(xy, N, W, H)` : creates a recursively cascaded list (of length N) of tuples
* `automate_swap(alpha, beta, N, image, arr)` : swaps pixels automatically for encryption
* `automate_swap_dec(alpha, beta, N, image, arr)` : swaps pixels automatically for decryption


## Plan
```
Step 1:		Start SecureSnaps
Step 2:		Select (Encrypt/Decrypt)
Step 3:		Input (folder_path, password)
Step 4:		Encrypts/Decrypts the images in the directory and removes the original images
Step 5:		End

```
## Plan for Encryption/Decryption Algorithm
* Add more cascade functions
* Increase the tuple size from 4 elements to 8
* Make the cascade functions non-linear