#!/usr/bin/env bash
# Drehstück CAD — one-shot setup & run
# Usage: bash setup.sh

set -e

echo "📦  Installing dependencies..."
pip install build123d numpy matplotlib numpy-stl --quiet

echo "🔧  Generating 3D model..."
python drehstuck.py

echo "🖼️   Rendering preview PNG..."
python render_preview.py

echo ""
echo "Done! Files created:"
echo "  drehstuck.step          ← open in FreeCAD / Fusion 360 / SOLIDWORKS"
echo "  drehstuck.stl           ← for 3D printing or online viewers"
echo "  drehstuck_preview.png   ← quick visual"
