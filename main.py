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
    counter = 4
    while counter >= 0:
        if merged_png:
            merged_png.paste(imgs_list[counter], (0,0), imgs_list[counter])
            path_to_merged_png = os.path.join( 'mergedPngs', f'{png_name}.png' )
            os.remove(path_to_merged_png)
            merged_png.save(path_to_merged_png)
            merged_png = prepareImg(path_to_merged_png)
        else:
            imgs_list[counter].paste(imgs_list[counter], (0,0), imgs_list[counter])
            path_to_merged_png = os.path.join( 'mergedPngs', f'{png_name}.png' )
            imgs_list[counter].save(path_to_merged_png)
            merged_png = prepareImg(path_to_merged_png)
        counter -= 1

def get_imgs():
    try:
        img1 = os.path.join( os.getcwd(), 'png_path_1', random.choice( os.listdir( os.path.join( os.getcwd(), 'png_path_1' ) ) ) )
        img2 = os.path.join( os.getcwd(), 'png_path_2', random.choice( os.listdir( os.path.join( os.getcwd(), 'png_path_2' ) ) ) )
        img3 = os.path.join( os.getcwd(), 'png_path_3', random.choice( os.listdir( os.path.join( os.getcwd(), 'png_path_3' ) ) ) )
        img4 = os.path.join( os.getcwd(), 'png_path_4', random.choice( os.listdir( os.path.join( os.getcwd(), 'png_path_4' ) ) ) )
        img5 = os.path.join( os.getcwd(), 'png_path_5', random.choice( os.listdir( os.path.join( os.getcwd(), 'png_path_5' ) ) ) )
        return [img1, img2, img3, img4, img5]
    except Exception as err:
        print(f'Some error with getting photos\nErr message: {err}')
        
    

def main():
    print(f'Start work.\nCount of finished imgs: {settings.count_of_works}')
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