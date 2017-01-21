# SecureSnaps
This repo is in its early stages of development.

##Directories:
```
SecureSnaps
---| Enc
---| Dec
---| Temp
```

##Process flow:
###Agenda for Phase-I [23rd Jan 2017 - 15th Feb 2017]

* write a python script which opens an image file (say, filename: file1.jpeg) and then save it as file1_enc.jpeg in 
the `Enc` directory as file1_enc.jpeg
* Take a string input and convert it into an integer array as mentioned in the paper (will be shared with only a few)
* Save the Height and Width of the image in H and W named variables respectively.
* Encoding is easier than Decoding, as Decoding involves recursion and recursion stack depth is finite.
