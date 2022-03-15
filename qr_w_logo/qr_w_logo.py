#!/usr/bin/env python

import qrcode
from PIL import Image, ImageDraw

def encode_qr_with_logo(body, logo_filename, output_filename, transparent=False, size=0, version=None, bg_color='white', fg_color='black'):
    qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_Q)
    qr.add_data(body)
    qr.make()
    qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color).convert('RGB')
    if size == 0:
        MARGIN_WIDTH = 40   # 4 modules
        size = (qr_image.width - (MARGIN_WIDTH * 2)) // 4
    logo = Image.open(logo_filename).convert('RGBA')
    logo = logo.resize((size,size), resample=Image.LANCZOS)
    pos = ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2)
    if transparent:
        qr_image.paste(logo, pos, logo)
    else:
        logo_w_bg = Image.new('RGB', logo.size, bg_color)
        logo_w_bg.paste(logo, mask=logo)
        qr_image.paste(logo_w_bg, pos)
    qr_image.save(output_filename)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Create QR code with logo')
    parser.add_argument('-o', '--output-filename', default='output.png')
    parser.add_argument('-l', '--logo-filename', default='logo.png')
    parser.add_argument('-i', '--input-filename', default=None)
    parser.add_argument('-t', '--transparent', action='store_true')
    parser.add_argument('-s', '--size', type=int, default=0)
    parser.add_argument('-v', '--version', type=int, default=None)
    parser.add_argument('-b', '--bg-color', default='white')
    parser.add_argument('-f', '--fg-color', default='black')
    parser.add_argument('body', nargs='?', default=None)
    opt = parser.parse_args()
    if opt.input_filename:
        with open(opt.input_filename) as f:
            body = f.read()
    else:
        body = opt.body
    if body is None:
        raise RuntimeError('Body should be supplied')
    encode_qr_with_logo(body, opt.logo_filename, opt.output_filename,
            opt.transparent, opt.size, opt.version, opt.bg_color, opt.fg_color)

if __name__ == "__main__":
    main()
