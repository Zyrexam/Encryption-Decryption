from collections import Counter
import re

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def calculate_frequency(text):
    """Calculate frequency of each character in the text."""
    # Only count alphabetic characters and convert to uppercase
    return Counter(c.upper() for c in text if c.isalpha())

def get_frequency_percentage(freq):
    """Convert raw frequencies to percentages."""
    total = sum(freq.values())
    return {char: (count/total)*100 for char, count in freq.items()}

def get_english_frequency():
    """Return approximate frequency distribution of letters in English text."""
    return {
        'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 
        'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
        'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
        'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
        'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
    }

def get_common_english_words():
    """Return a list of common English words to help with pattern matching."""
    return ['THE', 'BE', 'TO', 'OF', 'AND', 'A', 'IN', 'THAT', 'HAVE', 'I', 
            'IT', 'FOR', 'NOT', 'ON', 'WITH', 'HE', 'AS', 'YOU', 'DO', 'AT']

def decrypt_substitution(ciphertext, key_mapping):
    """Decrypt text using the provided substitution mapping."""
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            # Get the mapped character, preserving case
            mapped_char = key_mapping.get(char.upper(), char.upper())
            decrypted += mapped_char if char.isupper() else mapped_char.lower()
        else:
            decrypted += char
    return decrypted

def identify_patterns(text):
    """Identify common patterns in the text that might help with decryption."""
    # Convert to uppercase for pattern matching
    text = text.upper()
    patterns = {}
    
    # Find single-letter words (usually 'A' or 'I')
    single_letters = re.findall(r'\b[A-Z]\b', text)
    if single_letters:
        patterns['single_letters'] = Counter(single_letters)
    
    # Find two-letter words
    two_letters = re.findall(r'\b[A-Z]{2}\b', text)
    if two_letters:
        patterns['two_letters'] = Counter(two_letters)
    
    # Find three-letter words
    three_letters = re.findall(r'\b[A-Z]{3}\b', text)
    if three_letters:
        patterns['three_letters'] = Counter(three_letters)
    
    return patterns

def solve_substitution_cipher(ciphertext_path):
    # Read the ciphertext
    ciphertext = read_text(ciphertext_path)
    
    # Calculate frequency distribution in ciphertext
    cipher_freq = calculate_frequency(ciphertext)
    cipher_freq_percent = get_frequency_percentage(cipher_freq)
    
    # Get English letter frequencies
    english_freq = get_english_frequency()
    
    # Sort both frequency distributions
    sorted_cipher_freq = sorted(
        cipher_freq_percent.items(),
        key=lambda x: x[1],
        reverse=True
    )
    sorted_english_freq = sorted(
        english_freq.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    # Create initial mapping based on frequency analysis
    key_mapping = {}
    for (cipher_char, _), (english_char, _) in zip(sorted_cipher_freq, sorted_english_freq):
        key_mapping[cipher_char] = english_char
    
    # Analyze patterns in the ciphertext
    patterns = identify_patterns(ciphertext)
    
    # Adjust mapping based on common patterns
    # For example, if we find a single letter word, it's likely 'A' or 'I'
    if 'single_letters' in patterns:
        most_common_single = patterns['single_letters'].most_common(1)[0][0]
        if most_common_single in key_mapping:
            key_mapping[most_common_single] = 'I'  # Assume it's 'I' as it's more common as a word
    
    # Decrypt using our mapping
    decrypted_text = decrypt_substitution(ciphertext, key_mapping)
    
    return decrypted_text

if __name__ == "__main__":
    ciphertext_path = 'ciphertext_test_46.txt'
    
    # Perform decryption
    decrypted = solve_substitution_cipher(ciphertext_path)
    
    # Write result to file
    output_file = 'S_PlainText.txt'
    write_to_file(output_file, decrypted)
    
    # Print first few characters to check output
    print("First 100 characters of decrypted text:")
    print(decrypted[:100])