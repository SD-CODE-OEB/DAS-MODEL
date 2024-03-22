# Driver Drowsiness and Alert System

## Steps Followed:

### 1.we use opencv and dlib librsries for our system working.
### 2.we capture the real time frame of the Driver.
### 3.we convert the frame to grayscale as cv2 has BGR format colors.We do this to increse optimization and to reduce the amount of processing data...simply a DATA REDUCTION technique.
### 4.From the imported libraries, dlib has a face dection in-built method: get_frontal_face_detector() and in it to identify the face components such as EYES,NOSE,MOUTH,etc., we use the shape_detector(with parameter of the the file path consisting of the face points of a face, which is {shape_predictor_68_face_landmarks.dat})
### 5.