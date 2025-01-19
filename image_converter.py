from PIL import Image
from io import BytesIO
import os
import requests

def convert_image_to_png(image_path, output_filename):
    try:
        # Check if the input is a URL or local file
        if image_path.startswith(('http://', 'https://')):
            # Handle web image
            response = requests.get(image_path)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
        else:
            # Handle local image
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file not found: {image_path}")
            image = Image.open(image_path)
        
        # Convert and save as PNG
        output_path = f"{output_filename}.png"
        image.save(output_path, "PNG")
        
        print(f"Image successfully converted and saved as {output_path}")
        return True
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")
        return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Example with local image - replace with your image path
    local_image = "AWS-certificate-2022.webp"  # Update this path
    output_name = "AWS-certificate-2022"
    
    convert_image_to_png(local_image, output_name) 