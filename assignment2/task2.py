import bcrypt
import time
import nltk
from nltk.corpus import words
from multiprocessing import Pool, cpu_count

def parse_file(file_name):
    users = []
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            user, hash = line.split(":")
            algorithm, workfactor, salt_hash = hash[1:].split("$")
            salt, hash_value = salt_hash[:22], salt_hash[22:]
            users.append((user, algorithm, int(workfactor), salt, hash_value))
    return users

def chunkify(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def crack_password(data):
    word_chunk, user_info = data
    user, algorithm, workfactor, salt, hash_value = user_info
    #print(user)
    for word in word_chunk:
        full_hash = "$" + algorithm + "$" + str(workfactor).zfill(2) + "$" + salt + hash_value
        hashed = bcrypt.hashpw(word.encode(), full_hash.encode())
        if hashed.decode() == full_hash:
            return word


def crack_passwords(users):
    nltk.download('words')
    word_list = [word for word in words.words() if len(word) >= 6 and len(word) <= 10]
    chunks = list(chunkify(word_list, len(word_list) // cpu_count()))
    pool = Pool(processes=cpu_count())
    f = open("passwords.txt", "w")
    
    for user in users:
        print(f"Finding {user[0]}'s password")
        start_time = time.time()
        
        for password in pool.imap_unordered(crack_password, [(chunk, user) for chunk in chunks]):
            if password is not None:
                end_time = time.time()
                print(f"User: {user[0]}")
                print(f"Password: {password}")
                print(f"Time taken: {end_time - start_time}")
                print()
                f.write(f"User: {user[0]} | Password: {password} | Time taken: {end_time - start_time}\n" )
                break
    pool.terminate()
    f.close()

# def crack_passwords(users):
#     nltk.download('words')
#     word_list = [word for word in words.words() if len(word) >= 6 and len(word) <= 10]
#     for user, algorithm, workfactor, salt, hash_value in users:
#         print(f"Finding {user}'s password")
#         start_time = time.time()
#         for word in word_list:
#             hashed = bcrypt.hashpw(word.encode(), ("$" + algorithm + "$" + str(workfactor) + "$" + salt).encode())

#             hash_value = "$" + algorithm + "$" + str(workfactor).zfill(2) + "$" + salt + hash_value
#             if hashed.decode() == hash_value:
#                 end_time = time.time()
#                 print(f"User: {user}")
#                 print(f"Algorithm: {algorithm}")
#                 print(f"Workfactor: {workfactor}")
#                 print(f"Salt: {salt}")
#                 print(f"Hash: {hash_value}")
#                 print(f"Password: {word}")
#                 print(f"Time taken: {end_time - start_time}")
#                 print()
#                 break
            
            

if __name__ == "__main__":
    users = parse_file("shadow.txt")
    #users= parse_file("shadow.txt")
    crack_passwords(users)