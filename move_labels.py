import os
import shutil

# paths
train_images = "dataset/images/train"
val_images = "dataset/images/val"

labels_folder = "labels"
train_labels = "dataset/labels/train"
val_labels = "dataset/labels/val"

os.makedirs(train_labels, exist_ok=True)
os.makedirs(val_labels, exist_ok=True)

# move train labels
for img in os.listdir(train_images):
    label_name = img.replace(".jpg", ".txt")
    src = os.path.join(labels_folder, label_name)
    dst = os.path.join(train_labels, label_name)

    if os.path.exists(src):
        shutil.move(src, dst)

# move val labels
for img in os.listdir(val_images):
    label_name = img.replace(".jpg", ".txt")
    src = os.path.join(labels_folder, label_name)
    dst = os.path.join(val_labels, label_name)

    if os.path.exists(src):
        shutil.move(src, dst)

print("DONE")