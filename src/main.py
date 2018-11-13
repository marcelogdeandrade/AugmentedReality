import cv2
import utils as utils

IMAGE_REPLACE = "../images/dog.jpeg"

cap = cv2.VideoCapture(0)

gabarito = cv2.imread("../images/board_aruco.png")
foto = utils.read_img(IMAGE_REPLACE, gabarito)
corners_or, ids_or = utils.detect_markers(gabarito)

while(True):
    ret, frame = cap.read()
    corners_dest, ids_dest = utils.detect_markers(frame)
    if len(corners_dest) > 0: 
        origin, dest = utils.get_points(ids_or, ids_dest, corners_or, corners_dest)
        warped_img = utils.wrap_image(origin, dest, (frame.shape[0], frame.shape[1]), foto)
        frame = utils.merge_images(warped_img, frame)
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 1920,1080)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()