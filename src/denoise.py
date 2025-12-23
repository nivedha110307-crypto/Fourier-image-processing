import argparse
import cv2
import numpy as np

def denoise_image(image_path, output_path, cutoff_radius=30):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    noisy_img = img + np.random.normal(0, 25, img.shape).astype(np.uint8)

    fft_noisy = np.fft.fft2(noisy_img)
    fft_shifted = np.fft.fftshift(fft_noisy)

    rows, cols = img.shape
    center_row, center_col = rows // 2, cols // 2
    mask = np.zeros((rows, cols), dtype=np.uint8)
    cv2.circle(mask, (center_col, center_row), cutoff_radius, 1, -1)

    fft_filtered = fft_shifted * mask
    img_filtered = np.fft.ifft2(np.fft.ifftshift(fft_filtered))
    img_filtered = np.abs(img_filtered).astype(np.uint8)

    cv2.imwrite(output_path, img_filtered)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--cutoff", type=int, default=30)
    args = parser.parse_args()
    denoise_image(args.input, args.output, args.cutoff)
