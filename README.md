<h1>Detect Blood Cells</h1>
<p>This project is an image processing application that detects blood cells using the OpenCV library. Its main function is to identify blood cells in a given image and highlight them within a specified color range.</p>

<h2>Files:</h2>
<ul>
    <li><strong>data:</strong> Contains the image file <code>blood1.jpg</code></li>
    <li><strong>result:</strong> Contains the result files</li>
    <li><strong>main.py:</strong> Python file</li>
</ul>

<!-- How it Works -->
<h2>How it Works:</h2>
<ol>
    <li>The user runs the <code>main.py</code> file and enters the required information:
        <ul>
            <li>Path to the folder containing images (data)</li>
            <li>Path where the results will be saved (result)</li>
            <li>Data item name (e.g., <code>blood</code>)</li>
            <li>Maximum number of items (e.g., 10)</li>
        </ul>
    </li>
    <li>The program retrieves the names of images in the given folder and processes them to detect blood cells based on a specified color range.</li>
    <li>For each image, masking is performed based on the defined color range, and blood cells are highlighted on the image.</li>
    <li>The results are saved to the folder specified by the user (result).</li>
</ol>

<!-- Requirements -->
<h2>Requirements:</h2>
<ul>
    <li>Python 3</li>
    <li>OpenCV (cv2)</li>
    <li>NumPy</li>
</ul>

<!-- File Descriptions -->
<h2>File Descriptions:</h2>
<ul>
    <li><strong>main.py:</strong> The main Python code for detecting blood cells.</li>
    <li><strong>data/blood1.jpg:</strong> An example image of a blood cell.</li>
    <li><strong>result:</strong> The folder where the results will be saved.</li>
    <li><strong>requirements.txt:</strong> File containing the required Python libraries.</li>
</ul>

<!-- How to Use -->
<h2>How to Use:</h2>
<ol>
    <li>Install Python and the required libraries.</li>
    <li>Run the <code>main.py</code> file.</li>
    <li>Enter the requested information when prompted (data folder path, result folder path, data item name, and maximum item number).</li>
    <li>The program saves the results to the specified folder.</li>
</ol>

<!-- License -->
<h2>License:</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>
