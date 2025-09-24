import cv2
import os
import numpy as np
import argparse
import glob

def process_image(image_path, output_folder, scale_percent):
    """
    Reads a single image, detects red objects, counts them, draws contours,
    and saves the result to the output folder.
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Warning: Could not read image {image_path}. Skipping.")
            return

        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        hsv_img = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
        
        lower1 = np.array([0, 100, 20])
        upper1 = np.array([10, 255, 255])
        
        lower2 = np.array([160, 100, 20])
        upper2 = np.array([179, 255, 255])
        
        lower_mask = cv2.inRange(hsv_img, lower1, upper1)
        upper_mask = cv2.inRange(hsv_img, lower2, upper2)
        full_mask = lower_mask + upper_mask
        
        result_img = cv2.bitwise_and(resized, resized, mask=full_mask)

        contours, _ = cv2.findContours(full_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            cv2.drawContours(result_img, [contour], -1, (36, 255, 12), 1)

        cell_count = len(contours) 
        text = f"Detected Cells: {cell_count}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        position = (10, 30) 
        font_scale = 0.7
        font_color = (255, 255, 255) 
        thickness = 1

        cv2.putText(result_img, text, position, font, font_scale, font_color, thickness) 

        filename = os.path.basename(image_path)
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, result_img)
        
        print(f"Processed: {filename} - Found {cell_count} cells.") 

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Detect red blood cells in images using OpenCV.")
    parser.add_argument("-i", "--input_folder", help="Folder containing input images.", required=True)
    parser.add_argument("-o", "--output_folder", help="Folder to save processed images.", required=True)
    parser.add_argument("-s", "--scale", help="Scale percent for resizing (default: 80).", type=int, default=80)
    
    args = parser.parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    image_files = glob.glob(os.path.join(args.input_folder, "*.jpg"))
    image_files.extend(glob.glob(os.path.join(args.input_folder, "*.png")))

    if not image_files:
        print(f"No .jpg or .png images found in '{args.input_folder}'.")
        return

    print(f"Found {len(image_files)} images to process.")

    for image_path in image_files:
        process_image(image_path, args.output_folder, args.scale)
    
    print("\nProcessing complete!")

if __name__ == "__main__":
    main()

    