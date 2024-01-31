from PIL import Image
import os

# 元の画像ファイル名と出力ファイル名
def detect_files(directory):
    "count amounts of correct files in input folder"
    return [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name)) and name.endswith('.png')]


for file_name in detect_files('input'):
    # magnification
    scale_factor = 20 # multiply by 20

    # open the images
    image = Image.open(f'input/{file_name}')

    # magnify the images with nearest-neighbor
    new_width = image.width * scale_factor
    new_height = image.height * scale_factor
    resized_image = image.resize((new_width, new_height), Image.NEAREST)

    # save the magnified image
    resized_image.save(f'output/_{file_name}.png')


# show the image（if needed）
# resized_image.show()
