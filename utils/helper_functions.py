import os

def read_template(file_path: str) -> str:
    """
    Reads the content of a template file and returns it as a string.
    If the file does not exist, returns an empty string.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    return ""

def save_to_file(file_path: str, content: str):
    """
    Saves the provided content to a file at the specified file path.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
