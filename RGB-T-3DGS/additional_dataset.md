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
- paper: Visible-Thermal Tiny Object Detection: A Benchmark Dataset and Baselines(https://arxiv.org/pdf/2406.14482)
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
- DJI_0022_1: 130
- DJI_0024_2: 160
- DJI_0026_2: 440
- DJI_0028_2: 370
- DJI_0028_3: 570
- DJI_0028_4: 590
- DJI_0028_5: 590
- DJI_0030_2: 590
- DJI_0030_9: 590
- DJI_0032_3: 290
- DJI_0032_5: 350
- DJI_0043_2: 380
- DJI_0047_3: 310
- DJI_0049_2: 90
- DJI_0051_2: 580
- DJI_0051_3: 600
- DJI_0057_1: 560
- DJI_0061_2: 240
- DJI_0067_2: 500
- DJI_0069_1: 420
- DJI_0071_2: 590
- DJI_0073_3: 360
- DJI_0075_3: 240
- DJI_0077_2: 360
- DJI_0081_2: 350
- DJI_0083_2: 560
- DJI_0085_2: 320
- DJI_0089_2: 300
- DJI_0095_3: 280
- DJI_0101_2: 120
- DJI_0107_1: 70
- DJI_0109_1: 90
- DJI_0111_2: 180
- DJI_0113_3: 330
- DJI_0115_2: 290
- DJI_0117_2: 240
- DJI_0119_2: 180
- DJI_0121_2: 350
- DJI_0123_6: 310
- DJI_0125_1: 440
- DJI_0127_1: 500
- DJI_0129_2: 590
- DJI_0131_2: 550
- DJI_0133_2: 130
- DJI_0135_1: 260
- DJI_0137_3: 290
- DJI_0139_2: 400
- DJI_0141_2: 410
- DJI_0143_1: 430
- DJI_0145_1: 280
- DJI_0155_2: 410
- DJI_0157_2: 470
- DJI_0159_2: 250
- DJI_0163_1: 470
- DJI_0167_1: 550
- DJI_0169_3: 290
- DJI_0171_2: 400
- DJI_0173_2: 450
- DJI_0175_2: 450
- DJI_0177_2: 360
- DJI_0179_2: 340
- DJI_0181_3: 320
- DJI_0183_2: 350
- DJI_0217_2: 380
- DJI_0221_2: 590
- DJI_0225_1: 329
- DJI_0227_1: 390
- DJI_0229_2: 480
- DJI_0237_2: 410
- DJI_0241_2: 510
- DJI_0243_2: 340
- DJI_0253_1: 1090
- DJI_0253_2: 580
- DJI_0253_3: 520
- DJI_0255_1: 600
- DJI_0257_2: 590
- DJI_0257_5: 260
- DJI_0265_1: 80
- DJI_0271_2: 70
- DJI_0273_1: 1213
- DJI_0273_3: 290
- DJI_0275_3: 449
- DJI_0277_1: 550
- DJI_0277_2: 366
- DJI_0279_2: 386
- DJI_0279_4: 274
- DJI_0283_1: 450
- DJI_0285_3: 182
- DJI_0287_1: 273
- DJI_0287_2: 490
- DJI_0291_2: 153
- DJI_0293_1: 363
- DJI_0295_3: 550
- DJI_0303_2: 577
- DJI_0305_3: 333
- DJI_0305_7: 340
- DJI_0307_1: 250
- DJI_0307_2: 180
- DJI_0309_1: 432
- DJI_0309_2: 598
- DJI_0309_4: 603
- DJI_0317_2: 600
- DJI_0319_2: 598
- DJI_0323_2: 593
- DJI_0325_2: 595
- DJI_0327_3: 390
- DJI_0331_3: 360
- DJI_0337_3: 598
- DJI_0339_2: 600
- DJI_0341_2: 600
- DJI_0341_5: 314
- DJI_0343_3: 591
- DJI_0343_5: 281
- DJI_0345_2: 600
- DJI_0351_2: 200


dataset feature: for each scene, images seem to be captured as different frames in a continuous video. It has both RGB and grayscale images.

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
