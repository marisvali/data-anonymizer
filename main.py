from hash import TextHasher
import os
import shutil

# Create the text hasher object.
hasher = TextHasher()

def hashed_xml_content(content: str) -> str:
    # Get the substring in the xml file that has sensitive data.
    start_token = "<need>"
    end_token = "</need>"
    start_index = content.index(start_token)
    end_index = content.index(end_token)

    # Check if both tokens are found.
    if start_index == -1 or end_index == -1 or start_index >= end_index:
        raise Exception(f'Invalid XML content')

    # Make start_index point to the actual start of the substring.
    start_index += len(start_token)

    # Extract substring and replace it.
    substring = content[start_index:end_index]
    h_content = content[:start_index] + hasher.hashed_text(substring) + content[end_index:]
    return h_content

def hash_folder(source_folder: str, destination_folder: str):
    # Ensure the destination folder exists and is empty.
    if os.path.exists(destination_folder):
        # Remove the folder and all its contents.
        shutil.rmtree(destination_folder)
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)  # Full path of the source file

        # Check if it's a file (not a directory)
        if not os.path.isfile(source_file_path):
            raise Exception(f'Non-file found: {source_file_path}')

        # Read the content of the source file
        with open(source_file_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()

        # Write the content to the destination folder with the same filename
        destination_file_path = os.path.join(destination_folder, filename)
        with open(destination_file_path, 'w', encoding='utf-8') as destination_file:
            file_extension = os.path.splitext(destination_file_path)[1]
            if file_extension == '.xml':
                destination_file.write(hashed_xml_content(content))
            elif file_extension == '.txt':
                destination_file.write(hasher.hashed_text(content))
            else:
                raise Exception(f'File is not .txt or .xml: {source_file_path}')

        print(f'Hashed: {filename}')

hash_folder('input/Data/Items', 'output/Data/Items')