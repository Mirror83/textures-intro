from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageOps, ImageEnhance


def create_mask():
    circular_mask = Image.new(mode="L", size=(200, 200))
    draw = ImageDraw.Draw(circular_mask)
    draw.ellipse((0, 0) + circular_mask.size, fill=255)

    return circular_mask


def image_overlay(img: Image, color=(0, 255, 0), alpha=0.2) -> Image:
    overlay = Image.new(img.mode, img.size, color)
    bw_img = ImageEnhance.Color(img).enhance(0.0)
    return Image.blend(bw_img, overlay, alpha)


def crop_image(img: Image, img_mask: Image) -> Image:
    cropped = ImageOps.fit(img, img_mask.size, centering=(0.5, 0.5))
    cropped.putalpha(img_mask)
    return cropped


def main():
    window = Tk()
    window.title("Pillow + Tkinter Circular Image")

    space_launch_image = Image.open("../textures/launch.bmp")

    mask = create_mask()
    image_tinted = image_overlay(space_launch_image)
    cropped_image = crop_image(image_tinted, mask)

    image_tk = ImageTk.PhotoImage(cropped_image)

    canvas_size = (500, 500)
    canvas = Canvas(window, width=canvas_size[0], height=canvas_size[1])

    canvas.pack()
    canvas.create_image(canvas_size[0] // 2, canvas_size[1] // 2, image=image_tk)

    window.mainloop()


if __name__ == "__main__":
    main()
