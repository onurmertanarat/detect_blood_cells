# OpenCV Color Segmentation for Blood Cells

This project is a demonstration of fundamental computer vision techniques using OpenCV. It identifies red-colored objects in an image, presumed to be Red Blood Cells (RBCs), by applying a color mask in the HSV color space and then finding and counting the resulting contours.

<p>
  <img src="https://github.com/onurmertanarat/detect_blood_cells/blob/master/processed_images/blood1.jpg" alt="Application Screenshot">
</p>

**Important Disclaimer:** This is an educational script to showcase a basic CV pipeline. It is **not a medically accurate cell counter.** The counting method has significant limitations, which are detailed below.

---

## Features

* **Color-Based Segmentation:** Utilizes the HSV color space to accurately isolate red-colored pixels, correctly handling the hue wrap-around for the color red.
* **Contour Detection:** Finds and draws outlines around all detected red objects in the image.
* **Basic Object Counting:** Provides a simple count of the total number of contours (object groups) found.
* **Image Output:** Saves the processed images with the detected contours and the object count drawn directly onto them.

---

## Limitations

As this project uses a simple, color-based approach, its accuracy is limited. The main limitations are:

* **Overlapping Objects:** Treats multiple touching or overlapping cells as a single object, leading to a significantly inaccurate count.
* **Color Reliability:** Detection is highly dependent on image lighting, staining techniques, and the hardcoded color range. It may miss cells with slightly different color tones.
* **Object Specificity:** It only detects red objects and cannot identify or distinguish other cell types like White Blood Cells (WBCs) or Platelets.

---

## Technology Stack

* Python 3
* OpenCV-Python
* NumPy

---

## Setup and Usage

### Prerequisites

* Python 3.6+
* pip

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/onurmertanarat/detect_blood_cells.git](https://github.com/onurmertanarat/detect_blood_cells.git)
    cd detect_blood_cells
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # Create the environment
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Tool

To process images, run the script from the terminal with the following arguments:

```sh
python main.py --input_folder <path_to_input_folder> --output_folder <path_to_output_folder>
```

---

## Contact

Onur Mert Anarat

[linkedin.com/in/onurmertanarat](https://www.linkedin.com/in/onurmertanarat)
