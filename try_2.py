import cv2
import dlib
from scipy.spatial import distance

# Function to calculate the eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Load the face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("G:/Program Files/DRIVER PROJECT DATA/Source/assets/shape_predictor_68_face_landmarks.dat")

# Load the video capture
cap = cv2.VideoCapture(0)

# Initialize variables
counter = 0
closed_eyes = 0
eyes_open = True

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    for face in faces:
        # Detect facial landmarks
        left_eye_start = 42
        left_eye_end = 48
        right_eye_start = 36
        right_eye_end = 42

        landmarks = predictor(gray, face)

        # Extract the left and right eye coordinates
        left_eye = landmarks[left_eye_start:left_eye_end]
        right_eye = landmarks[right_eye_start:right_eye_end]

        # Calculate the eye aspect ratio for both eyes
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Average the eye aspect ratio for both eyes
        ear = (left_ear + right_ear) / 2.0

        # Check if the eyes are closed
        if ear < 0.18:
            closed_eyes += 1
            if closed_eyes >= 75:  # Adjust the threshold as per your requirement
                cv2.putText(frame, "ALERT: Eyes Closed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            closed_eyes = 0

    cv2.imshow("Driver Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()