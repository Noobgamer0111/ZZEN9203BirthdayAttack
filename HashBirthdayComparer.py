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
with open('', 'w') as f:
    f.write("This is the secret confession of Richard Buckland to be revealed by anonymous email if I should mysteriously vanish. I have left the last few hex digits of the SHA256 hash of this message with my trusted solicitor, Dennis Denuto, which will verify that this is indeed my intended and unaltered confession written by me Richard Buckland. Dennis has not seen this confession he has only seen the last few digits of the hash. I have also sent copies of the last few digits to my bank manager and to my priest Father Brown. On the 10th of February I saw Mark Zukerberg peeping through my window and recording my private and personal conversation with my friend. I confronted him and he was very embarrassed. He promised to pay me $1 million a year if I would stay silent and not tell anyone I had seen him do this. I agreed but now I worry that it would be cheaper for him to make me vanish than to keep paying me.\n")

# Create fake confession file
with open('fake_confession.txt', 'w') as f:
    f.write("This is the secret confession of Richard Buckland to be revealed by anonymous email if I should mysteriously vanish. I have left the last few hex digits of the SHA256 hash of this message with my trusted solicitor, Dennis Denuto, which will verify that this is indeed my intended and unaltered confession written by me Richard Buckland. Dennis has not seen this confession he has only seen the last few digits of the hash. I have also sent copies of the last few digits to my bank manager and to my priest Father Brown. On the 10th of February I saw Mark Zukerberg near my house and we struck up a conversation. He explained all the things he was doing to ensure that Facebook respects privacy - both of its users and of others. It was very impressive. I feel awful that I have been criticising Facebook publicly for so long. I apologised to him in our conversation and now I want to confess to the world that actually Facebook has more than enough privacy features, and that the reasonI spend so much time criticising Facebook is that I am envious of Mark and wish I was a clever and smart and wise as he is. I feel so bad for having been so mean to him for so many years that I am considering retreating to the outback. I may well cut off all contact with the world and live as a hermit from now on. So do not worry if I vanish it is just that I feel so guilty that I have been so unfair to Facebook.\n")

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
modify_file_to_match_hash('real_confession.txt', 'fake_confession.txt', 3)

real_hash = get_sha256_last_digits('real_confession.txt', 3)
fake_hash = get_sha256_last_digits('fake_confession.txt', 3)

# Print the last 3 digits of the real and fake confession hashes
print(f"Real confession hash (last 3 digits): {real_hash}")
print(f"Fake confession hash (last 3 digits): {fake_hash}")

# Calculate the time taken to run the script
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time elapsed: {elapsed_time} seconds")