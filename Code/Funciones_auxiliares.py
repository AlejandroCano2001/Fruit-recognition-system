# Conversion de píxeles a cm
def pixel2cm(ratio, pixels):
    if ratio != 0.0:
        return pixels/ratio
    else:
        return pixels