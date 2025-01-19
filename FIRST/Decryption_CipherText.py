from collections import Counter

# Define allowed characters (both uppercase and lowercase)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
]

# Read the ciphertext from a file
def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Write the decrypted text to a file
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Calculate the frequency of characters in the ciphertext
def calculate_frequency(ciphertext):
    return Counter(char for char in ciphertext if char in letters)

# Create mappings for both lowercase and uppercase letters based on frequency
def create_mapping(cipher_freq):
    sorted_cipher_freq = ''.join([item[0] for item in cipher_freq.most_common()])
    english_letter_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    # Debugging: Print the character frequencies
    print("Ciphertext Frequencies:", cipher_freq)

    # Mapping for lowercase
    lowercase_mapping = dict(zip(sorted_cipher_freq.lower(), english_letter_freq.lower()))
    # Mapping for uppercase
    uppercase_mapping = dict(zip(sorted_cipher_freq.upper(), english_letter_freq.upper()))
    
    # Debugging: Print the mappings
    print("Lowercase Mapping:", lowercase_mapping)
    print("Uppercase Mapping:", uppercase_mapping)
    
    # Combine both mappings
    return lowercase_mapping, uppercase_mapping

# Decrypt the ciphertext using the frequency-based mappings
def decrypt_with_frequency(ciphertext, lowercase_mapping, uppercase_mapping):
    decrypted_text = ''
    
    for char in ciphertext:
        if char.islower():
            decrypted_text += lowercase_mapping.get(char, char)
        elif char.isupper():
            decrypted_text += uppercase_mapping.get(char, char)
        else:
            decrypted_text += char  # Special characters and spaces remain unchanged

    return decrypted_text

# Main function to process the ciphertext and output the plaintext
def main(file_path, output_file):
    ciphertext = read_text(file_path)
    
    cipher_freq = calculate_frequency(ciphertext)
    lowercase_mapping, uppercase_mapping = create_mapping(cipher_freq)
    
    decrypted_text = decrypt_with_frequency(ciphertext, lowercase_mapping, uppercase_mapping)
    
    # Debugging: Print the final decrypted text
    print("Decrypted Text:", decrypted_text)
    
    write_to_file(output_file, decrypted_text)

# Example usage
file_path = 'ciphertext_test_46.txt'  # Path to your ciphertext file
output_file = 'S_PlainText.txt'  # Output file for decrypted text
main(file_path, output_file)
