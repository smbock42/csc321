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
            return random_str, hashed, attempts
        else:
            hash_values.add(hashed)
    

# give me two strings (of any length) whose Hamming distance is exacty 1 bit.

def task_1_b():
    string1 = "a"
    string2 = "b"
    for _ in range(3):
        print(string1)
        print(hash(string1.encode(), 256))
        print(string2)
        print(hash(string2.encode(), 256))
        string1 = chr(ord(string1) + 2)
        string2 = chr(ord(string2) + 2)


def task_1_c():
    # create a collision for SHA256

    # start with 8 - 16 bits
    with open("bit_collision.txt", "w") as f:
        for bits in range(8, 51, 2):
            start_time = time.time()
            original_str, hashed, attempts = find_collision(bits)
            end_time = time.time()
            f.write(f"{bits} {end_time - start_time} {attempts}\n")
            print(f"Bits: {bits}")
            print(f'Original: {original_str}')
            print(f'Hash: {hashed}')
        
def create_graphs():
    # Initialize lists to store the data
    digest_sizes = []
    times = []
    num_inputs = []

    # Read the data from the file
    with open("bit_collision.txt", "r") as f:
        for line in f:
            bits, time_taken, attempts = map(float, line.split())
            digest_sizes.append(bits)
            times.append(time_taken)
            num_inputs.append(attempts)
    

    # Create the first graph (digest size vs collision time)
    plt.figure(figsize=(10, 5))
    plt.plot(digest_sizes, times, marker='o')
    plt.title('Digest Size vs Collision Time')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Collision Time (seconds)')
    plt.grid(True)
    plt.show()
    # save the graph

    # Create the second graph (digest size vs number of inputs)
    plt.figure(figsize=(10, 5))
    plt.plot(digest_sizes, num_inputs, marker='o')
    plt.title('Digest Size vs Number of Inputs')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Number of Inputs')
    plt.grid(True)
    plt.show()
    # save the graph


if __name__ == "__main__":
    task_1_b()
    #task_1_c()
    #create_graphs() 