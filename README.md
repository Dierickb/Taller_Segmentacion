
# 🧠 Taller de Segmentación Médica en Imágenes 3D

Este repositorio contiene una serie de filtros y algoritmos para la segmentación de imágenes médicas 3D, utilizando **ITK**, **SimpleITK**, **VTK** y herramientas de visualización en Python.

---

## 📁 Estructura del Proyecto

```
Taller_Segmentacion/
├── lib/
│   └── python3/
│       └── PIM_T3/
│           ├── Filter/
│           │   ├── Base.py
│           │   ├── BinaryThresholding.py
│           │   ├── FastMarchingImageFilter.py
│           │   ├── OtsuThresholding.py
│           │   ├── WaterSheed.py
│           │   └── ClusterPixelesGrayScale.py
│           ├── Helpers.py
│           └── __init__.py
├── examples/
│   ├── code/
│   │   ├── binary_thresholding_cli.py
│   │   ├── fast_marching_cli.py
│   │   ├── otsu_thresholding_cli.py
│   │   └── watersheed_cli.py
│   └── images/
│       ├── OriginalImages/
│       └── (salidas organizadas por filtro)
└── FastMachingImageFilter/
    └── *.nii
```

---

## 🚀 Ejecución desde Línea de Comandos (CLI)

### 🔹 Binary Thresholding

```bash
python examples/code/binary_thresholding_cli.py \
  examples/images/OriginalImages/sample.nii.gz \
  50 \
  150 \
  0 \
  255
```

### 🔹 Fast Marching + Sigmoide + Threshold

```bash
python examples/code/fast_marching_cli.py \
  examples/images/OriginalImages/sample.nii.gz \
  1.0 \
  120 120 45 \
  100.0 \
  30.0 \
  --auto_sigmoid \
  --printing
```

### 🔹 Otsu Thresholding

```bash
python examples/code/otsu_thresholding_cli.py \
  examples/images/OriginalImages/sample.nii.gz \
  64 \
  3 \
  10
```

### 🔹 Watershed

```bash
python examples/code/watersheed_cli.py \
  examples/images/OriginalImages/sample.nii.gz \
  0.001 \
  0.2
```

### 🔹 K-Means Sintético + Visualización

```bash
python lib/python3/PIM_T3/Filter/ClusterPixelesGrayScale.py
```

---

## 🧪 Ejemplos de Uso por Script

### BinaryThresholding

```python
from PIM_T3.Filter import BinaryThresholding
binary = BinaryThresholding.BinaryThresholding(
    input_image_path="examples/images/OriginalImages/sample.nii.gz",
    file_executed="BinaryThresholding.py",
    lower_threshold=50,
    upper_threshold=150,
    outside_value=0,
    inside_value=255
)
binary.threshold_image()
```

### FastMarchingImageFilter

```python
from PIM_T3.Filter import FastMarchingImageFilter
fast = FastMarchingImageFilter.FastMarchingImageFilter(
    input_image_path="examples/images/OriginalImages/sample.nii.gz",
    file_executed="FastMarchingImageFilter.py",
    sigma=1.0,
    alpha_sigmoid=None,
    beta_sigmoid=None,
    x_position=120,
    y_position=120,
    z_position=45,
    stop=100.0,
    time_threshold=30.0,
    auto_sigmoid=True,
    printing=True
)
fast.fast_marching_image()
```

### OtsuThresholding

```python
from PIM_T3.Filter import OtsuThresholding
otsu = OtsuThresholding.OtsuThresholding(
    input_image_path="examples/images/OriginalImages/sample.nii.gz",
    file_executed="OtsuThresholding.py",
    num_bins=64,
    num_thresholds=3,
    label_offset=10
)
otsu.otsu_threshold_image()
```

### Watershed

```python
from PIM_T3.Filter import WaterSheed
watershed = WaterSheed.WaterSheed(
    input_image_path="examples/images/OriginalImages/sample.nii.gz",
    file_executed="WaterSheed.py",
    threshold=0.001,
    level=0.2
)
watershed.watershed_image()
```

### K-Means Visualizador

```python
from PIM_T3.Filter import ClusterPixelesGrayScale
visualizer = ClusterPixelesGrayScale.KMeansSegmentationVisualizer()
visualizer.apply_kmeans()
visualizer.show_matplotlib()
visualizer.show_vtk()
```

---

## ⚙️ Requisitos

```bash
pip install itk SimpleITK vtk matplotlib numpy
```

---

## 📄 Licencia

MIT License
