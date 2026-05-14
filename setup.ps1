# Drehstück CAD — Windows PowerShell setup & run
# Usage: .\setup.ps1

Write-Host "📦  Installing dependencies..." -ForegroundColor Cyan
pip install build123d numpy matplotlib numpy-stl --quiet

Write-Host "🔧  Generating 3D model..." -ForegroundColor Cyan
python drehstuck.py

Write-Host "🖼️   Rendering preview PNG..." -ForegroundColor Cyan
python render_preview.py

Write-Host ""
Write-Host "Done! Files created:" -ForegroundColor Green
Write-Host "  drehstuck.step          <- open in FreeCAD / Fusion 360 / SOLIDWORKS"
Write-Host "  drehstuck.stl           <- for 3D printing or online viewers"
Write-Host "  drehstuck_preview.png   <- quick visual"
