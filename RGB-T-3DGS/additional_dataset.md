# thermal/RGB image pair datasets selected
⭐1. dataset: RGBT-Scenes

source: 
- paper: ThermalGaussian: Thermal 3D Gaussian Splatting
(https://arxiv.org/pdf/2409.07200)
- code: https://github.com/chen-hangyu/Thermal-Gaussian-main
- download link: https://drive.google.com/drive/folders/1A6kdIjDe7kw-iKQkzjHNw0wgk_3V7hcp

✅2. dataset: VT5000

source: 
- paper: RGBT Salient Object Detection: A Large-scale
Dataset and Benchmark(https://arxiv.org/pdf/2007.03262)
- code: https://github.com/lz118/RGBT-Salient-Object-Detection
- download link: https://pan.baidu.com/s/196S1GcnI56Vn6fLO3oXb5Q [y9jj]

✅3. dataset: NTR

source: 
- paper: NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics(https://arxiv.org/pdf/2503.03115)
- code: https://github.com/NPU-CVPG/NTR-Gaussian
- download link: https://drive.usercontent.google.com/download?id=17evbWmeZKgVeXseyVv7fNm-2Q_a17ObB&export=download&authuser=0

✅4. dataset: TI-NSD(Thermal Infrared Novelview Synthesis Dataset)

source: 
- paper: Thermal3D-GS: Physics-induced 3D Gaussians for Thermal Infrared Novel-view Synthesis(https://arxiv.org/pdf/2409.08042)
- code: https://github.com/mzzcdf/Thermal3DGS
- download link: https://drive.google.com/drive/folders/1scp7-dB0BVE84ra8KkgQ7z9zLk5yCPFH

✅5. dataset: RGBT-Tiny

source:
- paper: Visible-Thermal Tiny Object Detection: A Benchmark Dataset and Baselines(https://arxiv.org/abs/2406.14482)
- code: https://github.com/XinyiYing/RGBT-Tiny
- download link: https://pan.baidu.com/s/1IVwZglXdkSTqmC1llPXG2w?pwd=h2t2

https://github.com/xuqingyu26/HGTMT

❌6. dataset: ViVID++

source:
- paper: https://arxiv.org/pdf/2204.06183
- download link: https://urserver.kaist.ac.kr/publicdata/ViViD++/download_links.txt
I have difficulty downloading this dataset.

# storage location
The dataset directory is [here](../RGB-T-dataset)

# dataset architecture

## RGBT-Scenes
```bash
cd $(git rev-parse --show-toplevel)
jupyter nbconvert --to notebook --execute --inplace tools/count_dataset.ipynb
```

This is a dataset with 10 scenes, RGB and thermal paired dataset with identical sample size

- Building: 273 images(238 train, 35 test)
- DailyStuff: 78 images(68 train, 10 test)
- Dimsum: 154 images(134 train, 20 test)
- Ebike: 48 images(42 train, 6 test)
- IronIngot: 61 images(53 train, 8 test)
- LandScape: 103 images(90 train, 13 test)
- Parterre: 66 images(57 train, 9 test)
- RoadBlock: 71 images(62 train, 9 test)
- RotaryKiln: 106 images(92 train, 14 test)
- Truck: 73 images(64 train, 9 test)

data feature: for each scene, all images are captured from the same location with different perspectives

## VT5000
This is a dataset with random object images.

- Train: 2500 RGB-Thermal image pairs
- Test: 2500 RGB-Thermal image pairs

data feature: all images don't seem to relevant to each other

## NTR
This is a dataset with two urban scenes primarily characterized by buildings and roads (S1, S2), and two suburban scenes dominated by farmland and ponds (S3, S4).

- S1: 1003 images (466 train, 537 test)
- S2: 951 images (475 train, 476 test)
- S3: 586 images (293 train, 293 test)
- S4: 592 images (485 train, 107 test)

data feature: We only have thermal images here with 4 scenes.


## TI-NSD
This is a dataset with 20 objects.

- UAV1: 343
- UAV2: 543
- UAV3: 375
- UAV4: 84
- UAV5: 109
- UAV6: 132
- apples: 167
- basketball_court: 189
- bicycle: 203
- bridge: 92
- car: 216
- chair: 704
- corridor: 110
- heated: 315
- merge: 314
- sitting: 134
- soccer_goal: 250
- standing: 318
- tall_building: 88
- wall: 200

data feature: We only have thermal images for each object, without train/test split.

## RGBT-Tiny    
This is a huge dataset with 115 different scenes.



# set up dataset
step 1: prepare dataset architecture
```bash
cd $(git rev-parse --show-toplevel)
mkdir -p RGB-T-dataset
grep -qxF "/RGB-T-dataset/" .gitignore || echo "/RGB-T-dataset/" >> .gitignore 

```

step 2: download dataset
download RGBT-Scenes here: 
```text
link: https://1024terabox.com/s/1YYhBiPhUrKmbMNeiscgfMw 

Password:12s9
```
then move it to RGB-T-dataset

```bash
unzip RGBT-scenes.zip 
```
