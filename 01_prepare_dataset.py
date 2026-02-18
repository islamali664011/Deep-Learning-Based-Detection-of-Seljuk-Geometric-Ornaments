## code to Download the data from drive to colab or Visual studio code App.
## clean the data "images and labels" 
## combine between the images in Iran and Anatolina
## establish YAML code 
import os
import shutil
import yaml
from google.colab import drive


def mount_drive():
    drive.mount('/content/drive')


def copy_and_clean(src_folder, dst_folder):
    os.makedirs(dst_folder, exist_ok=True)
    for f in os.listdir(src_folder):
        shutil.copy(os.path.join(src_folder, f), dst_folder)
    return set(os.listdir(dst_folder))


def clean_pairs(images_set, labels_set, images_folder, labels_folder):
    valid_images = {f for f in images_set if os.path.splitext(f)[0] in {os.path.splitext(l)[0] for l in labels_set}}
    valid_labels = {l for l in labels_set if os.path.splitext(l)[0] in {os.path.splitext(f)[0] for f in images_set}}

    for f in images_set - valid_images:
        os.remove(os.path.join(images_folder, f))
    for l in labels_set - valid_labels:
        os.remove(os.path.join(labels_folder, l))

    return valid_images, valid_labels


def prepare_dataset():
    mount_drive()

    drive_base = '/content/drive/MyDrive/CrackModel/Seljuk1_Project/'
    colab_base = '/content/SeljukDetection/'
    os.makedirs(colab_base, exist_ok=True)

    folders = {
        "images_antolina": "Seljuk_detection_images_antolina",
        "labels_antolina": "Seljuk_detection_labels_antolina",
        "images_iran": "Seljuk_detection_images_in_iran",
        "labels_iran": "Seljuk_detection_labels_in_iran"
    }

    images_antolina = copy_and_clean(
        os.path.join(drive_base, folders["images_antolina"]),
        os.path.join(colab_base, "images_antolina")
    )
    labels_antolina = copy_and_clean(
        os.path.join(drive_base, folders["labels_antolina"]),
        os.path.join(colab_base, "labels_antolina")
    )

    images_iran = copy_and_clean(
        os.path.join(drive_base, folders["images_iran"]),
        os.path.join(colab_base, "images_iran")
    )
    labels_iran = copy_and_clean(
        os.path.join(drive_base, folders["labels_iran"]),
        os.path.join(colab_base, "labels_iran")
    )

    images_antolina, labels_antolina = clean_pairs(
        images_antolina, labels_antolina,
        os.path.join(colab_base, "images_antolina"),
        os.path.join(colab_base, "labels_antolina")
    )

    images_iran, labels_iran = clean_pairs(
        images_iran, labels_iran,
        os.path.join(colab_base, "images_iran"),
        os.path.join(colab_base, "labels_iran")
    )

    final_images = os.path.join(colab_base, "images_all")
    final_labels = os.path.join(colab_base, "labels_all")

    os.makedirs(final_images, exist_ok=True)
    os.makedirs(final_labels, exist_ok=True)

    for img in images_antolina.union(images_iran):
        src = os.path.join(colab_base, "images_antolina" if img in images_antolina else "images_iran", img)
        shutil.copy(src, final_images)

    for lbl in labels_antolina.union(labels_iran):
        src = os.path.join(colab_base, "labels_antolina" if lbl in labels_antolina else "labels_iran", lbl)
        shutil.copy(src, final_labels)

    data_yaml = {
        'train': final_images,
        'val': final_images,
        'nc': 1,
        'names': ['seljuk_shape']
    }

    yaml_path = os.path.join(colab_base, 'seljuk_data.yaml')
    with open(yaml_path, 'w') as f:
        yaml.dump(data_yaml, f)

    print(" Dataset prepared successfully")
    print("Images:", len(os.listdir(final_images)))
    print("Labels:", len(os.listdir(final_labels)))
    print("YAML:", yaml_path)


if __name__ == "__main__":
    prepare_dataset()
