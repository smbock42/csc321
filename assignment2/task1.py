from Crypto.Hash import SHA256 
import random
import string


def hash(data, truncate: int):
    h = SHA256.new()
    h.update(data)
    if truncate == 8: 
    # truncate digest to only 8 bits
        truncated_digest = h.digest()[:1]
        print(truncated_digest)
        return truncated_digest
    else:
        print(h.hexdigest())
        return h.hexdigest()
    
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def find_collision(bits: int):
    hash_values = {}

    while True:
        random_str = generate_random_string(64)
        hashed = hash(random_str.encode(), bits)

        if hashed in hash_values:
            return random_str, hash_values[hashed], hashed
        else:
            hash_values[hashed] = random_str




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
    string1 = "ab"
    string2 = "ba"
    print(string1)
    #hash(string1.encode(), True)
    print(string2)
    #hash(string2.encode(), True)

    # hash(string1.encode(), True)
    original_str, collision_str, hashed = find_collision(8)
    print(f'Original: {original_str}')
    print(f'Collision: {collision_str}')
    print(f'Hash: {hashed}')


    
if __name__ == "__main__":
    #task_1_b()
    task_1_c()