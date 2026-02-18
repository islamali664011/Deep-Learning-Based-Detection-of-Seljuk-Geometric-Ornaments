## TO split the data into Train and val, Test 
import os
import random
import shutil
from pathlib import Path
import yaml


def split_dataset(
        base_dir="/content/SeljukDetection",
        train_ratio=0.7,
        val_ratio=0.15,
        seed=42
    ):

    random.seed(seed)

    base_dir = Path(base_dir)
    images_all = base_dir / "images_all"
    labels_all = base_dir / "labels_all"

    assert images_all.exists(), "images_all folder not found"
    assert labels_all.exists(), "labels_all folder not found"

    # Create split folders
    for split in ["train", "val", "test"]:
        (base_dir / split / "images").mkdir(parents=True, exist_ok=True)
        (base_dir / split / "labels").mkdir(parents=True, exist_ok=True)

    all_images = list(images_all.glob("*"))
    random.shuffle(all_images)

    train_end = int(len(all_images) * train_ratio)
    val_end   = int(len(all_images) * (train_ratio + val_ratio))

    train_imgs = all_images[:train_end]
    val_imgs   = all_images[train_end:val_end]
    test_imgs  = all_images[val_end:]

    def copy_split(img_list, split_name):
        for img_path in img_list:
            label_path = labels_all / f"{img_path.stem}.txt"

            shutil.copy(img_path, base_dir / split_name / "images")
            shutil.copy(label_path, base_dir / split_name / "labels")

    copy_split(train_imgs, "train")
    copy_split(val_imgs, "val")
    copy_split(test_imgs, "test")

    print(" Dataset Splitting Completed")
    print(f"Train: {len(train_imgs)} images")
    print(f"Val:   {len(val_imgs)} images")
    print(f"Test:  {len(test_imgs)} images")

    return train_imgs, val_imgs, test_imgs
