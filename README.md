# save-cropped-nails
1. Source Directory에 존재하는 이미지 파일들을 S3에 업로드하고 DB에 저장합니다.
2. Source Directory에 라벨링된 이미지 파일들을 8:1:1의 비율로 train:test:validation 셋으로 분할합니다

## Clone repository
```shell
git clone https://github.com/Nail-Auto-Tagging/create_resnet_dataset
cd create_resnet_dataset
```

## Install packages
```shell
pip install -r requirements.txt
```

## Change arguments
```main.py```의 Args 수정
```divide_dataset.py```의 Args 수정

## Run code
```shell
python main.py
```

## 참고사항
* 현재 cropped_nails collection에는 cropped_id에 대해 unique한 index를 걸어둔 상태입니다.
* 따라서 DB로 insert하려는 cropped_id가 이미 DB 상에 존재할 경우, 새로 insert되지 않고 기존의 것이 유지됩니다. (기존 데이터의 태깅 정보를 overwrite 못하게 하기 위함) 

