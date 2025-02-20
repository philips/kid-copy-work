from PIL import Image
import os

def crop_and_whiten_png(input_path, output_path):
    """
    Crops a PNG image, then replaces the alpha layer with white.

    Args:
        input_path (str): Path to the input PNG file.
        output_path (str): Path to save the modified PNG file.
    """
    try:
        img = Image.open(input_path).convert("RGBA")
        bbox = img.getbbox()

        if bbox:
            cropped_img = img.crop(bbox)
            new_img = Image.new("RGB", cropped_img.size, "white") #Create a white image
            new_img.paste(cropped_img, mask=cropped_img.split()[3]) #paste the cropped image using the alpha layer as a mask.
            new_img.save(output_path, "PNG")
            print(f"Cropped, whitened, and saved: {output_path}")
        else:
            print(f"Image {input_path} is fully transparent, skipping.")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def batch_crop_and_whiten(input_folder, output_folder):
    """
    Processes all PNG files in a folder, cropping and whitening them.

    Args:
        input_folder (str): Path to the input folder containing PNG files.
        output_folder (str): Path to the output folder to save modified PNG files.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}")
            crop_and_whiten_png(input_path, output_path)

if __name__ == "__main__":
    input_folder = "in"
    output_folder = "out"

    batch_crop_and_whiten(input_folder, output_folder)
    print("Batch cropping and whitening completed.")
