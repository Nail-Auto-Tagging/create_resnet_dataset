"""
1. 네일아트의 카테고리 클래스를 폴더명으로 하는 폴더들을 여러개 생성합니다.
    EX) 
    * 1_glitter - 글리터네일은 1번 클래스
    * 2_french - 프렌치네일은 2번 클래스

2. 네일아트가 있는 손톱 이미지 파일들을 각각의 클래스에 해당하는 폴더로 분류합니다.
3. 각각의 클래스 폴더를 source_directory로 하여 손톱 이미지들은 S3에 저장, 손톱 데이터들은 DB에 저장합니다.
"""

import os
from typing import List
from lib.db import DB
from lib.aws import upload_image_to_s3


Args = {
    "source_directory": "categories/1_glitter",
    "s3_prefix": "nailedit/cropped_nails",
    "collection": "categories",
}
db = DB(Args["collection"])


if __name__ == "__main__":
    try:
        # list all files in source directory
        cropped_nail_image_files: List[str] = os.listdir(Args["source_directory"])
        cropped_nail_label: int = int(Args["source_directory"].split("/")[-1].split("_")[0])

        for cropped_nail_image_file in cropped_nail_image_files:
            s3_path = f"{Args['s3_prefix']}/{cropped_nail_image_file}"
            local_path = f"{Args['source_directory']}/{cropped_nail_image_file}"

            # upload local image to s3
            image = upload_image_to_s3(local_path, s3_path)

            # get cropped_id & nail_id from filename
            cropped_id = cropped_nail_image_file.split(".jpg")[0]
            nail_id = cropped_id.split("(")[0]

            # insert cropped nail data to db
            db.upsert_document(
                {
                    "cropped_id": cropped_id,
                },
                {
                    "$set": {
                        "nail_id": nail_id,
                        "cropped_id": cropped_id,
                        "image": image,
                        "categories": [cropped_nail_label],
                        "is_tagged": True,
                        "is_pass": False,
                        "member": "김민선",
                    }
                },
            )
            print(cropped_id)
    except Exception as e:
        print(e.__str__())
