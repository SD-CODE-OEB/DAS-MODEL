# 🚗💤⚠️Driver Drowsiness and Alert System

## 🪜Steps Followed:

### 0️⃣1️⃣ - We use opencv and dlib librsries for our system working.

### 0️⃣2️⃣ - We capture the real time frame of the Driver.

### 0️⃣3️⃣ - We convert the frame to grayscale as cv2 has BGR format colors.We do this to increse optimization and to reduce the amount of processing data...simply a DATA REDUCTION technique.

### 0️⃣4️⃣ - From the imported libraries, dlib has a face dection in-built method: get_frontal_face_detector() and in it to identify the face components such as EYES,NOSE,MOUTH,etc., we use the shape_detector(with parameter of the the file path consisting of the face points of a face,which is {shape_predictor_68_face_landmarks.dat}).

### 0️⃣5️⃣ - Our Parameters for this project are:

- [x] Eye Ratio (Sleepiness)
- [x] Mouth Ratio (Yawning)
- [x] Face in a frame (No Deviation)

### 0️⃣6️⃣ - We have also imported the 'winsound' package to sound alarm for alerting the driver.

### 0️⃣7️⃣ - The following functions have have been created for their resuability and modularity:

- [x] play_beep()- To sound the alarm.
- [x] eye_aspect_ratio(eye)- To calculate the threshold for drowsy eyes.
- [x] mouth_open(frame) - with its smaller functions to calculate the threshold of Yawning.
- [x] get_landmarks(frame) && show_landmarks(frame,landmarks)- To get landmarks from '.dat' file and show them on a face.

### 0️⃣8️⃣ - We now initialize the loop to run our frame/video continiously.

### 0️⃣9️⃣ - In the loop, we give the left_eye and right_eye cordinates which can be acquired from the landmarks[] from get_landmarks(frame).

### 1️⃣0️⃣ - Now, from those co-ordinates we calculate the eye_aspect_ratio() of left and right eye.

### 1️⃣1️⃣ - we store the mouth_aspect_ratio() calculating frame in lip_distance variable.

### 1️⃣2️⃣ - Based on teh reaserch we have done on the Yawning of humans:

##### - Yawns are part of your body’s process of staying awake.

##### - Yawning is also commonly associated with boredom. If your environment isn’t stimulating, you’ll feel drowsy.

##### - Healthcare providers consider excessive yawning as more than three yawns per 15 minutes several times a day.

### 1️⃣3️⃣ - From this research, We have set a time constraint of 15 mins using the 'time' package python and initialized current time through "star_time" variable where if the driver yawns for more than 3 times in the given constraint of time , i.e., [ elapsed_time <= 900 ] ,then we buzz the alarm as yawning limit is reached.

### 1️⃣4️⃣ - If the time has elapsed 15 mins with (<=3) yawns , we againbeginthe time counter of 15 mins by resettng the yawns.

### 1️⃣5️⃣ - Next, We set the eye_aspect_ratio() constraint with its threshold and buzz alarm when both his eyes are below the threshold.

### 1️⃣6️⃣ - The Main-Frame is now intialized, which can be destroyed by presssing the 'ENTER' key.
