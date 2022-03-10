# qr_with_logo

Python code to generate QR code with logo inside.

## Install

Please install this with `pip` command.

```
pip install -e git+https://github.com/aikige/qr_with_logo.git
```

## Synopsis

> **qr_with_logo** \[**-o** *OUTPUT_FILENNAME*\] \[**-l** *LOGO_FILENAME*\] \[**-i** *INPUT_FILENAME*\] \[*BODY*\]

## Description

This is script which can be used to generate QR code with logo image at center of it.

For those who is simply want to generate QR code, please use `qr` command distributed with [qrcode](https://github.com/lincolnloop/python-qrcode) package of Python.

### Options

- *BODY* &mdash; this is string which is converted to the QR code.
- **-o** *OUTPUT_FILENNAME* &mdash; this is option to specify output filename. `output.png` will be used when nothing specified.
- **-l** *LOGO_FILENAME* &mdash; this is used to specify file which contains logo data.
- **-i** *INPUT_FILENAME* &mdash; if `-i` option is set, script reads text from the file and use as contents of QR code.
- **-t** &mdash; when this option is set, transparent part in logo are kept transparent, otherwise black background is used for logo area.

Either of *BODY* or **-i** option shall be set to run this script.
