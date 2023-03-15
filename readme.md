# Python PDF Watermarker
Simple python script that adds a watermark to a .pdf file, the watermark text and file are given as inputs. It can handle both landscape and portrait rotation of A4 pages (which the free online tools cannot - hence my motivation to create the script).

Currently adds a red one-line text at the right top corner to all pages.

## Usage
Place the file you want to watermark in the same folder as the script, install the requirements and run the script via:
```
python watermark.py [Watermark text] [filename]
```

Example usage:
```
python watermark.py "CONFIDENTIAL - DO NOT SHARE" secret-doc.pdf
```