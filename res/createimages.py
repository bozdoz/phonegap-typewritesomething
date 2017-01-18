import os, subprocess

from PIL import Image

realpath = os.path.dirname(os.path.realpath(__file__))

svg_file = os.path.join(realpath, 'tws.svg')

icon_android = './icon/android/'
icon_ios = './icon/ios/'
screen_android = './screen/android/'
screen_ios = './screen/ios/'

def replaceIcons (the_dir) :

    os.chdir(the_dir)

    for filename in os.listdir('.'):
        image_file = Image.open(filename)
        size = 'x'.join([str(a) for a in image_file.size])
        subprocess.call(['convert', 
            '-density', '300', 
            '-size', size, 
            '-background', 'none', 
            svg_file, 
            '-resize', size, 
            filename])

    os.chdir(realpath)

def replaceScreen (the_dir) :
    # needs padding
    os.chdir(the_dir)

    for filename in os.listdir('.'):
        image_file = Image.open(filename)
        width, height = image_file.size
        size = '%dx%d' % image_file.size
        icon_size = '%dx%d' % (
            int(width*0.6),
            int(height*0.6),
            )
        filename = filename.replace('drawable', 'tws')
        filename = filename.replace('Default', 'tws')

        subprocess.call(['convert', 
            '-density', '300', 
            '-resize', icon_size, 
            '-extent', size, 
            '-gravity', 'center', 
            '-background', '#f6f3e3', 
            svg_file, 
            filename])

    os.chdir(realpath)

print 'SVG file : %s' % svg_file

# replaceIcons(icon_android)
# replaceIcons(icon_ios)
# replaceScreen(screen_android)
# replaceScreen(screen_ios)

print 'If nothing happened make sure you have an svg in the same directory, and uncomment function calls above'