from PIL import Image
n=0

# Function to encode text into image
def encode_text(input_image_path, output_image_path, secret_text):
    # Open the input image
    image = Image.open(input_image_path)
    encoded = image.copy()
    width, height = image.size
    
    # Convert text to binary
    binary_secret = ''.join(format(ord(char), '08b') for char in secret_text)
    binary_secret += '1111111111111110'  # Delimiter to mark end of text
    
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_secret):
                pixel = list(image.getpixel((x, y)))
                for n in range(3):  # For R, G, B
                    if data_index < len(binary_secret):
                        pixel[n] = pixel[n] & ~1 | int(binary_secret[data_index])
                        data_index += 1
                encoded.putpixel((x, y), tuple(pixel))
    
    encoded.save(output_image_path)
    print(f"✅ Text encoded into {output_image_path}")

# Function to decode hidden text from image
def decode_text(encoded_image_path):
    image = Image.open(encoded_image_path)
    binary_data = ""
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):
                binary_data += str(pixel[n] & 1)
    
    # Split binary data into bytes
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    
    decoded_text = ""
    for byte in all_bytes:
        decoded_text += chr(int(byte, 2))
        if decoded_text.endswith("þ"):  # End marker
            return decoded_text[:-1]
    return decoded_text

def choice():
    print("Choose one\n")
    print("1. To encode the file\n ")
    print("2. To decode the file\n")
    print("EXIT")
    n=int(input("Enter choice: "))
    return n

n=choice()
while n==1:
    img_path=input("Enter the image path: ")
    msg=input("Enter your message: " )
    output_name=input("Enter the output name: ")
    encode_text(img_path,output_name,msg)
    n=choice()

while n==2:
    img_path=input("Enter the image path: ")
    msg=decode_text(img_path)
    print("Decoded message: ",msg)
    n=choice()
