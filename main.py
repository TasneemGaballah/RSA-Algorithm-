import RSA_algorithm as rsa
import RSA_digital_signature as signature

# range of primes
Rbeg_small= 10
Rend_small=100
Rbeg_large=500
Rend_large=1000

if __name__ == "__main__" :
    print(" \n ###### WELCOME OUR SECURITY SYSTEM ###### ")
    msg = 'Hi'
    
    def security(msg):                                                       # range random number
        p = rsa.generate_prime(Rbeg_small,Rend_small)           #Rbeg_small = 1 Rend_small = 100
        q = rsa.generate_prime(Rbeg_small,Rend_small)
        while (p == q):
            q = rsa.generate_prime(Rbeg_small,Rend_small)
        return rsa.main(p,q,msg)

    def more_security(msg):
        p = rsa.generate_prime(Rbeg_large, Rend_large)         # Rbeg_large = 100 ,Rend_large = 1000
        q = rsa.generate_prime(Rbeg_large, Rend_large)
        while (p == q):
            q = rsa.generate_prime(Rbeg_large, Rend_large)
        return rsa.main(p,q,msg)

    def authenticator(msg):                                                       # range random number
        p = rsa.generate_prime(Rbeg_small,Rend_small)           #Rbeg_small = 1 Rend_small = 100
        q = rsa.generate_prime(Rbeg_small,Rend_small)
        while (p == q):
            q = rsa.generate_prime(Rbeg_small,Rend_small)
        e = rsa.generate_ekey(p, q)
        d = rsa.generate_dkey(e,p, q)
        y = signature.create_signature(p,q,msg,e,d)[1]
        signature.send_message_with_signature(msg,y)
        result = signature.verify_message(msg,y,e,p,q)
        print(result)
        return msg

    def more_authenticator(msg):
        p = rsa.generate_prime(Rbeg_large, Rend_large)         # Rbeg_large = 100 ,Rend_large = 1000
        q = rsa.generate_prime(Rbeg_large, Rend_large)
        while (p == q):
            q = rsa.generate_prime(Rbeg_large, Rend_large)
        e = rsa.generate_ekey(p, q)
        d = rsa.generate_dkey(e,p, q)
        y = signature.create_signature(p,q,msg,e,d)[1]
        signature.send_message_with_signature(msg,y)
        result = signature.verify_message(msg,y,e,p,q)
        print(result)
        return msg
    
    # after_enc = security(msg)
    # print(after_enc)

    while(1):
        cipher = int (input ("\n 1.security \n 2.more_security \n 3.authenticator \n 4.more_authenticator\n 5.Exit \n Enter Type mode : ") )
        # Input message to be encrypted
        m = (input('Enter the value of message m = '))

        if(cipher == 1 ):
                                                                # range random number
            p = rsa.generate_prime(Rbeg_small,Rend_small)           #Rbeg_small = 1 Rend_small = 100
            q = rsa.generate_prime(Rbeg_small,Rend_small)
            while (p == q):
                q = rsa.generate_prime(Rbeg_small,Rend_small)
            rsa.main(p,q,m)

        elif(cipher == 2) :

            p = rsa.generate_prime(Rbeg_large, Rend_large)         # Rbeg_large = 100 ,Rend_large = 1000
            q = rsa.generate_prime(Rbeg_large, Rend_large)
            while (p == q):
                q = rsa.generate_prime(Rbeg_large, Rend_large)

            rsa.main(p,q,m)

        elif(cipher == 3 ):
                                                                # range random number
            p = rsa.generate_prime(Rbeg_small,Rend_small)           #Rbeg_small = 1 Rend_small = 100
            q = rsa.generate_prime(Rbeg_small,Rend_small)
            while (p == q):
                q = rsa.generate_prime(Rbeg_small,Rend_small)
            e = rsa.generate_ekey(p, q)
            d = rsa.generate_dkey(e,p, q)
            y = signature.create_signature(p,q,m,e,d)[1]
            signature.send_message_with_signature(m,y)
            result = signature.verify_message(m,y,e,p,q)
            print(result)

        elif(cipher == 4) :

            p = rsa.generate_prime(Rbeg_large, Rend_large)         # Rbeg_large = 100 ,Rend_large = 1000
            q = rsa.generate_prime(Rbeg_large, Rend_large)
            while (p == q):
                q = rsa.generate_prime(Rbeg_large, Rend_large)
            e = rsa.generate_ekey(p, q)
            d = rsa.generate_dkey(e,p, q)
            y = signature.create_signature(p,q,m,e,d)[1]
            signature.send_message_with_signature(m,y)
            result = signature.verify_message(m,y,e,p,q)
            print(result)

        elif(cipher == 5) :
            exit()
        else:
            print("choose correct choice ")