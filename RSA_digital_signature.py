import RSA_algorithm as rsa
# import lcd

def create_signature(p,q ,message,e,d):
    print('\tPrime 1: ', p)
    print('\tPrime 2: ', q)

    n = rsa.generate_nkey(p, q)

    print('Public key {e, n}: {%d, %d}' %(e, n))
    print('Private key {d, n}: {%d, %d}' %(d, n))

    message_dec = rsa.str2dec(message)
    print('Plian text : ', message, '\n\t', message_dec)
    print('encrypting ...')
    
    # Encrypt message using the public key
    encrypted = [rsa.endecrypt_message(i, e, n) for i in message_dec]
    chiper_text = 'Signature :' + ''.join(map(lambda x: str(x),encrypted))
    print(chiper_text)

    # chunks, chunk_size = len(chiper_text), 16
    # lcd_list = [ chiper_text[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    # lcd.remove_message()
    # for index in range (len(lcd_list)//2):
    #     lcd.lcd.message = f'{lcd_list[index*2]}\n{lcd_list[index*2+1]}'
    #     lcd.sleep(4)
    # lcd.lcd.message = f'Created         \n\t Signature  .. '
    # lcd.sleep(4)
    # lcd.remove_message()

    print('\t',encrypted)
    return message , encrypted , e

def send_message_with_signature(x,s):
    print( f'Sending Message ..... ')
    # lcd.lcd.message = f'Sending         \n\t Message    .. '
    # lcd.sleep(4)
    # lcd.remove_message()
    return x,s

def verify_message(x, s,e , p ,q ):  
    d = rsa.generate_dkey(e,p, q)
    # Decrypt message using the private key
    decrypted = [rsa.endecrypt_message(i, d, p*q) for i in s]
    print('decrypting signature ...')
    print ('Output text : ', rsa.dec2str(decrypted), '\n\t', decrypted)
    y = rsa.dec2str(decrypted)
    # lcd.lcd.message = f'Verifing        \n\t Message    .. '
    # lcd.sleep(4)
    # lcd.remove_message()
    if x ==y:
        # lcd.lcd.message = f'Valid           \n\t Message    .. '
        # lcd.sleep(4)
        # lcd.remove_message()
        return 'valid message'
    else:
        # lcd.lcd.message = f'Invalid         \n\t Message    .. '
        # lcd.sleep(4)
        # lcd.remove_message()
        return 'invalid message'