"""
This code attempts to get the miss decryption ket.d
"""
import binascii #import library
from Crypto.PublicKey import RSA

def string2int(my_str): # method to convert String to integer
    return int(binascii.hexlify(my_str), 16) #return converted String

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8") #returning binary ascii code passing in an integer

# From wekipeadis search i found modular multiplicative inverse  on the following site (https://en.wikipedia.org/wiki/RSA_(cryptosystem) )
# Using the mudolar multicative invese, i search on http://www.rosettacode.org/wiki/Modular_inverse#Python
# THen i got the function below

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

e = 65537
p = 163598797232837275790583032413921422452851861145478369331976309880028992955089558380171554447759405365296693377570783300198791468861355639873166150884714034914366548252757855530548966926710596087588892893653952147784119788340592861717511574050564549916735627066568966135368285851889401719649796310308064172229
q = 151928351783926490385254692544226090032004315756120674902384041799040568083955129227360764179393042678005292005933989750269377019057534023167675372696224003953154715102625798599561576746593076228704448522848509650863715575134525964992439285085243915010868628145127710442853766119688772555932018349278733467937
n = p*q
d = modinv(e,( q-1)*(p-1))

#given cipher in key2
ciphertext = 4413233431418367729487001191499320110908628864393005850336194538378846901872012263024060279733910394528568658924541767014298273106072428208428621362441660742168169457839232452898840402021800460905562638079257404470183053387353849960252811956727755974787563684430128654542847575219444418360279725423441999278619584162289488016498634231451443666882615379215688913514242136494373656647328276909398980200846880640231426382657437148137610018777974884800967755913109702229247523206388812041488414941125272083962209616158810973532091497979384180936871075352614021504627549173686729322478688708849605857667792183339692021980

#using wikipeadia
decrypted = pow(ciphertext, d, n)  # decrypting using the pow decryption method
plaintext = int2string(decrypted) # decrypting using the pow decryption method
print (plaintext) # decrypted message converted and pass into plaintext
