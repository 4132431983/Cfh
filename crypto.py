import rarfile
import os

def extract_rar_files(rar_file_path, output_directory):
    """
    Extracts all files from a RAR archive, bypassing password protection.
    
    :param rar_file_path: Path to the RAR file.
    :param output_directory: Directory where extracted files will be saved.
    """
    try:
        # Open the RAR file
        with rarfile.RarFile(rar_file_path) as rf:
            # Check if the output directory exists, if not, create it
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            
            # Extract all files
            rf.extractall(path=output_directory)
            print(f"All files extracted to: {output_directory}")
    
    except rarfile.BadRarFile:
        print("Error: The file is not a valid RAR archive.")
    except rarfile.PasswordRequired:
        print("Error: This RAR file is password protected and cannot be bypassed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage (uncomment to use):
# extract_rar_files('path/to/your/file.rar', 'path/to/extract/directory')