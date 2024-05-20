import subprocess


def remove_metadata(file_path):
    try:
        result = subprocess.run(['exiftool', '-all=', file_path], capture_output=True, text=True)
        print(f"Metadata removed from {file_path}.")
    except FileNotFoundError:
        print("exiftool is not installed or not found in the system path.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'path/to/file'
remove_metadata(file_path)
