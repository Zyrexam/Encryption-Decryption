from collections import Counter

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def clean_text(ciphertext):
    return "".join([char.upper() for char in ciphertext if char.isalpha()])

def find_key_length(ciphertext):
    def calculate_ioc(text):
        n = len(text)
        frequencies = Counter(text)
        return sum(freq * (freq - 1) for freq in frequencies.values()) / (n * (n - 1))

    max_key_length = 20 
    iocs = []

    for key_len in range(1, max_key_length + 1):
        chunks = [ciphertext[i::key_len] for i in range(key_len)]
        avg_ioc = sum(calculate_ioc(chunk) for chunk in chunks) / key_len
        iocs.append((key_len, avg_ioc))

    # Find the key length with the highest average IoC
    likely_key_length = max(iocs, key=lambda x: x[1])[0]
    return likely_key_length


def find_key(ciphertext, key_length):
    def most_common_letter(text):
        return Counter(text).most_common(1)[0][0]

    key = []
    for i in range(key_length):
        segment = ciphertext[i::key_length]
        most_common = most_common_letter(segment)
        # Assume 'E' is the most frequent letter in plaintext
        key_char = chr((ord(most_common) - ord('E')) % 26 + ord('A'))
        key.append(key_char)

    return ''.join(key)


def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(char) for char in key]
    ciphertext_as_int = [ord(char) for char in ciphertext]
    
    for i in range(len(ciphertext_as_int)):
        value = (ciphertext_as_int[i] - key_as_int[i % key_length]) % 26
        decrypted_text.append(chr(value + ord('A')))
    
    return ''.join(decrypted_text)

file_path = 'v_ciphertext_46.txt' 
ciphertext = read_text(file_path)
cleaned_ciphertext = clean_text(ciphertext)

# Step 1: Find Key Length
key_length = find_key_length(cleaned_ciphertext)
print(f"Estimated Key Length: {key_length}")

# Step 2: Find Key
key = find_key(cleaned_ciphertext, key_length)
print(f"Found Key: {key}")

# Optional: Write key to a file
write_to_file('found_key.txt', key)

# Step 3: Decrypt Text
decrypted_text = vigenere_decrypt(cleaned_ciphertext, key)
write_to_file('V_plaintext.txt', decrypted_text)
