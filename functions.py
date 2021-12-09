import os
import shutil

folder = f'C:\\Users\\nais5\\Desktop\\generator'


def unarchive(path):  # path - путь до архива
    # with zipfile.ZipFile(path, 'r') as zip_file:
    #     folder = 'Исходники\\Sources'
    #     zip_file.extractall(folder)
    # os.remove('Sources\\source.zip')

    foundation = folder + '\\Sources\\source\\foundation.png'
    backgrounds = folder + '\\Sources\\source\\backgrounds'
    skins = folder + '\\Sources\\source\\skins'
    clothes = folder + '\\Sources\\source\\clothes'
    haircuts = folder + '\\Sources\\source\\haircuts'
    faces = folder + '\\Sources\\source\\faces'

    output = folder + '\\Output'

    return foundation, backgrounds, skins, clothes, haircuts, faces, output


def archiver(f):
    os.chdir(folder + '\\Output\\')
    # архивируем каталог
    shutil.make_archive(f, 'zip', folder + f'\\Output\\{f}')
    # удаляем каталог
    shutil.rmtree(folder + f'\\Output\\{f}')
    # удаляем исходники
    shutil.rmtree(folder + f'\\Sources\\source')
