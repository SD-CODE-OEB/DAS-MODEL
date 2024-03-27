pairs = [("Alice", 85), ("Bob", 92), ("Charlie", 88)]
names, scores = zip(*pairs)

print(names,scores)

keys = ["name", "age", "job"]
values = ["Alice", 25, "Engineer"]
dictionary = dict(zip(keys, values))

print(dictionary)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed =list(zip(*matrix))

print(transposed)


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 88]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
    
    
# import dlib
# import cv2

# # Assume you have a detector and shape predictor
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("assets/shape_predictor_68_face_landmarks.dat")

# video = cv2.VideoCapture(0)

# while True:
#     # Assume you have a frame from your video capture
#     ret, frame = video.read()

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the grayscale frame
#     faces = detector(gray)

# # Iterate over the detected faces
#     for face in faces:
#     # Get the facial landmarks for the face
#         landmarks = predictor(gray, face)

#     # Get the aligned face chip
#         aligned_face = dlib.get_face_chip(frame, landmarks)

#     # Now you can use the aligned_face image
#     cv2.imshow("Aligned Face", aligned_face)
#     cv2.waitKey(0)

# # Release the video capture
#     video.release()
#     cv2.destroyAllWindows()