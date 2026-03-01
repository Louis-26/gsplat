import os
import shutil
import argparse


def main():
    # 1. Initialize the argument parser
    parser = argparse.ArgumentParser(description="Batch copy gsplat render results.")

    # 2. Define path arguments with your current defaults
    parser.add_argument(
        "--src",
        type=str,
        default="/brtx/605-nvme2/ylu174/research/gsplat/examples/results/RGBT-Scenes",
        help="Base source directory containing object folders.",
    )

    parser.add_argument(
        "--tgt",
        type=str,
        default="/brtx/605-nvme2/ylu174/research/gsplat/render_result/RGBT-Scenes",
        help="Base target directory where videos will be stored.",
    )

    # 3. Define the list of objects (scenes) to process
    parser.add_argument(
        "--objects",
        nargs="+",
        default=[
            "Building",
            "DailyStuff",
            "Dimsum",
            "Ebike",
            "IronIngot",
            "LandScape",
            "Parterre",
            "RoadBlock",
            "RotaryKiln",
            "Truck",
        ],
        help="List of scene names to process.",
    )
    
    parser.add_argument(
        "--image_type",
        type=str,
        default="rgb",
        help="rgb or thermal",
    )

    args = parser.parse_args()

    # 4. Execution logic
    for obj in args.objects:
        # Assuming the standard gsplat output structure: src/obj/videos/
        source_dir = os.path.join(args.src, args.image_type, obj, "videos")
        target_dir = os.path.join(args.tgt, args.image_type, obj)

        if not os.path.exists(source_dir):
            print(f"Skipping {obj}: Source directory not found at {source_dir}")
            continue

        os.makedirs(target_dir, exist_ok=True)

        copied_count = 0
        for file_name in os.listdir(source_dir):
            if file_name.endswith(".mp4"):
                full_source_path = os.path.join(source_dir, file_name)
                full_target_path = os.path.join(target_dir, file_name)

                shutil.copy(full_source_path, full_target_path)
                copied_count += 1

        if copied_count > 0:
            print(
                f"Successfully copied {copied_count} videos for '{obj}' to {target_dir}"
            )
        else:
            print(f"No .mp4 files found in {source_dir}")


if __name__ == "__main__":
    main()
