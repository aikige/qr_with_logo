#!/usr/bin/env python

import qrcode
from PIL import Image

def encode_qr_with_logo(body, logo_filename, output_filename, transparent=False):
    logo = Image.open(logo_filename)
    logo = logo.resize((60,60)).convert('RGBA')
    qr_output = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr_output.add_data(body)
    qr_output.make()
    img_qr_big = qr_output.make_image().convert('RGBA')
    pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
    if transparent:
        img_qr_big.paste(logo, pos, logo)
    else:
        img_qr_big.paste(logo, pos)
    img_qr_big.save(output_filename)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Create QR code with logo')
    parser.add_argument('-o', '--output-filename', default='output.png')
    parser.add_argument('-l', '--logo-filename', default='logo.png')
    parser.add_argument('-i', '--input-filename', default=None)
    parser.add_argument('-t', '--transparent', action='store_true')
    parser.add_argument('body', nargs='?', default=None)
    opt = parser.parse_args()
    if opt.input_filename:
        with open(opt.input_filename) as f:
            body = f.read()
    else:
        body = opt.body
    if body is None:
        raise RuntimeError('Body should be supplied')
    encode_qr_with_logo(body, opt.logo_filename, opt.output_filename, opt.transparent)

if __name__ == "__main__":
    main()
