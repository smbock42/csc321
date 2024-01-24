from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# --------Padding-------
def pad(block):
    # ensure the block sizes are padded to be divisible by 128
    pad_len = AES.block_size - len(block) % AES.block_size
    return block + bytes([pad_len] * pad_len)


def unpad(padded_data):
    pad_len = padded_data[-1]
    return padded_data[:-pad_len]

# -------Generate Random Key-------
def generate_key(size):
    return get_random_bytes(size)

# --------ECB Encryption-------
def ecb_encrypt(plaintext, key):
    # generate AES cipher and start of ciphertext
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""

    padded_text = pad(plaintext)

    # encrypt block by block
    for i in range(0, len(padded_text), AES.block_size):
        block = padded_text[i:i + AES.block_size]
        encrypted_block = cipher.encrypt(block)
        ciphertext += encrypted_block

    return ciphertext

# --------CBC Encryption-------
def cbc_encrypt(plaintext, key, iv):
    ciphertext = b""
    prev_block = iv

    # loop through by blocksize, padding the block
    # create new cipher based on previous block 
    # apply and append to cyber text
    for i in range(0, len(plaintext), AES.block_size):
        block = plaintext[i:i + AES.block_size]
        block  = pad(block)

        cipher = AES.new(key, AES.MODE_ECB)

        xor_res = bytes(x ^ y for x, y in zip(block, prev_block))

        encrypted_block = cipher.encrypt(xor_res)

        ciphertext += encrypted_block
        prev_block = encrypted_block

    return ciphertext

