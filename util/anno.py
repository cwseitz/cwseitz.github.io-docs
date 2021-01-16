from exif import Image as _Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from glob import glob

def get_exif(file):
	
	f = open(file, 'rb')
	b = _Image(f)
	b.datetime = b.datetime.split(' ')[0]

	str = f'Camera: {b.model}\nTimestamp: {b.datetime}\n'
	str += f'Size: {(b.pixel_x_dimension, b.pixel_y_dimension)}\n'
	str += f'Lens: Tamron 16-300mm\nF-stop: {b.f_number}\n'
	str += f'Exposure: {b.exposure_time*1e3}ms\n'
	str += f'Focal Length: {b.focal_length}mm\nDepth: 32-bit RGB'
	f.close()

	return str

def anno_exif(file, str, box_size=(600,400), out_file=None):

	"""Annotates EXIF parameters onto image"""

	if not out_file:
		out_file=file

	img = Image.open(file)
	width, height = img.size
	rect_width, rect_height = box_size

	font = ImageFont.truetype('assets/arial.ttf', 50)
	draw = ImageDraw.Draw(img)
	draw.rectangle((width-rect_width, height-rect_height, width, height), fill='black')
	draw.text((width-rect_width,height-rect_height),str,(255,255,255), font=font)

	img.save(out_file)


str = 'photos/*.jpg'
files = glob(str)
for file in files:
	exif = get_exif(file)
	anno_exif(file, exif)
