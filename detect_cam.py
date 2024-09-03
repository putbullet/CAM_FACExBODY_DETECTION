import cv2

def list_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def select_camera():
    cameras = list_cameras()
    if not cameras:
        print("No cameras detected.")
        return None

    print("Available camera interfaces:")
    for i, camera in enumerate(cameras):
        print(f"[{i}] Camera {camera}")
    
    cam_index = int(input("Select a camera interface (enter the number): "))
    
    if cam_index < 0 or cam_index >= len(cameras):
        print("Invalid selection.")
        return None
    
    return cameras[cam_index]
