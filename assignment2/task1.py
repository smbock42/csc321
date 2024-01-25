from Crypto.Hash import SHA256 


def hash(data, truncate: bool):
    h = SHA256.new()
    h.update(data)
    if truncate: 
    # truncate digest to only 8 bits
        truncated_digest = h.digest()[:1]
        print(truncated_digest)
        return truncated_digest
    else:
        print(h.hexdigest())
        return h.hexdigest()


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
    hash(string1.encode())
    print(string2)
    hash(string2.encode())
    
if __name__ == "__main__":
    #task_1_b()
    task_1_c