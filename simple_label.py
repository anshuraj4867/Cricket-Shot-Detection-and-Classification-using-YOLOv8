import cv2
import os

image_folder = "images"
label_folder = "labels"

os.makedirs(label_folder, exist_ok=True)

images = os.listdir(image_folder)

for img_name in images:
    img_path = os.path.join(image_folder, img_name)
    img = cv2.imread(img_path)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    print(f"\nImage: {img_name}")
    print("Press:")
    print("1 → cover_drive")
    print("2 → pull_shot")
    print("3 → defensive_shot")
    print("s → skip")

    key = cv2.waitKey(0)

    if key == ord('1'):
        label = 0
    elif key == ord('2'):
        label = 1
    elif key == ord('3'):
        label = 2
    else:
        continue

    h, w, _ = img.shape

    # full image box (simple)
    x_center = 0.5
    y_center = 0.5
    bw = 1.0
    bh = 1.0

    with open(os.path.join(label_folder, img_name.replace(".jpg", ".txt")), "w") as f:
        f.write(f"{label} {x_center} {y_center} {bw} {bh}")

    cv2.destroyAllWindows()

print("DONE")