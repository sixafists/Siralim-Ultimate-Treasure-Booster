import subprocess
import os

# Fixed save file path
# Example : C:\Users\admin\AppData\Local\SiralimUltimate\save\slot1.sav
SAVE_FILE_PATH = r"Save File Path Here"

def run_node_script(input_file, output_file, mode):
    """Run the Node.js script for encryption or decryption."""
    command = [
        "node",
        "encrypt_decrypt.js",
        input_file,
        output_file,
        mode
    ]
    subprocess.run(command, check=True)

def update_realm_props(file_path):
    """
    Locate the line `[RealmProps]` and replace the two lines underneath it with specific values.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        updated_lines = []
        i = 0
        while i < len(lines):
            # Check for `[RealmProps]`
            if lines[i].strip() == "[RealmProps]":
                # Add `[RealmProps]` back
                updated_lines.append(lines[i])
                # Replace the next two lines
                updated_lines.append('Values="5,5,-1,-1,25,4000,"\n')
                updated_lines.append('Properties="5,40,6,60,20,32,"\n')
                # Skip the next two lines
                i += 3
            else:
                updated_lines.append(lines[i])
                i += 1
        
        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        
        print(f"Successfully updated `{file_path}`.")
    
    except FileNotFoundError:
        print(f"Error: File `{file_path}` not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if not os.path.exists(SAVE_FILE_PATH):
        print(f"Save file does not exist at {SAVE_FILE_PATH}!")
        return

    # Paths for intermediate files
    decrypted_file = SAVE_FILE_PATH + ".decoded.txt"
    encrypted_file = SAVE_FILE_PATH

    print("Decrypting the save file...")
    run_node_script(SAVE_FILE_PATH, decrypted_file, "decrypt")

    print("Modifying the save file...")
    update_realm_props(decrypted_file)

    print("Re-encrypting the save file...")
    run_node_script(decrypted_file, encrypted_file, "encrypt")

    print(f"Process complete! Updated file saved back to {encrypted_file}")

if __name__ == "__main__":
    main()
