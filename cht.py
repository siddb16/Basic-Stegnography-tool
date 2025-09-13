from PIL import Image

# Function to encode message into image
def encode_image(img_path, message, output_path):
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Add a delimiter to indicate end of message
    message += "%%END%%"
    binary_message = ''.join([format(ord(char), "08b") for char in message])

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                b = img.getpixel((col, row))
                # Replace LSB of blue channel with message bit
                b = (b & ~1) | int(binary_message[index])
                encoded.putpixel((col, row), (r, g, b))
                index += 1

    encoded.save("/home/kali/Desktop/Basic-Stegnography-tool")
    print("✅ Message encoded successfully in", output_path)


# Function to decode message from image
def decode_image(img_path):
    img = Image.open(img_path)
    width, height = img.size
    binary_data = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(b & 1)

    # Split binary into characters
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_message = ""
    for char in chars:
        decoded_message += chr(int(char, 2))
        if decoded_message.endswith("%%END%%"):
            return decoded_message[:-7]

    return "⚠️ No hidden message found!"


# Example usage
if __name__ == "__main__":
    # Encode message
    encode_image("cute.png", "Hello Siddhant, this is secret!", "encoded.png")

    # Decode message
    secret = decode_image("encoded.png")
    print("🔎 Decoded Message:", secret)
