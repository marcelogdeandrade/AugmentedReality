# AugmentedReality
This projects uses Python and OpenCV to place objects on a plane.

## Requirements

All python requirements are listed on `requirements.txt`.

You need a webmcam to run `main.py`.

You also need to print `images/board_aruco.png` to show it on your webmcam.

## Usage

Execute 

```
$ python main.py
```

A new window will open with a livestream of your webcam. Show your printed `images/board_aruco.png` image to replace with a new image.

To change the default image, add any image to `images/` and change the code on `main.py` to your new image path:

```
IMAGE_REPLACE = "../images/new_image.jpeg"
```
