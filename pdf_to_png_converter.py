from pdf2image import convert_from_path
import os

def convert_pdf_to_png(pdf_path, output_dir=None, dpi=200):
    """
    Convert a PDF file to PNG images.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Directory to save the PNG files (default: same as PDF)
        dpi (int): DPI resolution for the output images (default: 200)
    
    Returns:
        list: List of paths to the generated PNG files
    """
    # Validate PDF path
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.dirname(pdf_path)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get PDF file name without extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Convert PDF to images
    try:
        images = convert_from_path(pdf_path, dpi=dpi)
    except Exception as e:
        raise Exception(f"Error converting PDF: {str(e)}")
    
    # Save images as PNG files
    png_paths = []
    for i, image in enumerate(images):
        # Generate output path for each page
        output_path = os.path.join(output_dir, f"{pdf_name}_page_{i+1}.png")
        
        # Save the image
        image.save(output_path, "PNG")
        png_paths.append(output_path)
        
    return png_paths

def main():
    # Example usage
    try:
        pdf_path = input("Enter the path to your PDF file: ")
        output_dir = input("Enter output directory (press Enter for same as PDF location): ").strip()
        dpi = input("Enter DPI resolution (press Enter for default 200): ").strip()
        
        # Use default values if no input provided
        output_dir = None if not output_dir else output_dir
        dpi = 200 if not dpi else int(dpi)
        
        # Convert PDF to PNG
        png_files = convert_pdf_to_png(pdf_path, output_dir, dpi)
        
        print("\nConversion completed successfully!")
        print("Generated PNG files:")
        for png_file in png_files:
            print(f"- {png_file}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 