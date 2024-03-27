import dlib
import cv2
from scipy.spatial import distance
import winsound
# Function to play beep sound
def play_beep():
    frequency = 2500  # Set the frequency of the beep sound
    duration = 1000  # Set the duration of the beep sound in milliseconds
    winsound.Beep(frequency, duration)

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Load the face detector model
detector = dlib.get_frontal_face_detector()

# Load the face landmarks predictor model
predictor = dlib.shape_predictor("G:/Program Files/DRIVER PROJECT DATA/Source/assets/shape_predictor_68_face_landmarks.dat")

# Load the input image
# image = cv2.imread("G:/Program Files/DRIVER PROJECT DATA/WIN_20240321_12_47_48_Pro.jpg")

video = cv2.VideoCapture(0)


while True:
    
    ret, frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
    faces = detector(gray)

    # Iterate over the detected faces
    for face in faces:
        # Predict the face landmarks
        landmarks = predictor(gray, face)

        # coounting and placing the face landmarks
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y

            # Draw a circle on each face landmark
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
            # Use the eye_aspect_ratio function to calculate the eye aspect ratio for the left eye
            left_eye = [(landmarks.part(36).x, landmarks.part(36).y),
                         (landmarks.part(37).x, landmarks.part(37).y),
                         (landmarks.part(38).x, landmarks.part(38).y),
                         (landmarks.part(39).x, landmarks.part(39).y),
                         (landmarks.part(40).x, landmarks.part(40).y),
                         (landmarks.part(41).x, landmarks.part(41).y)]
            left_ear = eye_aspect_ratio(left_eye)

            # Use the eye_aspect_ratio function to calculate the eye aspect ratio for the right eye
            right_eye = [(landmarks.part(42).x, landmarks.part(42).y),
                          (landmarks.part(43).x, landmarks.part(43).y),
                          (landmarks.part(44).x, landmarks.part(44).y),
                          (landmarks.part(45).x, landmarks.part(45).y),
                          (landmarks.part(46).x, landmarks.part(46).y),
                          (landmarks.part(47).x, landmarks.part(47).y)]
            right_ear = eye_aspect_ratio(right_eye)

            # Print the eye aspect ratios
        print("Left Eye Aspect Ratio:", left_ear)
        print("Right Eye Aspect Ratio:", right_ear)

                    # Check if the left eye is closed
        if left_ear < .11:
                        print("Left Eye is closed")
                        play_beep()
        else:
                        print("Left Eye is open")

                    # Check if the right eye is closed
        if right_ear < .12:
                        print("Right Eye is closed")
                        play_beep()
        else:
                        print("Right Eye is open")
    
    cv2.imshow("Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
video.release()
cv2.destroyAllWindows()
