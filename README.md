# RAW2FITS
Just another tool to convert consumer digital cameras RAW images to FITS.

Designed for speed (<1s per 50MB image).

Made for the Desert Fireball Network data processing pipeline.


## Functionalities
- Decode RAW files (Nikon NEF, Canon CR2, Sony ARW...)
- Various De-Bayering options
- add FITS keywords both from EXIF and external config file


## Requirements
### dcraw
Available with package manager:
`sudo` `apt | zypper | yum` `install dcraw`

Or compile latest version from: https://www.cybercom.net/~dcoffin/dcraw/ (useful for new cameras)


### rawpy (optional)
Faster than dcraw
`pip3 install rawpy`


### stiff (optional)
To convert images to nicely scaled TIFFs
https://www.astromatic.net/software/stiff
