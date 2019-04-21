from Crypto.PublicKey import RSA # rsa import

#Private key vairable to open mykey3 as a readable file
file_private_key = open("mykey2","r")
binPrivateKey = RSA.importKey(file_private_key)

print(binPrivateKey.n) # print the value of n
print("space")
print(binPrivateKey.e) # print the value of e
print("space")
print(binPrivateKey.d) # print the value of d
