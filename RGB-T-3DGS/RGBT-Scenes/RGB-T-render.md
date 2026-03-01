# procedure to perform 3DGS rendering on RGB-Scenes dataset
step 1: set up the dataset
```bash
cd $(git rev-parse --show-toplevel)/RGB-T-dataset
unzip RGBT-Scenes.zip -d $(git rev-parse --show-toplevel)/examples/data
```

step 2: data preprocessing
```bash
for SCENE in Building DailyStuff Dimsum Ebike IronIngot LandScape Parterre RoadBlock RotaryKiln Truck; do \
  for TYPE in rgb thermal; do \
    cd $(git rev-parse --show-toplevel)/examples/data/RGBT-Scenes/$SCENE/$TYPE && mkdir -p all && cp train/*.jpg all/ && cp test/*.jpg all/; \
  done; \
done
```

## RGB
```bash
cd $(git rev-parse --show-toplevel)/examples
bash benchmarks/RGB-thermal/RGBT-Scenes_rgb_3DGS.sh
bash benchmarks/RGB-thermal/RGBT-Scenes_thermal_3DGS.sh
```

in SLURM
```bash
cd $(git rev-parse --show-toplevel)/SLURM_execution/SLURM_script
sbatch RGBT_Scenes_experiment_rgb_script.sh
```

## Thermal
```bash
cd $(git rev-parse --show-toplevel)/examples
bash benchmarks/RGB-thermal/RGBT-Scenes_thermal_3DGS.sh
```

in SLURM
```bash
cd $(git rev-parse --show-toplevel)/SLURM_execution/SLURM_script
sbatch RGBT_Scenes_experiment_thermal_script.sh
```