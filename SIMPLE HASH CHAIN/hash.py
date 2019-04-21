import hashlib #imported python hashing library

# seed=('a2c83976c0adb482d280c6b10a042be3')
seed='ECSC'.lower() # using the example given, username 'ECSC' changed to lower case to be hashed to arrive at seed
# seed.lower()

challengehash='c89aa2ffb9edcc6604005196b5f0e0e4' # the given challenge hash for 'ECSC'

hash = hashlib.md5()  #The md5 hash to hash the given ECSC string

# for the md5 hashing algorithm to run on a string variable it needs to convert the string to byte using the utf-8 encording
hash.update(seed.encode('utf-8')) # Now hash the seed using md5b

seen = False # declare a variable called seed & initialize it to false
myseedhash=(hash.hexdigest()) # md5 hash value made readable
print(myseedhash) # print challenge hash found

while (seen== False): # while challenge hash is not found
    if(myseedhash==challengehash): #if challenge hash is found, print found challenge hash
        print("found challengehash") # print found challenge hash
        seen = True # make seed to become true
        break # break out of loop

    else: # challenge hash not found then continue to hash
        myseedhash = hashlib.md5(myseedhash.encode('utf-8')).hexdigest() # if challenge hash is
        print(myseedhash) # printing hashes as it loops through
