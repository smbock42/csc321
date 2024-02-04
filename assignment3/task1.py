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

    # q = 37
    # a = 5
    q = "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371"
    a = "A4D1CBD5C3FD3412 6765A442 EFB99905 F8104DD2 58AC507F D6406CFF 14266D31 266FEA1E 5C41564B 777E690F 5504F213 160217B4 B01B886A 5E91547F 9E2749F4 D7FBD7D3 B9A92EE1 909D0D22 63F80A76 A6A24C08 7A091F53 1DBF0A01 69B6A28A D662A4D1 8E73AFA3 2D779D59 18D08BC8 858F4DCE F97C2A24 855E6EEB 22B3B2E5"
    # realized I can just do this 
    a = a.replace(" ", "")

    q = int(q, 16)
    a = int(a, 16)

    m0 = "Hi Bob!"
    m1 = "Hi Alice!"

    # generate Alice's keys
    pr_alice = generate_private_key(q)
    pu_alice = generate_public_key(a, pr_alice, q)

    # generate bobs keys
    pr_bob = generate_private_key(q)
    pu_bob = generate_public_key(a, pr_bob, q)

    # compute shared secret for both
    sh_alice = generate_shared_secret(pu_bob, pr_alice, q)
    sh_bob = generate_shared_secret(pu_alice, pr_bob, q)

    # check if they are equal
    print(sh_alice == sh_bob)

    # now hash shared secret for making the AES key 
    k_alice = hash(str(sh_alice).encode())
    k_bob = hash(str(sh_bob).encode())

    # now encrypt the messages 
    c0 = aes_cbc_encrypt(k_alice, m0)
    c1 = aes_cbc_encrypt(k_bob, m1)

    # Bob decrypt alice's message!
    print("Bob sees:", aes_cbc_decrypt(k_bob, c0))

    # Alice decrypt bob's message!
    print("Alice sees:", aes_cbc_decrypt(k_alice, c1))

if __name__ == '__main__':
    main()