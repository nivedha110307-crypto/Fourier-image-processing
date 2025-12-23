# Fourier Transforms in Image Processing and Compression

Academic mini-project implementing:
- Image compression using 2D FFT (keep low-frequency coefficients).
- Image denoising using FFT-based low-pass filtering.

## Tech Stack
- Python, NumPy, OpenCV, Matplotlib
# Fourier Transforms in Image Processing and Compression

Academic mini-project implementing:
- Image compression using 2D FFT (keeping only low-frequency coefficients).
- Image denoising using FFT-based low-pass filtering.

This project is based on a course assignment for Differential Equations and Transforms, demonstrating practical use of Fourier analysis in image processing.

## Tech Stack

- Python
- NumPy
- OpenCV
- Matplotlib

## How to Run

1. **Clone the repository**

2. **Install dependencies**

3. **Run image compression**

- `examples/sample.png` – input image  
- `outputs/compressed_10.png` – compressed output image (you can choose any path)  
- `--keep 0.1` – keep 10% of low-frequency coefficients

4. **Run image denoising**


- Adds Gaussian noise, then applies a low-pass filter in the frequency domain  
- `--cutoff` controls the radius of the low-pass filter

> Make sure the `outputs/` folder exists or change paths to somewhere that exists.

## Project Structure
src/
compress.py # FFT-based image compression
denoise.py # FFT-based image denoising (noise + low-pass filter)
examples/
sample.png # example input image
report/
DET-project.pdf # original course report
requirements.txt
README.md

## Theory (Short)

- Applies 2D FFT to convert images from spatial domain to frequency domain.
- For compression, retains low frequencies (global structure) and discards high frequencies (fine detail/noise).
- For denoising, applies a circular low-pass mask to suppress high-frequency noise before inverse FFT reconstruction.







## How to Run

