from PIL import Image

image_path = input("Enter the image file path: ")
img = Image.open(image_path)

width, height = img.size

img = img.convert("RGB")

for x in range(width // 4): 
    for y in range(height):
        img.putpixel((x, y), (0, 0, 0)) 

output_path = "modified_image.png"
img.save(output_path)
print(f"Modified image saved as {output_path}")
