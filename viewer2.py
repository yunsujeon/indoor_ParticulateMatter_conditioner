import cv2
import screeninfo
from viewmade import token
screen_id = 0

screen = screeninfo.get_monitors()[screen_id]
width, height = screen.width, screen.height

if token == 1:
    image = cv2.imread('C:/Users/dbstn/Desktop/closewindows.png')
elif token == 2:
    image = cv2.imread('C:/Users/dbstn/Desktop/windoff.png')

window_name = 'projector'
# cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
# cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
#                       cv2.WINDOW_FULLSCREEN)
cv2.imshow(window_name, image)
cv2.waitKey()
cv2.destroyAllWindows()