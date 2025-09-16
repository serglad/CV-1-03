# CV-1-03
Edge detection using gaussian blur and Canny algorithm.

# Command line usage: 
    ```
    python3 get_edges.py <Cmin> <Cmax>
    ```
        Cmin - Minimum threshold for Canny
        Cmax - Maximum threshold for Canny
        Optional flag: -c - Use the camera input instead of the test image

# Functions:
    get_edges(img, Cmin, Cmax):
        img - source image
        Cmin - Minimum threshold for Canny
        Cmax - Maximum threshold for Canny
        return value - processed image

# Dependencies: 
    pip install -r requirements.txt