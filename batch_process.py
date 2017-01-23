from typewriter import generate_image
import os
import sys


def batch_process(input_folder, output_folder, author):
    # For each file in input_folder, make image in output_folder
    for root, dirnames, filenames in os.walk(input_folder):
            for filename in filenames:
                print(filename)
                input_file = input_folder + filename
                output_file = output_folder + 'typewriter_' + filename + '.gif'
                generate_image(input_file, output_file, author_name=author)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Format: python typewriter.py input_path output_path author")
        sys.exit()

    input_path, output_path = sys.argv[1], sys.argv[2]
    author_name = ""
    if len(sys.argv) == 4:
        author_name = sys.argv[3]

    batch_process(input_path, output_path, author_name)
