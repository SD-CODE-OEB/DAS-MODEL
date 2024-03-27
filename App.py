import cv2, dlib
import dlib
from scipy.spatial import distance as dist
import winsound
import time

    
detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("assets/shape_predictor_68_face_landmarks.dat")

def play_beep():
    frequency = 2500  # Set the frequency of the beep sound
    duration = 1000  # Set the duration of the beep sound in milliseconds
    winsound.Beep(frequency, duration)
    
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def get_landmarks(frame):
    faces = detector(frame, 1)
    # Detecting only one face per frame.
    if len(faces) > 1:
        return "error"
    if len(faces) == 0:
        return "error"
    # Storing all the coordinates of the face landmarks inside a list.
    landmarks = []
    for p in predictor(frame, faces[0]).parts():
        landmarks.append([p.x, p.y])
         
    # Face in a box {
    bbox = (230, 110, 200, 230)  # (x of top-left, y of top-left, width, height)
    cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[0]+bbox[2], bbox[1]+bbox[3]), (0, 255, 0), 2) #(frm, top-left, bottom-right, color, thickness)
    if faces[0].left() < bbox[0] or faces[0].right() > bbox[0]+bbox[2] or faces[0].top() < bbox[1] or faces[0].bottom() > bbox[1]+bbox[3]:
        # play_beep()
        cv2.putText(frame, "User is deviated", (50,450), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
    #  } Face in a box
      
    return landmarks

def show_landmarks(frame, landmarks):
    # Making a frame copy to not disturb the original frame and marking the landmarks on the copied frame which can be accesed seperately.
    frame = frame.copy()
    for point in landmarks:
        pos = (point[0], point[1])
        cv2.circle(frame, pos, 1, color=(255, 255, 255))
    return frame

def lip_center(landmarks, top_indices, bottom_indices):
    lip_pts = []
    for i in top_indices:
        lip_pts.append(landmarks[i])
    for i in bottom_indices:
        lip_pts.append(landmarks[i])
    lip_mean = [sum(x) / len(x) for x in zip(*lip_pts)]
    return int(lip_mean[1])

def top_lip(landmarks):
    return lip_center(landmarks, range(50, 53), range(61, 64))

def bottom_lip(landmarks):
    return lip_center(landmarks, range(65, 68), range(56, 59))

def mouth_open(frame):
    landmarks = get_landmarks(frame)    
    image_with_landmarks = show_landmarks(frame, landmarks)
    top_lip_center = top_lip(landmarks)
    bottom_lip_center = bottom_lip(landmarks)
    lip_distance = abs(top_lip_center - bottom_lip_center)
    return image_with_landmarks, lip_distance

video = cv2.VideoCapture(0)
yawns = 0
yawn_status = False

while True:
    ret, frame = video.read()
    if ret == False:
        break
    landmarks = get_landmarks(frame)   
    # indices of left eye points.
    left_eye = [landmarks[36], landmarks[37], landmarks[38], landmarks[39], landmarks[40], landmarks[41]]
    left_ear = eye_aspect_ratio(left_eye)

    # indices form the .dat file of right eye points.
    right_eye = [landmarks[42], landmarks[43], landmarks[44], landmarks[45], landmarks[46], landmarks[47]]
    right_ear = eye_aspect_ratio(right_eye)
    
    image_landmarks, lip_distance = mouth_open(frame)
    
    prev_yawn_status = yawn_status
    start_time = time.time()

    # Calculating mouth distance to monitor yawns of driver.
    if lip_distance > 25:
        yawn_status = True 
        if yawns <=3 :
            cv2.putText(frame, "Subject is Yawning", (50,450),cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)

        output_text = " Yawn Count: " + str(yawns + 1)

        cv2.putText(frame, output_text, (50,50),
                    cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
        if yawns > 3:
            elapsed_time = time.time() - start_time
            if elapsed_time <= 900:  # 15 minutes = 900 seconds
                cv2.putText(frame, "Yawn Limit Reached.", (50,450), 
                            cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),1)
                cv2.putText(frame, "You are Drowsy", (50,400),cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
                play_beep()
            else:
                start_time = time.time()
                yawns = 0
    else:
        yawn_status = False 

    if prev_yawn_status == True and yawn_status == False:
        yawns += 1

# Calculating eye aspect ratio to monitor drowsiness of driver.
    if left_ear < .15 and right_ear < .15:
        cv2.putText(frame, "Subject is sleeping", (50,450), 
                    cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
        play_beep()
        
    cv2.putText(frame, "Left Eye EAR: {:.2f}".format(left_ear), (450,100),
                cv2.FONT_HERSHEY_COMPLEX, .5,(0,0,255),2)
    cv2.putText(frame, "Right Eye EAR: {:.2f}".format(right_ear), (450,150),
                cv2.FONT_HERSHEY_COMPLEX, .5,(0,0,255),2)

    # cv2.imshow('Live Landmarks', image_landmarks ) #this frame only shows the landmarks on face implemented through show_landmarks().
    
# --------------------Main Frame---------------------
    cv2.imshow('Detection', frame )
# ---------------------------------------------------
    if cv2.waitKey(1) == 13: 
        break
    
video.release()

cv2.destroyAllWindows()
