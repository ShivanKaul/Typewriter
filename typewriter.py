import sys
import os
# import scipy.ndimage.filters
# import scipy.misc
# import scipy.signal
# from effects import apply_hefe
# from PIL import Image


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
    # List of (effect name (as argument to function) and its parameters)
    all_effects = [(blur,
                    " -blur 1x1 "),
                   (border,
                    " -border " + str(bordersize) +
                    " -bordercolor " + bordercolor + " ")]
    # Reduce above list to text
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


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Format: python typewriter.py input_text_file output_image [author]")
        sys.exit()
    input_file, output_file = sys.argv[1], sys.argv[2]
    if not output_file.endswith('.gif'):
        # Crash and burn
        print("Output file must be .gif!")
        sys.exit()
    author_name = ""
    if len(sys.argv) == 4:
        author_name = sys.argv[3]
        generate_image(input_file, output_file, author_name=author_name)

# Post processing
# Can be many different formats.

# img = scipy.misc.imread(output_file) / 255
# apply_hefe(output_file, output_file)
