import os
import random

from PIL import Image

import functions

foundation, backgrounds, skins, clothes, haircuts, faces, output = functions.unarchive('Sources\\source.zip')

# Смена текущий директории на указанную в backgrounds
os.chdir(backgrounds)
# Список файлов в директории с деталями
my_list_backgrounds = os.listdir()

# Количество файлов в директории с деталями
amount_files_backgrounds = len((os.listdir()))

# ---------------------------------------------------------------------------------------------------------------------

# Смена текущий директории на указанную в skins
os.chdir(skins)

# Список файлов в директории с деталями
my_list_skins = os.listdir()

# Количество файлов в директории с деталями
amount_files_skins = len((os.listdir()))

# ---------------------------------------------------------------------------------------------------------------------

# Смена текущий директории на указанную в clothes
os.chdir(clothes)

# Список файлов в директории с деталями
my_list_clothes = os.listdir()

# Количество файлов в директории с деталями
amount_files_clothes = len((os.listdir()))

# ---------------------------------------------------------------------------------------------------------------------

# Смена текущий директории на указанную в haircuts
os.chdir(haircuts)

# Список файлов в директории с деталями
my_list_haircuts = os.listdir()

# Количество файлов в директории с деталями
amount_files_haircuts = len((os.listdir()))

# ---------------------------------------------------------------------------------------------------------------------

# Смена текущий директории на указанную в faces
os.chdir(faces)

# Список файлов в директории с деталями
my_list_faces = os.listdir()

# Количество файлов в директории с деталями
amount_files_faces = len((os.listdir()))

# ---------------------------------------------------------------------------------------------------------------------

try:
    folder_name = str(random.randint(1, 100))
    os.mkdir(f"{output}\\{folder_name}")
except FileExistsError:
    folder_name = str(random.randint(1, 100))
    os.mkdir(f"{output}\\{folder_name}")

for b in range(amount_files_backgrounds):
    os.chdir(backgrounds)

    main_img = Image.open(foundation)

    img_list_backgrounds = Image.open(my_list_backgrounds[b])

    img_list_backgrounds.paste(main_img, (0, 0), main_img)

    # img_list_backgrounds.save(f"{third}\{folder_name}\фон {b}.png")

    for k in range(amount_files_skins):
        os.chdir(skins)
        # main_img = Image.open(first)

        zero_img = img_list_backgrounds.copy()

        img_list_skins = Image.open(my_list_skins[k])

        zero_img.paste(img_list_skins, (0, 0), img_list_skins)

        # main_img.save(f"{third}\{folder_name}\кожа {k}.png")

        for j in range(amount_files_faces):
            os.chdir(faces)

            foundation_img = zero_img.copy()

            img_list_face = Image.open(my_list_faces[j])

            foundation_img.paste(img_list_face, (0, 0), img_list_face)

            # first_img.save(f"{third}\{folder_name}\кожа {k}, лицо {j}.png")

            for i in range(amount_files_haircuts):
                os.chdir(haircuts)

                second_img = foundation_img.copy()

                img_list_haircuts = Image.open(my_list_haircuts[i])

                second_img.paste(img_list_haircuts, (0, 0), img_list_haircuts)

                second_img.save(f"{output}\\{folder_name}\\фон {b}, кожа {k}, прическа {i}, лицо {j}.png")

                for h in range(amount_files_clothes):
                    os.chdir(clothes)

                    third_img = second_img.copy()
                    img_list_clothes = Image.open(my_list_clothes[h])

                    third_img.paste(img_list_clothes, (0, 0), img_list_clothes)

                    third_img.save(
                        f"{output}\\{folder_name}\\фон {b}, кожа {k}, прическа {i}, лицо {j}, одежда {h}.png")

functions.archiver(folder_name)
