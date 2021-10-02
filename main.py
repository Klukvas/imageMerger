from posix import listdir
from posixpath import join
from PIL import Image
import settings
import os
import random
from datetime import datetime

def prepareImg(img_path):
    width = settings.width
    height = settings.height
    img1 = Image.open(img_path).resize((width, height), Image.ANTIALIAS)
    return img1

def mergeImg(imgs_list):
    merged_png = None
    png_name = datetime.strftime( datetime.today(), '%m%d%Y%H%M%S%f' )
    for i in range(1, len(imgs_list)):
        if merged_png:
            merged_png.paste(imgs_list[i], (0,0), imgs_list[i])
            path_to_merged_png = os.path.join( 'mergedPngs', f'{png_name}.png' )
            os.remove(path_to_merged_png)
            merged_png.save(path_to_merged_png)
            merged_png = prepareImg(path_to_merged_png)
        else:
            imgs_list[0].paste(imgs_list[i], (0,0), imgs_list[i])
            path_to_merged_png = os.path.join( 'mergedPngs', f'{png_name}.png' )
            imgs_list[0].save(path_to_merged_png)
            merged_png = prepareImg(path_to_merged_png)


def get_imgs():
    random_img_paths = []
    img_paths = [  os.path.join(os.getcwd(), folder, path)
        for folder in [ os.path.join( os.getcwd(), item ) for item in os.listdir() if 'png_path' in item ] 
        for path in os.listdir(folder)
    ]
    if settings.count_photos_to_merge > len(img_paths):
        print(f'Count o images to merge in setting( {settings.count_photos_to_merge} ) more that count of images in folders( {len(img_paths)} )')
        return None
    elif settings.count_photos_to_merge == len(img_paths):
        return img_paths
    else:
        for _ in range(settings.count_photos_to_merge):
            rnd_img_ph = random.choice( img_paths )
            random_img_paths.append( rnd_img_ph )
            img_paths.remove(rnd_img_ph)
        return random_img_paths

def main():
    print(f'Start work.\nCount of imgs to merge: {settings.count_photos_to_merge}\nCount of finished imgs: {settings.count_of_works}')
    for _ in range(settings.count_of_works):
        imgs = []
        img_paths = get_imgs()
        if img_paths:
            for path in img_paths:
                imgs.append(prepareImg(path))
            mergeImg(imgs)
    print(f'Work finished')



if __name__ == '__main__':
    main()