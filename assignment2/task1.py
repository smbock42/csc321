from Crypto.Hash import SHA256 


def hash(data):
    h = SHA256.new()
    h.update(data)
    print(h.hexdigest())
    return h.hexdigest()

    


# give me two strings (of any length) whose Hamming distance is exacty 1 bit.

def task_1_b():
    string1 = "a"
    string2 = "b"
    for i in range(3):
        print(string1)
        hash(string1.encode())
        print(string2)
        hash(string2.encode())
        string1 = chr(ord(string1) + 2)
        string2 = chr(ord(string2) + 2)


if __name__ == "__main__":
    task_1_b()