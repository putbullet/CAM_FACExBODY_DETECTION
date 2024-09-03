import cv2
import datetime
import time
from detect_cam import list_cameras, select_camera


list_cameras()
camera_index = select_camera()
if camera_index is not None:
    cap = cv2.VideoCapture(camera_index)
else:
    print("No camera selected, exiting.")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

detection = False
detection_stop_time = None
timer_started = False
seconds_after_detection = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) + len(bodies) > 0:
        if not detection:
            detection = True
            timer_started = False
            current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            out = cv2.VideoWriter(f'{current_time}.mp4', fourcc, 20.0, frame_size)
            print(f'Recording Started: {current_time}')
    elif detection:
        if timer_started:
            if time.time() - detection_stop_time >= seconds_after_detection:
                detection = False
                timer_started = False
                out.release()
                print(f'Recording Stopped: {current_time}')
        else:
            timer_started = True
            detection_stop_time = time.time()
    
    if detection:
        out.write(frame)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    cv2.imshow('CCTV', frame)
    
    if cv2.waitKey(1) == ord('q'):
        if detection:
            out.release()
        break

if detection:
    out.release()

cap.release()
cv2.destroyAllWindows()
