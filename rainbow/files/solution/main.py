from PIL import Image

size = (800,800)

def dec_to_bin(rvb):
    nr, nv, nb = bin(rvb[0])[2:], bin(rvb[1])[2:], bin(rvb[2])[2:]
    return "0" * (8 - len(nr)) + nr, "0" * (8 - len(nv)) + nv, "0" * (8 - len(nb)) + nb


def to_xor(r2, r1):
    xor = bin((int(r2, 2)) ^ (int(r1, 2)))[2:]
    return "0" * (4 - len(xor)) + xor


def hide_me(img1, img2):
    new_img = Image.new('RGB', size, "black")
    pixels = new_img.load()
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r1, v1, b1 = dec_to_bin(img1.getpixel((i, j)))
            r2, v2, b2 = dec_to_bin(img2.getpixel((i, j)))
            r1 = r1[:4] + to_xor(r2[4:], r1[:4])
            v1 = v1[:4] + to_xor(v2[4:], v1[:4])
            b1 = b1[:4] + to_xor(b2[4:], b1[:4])

            pixels[i, j] = (int(r1, 2), int(v1, 2), int(b1, 2))
    new_img.save("rainbow.png")
    return new_img


def show_me(img):
    new_img = Image.new('RGB', size, "black")
    pixels = new_img.load()
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r1, v1, b1 = dec_to_bin(img.getpixel((i, j)))

            r1 = r1[4:] + to_xor(r1[:4], r1[4:])
            v1 = v1[4:] + to_xor(v1[:4], v1[4:])
            b1 = b1[4:] + to_xor(v1[:4], v1[4:])

            pixels[i, j] = (int(r1, 2), int(v1, 2), int(b1, 2))
    new_img.save("reveal.png")


mimg1 = Image.open("prism.png")
mimg2 = Image.open("code.png")

ahoe = hide_me(mimg1, mimg2)
show_me(ahoe)
