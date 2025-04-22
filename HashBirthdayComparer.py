# Code created by Aadil Syed
# Code modified by GitHub Copilot for Education
# Date: 2025-03-28 (28th March 2025)
# Description: This code generates a real and fake confession file and calculates the
# SHA256 hash of the files. The fake confession file is modified by adding spaces until the hash matches the 
# real confession file. The last 3 digits of the real and fake confession hashes are printed.
# Python version used: Python for Windows (64-bit) version 13.12.8

import time, hashlib

start_time = time.time()
# Create real confession file
with open('AliceForPresident.pdf', 'w') as f:
    f.write("My zid is z5263769,\n\nI believe that Alice will become President - and I'm pretty good at predicting things.")

# Create fake confession file
with open('BobForPresident.pdf', 'w') as f:
    f.write("My zid is z5263769,\n\nI believe that Bob will become President - and I'm pretty good at predicting things.")

# Calculate the SHA256 hash of the confession files.
def get_sha256_last_digits(file_path,num_digits):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    sha256_hash = hashlib.sha256(file_data).hexdigest()
    return sha256_hash[-num_digits:]

def modify_file_to_match_hash(real_file, fake_file, num_digits):
    real_hash = get_sha256_last_digits(real_file, num_digits)

# Keep adding spaces to the fake confession file until the hash matches the real confession file
    while True:
        with open(fake_file, 'a') as f:
            f.write(' ')
        
        fake_hash = get_sha256_last_digits(fake_file, num_digits)
        
        if real_hash == fake_hash:
            break

# Modify the fake confession file to match the hash of the real confession file
modify_file_to_match_hash('real_confession.txt', 'fake_confession.txt', 2)

real_hash = get_sha256_last_digits('real_confession.txt', 2)
fake_hash = get_sha256_last_digits('fake_confession.txt', 2)

# Print the last 3 digits of the real and fake confession hashes
print(f"Real confession hash (last 2 digits): {real_hash}")
print(f"Fake confession hash (last 2 digits): {fake_hash}")

# Calculate the time taken to run the script
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time elapsed: {elapsed_time} seconds")