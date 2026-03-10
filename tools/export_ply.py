import torch
import numpy as np
import argparse
import os
from plyfile import PlyData, PlyElement


def export_ply(ckpt_path, save_path):
    """
    Converts a 3DGS checkpoint (.pt) to a standard PLY file.
    """
    if not os.path.exists(ckpt_path):
        print(f"❌ Input file not found: {ckpt_path}")
        return

    # Automatically create the output directory
    output_dir = os.path.dirname(save_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    print(f"Loading checkpoint: {ckpt_path}")
    # map_location="cpu" ensures loading works even without a GPU
    ckpt = torch.load(ckpt_path, map_location="cpu")

    # Compatibility check: handle both 'splats' and 'gaussians' keys
    splats = ckpt.get("splats", ckpt.get("gaussians", None))
    if splats is None:
        print("❌ Error: No 'splats' or 'gaussians' field found in checkpoint.")
        return

    # Extract tensors and convert to numpy
    # Using .detach().cpu() to ensure data is moved off the computation graph and GPU
    means = splats["means"].detach().cpu().numpy()
    scales = splats["scales"].detach().cpu().numpy()
    quats = splats["quats"].detach().cpu().numpy()
    opacities = splats["opacities"].detach().cpu().numpy()

    # Extract Zero-order Spherical Harmonics (f_dc) representing base color
    sh0 = splats["sh0"].detach().cpu().numpy().reshape(-1, 3)

    num_verts = means.shape[0]

    # Define standard 3DGS PLY attributes
    # Third-party viewers expect these specific property names
    attrs = [
        "x",
        "y",
        "z",
        "nx",
        "ny",
        "nz",
        "f_dc_0",
        "f_dc_1",
        "f_dc_2",
        "opacity",
        "scale_0",
        "scale_1",
        "scale_2",
        "rot_0",
        "rot_1",
        "rot_2",
        "rot_3",
    ]

    # Create a structured numpy array for PLY data
    vertex_data = np.zeros(num_verts, dtype=[(name, "f4") for name in attrs])

    # Fill the array. Using .flatten() on opacities to ensure (N,) shape compatibility
    vertex_data["x"], vertex_data["y"], vertex_data["z"] = (
        means[:, 0],
        means[:, 1],
        means[:, 2],
    )
    vertex_data["f_dc_0"], vertex_data["f_dc_1"], vertex_data["f_dc_2"] = (
        sh0[:, 0],
        sh0[:, 1],
        sh0[:, 2],
    )
    vertex_data["opacity"] = opacities.flatten()
    vertex_data["scale_0"], vertex_data["scale_1"], vertex_data["scale_2"] = (
        scales[:, 0],
        scales[:, 1],
        scales[:, 2],
    )
    (
        vertex_data["rot_0"],
        vertex_data["rot_1"],
        vertex_data["rot_2"],
        vertex_data["rot_3"],
    ) = (quats[:, 0], quats[:, 1], quats[:, 2], quats[:, 3])
    # nx, ny, nz default to 0 as expected by most Gaussian viewers

    # Describe and write the PLY file
    el = PlyElement.describe(vertex_data, "vertex")
    print(f"Writing {num_verts} Gaussians to: {save_path}")
    PlyData([el]).write(save_path)
    print("✅ Export successful!")


if __name__ == "__main__":
    # Define default paths based on your RGBT-Scenes workspace
    DEFAULT_INPUT = "../examples/results/benchmark/bicycle/ckpts/ckpt_29999_rank0.pt"
    DEFAULT_OUTPUT = "../examples/results/benchmark/bicycle/ply/bicycle_30k.ply"

    parser = argparse.ArgumentParser(
        description="Convert 3DGS .pt checkpoints to .ply format."
    )

    parser.add_argument(
        "-i",
        "--input",
        default=DEFAULT_INPUT,
        help=f"Path to input .pt file (Default: {DEFAULT_INPUT})",
    )

    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Path to output .ply file (Default: {DEFAULT_OUTPUT})",
    )

    args = parser.parse_args()

    # If a custom input is provided but no output, generate output path automatically
    if args.input != DEFAULT_INPUT and args.output == DEFAULT_OUTPUT:
        args.output = os.path.splitext(args.input)[0] + ".ply"

    export_ply(args.input, args.output)
