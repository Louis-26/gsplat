# Benchmark 
cd $(git rev-parse --show-toplevel)

for s in bicycle bonsai counter garden kitchen room stump; do
    mkdir -p "examples/results/benchmark/$s/ply"    
    python tools/export_ply.py \
        --input "examples/results/benchmark/$s/ckpts/ckpt_29999_rank0.pt" \
        --output "examples/results/benchmark/$s/ply/${s}_30k.ply"
done


# RGBT-Scenes
SCENES="Building DailyStuff Dimsum Ebike IronIngot LandScape Parterre RoadBlock RotaryKiln Truck"

# RGB
for s in $SCENES; do
  mkdir -p examples/results/RGBT-Scenes/rgb/$s/ply
  python tools/export_ply.py \
    --input examples/results/RGBT-Scenes/rgb/$s/ckpts/ckpt_29999_rank0.pt \
    --output examples/results/RGBT-Scenes/rgb/$s/ply/${s}_30k.ply
done

# Thermal
for s in $SCENES; do
  mkdir -p examples/results/RGBT-Scenes/thermal/$s/ply
  python tools/export_ply.py \
    --input examples/results/RGBT-Scenes/thermal/$s/ckpts/ckpt_29999_rank0.pt \
    --output examples/results/RGBT-Scenes/thermal/$s/ply/${s}_30k.ply
done