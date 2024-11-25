import os
import logging

# Set up logging
logging.basicConfig(filename='braille_conversion.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Braille Converter

# Extended mapping of letters, numbers, and punctuation to Braille
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' ',
    '0': '⠼⠚', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙',
    '5': '⠼⠑', '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊',
    '.': '⠲', ',': '⠂', '?': '⠢', '!': '⠖', "'": '⠄',
    ':': '⠒', ';': '⠔', '-': '⠤', '(': '⠣', ')': '⠜',
}

def text_to_braille(text):
    return ''.join(braille_dict.get(char, '') for char in text.lower())

def convert_file_to_braille(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            text = infile.read()
        
        braille_output = text_to_braille(text)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(braille_output)

        logging.info(f"Braille output written to {output_file}")

    except Exception as e:
        logging.error(f"An error occurred with file {input_file}: {e}")

def convert_directory_to_braille(input_dir, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        text_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
        total_files = len(text_files)

        for index, filename in enumerate(text_files, start=1):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_braille.txt")
            convert_file_to_braille(input_file, output_file)
            print(f"Processed {index}/{total_files}: {filename}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    choice = input("Do you want to convert text directly or text from a file or directory? (file/directory/text): ").strip().lower()
    
    if choice == 'directory':
        input_dir = input("Enter the input directory path: ").strip()
        output_dir = input("Enter the output directory path: ").strip()
        convert_directory_to_braille(input_dir, output_dir)
    elif choice == 'file':
        input_file = input("Enter the input file path: ").strip()
        output_file = input("Enter the output file path: ").strip()
        convert_file_to_braille(input_file, output_file)
    elif choice == 'text':
        input_text = input("Enter text : ")
        output_text = text_to_braille(input_text)
        print(output_text)
    else:
        print("Invalid choice. Please enter 'text' or 'file' or 'directory'.")

