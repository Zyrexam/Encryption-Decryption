from collections import Counter


letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
]



def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def frequency_analysis(ciphertext):
    return Counter(ciphertext)


def decrypt(ciphertext, mapping):
    return ''.join(mapping.get(char, char) for char in ciphertext)


file_path = 'ciphertext_test_46.txt'  
ciphertext = read_text(file_path)


frequency = frequency_analysis(ciphertext)
print("Frequency analysis:", frequency)

