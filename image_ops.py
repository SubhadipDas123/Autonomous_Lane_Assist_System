"""Simple image operations used for demonstration and testing.

Refactored from an example script into functions that accept paths or arrays.
"""

from typing import Tuple
import cv2
import numpy as np
from scipy.ndimage import gaussian_filter


def read_image(path: str) -> np.ndarray:
    return cv2.imread(path)


def to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def gaussian_blur(image: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """Apply a Gaussian blur using SciPy's gaussian_filter.

    The function accepts either a color or grayscale image. For color images
    the filter is applied per-channel.
    """
    if image.ndim == 3:
        blurred = np.stack([gaussian_filter(image[..., c], sigma=sigma) for c in range(image.shape[2])], axis=-1)
        return blurred.astype(image.dtype)
    else:
        return gaussian_filter(image, sigma=sigma).astype(image.dtype)


def canny_edges(image: np.ndarray, low_threshold: int = 125, high_threshold: int = 175) -> np.ndarray:
    return cv2.Canny(image, low_threshold, high_threshold)


def dilate(image: np.ndarray, kernel_size: Tuple[int, int] = (3, 3), iterations: int = 1) -> np.ndarray:
    kernel = np.ones(kernel_size, np.uint8)
    return cv2.dilate(image, kernel, iterations=iterations)


def find_and_draw_contours(image: np.ndarray, edged: np.ndarray):
    contours, hierarchies = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    drawn = cv2.drawContours(image.copy(), contours, -1, (0, 0, 255), 2)
    return drawn, len(contours)


if __name__ == "__main__":
    # small demo when run as script
    import os
    sample = os.path.join(os.path.dirname(__file__), "..", "Road_Sample_Image_Frame.jpeg")
    sample = os.path.abspath(sample)
    img = read_image(sample)
    if img is None:
        print("No sample image found at:", sample)
    else:
        gray = to_grayscale(img)
        blur = gaussian_blur(img)
        edges = canny_edges(blur)
        dil = dilate(img)
        drawn, count = find_and_draw_contours(img, edges)
        print("Found contours:", count)
        cv2.imshow("image", img)
        cv2.imshow("Gray", gray)
        cv2.imshow("Edges", edges)
        cv2.waitKey(0)
