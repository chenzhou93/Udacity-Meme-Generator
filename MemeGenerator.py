from PIL import Image, ImageDraw, ImageFont

class MemeGenerator():
    """Meme Generator entrance"""
    def __init__(self, output_dir) -> None:
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Add meme to an image"""
        img = Image.open(img_path)
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/Font/Arial Unicode.ttf', 24)

        # Choose the position
        image_width, image_height = img.size
        text_content = text + ' - ' + author
        left, top, right, bottom = draw.textbbox((0,0),text_content, font=font)
        text_width = right - left
        text_height = bottom - top

        text_position = ((image_width - text_width) // 2, (image_height - text_height) // 2)

        # Add text to the image
        draw.text(text_position, text_content)

        # Save the modified image
        #print('output_dir: ' + self.output_dir)
        self.output_dir = self.output_dir + '/output.jpg'
        img.save(self.output_dir)

        return self.output_dir
        