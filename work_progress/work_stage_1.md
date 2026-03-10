# Requirement

Thermal splatting survey and gsplat package.

Work:

1) Setup gsplat package: https://github.com/nerfstudio-project/gsplat
2) Find some good thermal/RGB image pair datasets from the literature survey, and then try to use gsplat to optimize the rendering of both RGB and thermal images.

# Finished Work
## 0. get temporary GPU cluster✅
get GPU cluster temporarily, but no long-term, need steady GPU cluster resource for later work

## 1. setup gsplat package✅
The environment configuration and installation steps are documented [here](../env_config.md). 

The benchmark experiment has been executed successfully, and the results are documented [here](../evaluation_result.md)



## 2. find thermal/RGB image pair datasets✅
Based on [refined literature summary](../literature_survey/summary.md), `RGBT-Scenes` dataset has been prioritized for the thermal/RGB image pair rendering task, as documented [here](../RGB-T-3DGS/additional_dataset.md), and the dataset has been downloaded and stored [here](../RGB-T-dataset/)


## 3. get rendering result for RGB-Scenes dataset✅
As RGB-Scenes dataset is the only one with both RGB and thermal images, with multiple views(similar to gsplat package demo), I try to render this dataset first.

Detailed rendering procedure is documented [here](../RGB-T-3DGS/RGBT-Scenes/RGB-T-render.md).

Meanwhile, the execution details and rendering result are [here](../RGB-T-3DGS/RGBT-Scenes/evaluation_result.md).

## 4. get .ply files for visualization✅
For visualization purpose, .ply files are generated given .pt, by the [tool_script](../tools/export_ply.py), output to `../examples/results/benchmark/$Scene/ply`
and `../examples/results/RGBT-Scenes/rgb/$Scene/ply`, `../examples/results/RGBT-Scenes/thermal/$Scene/ply` respectively.
```bash
cd $(git rev-parse --show-toplevel)
bash tools/generate_all_ply.sh
```

In contrast, --save_ply is enabled to produce .ply files as well, and the corresponding .ply files are output to the same directory as the checkpoint, e.g., `../examples/new_results/benchmark/$Scene/ckpts/$Checkpoint/ply`, `../examples/new_results/RGBT-Scenes/rgb/$Scene/ckpts/$Checkpoint/ply` and `../examples/new_results/RGBT-Scenes/thermal/$Scene/ckpts/$Checkpoint/ply` respectively.


# question
- .ply visualization tool(no usable for >200 MB .ply files), CloudCompare software
- how to check .ply files make sense or not, just a 3D visualization


# request
- stable GPU cluster - AMD GPU 
- OPT first year agreement support - voluntary work