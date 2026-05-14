"""
Optional: generate a PNG preview using build123d's OCP CAD Viewer or
a simple matplotlib 3D wireframe from the STL.

Requires: pip install numpy matplotlib numpy-stl
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh as stl_mesh

STL_FILE = "drehstuck.stl"

def render_stl(path: str, output_png: str = "drehstuck_preview.png"):
    m = stl_mesh.Mesh.from_file(path)
    fig = plt.figure(figsize=(10, 8), facecolor="#1a1a2e")
    ax  = fig.add_subplot(111, projection="3d", facecolor="#1a1a2e")

    verts = m.vectors
    poly  = Poly3DCollection(verts, alpha=0.85,
                             facecolor="#c0922a",   # brass-ish
                             edgecolor="#8a6010",
                             linewidth=0.2)
    ax.add_collection3d(poly)

    scale = m.points.flatten()
    ax.auto_scale_xyz(scale, scale, scale)

    ax.set_xlabel("X", color="white")
    ax.set_ylabel("Y", color="white")
    ax.set_zlabel("Z", color="white")
    ax.tick_params(colors="white")
    ax.set_title("Drehstück 246370 — build123d preview",
                 color="white", fontsize=13, pad=12)

    plt.tight_layout()
    plt.savefig(output_png, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print(f"✅  Preview saved: {output_png}")
    plt.close()

if __name__ == "__main__":
    render_stl(STL_FILE)
