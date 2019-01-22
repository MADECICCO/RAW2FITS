# RAW2FITS
Just another tool to convert consumer digital cameras RAW images to FITS.

Maintained by [Hadrien Devillepoix](https://github.com/hdevillepoix)

Designed for speed (<1s per 50MB image).

Made for the Desert Fireball Network data processing pipeline.

Tested on Linux with Python 3.


## Functionalities
- Decode RAW files (Nikon NEF, Canon CR2, Sony ARW...)
- Various de-Bayering options
- add FITS keywords both from EXIF and external config file


## Requirements
### dcraw
Available with package manager:
`sudo [ apt | zypper | yum ] install dcraw`

Or compile latest version from: https://www.cybercom.net/~dcoffin/dcraw/ (useful for new cameras)


### rawpy (optional)
Faster than dcraw
`pip install rawpy`


### stiff (optional)
To convert images to nicely scaled TIFFs
https://www.astromatic.net/software/stiff

## How to use
### Command line
 - Single file: `python fitsConversion.py -i /path/to/file.raw`
 - Whole directory: `python fitsConversion.py -d /path/to/folder/containg/raw/files`
 - Check all the options: `python fitsConversion.py -h`

### Use as a library
`import fitsConversion`
 - `fitsConversion.raw2fits()` for decoding
 - `fitsConversion.de_Bayer()` for de-Bayering
 
