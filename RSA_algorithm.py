import random
import math
# import lcd

# Converts a string to a list of decimal numbers
def str2dec(st):
    dec_list = []
    for i in st:
        dec_list.append(ord(i))
    return dec_list

# Converts a list of decimal numbers to string
def dec2str(dec):
    str_list = []
    for i in dec:
        str_list.append(chr(i))
    return ''.join(str_list)

def generate_prime(beg, end):
    beg_rand = random.randint(beg, end)
    if beg_rand % 2 == 0:
        beg_rand += 1

    for possiblePrime in range(beg_rand, end, 2):

        # Assume number is prime until shown it is not.

        isPrime = True
        for num in range(3, math.floor(possiblePrime/2), 2):

            if possiblePrime % num == 0:
                isPrime = False

        if isPrime:

            return possiblePrime

# This value is the multiplication of the two prime numbers,
# because the prime numbers are large this value is difficult to factorize
def generate_nkey(p, q):
    return p * q

# This 'e' key with 'n' is considered the public key
def generate_ekey(p, q):
    phi = (p-1) * (q-1)

    for e in range(random.randrange(3, phi-1, 2), phi-1):
        if math.gcd(e, phi) == 1:
            return e

# This 'd' key with 'n' is considered the private key
def generate_dkey(e,p, q):
    phi = (p-1) * (q-1)

    d = int(phi / e)
    while (True):

        if (d * e) % phi == 1:

            return d
        d += 1

def endecrypt_message(m, key, n):
    dec = (m ** key) % n
    return dec

def main (p,q ,message) :
    print('\tPrime 1: ', p)
    print('\tPrime 2: ', q)

    n = generate_nkey(p, q)
    e = generate_ekey(p, q)
    d = generate_dkey(e,p, q)

    print('Public key {e, n}: {%d, %d}' %(e, n))
    print('Private key {d, n}: {%d, %d}' %(d, n))

    message_dec = str2dec(message)
    print('Plian text : ', message, '\n\t', message_dec)
    print('encrypting ...')
    
    # Encrypt message using the public key
    encrypted = [endecrypt_message(i, e, n) for i in message_dec]
    chiper_text = 'Chiper text :   ' + ''.join(map(lambda x: str(x),encrypted))
    print(chiper_text)

    # chunks, chunk_size = len(chiper_text), 16
    # lcd_list = [ chiper_text[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    # lcd.remove_message()
    # for index in range (len(lcd_list)//2):
    #     lcd.lcd.message = f'{lcd_list[index*2]}\n{lcd_list[index*2+1]}'
    #     lcd.sleep(4)
    # lcd.lcd.message = f'Completed       \n\t Encryption .. '
    # lcd.remove_message()

    print('\t',encrypted)
    print('decrypting ...')
    
    # Decrypt message using the private key
    decrypted = [endecrypt_message(i, d, n) for i in encrypted]
    result = dec2str(decrypted)
    print ('Plian text : ', dec2str(decrypted), '\n\t', decrypted)
    return result