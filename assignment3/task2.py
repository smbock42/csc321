import random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad





def generate_private_key(q):
    return random.randint(1, q-1)

def generate_public_key(a, private_key, q):
    # pow(x, y, z) = x^y % z
    return pow(a, private_key, q)

def generate_shared_secret(public_key, private_key, q):
    return pow(public_key, private_key, q)

def hash(data):
    h = SHA256.new()
    h.update(data)
    return h.digest()[:16]

def aes_cbc_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    iv = cipher.iv
    return iv + ct_bytes

def aes_cbc_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    ct = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()


def main():
    q = 37 # prime number
    a = 1 # mallory tampers with generator
    
    alicePriv = generate_private_key(q)
    alicePub = generate_public_key(a, alicePriv, q)
    
    bobPriv = generate_private_key(q)
    bobPub = generate_public_key(a, bobPriv, q)
    
    # mallorie modifies the keys to be q instead and results in 
    # the secret key beign the same. 

    aliceShared = generate_shared_secret(bobPub, alicePriv, q)
    bobShared = generate_shared_secret(alicePub, bobPriv, q)
    
    print("aliceShared: ", aliceShared)
    print("bobShared: ", bobShared)
    
    print(aliceShared == bobShared)
    

    aliceKey = hash(str(aliceShared).encode())
    bobKey = hash(str(bobShared).encode())
    
    aliceMessage = "Hi Bob!"
    bobMessage = "Hi Alice!"
    
    aliceEncrypt = aes_cbc_encrypt(aliceKey, aliceMessage)
    bobEncrypt = aes_cbc_encrypt(bobKey, bobMessage)

    bobDecrypted = aes_cbc_decrypt(bobKey, aliceEncrypt)
    aliceDecrypted = aes_cbc_decrypt(aliceKey, bobEncrypt)
    
    print(bobDecrypted)
    print(aliceDecrypted)
    
    # ...

    malloryShared = a  # Mallory computes the shared secret
    malloryKey = hash(str(malloryShared).encode())  # Mallory generates the key

    malloryDecryptAlice = aes_cbc_decrypt(malloryKey, aliceEncrypt)  # Mallory decrypts Alice's message
    print(malloryDecryptAlice)

    malloryDecryptBob = aes_cbc_decrypt(malloryKey, bobEncrypt)  # Mallory decrypts Bob's message
    print(malloryDecryptBob)

    # ...
    
    
    
    
if __name__ == "__main__":
    main()