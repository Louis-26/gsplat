# thermal/RGB image pair datasets selected

1. 
dataset: VT5000
source: 
- paper: RGBT Salient Object Detection: A Large-scale
Dataset and Benchmark(https://arxiv.org/pdf/2007.03262)
- code: https://github.com/lz118/RGBT-Salient-Object-Detection

2. 
dataset: NTR
source: 
- paper: NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics(https://arxiv.org/pdf/2503.03115)
- code: https://github.com/NPU-CVPG/NTR-Gaussian


3. 
dataset: TI-NSD(Thermal Infrared Novelview Synthesis Dataset )
source: 
- paper: Thermal3D-GS: Physics-induced 3D Gaussians for Thermal Infrared Novel-view Synthesis(https://arxiv.org/pdf/2409.08042)
- code: https://github.com/mzzcdf/Thermal3DGS

# set up dataset
step 1: prepare dataset architecture
```bash
cd $(git rev-parse --show-toplevel)
mkdir -p RGB-T-dataset
grep -qxF "/RGB-T-dataset/" .gitignore || echo "/RGB-T-dataset/" >> .gitignore 

```

step 2: download dataset
download VT5000 here: 
```text
link: https://1024terabox.com/s/1YYhBiPhUrKmbMNeiscgfMw 

Password:12s9
```
then move it to RGB-T-dataset

```bash
unzip VT5000.zip 
```
