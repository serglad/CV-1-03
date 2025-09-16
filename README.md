# CV-1-03
Edge detection using gaussian blur and Canny algorithm.
The main script displays the original and processed test images side by side in a new window using matplotlib.

## Command line usage 
    python3 get_edges.py <Cmin> <Cmax> -c
        Cmin - Minimum threshold for Canny
        Cmax - Maximum threshold for Canny
        -c - Use the camera input instead of the test image

## Functions:
    get_edges(img, Cmin, Cmax):
        img - Source image
        Cmin - Minimum threshold for Canny
        Cmax - Maximum threshold for Canny
        Returns the processed image

## Dependencies: 
    pip install -r requirements.txt
Note: the script uses argparse, which might not work on all platforms
