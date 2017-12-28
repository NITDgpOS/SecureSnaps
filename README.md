# SecureSnaps

[![Join the chat at https://gitter.im/SecureSnaps55/Lobby](https://badges.gitter.im/SecureSnaps55/Lobby.svg)](https://gitter.im/SecureSnaps55/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg "Made with Python")

Image encryption and Decryption based on private-key cryptography

## Algorithm Description
* Step 1: User enters a password: `password`
* Step 2: The `password` is encoded in `utf-8` followed by generating a `sha256 hash`
* Step 3: The `sha256 hash` is converted to `hex`
* Step 4: This `hex` values are used to generate an array of integer values
* Step 5: The array is divided into four `key tuples`, each containing 4 integers.
* Step 6: Each key tuple is used to encode/ decode the image. The number of times, the recursive encryption/decryption takes place for a key tuple is called the degree of the key tuple.
* Step 7: Using the key tuples, the color is also encoded using a XOR cipher

### Encryption using Key tuples
Let's say we have a key tuple [a, b, c, d] , codec function f(x) and degree = n

|ith degree |Key tuple 								|Process 													|
|:----------|:-----------------------------------------|:--------------------------------------------------------------|
|0	|	[a, b, c, d]							|	nothing														|
|1	|	[f(a), f(b), f(c), f(d)]				|	Swap Pixel f(a),f(b) with Pixel f(c),f(d)				|
|2	|	[f(f(a)), f(f(b)), f(f(c)), f(f(d))]	|	Swap Pixel f(f(a)),f(f(b)) with Pixel f(f(c)),f(f(d))	|
|...|	...										|	...															|
|n 	|	[fn(a), fn(b), fn(c), fn(d)]			|	Swap pixel Pixel fn(a),fn(b) with Pixel fn(c),fn(d)			|

Note: Decryption algorithm is simply the reversal of Encryption process.

### Color encryption using XOR
* Extract 3 values from a key tuple [a, b, c]
* A single pixel consists of three values - (RED, GREEN, BLUE)
* Here, we use XOR logical operation between each pixel parameter and key tuple value
   *  NEW_RED = RED ^ a

   * NEW_GREEN = GREEN ^ b

   * NEW_BLUE = BLUE ^ c,  where ^ is XOR


* We replace the old pixel with the newly formed pixel (NEW_RED, NEW_GREEN, NEW_BLUE)
* XOR has a special property which enables us to trace back the original pixel values without loss of data

   * a^b = c

   * c^b = a


*  Here, let `a` be the pixel parameter and `b` be the key tuple value. On XORing it, we obtain `c` and we store it.
*  For decryption, XORing `c` with key tuple value `b` will give us the original pixel value `a`.
* Each pixel value ranges from 0 to 255. Hence the modulus of 256 is applied over final results after XORing.

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
* `color(arr, val, W, H)` : Encrypts the color of each pixel against key tuple using XOR operation

## Installation and Usage
```
git clone https://github.com/NITDgpOS/SecureSnaps.git
cd SecureSnaps
sudo bash install
```
* To encode:
`ssnaps -e <image_path>`
* To decode:
`ssnaps -d <image_path>`

Check the [Contribution Guidelines here](docs/CONTRIBUTING.md)
