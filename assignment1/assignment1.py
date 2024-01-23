from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

def pad(block):
    # ensure the block sizes are padded to be divisible by 128
    pad_len = AES.block_size - len(block) % AES.block_size
    return block + bytes([pad_len] * pad_len)

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

def task1():
    input_file = 'assignment1/cp-logo.bmp'
    ecb_output_file = 'encrypted_ecb.bmp'
    cbc_output_file = 'encrytped_cbc.bmp'
    key = get_random_bytes(AES.block_size)

    # for cbc
    iv = get_random_bytes(AES.block_size)

    with open(input_file, 'rb') as file:
        bmp_header = file.read(54)
        bmp_image_data = file.read()

    ecb_image_data = ecb_encrypt(bmp_image_data, key)
    cbc_image_data = cbc_encrypt(bmp_image_data, key, iv)

    print("Image encrypted.")

    with open(ecb_output_file, 'wb') as file:
        file.write(bmp_header)
        file.write(ecb_image_data)

    with open(cbc_output_file, 'wb') as file:
        file.write(bmp_header)
        file.write(iv)
        file.write(cbc_image_data)

    print("Files written.")

def main():
    task1()

if __name__ == "__main__":
    main()