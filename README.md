# Typewriter

Generate pretty images of text, thusly:

```
Magic is dead.

It lives like a refugee, in
the spaces between your fingers:

for times when you forget
that your lips are just sensors, and
the thrill down my spine
when you kiss me
is just my brain snorting
information.
```

generates:

![Magic](/generated_images/typewriter_magic.gif?raw=true "Poem, Magic") 

### Setup

The Typewriter script uses ImageMagick (NOT the Python library, the script simply calls the CLI) for basic functionality and also `scipy`/`numpy`/`matplotlib` for further optional image processing. I installed the [Kingthings font](http://www.dafont.com/kingthings-trypewriter.font), but you can use any (script defaults to Kingthings). 

For setting up on Mac (like I did), you need to first install [ImageMagick](https://www.imagemagick.org/) using something like [Homebrew](http://brew.sh/). You can then follow this [StackOverflow answer](https://stackoverflow.com/questions/24696433/why-font-list-is-empty-for-imagemagick). 

Apart from that, if not doing any fancy stuff like Gaussian blurring or smudging (the functions to do so are provided but not used in the script), all you need is Python (2.7). Else, you'll have to run `pip install -r requirements.txt` to get `scipy`/`numpy`/`matplotlib`. 

### Usage

`$ python typewriter.py input_path output_path author_name`

The script assumes that all the text files are in the folder specified in input_path, and then it generates the image with the name "typewriter_original-filename" in folder specified by output_path. The main work is done by the `generate_image()` function in the `typewriter.py` script. Modify that if things don't work / don't work for you.

Author name is optional parameter. Different accreditation styles can be tweaked in `generate_image()`.
 
