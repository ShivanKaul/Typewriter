import sys
import os
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import random
# import scipy.ndimage.filters
# import scipy.misc
# import scipy.signal


def generate_image(input_file, output_file,
                   height=700, width=700,
                   blur=False,
                   author_name="",
                   border=True, bordercolor="black", bordersize=2,
                   font_name="KingthingsTrypewriter2", font_size=24):
    # Append author name to piece
    # Another style = '\n\n-'
    accr_style = '\n\n...\n\n'
    by_line = accr_style + author_name + '"' if author_name is not "" else '"'
    text = 'echo "$(cat ' + input_file + ')' + by_line

    # Apply effects
    all_effects = [(blur,
                    " -blur 1x1 "),
                   (border,
                    " -border " + str(bordersize) +
                    " -bordercolor " + bordercolor + " ")]
    effects = reduce(
        lambda effects, (effect, effectString):
        effects + effectString
        if effect else effects, all_effects, "")
    # Do image magic
    dimensions = str(height) + 'x' + str(width)
    imageMagick = ('convert -size ' + dimensions + ' -font ' + font_name +
                   ' -pointsize ' + str(font_size) +
                   effects +
                   ' -gravity center label:@- ' +
                   output_file)
    cmd = text + " | " + imageMagick
    os.system(cmd)


def batch_process(input_folder, output_folder, author):
    # For each file in input_folder, make image in output_folder
    for root, dirnames, filenames in os.walk(input_folder):
            for filename in filenames:
                input_file = input_folder + filename
                output_file = output_folder + 'typewriter_' + filename + '.gif'
                generate_image(input_file, output_file, author_name=author)


def make_vignette(img, output_file):
    vignette = scipy.signal.convolve2d(
        np.ones(img.shape), generate_gaussian(10, 100), mode="same")
    mpimg.imsave(output_file, img*vignette, cmap=plt.get_cmap('gray'))


def make_smudge(img, output_file):
    gradient = np.gradient(img)
    print(gradient)
    new_img = np.zeros(img.shape)
    print(img.shape)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            dx = gradient[0][x, y]
            dy = gradient[1][x, y]
            if (dx > 0.1 or dy > 0.1):
                if(random.random() > 0.7):
                    new_img[x, y] = img[x, y]
                else:
                    new_img[x, y] = 0
            else:
                new_img[x, y] = img[x, y]

    new_img = scipy.ndimage.filters.convolve(
        new_img, generate_gaussian(0.7, 4), mode='nearest')
    mpimg.imsave(output_file, new_img, cmap=plt.get_cmap('gray'))


def generate_gaussian(sigma, N):
    neg = -int(N / 2)
    pos = int(N / 2)

    x_vals = range(neg, pos)
    y_vals = range(neg, pos)

    x, y = np.meshgrid(x_vals, y_vals)
    g = np.exp((-np.power(x, 2) /
                (2 * (pow(sigma, 2)))) - (np.power(y, 2)/(2*(pow(sigma, 2)))))
    g = np.divide(g, np.sum(g))
    return g


if len(sys.argv) < 3:
    print("Format: python typewriter.py input_path output_path author")
    sys.exit()

input_path, output_path = sys.argv[1], sys.argv[2]
author_name = ""
if len(sys.argv) == 4:
    author_name = sys.argv[3]

batch_process(input_path, output_path, author_name)

# Post processing
# img = scipy.misc.imread(output_file) / 255
# make_vignette(img, output_file)
# make_smudge(img, output_file)
