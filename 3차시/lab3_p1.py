#imprt a math function
import math

#Get user's UAB size
USB_size_GB = int(input('Enter USB size (GB): '))

#Convert GB to byte
USB_size = USB_size_GB * 1000000000

#Define GIF, JPEG,  PNG, TIFF
GIF_size = math.floor((600*800*1)/5)
JPEG_size = math.floor((600*800*3)/25)
PNG_size = math.floor((600*800*3)/8)
TIFF_size = math.floor(600*800*6)
print('')

#output reslut
print(format(math.floor(USB_size/GIF_size), '>5'),'images in GIF format can be stored')
print(format(math.floor(USB_size/JPEG_size), '>5'),'images in JPEG format can be stored')
print(format(math.floor(USB_size/PNG_size), '>5') ,'images in PNG format can be stored')
print(format(math.floor(USB_size/TIFF_size), '>5'), 'images in TIFF format can be stored')
