from Crypto.Hash import SHA256 
import random
import string
import matplotlib.pyplot as plt
import time

def hash(data, truncate_bits: int):
    h = SHA256.new()
    h.update(data)
    truncate_bytes = (truncate_bits + 7) // 8  # Round up to nearest byte
    truncated_digest = h.digest()[:truncate_bytes]
    
    # Further truncate to the exact number of bits
    excess_bits = truncate_bytes * 8 - truncate_bits
    if excess_bits > 0:
        truncated_digest = bytearray(truncated_digest)
        truncated_digest[-1] &= 0xFF << excess_bits  # Zero out the excess bits
        truncated_digest = bytes(truncated_digest)
    #print(truncated_digest)
    return truncated_digest
    
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def find_collision(bits: int):
    hash_values = set()
    attempts = 0
    while True:
        random_str = generate_random_string(64)
        hashed = hash(random_str.encode(), bits)
        attempts += 1
        if hashed in hash_values:
            return random_str, hash_values[hashed], hashed, attempts
        else:
            hash_values.add(hashed)
    

# give me two strings (of any length) whose Hamming distance is exacty 1 bit.

def task_1_b():
    string1 = "a"
    string2 = "b"
    for i in range(3):
        print(string1)
        hash(string1.encode(), False)
        print(string2)
        hash(string2.encode(), False)
        string1 = chr(ord(string1) + 2)
        string2 = chr(ord(string2) + 2)


def task_1_c():
    # create a collision for SHA256

    # start with 8 - 16 bits
    with open("bit_collision.txt", "w") as f:
        for bits in range(8, 51, 2):
            start_time = time.time()
            original_str, collision_str, hashed, attempts = find_collision(bits)
            end_time = time.time()
            f.write(f"{bits} {end_time - start_time} {attempts}\n")
            print(f"Bits: {bits}")
            print(f'Original: {original_str}')
            print(f'Collision: {collision_str}')
            print(f'Hash: {hashed}')
        

if __name__ == "__main__":
    #task_1_b()
    task_1_c()