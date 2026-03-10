# Requirement
1. set up AMD, with link: https://github.com/ROCm/gsplat
2. count the number of RGB/thermal images in each dataset
3. add thermal images into SLAM reconstruction, see this: https://arxiv.org/abs/2506.06517
Take a look at reference paper, ThermalGaussian: Thermal 3D Splatting, [here](https://arxiv.org/html/2409.07200v1)
4. calibrate thermal camera, (whether the code exists), they will have different locations
5. compare with paper rendering results, see this: , any new techniques?

# Goal
In building detection/drone area, better 3D reconstruction with thermal and RGB images 

# Finished Work
## 1. set up AMD GPU server for gsplat❌
not able to finish it at this stage, as I haven't got assigned to the AMD GPU server

## 2. count the detailed architecture/number of RGB/thermal images in each dataset✅
- complement the dataset detail [here](../RGB-T-3DGS/additional_dataset.md)

## 3. add thermal images into SLAM reconstruction✅
- finish reading the [lab paper](https://arxiv.org/pdf/2506.06517)
- complete google slide for paper understanding(**SLAM**) and **thermal image integration** [here](https://docs.google.com/presentation/d/1k45Gwcyut-r5YxXbYAklH2huWawtFqc5dWa1mV5fYB4/edit?usp=sharing)

## 4&5. calibrate thermal camera and results analysis✅
- finish reading the [reference paper](https://arxiv.org/pdf/2409.07200)
- complete google slide for paper summary and **thermal camera calibration** [here](https://docs.google.com/presentation/d/1QQflCvNscf5a_RWNQV67Pe6kxKePz0vxd8gPLl5S4I8/edit?usp=sharing)
- results comparison between ThermalGaussian paper and gsplat package benchmark experiment have been documented [here](../RGB-T-3DGS/RGBT-Scenes/result_comparison.md)

# question & request
## paper
1. no definition for $\mathcal{L}_{seg}$ in GS4 paper   
## other
1. still not able to visualize .ply files, with cloudcompare installed
2. visitor form still not received
3. follow up with gpu server

# potential next step
1. reproduce ThermalGaussian paper results(containing the thermal camera calibration code, might need gpu)