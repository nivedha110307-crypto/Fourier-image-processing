import argparse
import cv2
import numpy as np

def compress_image(image_path, output_path, keep_percent=0.1):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    fft = np.fft.fft2(img)
    fft_shifted = np.fft.fftshift(fft)

    rows, cols = img.shape
    center_row, center_col = rows // 2, cols // 2
    radius = int(min(center_row, center_col) * keep_percent)

    mask = np.zeros((rows, cols), dtype=np.uint8)
    cv2.circle(mask, (center_col, center_row), radius, 1, -1)

    fft_filtered = fft_shifted * mask
    reconstructed = np.fft.ifft2(np.fft.ifftshift(fft_filtered))
    reconstructed = np.abs(reconstructed).astype(np.uint8)

    cv2.imwrite(output_path, reconstructed)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--keep", type=float, default=0.1)
    args = parser.parse_args()
    compress_image(args.input, args.output, args.keep)
