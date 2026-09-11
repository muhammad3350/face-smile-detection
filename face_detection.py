#Workflow of the code
# --------------------
#Camera
#   ↓
#Capture Frame
#   ↓
#Flip Image
#   ↓
#Convert to Grayscale
#   ↓
#Detect Faces
#   ↓
#Draw Rectangle Around Faces
#   ↓
#Display Number of Faces
#   ↓
#Display Number of Smiles
#   ↓
#Show Frame
#   ↓
#Press Q → Exit




import cv2
# Initialize the camera
cap = cv2.VideoCapture(0) # VideoCapture(0) is used to access the default camera (usually the built-in webcam on a laptop). If you have multiple cameras connected to your system, you can change the index (0, 1, 2, etc.) to access a different camera.
# make object called face_cascade to detect faces,
# cascade classifier is a machine learning object detection algorithm used to identify objects in images or video. In this case, it is used to detect faces.
# data.haarcascades is a directory in the OpenCV library that contains pre-trained Haar Cascade classifiers for various object detection tasks, including face detection.
# The haarcascade_frontalface_default.xml file is one of these classifiers specifically trained to detect frontal faces in images.

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

# smile_cascade
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

# start an infinite loop to continuously capture frames from the camera and process them for face detection.
#  The loop will run until the user presses the 'q' key to exit.
while True:
    # ret, frame = cap.read() it reads a frame from the camera. The cap.read() method returns two values: ret and frame. 
    # ret is a boolean value that indicates whether the frame was successfully captured from the camera.
    # If ret is True, it means the frame was captured successfully; if False, it means there was an error in capturing the frame.
    # frame is the actual image frame captured from the camera, represented as a NumPy array.
    ret, frame = cap.read()
#-------------------------------
    # Check if the frame was successfully captured. If not, print an error message and break the loop to exit the program.
    if not ret:
        print('Could not access the camera')
        break
    # Flip the frame horizontally to create a mirror effect, 1 means flipping around the y-axis (horizontal flip). (Like the front camera of a smartphone)
    # This is often done in applications where the user expects to see themselves as they would in a mirror.    
    frame = cv2.flip(frame, 1)
    # Convert the captured frame to grayscale.
    # why use grayscale? Because face detection algorithms often work better on grayscale images, as they reduce the complexity of the image data and focus on the intensity of light rather than color information. This can improve the accuracy and speed of face detection.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# -------------------------------
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5
        )


    smile_count = 0
    # Draw rectangles around detected faces and display the number of faces detected on the frame.
    for x, y, w, h in faces:
        cv2.rectangle(
            frame,
            (x, y), # The top-left corner of the rectangle is defined by the coordinates (x, y), which represent the position of the detected face in the image.
            (x + w, y + h), # The bottom-right corner of the rectangle is defined by the coordinates (x + w, y + h), where w is the width and h is the height of the detected face. This ensures that the rectangle encompasses the entire face.
            (0, 255, 0), # The color of the rectangle is specified in BGR format (Blue, Green, Red). In this case, (0, 255, 0) represents green.
            2 # The thickness of the rectangle's border = 2 pixels
        )

        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]

    # Detect smiles inside the face 
        smiles = smile_cascade.detectMultiScale(
         face_gray,
         scaleFactor=1.7,
         minNeighbors=30 )

        for sx, sy, sw, sh in smiles:
             cv2.rectangle(
                 face_color,
                 (sx, sy),
                 (sx + sw, sy + sh),
                 (255, 0, 0),
                 2 )
             smile_count += 1

    # write the number of detected faces on the frame using cv2.putText().
    cv2.putText(
        frame,
        f'Faces: {len(faces)}',
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, # The scale factor for the text size.
        (0, 255, 0),
        2 # The thickness of the text stroke in pixels.
    )

    # Display number of smiles 
    cv2.putText(
         frame, f'Smiles: {smile_count}',
         (20, 80),
         cv2.FONT_HERSHEY_SIMPLEX,
         1,
         (255, 0, 0),
         2 )
    
    # Show the processed frame with detected faces and the number of faces displayed on it in a window titled 'Face and Smile Detection'.
    cv2.imshow('Face and Smile Detection', frame) # Display the frame in a window named 'Face and Smile Detection'
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Wait for the 'q' key to be pressed to quit
        break

cap.release() # Release the camera resource to free it up for other applications. This is important to avoid locking the camera and ensure that it can be accessed by other programs or future runs of this script.
cv2.destroyAllWindows() # Close all OpenCV windows that were opened during the execution of the program. This is important to clean up the GUI resources and ensure that no windows remain open after the program has finished running.
    
    