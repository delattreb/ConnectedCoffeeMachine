"""
Main.py
Auteur: Bruno DELATTRE
Date : 11/08/2016
"""

# Source https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/
#camera.rotation = 180 Rotation : 90 180 270
#camera.start_preview(alpha=200) : Réglage alpga
#camera.brightness = 70 Luminosité 0-100
#camera.contrast = 50 Contraste 0-100
#camera.capture('/home/pi/Desktop/image%s.jpg' % i)

#recording
#camera.start_recording('/home/pi/video.h264')
#sleep(10)
#camera.stop_recording()

#Ajustement
"""
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()

Effet couleur
camera.image_effect = 'colorswap'
none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1, and deinterlace2. The default is none

Balance des blanc
camera.awb_mode = 'sunlight'
off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, and horizon. The default is auto

Exposition
camera.exposure_mode = 'beach'
off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, and fireworks. The default is auto
"""

from picamera import PiCamera

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
camera.annotate_text_size = 50 #6-160 defaut 32
camera.annotate_text = "Camera Test"
camera.capture('image.jpg')
camera.stop_preview()





