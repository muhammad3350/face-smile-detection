# Face and Smile Detection with Python and OpenCV

A simple real-time face and smile detection project built with **Python** and **OpenCV**. The program uses the computer's webcam to detect faces and smiles in real time.

## Features

* Real-time face detection using a webcam.
* Real-time smile detection.
* Detects multiple faces at the same time.
* Detects smiles inside detected faces.
* Displays a rectangle around each detected face.
* Displays a rectangle around detected smiles.
* Displays the number of detected faces.
* Displays the number of detected smiles.
* Uses pre-trained Haar Cascade classifiers provided by OpenCV.

## Technologies Used

* **Python**
* **OpenCV 4.10.0.84**
* **Haar Cascade Classifier**
* **Computer Vision**

## Requirements

Make sure you have Python installed on your computer.

This project uses:

* **Python**
* **OpenCV 4.10.0.84**

To install the required OpenCV version manually:

```bash
python -m pip install opencv-python==4.10.0.84
```

Or install all dependencies from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains the specific OpenCV version required for this project.

## How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd face-detection-project
```

3. Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Run the Python file:

```bash
python main.py
```

5. The webcam will open and start detecting faces and smiles.

6. Press **Q** to close the program.

## How It Works

The project uses OpenCV's pre-trained **Haar Cascade Classifiers** for face and smile detection.

The process works as follows:

```text
Webcam
   ↓
Capture Frame
   ↓
Flip Frame
   ↓
Convert to Grayscale
   ↓
Detect Faces
   ↓
For Each Detected Face
   ↓
Crop the Face Region
   ↓
Detect Smiles Inside the Face
   ↓
Draw Rectangle Around Face
   ↓
Draw Rectangle Around Smile
   ↓
Display Number of Faces and Smiles
```

## Face Detection

The program uses the following pre-trained Haar Cascade classifier to detect faces:

```text
haarcascade_frontalface_default.xml
```

The classifier detects frontal faces in each frame captured from the webcam.

## Smile Detection

After detecting a face, the program searches for smiles inside the detected face region using:

```text
haarcascade_smile.xml
```

This makes the smile detection more focused because the program does not search for smiles across the entire image.
