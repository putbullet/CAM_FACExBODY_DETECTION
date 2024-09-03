# CCTV Face Recognition

## Description
The CCTV Face Recognition project uses Python and OpenCV to detect faces through a connected camera. It records video when faces or bodies are detected and saves the video with a timestamped filename. The project allows users to select from multiple camera interfaces available on their computer, making it versatile for various setups.

## Documentation

### How It Works

1. **Camera Detection**: 
   - The script detects all available camera interfaces using OpenCV.
   - Users are prompted to select the desired camera interface.

2. **Face and Body Detection**:
   - The script utilizes Haar Cascades for detecting faces and bodies in the video feed.
   - When a face or body is detected, it triggers video recording.

3. **Video Recording**:
   - The recording starts when a face or body is detected and continues until no detection is made for a specified duration (default is 5 seconds).
   - The recorded video is saved in the current working directory with a timestamp as the filename (format: `YYYY-MM-DD_HH-MM-SS.mp4`).

4. **User Interface**:
   - The video feed is displayed in a window named "CCTV".
   - Users can exit the application by pressing the 'q' key.

### Important Classes and Functions

- `list_cameras()`: Scans for available camera interfaces and returns a list of indices.
- `select_camera()`: Prompts the user to select a camera from the detected interfaces.
- `cv2.VideoCapture(n)`: Initializes video capture from the selected camera index.
- `cv2.VideoWriter()`: Handles video file writing with specified codec and frame rate.

### How to Use
1. Ensure you have a camera connected to your computer.
2. Run the script. It will display available camera interfaces.
3. Select a camera by entering its corresponding number.
4. The application will start displaying the video feed and detecting faces.
5. To exit, press the 'q' key.

## Installation

To run this project, you need to install the OpenCV library. You can install it using pip:

```bash
pip install opencv-python
```
Make sure your Python environment is set up correctly and you have the necessary permissions to access the camera.

