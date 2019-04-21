"""
This code attempts to get the public key and a ciphertext should he imposible
"""

import binascii #import binascii library
from Crypto.PublicKey import RSA #import rsa library

import gmpy2 #import gmpy2

def string2int(my_str): #method to convert string to integer
    return int(binascii.hexlify(my_str), 16) #return converted String

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8") #returning binary ascii code passing in an integer

# a while loop method to decrypt the cipher
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m


def rsa_unpadded_message_attack(ct, modulus, exponent=3): # rsa attack tool for decrypting
  while True:
    rec, e = gmpy2.iroot(ct, exponent)
    if e:
      break

    ct += modulus

  return gmpy2.long_to_bytes(rec)


n= 23516695565660963250242846975094031309572348962900032827958534374248114661507001374384417953124930587796472484525315334716723068326965228898857733318407681656604325744994115789416012096318656034667361976251100005599211469354510367804546831680730445574797161330145320706346512982316782618118878428893337849886890813813050423818145497040676697510093220374542784895778086554812954376689653727580227087363619223145837820593375994747273662064715654881379557354513619477314410917942381406981452545764657853425675230343749326640073923166795823683203941972393206970228647854927797483660176460658959810390117898333516129469397
e= 3

ciphertext = 145069245024457407970388457302568525045688441508350620445553303097210529802020156842534271527464635050860748816803790910853366771838992303776518246009397475087259557220229739272919078824096942593663260736405547321937692016524108920147672998393440513476061602816076372323775207700936797148289812069641665092971298180210327453380160362030493

decrypted = rsa_unpadded_message_attack(ciphertext,n,e) # decrypting using the pow decryption method
plaintext = int2string(decrypted) # decrypted message converted and pass into plaintext
print (plaintext) # decrypted message converted and pass into plaintext
