
_________________________________________________________________________________________
______________________________OpenCV_____________________________________________________

# IMAGES:
    black = np.zeros((512,512,3), np.uint8) 

    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    ret,im_thres = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY)

    hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
    lower = np.array([0,30,30])  # Hue: tono del color | Saturacion | Value: brillo
    upper = np.array([255,255,255])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(fondo_verde,fondo_verde, mask= mask)

# Contours:
    contours = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    cv2.drawContours(img, contours, -1, colors.black, 2)
    max_contour = max(contours, key=cv2.contourArea)    

# TRATAMIENTOS:
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # eliminar puntos exteriores
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # rellenar pequeños huecos interiores
    erosion = cv2.erode(img,kernel,iterations = 1)
    dilation = cv2.dilate(img,kernel,iterations = 1)

# DRAWINGS

    img = cv2.line(black,(0,0),(511,511),(255,0,0),5) 

    img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) #top-left(384,0)   bottom-right(510,128) 

    cv2.circle(img,(447,63), 63, (0,0,255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

    #Dibujar semicirculo (por angulo)
    radius = 50
    axes = (radius, radius)
    cv2.ellipse(img, center, axes, rotation, startAngle, endAngle, color, 10)

# CAM Snapshot:
    __________________WebCAM_______________________________________
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
    ret, snapshot = cam.read()
    cam.release()

    _________________RaspiCAM_______________________________________
    camera = PiCamera()
    camera.resolution  = ( camera_w, camera_h)
    camera.framerate = 32
    camera.hflip = True
    camera.vflip = True 
    # more.... https://www.raspberrypi.org/documentation/usage/camera/python/README.md
               http://picamera.readthedocs.io/en/release-1.10/api_camera.html

    rawCapture = PiRGBArray(camera, size = (camera_w, camera_h))

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        snapshot = frame.array
        rawCapture.truncate(0)
    
    camera.close()

# IMG READ:
    img_rgb = cv2.imread('mario.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    height, width = img_rgb.shape[:2]

# IMG SAVE:
    cv2.imwrite('image.png',img2)

# WINDOWS:
    cv2.namedWindow("fondo", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("fondo",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)


_________________________________________________________________________________________
______________________________Python_____________________________________________________

# Estructura:
    if __name__ == "__main__":

# I/O Files:
    ___________________Writing_____________________________________
    data_w["calibration_points"] = pickle.dumps(pts_src, protocol=0)
    with open( self.calibration_file , 'w') as outfile:
            json.dump(data_w, outfile)

    __________________Reading______________________________________
    with open(self.calibration_file) as json_file:  
        data_r = json.load(json_file)
        pts_src = pickle.loads(data_r['calibration_points'])

# Dict:
    for key, value in d.iteritems():

# Eficiencia:
    %timeit funcion(arg_1,arg_2)  -> devuelve el tiempo de ejecucion
