# 3D Computer Vision Basics, 2025 Fall Semester

## Schedule
* 1/7 – Stereo Vision Part 1
* 1/21 – Stereo Vision Part 2
* 1/28 - 奈良県立医科大学の見学
* **1/31 23:59 JST - Final Report Deadline (submitted via LMS)**

## Overview - From Pixels to 3D Worlds!
This course introduces the fundamental principles of 3D computer vision, exploring how images captured by cameras can be transformed into meaningful 3D reconstructions. 
Students will learn the mathematical and computational foundations behind stereo vision and its real-world applications.
<p align="center">
<img width="781" height="322" alt="Screenshot 2025-11-12 at 12 05 33 PM" src="https://github.com/user-attachments/assets/2fcce131-2a5c-46c9-8437-0db8752b6121" />
</p>

### Requirements
* A Gmail Account $\rightarrow$ To run Google Colab 
* Basic knowledge of linear algebra
* Main Python packages used in this course (available in Google Colab): NumPy, OpenCV, Matplotlib, Plotly

### References
* Numpy documentation: https://numpy.org/doc/2.3/user/absolute_beginners.html
* OpenCV documentation:
  * Preparing 2D–3D correspondences of a checkerboard: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
  * General Documentation for Camera Calibration + 3D Reconstruction: https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html

## Final Report (within 2 A4 pages): 1/31 23:59 JST
* **Brief description of your code (90pt)**
$\rightarrow$ the algorithm you implemented, relevant equations, and visualization results
  * **Calibration (25pt)**
    * Code Explanation
    * Report Relative Pose (from Camera 2 to Camera 1): Rotation 𝑅 (3x3 matrix) and Translation 𝑇 (3x1 matrix)
  * **Image Rectification (25pt)**
    * Code Explanation
    * Visualization of Rectified Image Pairs
  * **Correspondence Search + Depth Estimation (20pt)**
    * Code Explanation
    * Visualization of Disparity and Depth Maps
  * **Depth to 3D colored point clouds (20pt)**
    * Code Explanation
    * Screenshot of the 3D Reconstruction from at least two views
* **Try the full pipeline on your own images (Optional, for additional 10pt)**

<img width="1259" height="39" alt="image" src="https://github.com/user-attachments/assets/558b0baf-cf21-4de1-8ece-98d52d5ef331" />
