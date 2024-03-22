import dlib
import cv2

# Load the face detector and facial landmark predictor
video = cv2.VideoCapture(0)

detect_face = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("G:/Program Files/DRIVER PROJECT DATA/shape_predictor_68_face_landmarks.dat")

while True:
    ret, frame = video.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detect_face(gray)

    # Iterate over the detected faces
    for face in faces:
        # Get the facial landmarks for the face
        landmarks = predictor(gray, face)

        # Draw a rectangle around the face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw the facial landmarks on the face
        for i in range(68):
            x, y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    # Display the frame with the detected faces
    cv2.imshow("Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
video.release()
cv2.destroyAllWindows()