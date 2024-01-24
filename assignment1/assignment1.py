from Crypto.Cipher import AES

from helpers import pad, unpad, generate_key, ecb_encrypt, cbc_encrypt


# --------TASK 1-------
def task1(key, iv):
    input_file = input("Enter the name of the file to encrypt: ")
    ecb_output_file = 'encrypted_ecb_' + input_file
    cbc_output_file = 'encrytped_cbc_' + input_file

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

# --------TASK 2-------
def task2(key, iv):
    user_input = "1111111admin1true1"
    encrypted_data = submit(user_input, key, iv)
    is_admin = verify(encrypted_data, key, iv)
    print(f"Before modification - Is admin: {is_admin}")
    
    modified_data = modify(encrypted_data)
    is_admin = verify(modified_data, key, iv)
    print(f"After modification - Is admin: {is_admin}")
    return is_admin
    
# --------TASK 2 Submit function-------    
def submit(user_input, key , iv):
    # sanitize user input for ; and = 
    user_input = user_input.replace("=", "")
    user_input = user_input.replace(";", "")
    
    data = "userid=456;userdata=" + user_input + ";session-id=31337"
    # url encode data's = and ;
    data = data.replace("=", "%3D")
    data = data.replace(";", "%3B")
    data = data.encode("utf-8")
    
    
    # pad string to be divisible by 16
    data = pad(data)
    # encrypt data
    data = cbc_encrypt(data, key, iv)
    return data
    
def verify(data, key, iv):
    # decrypt data (can use AES-CBC decrypt library)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(data)
    # unpad plaintext
    plaintext = unpad(plaintext)
    # convert url encoded plaintext to string
    plaintext = plaintext.decode("utf-8",errors="ignore")
    plaintext = plaintext.replace("%3D", "=")
    plaintext = plaintext.replace("%3B", ";")
    # check if ;admin=true; is in plaintext
    return ';admin=true;' in plaintext

def modify(data):

    data = bytearray(data)
    

    data[16] = data[16] ^ ord("1") ^ ord(';') 
    data[22] = data[22] ^ ord("1") ^ ord('=') 
    data[27] = data[27] ^ ord("1") ^ ord(';') 
    
        
    data = bytes(data)

    return data


    

def main():
    # generate key and iv once
    key = generate_key(AES.block_size)
    iv = generate_key(AES.block_size)
    #task1(key, iv)
    task2(key, iv)



if __name__ == "__main__":
    main()