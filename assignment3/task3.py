from Crypto.Util.number import getPrime, inverse

def generate_key(bits):
    e = 65537
    p = getPrime(bits)
    q = getPrime(bits)

    n = p * q
    z = (p - 1) * (q - 1)

    #d = e - 1 % (z)
    d = inverse(e, z)

    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key
    
    
def encrypt(message, public_key):
    message = message.encode('utf-8')
    int_message = int.from_bytes(message, byteorder='big')
    encrypted = pow(int_message, public_key[1], public_key[0])
    return encrypted

def decrypt(encrypted_message, private_key):
    decrypted = pow(encrypted_message, private_key[1], private_key[0])
    decrypted = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder='big')
    try:
        decrypted = decrypted.decode('utf-8')
    except UnicodeDecodeError:
        decrypted = str(decrypted)
    return decrypted

def main():
    # public_key[0] = n, public_key[1] = e, private_key[0] = n, private_key[1] = d
    public_key, private_key = generate_key(256)
    message = 'Hi!'
    print('Original message:', message)
    encrypted_message = encrypt(message, public_key)
        
    decrypted_message = decrypt(encrypted_message, private_key)
    print('Decrypted message:', decrypted_message)
    
    # mallory intercepts the message and modifies it c' = F(c)
    k = 2

    # c = m^3 mod n where m is original message
    
    # k^e mod n - encrypt k 
    k_encrypted = pow(k, public_key[1], public_key[0])
    
    #modified ciphertext
    c_prime = (encrypted_message * k_encrypted) % public_key[0]
    
    print('Mallory intercepts the message and modifies it: ', c_prime)
    
    #decrypt modified message - when decrypted, it will be m * k
    # modified_decrypted_message = decrypt(c_prime, private_key)
    pow(c_prime, private_key[1], private_key[0])
    modified_decrypted_message = int.from_bytes(modified_decrypted_message.encode('utf-8'), byteorder='big') // k
    modified_decrypted_message = modified_decrypted_message.to_bytes((modified_decrypted_message.bit_length() + 7) // 8, byteorder='big')

    print('Decrypted modified message:', modified_decrypted_message)

    # k_encrypted = pow(k, public_key[1], public_key[0])
    # c_prime = (encrypted_message * k_encrypted) % public_key[0]
    # print('Mallory intercepts the message and modifies it: ', c_prime)
    # modified_decrypted_message = decrypt(c_prime, public_key)
    # print('Decrypted modified message:', modified_decrypted_message)
        
    
if __name__ == "__main__":
    main()