import os
import shutil

# Define source and target directories for each object
objects = [
    "bicycle",
    "bonsai",
    "counter",
    "garden",
    "kitchen",
    "room",
    "stump"
]

base_source_dir = "/brtx/605-nvme2/ylu174/research/gsplat/examples/results/benchmark"
base_target_dir = "/brtx/605-nvme2/ylu174/research/gsplat/render_result/original_example"

for obj in objects:
    source_dir = os.path.join(base_source_dir, obj, "videos")
    target_dir = os.path.join(base_target_dir, obj)

    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Copy all video files from source to target
    for file_name in os.listdir(source_dir):
        if file_name.endswith(".mp4"):  # Ensure only video files are copied
            full_source_path = os.path.join(source_dir, file_name)
            full_target_path = os.path.join(target_dir, file_name)
            shutil.copy(full_source_path, full_target_path)
            print(f"Copied {file_name} to {target_dir}")