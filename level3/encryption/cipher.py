def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    filename = input("Enter filename to read: ").strip()
    shift = int(input("Enter shift key (number): ").strip())

    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found!")
        return

    if choice == "e":
        result = encrypt(content, shift)
        output_file = "encrypted_" + filename
    elif choice == "d":
        result = decrypt(content, shift)
        output_file = "decrypted_" + filename
    else:
        print("Invalid choice")
        return

    with open(output_file, "w") as f:
        f.write(result)
    print(f"Done! Saved to {output_file}")

if __name__ == "__main__":
    main()