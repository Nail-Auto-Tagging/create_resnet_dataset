"""
데이터셋을 8:1:1의 비율로 train:test:validation셋으로 나눕니다.
"""

import os
import random
import shutil


Args = {
    "destination_directory": "resnet",
    "source_directory": "categories",
}


def create_directory(directory_name: str):
    try:
        os.mkdir(directory_name)
    except Exception as e:
        print(f"create_directory: {e.__str__()}")
        pass


def get_files_from_directory(directory_name: str):
    try:
        return os.listdir(directory_name)
    except Exception as e:
        print(f"get_files_from_directory: {e.__str__()}")
        return []


def move_file(source: str, destination: str):
    try:
        shutil.move(source, destination)
    except Exception as e:
        print(f"move_file: {e.__str__()}")


if __name__ == "__main__":
    source = Args["source_directory"]
    destination = Args["destination_directory"]

    create_directory(f"{destination}/train")
    create_directory(f"{destination}/test")
    create_directory(f"{destination}/validation")

    label_directories = get_files_from_directory(source)
    for label_directory in label_directories:
        directory_name = f"{source}/{label_directory}"
        cropped_nail_images = get_files_from_directory(directory_name)
        print(directory_name)

        total_len = len(cropped_nail_images)
        test_len = int(total_len * 0.1)
        validation_len = int(total_len * 0.1)

        random.shuffle(cropped_nail_images)

        create_directory(f"{destination}/train/{label_directory}")
        create_directory(f"{destination}/test/{label_directory}")
        create_directory(f"{destination}/validation/{label_directory}")

        for image_file in cropped_nail_images[:test_len]:
            move_file(
                f"{source}/{label_directory}/{image_file}",
                f"{destination}/test/{label_directory}/{image_file}",
            )

        for image_file in cropped_nail_images[test_len : test_len + validation_len]:
            move_file(
                f"{source}/{label_directory}/{image_file}",
                f"{destination}/validation/{label_directory}/{image_file}",
            )

        for image_file in cropped_nail_images[test_len + validation_len :]:
            move_file(
                f"{source}/{label_directory}/{image_file}",
                f"{destination}/train/{label_directory}/{image_file}",
            )
