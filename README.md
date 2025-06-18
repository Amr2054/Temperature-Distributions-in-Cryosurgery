# 🔄 ADI Method

This branch contains the implementation of the **Alternating Direction Implicit (ADI)** method for modeling temperature distribution in tissue during cryosurgery.

## 📌 Method Overview

The ADI method is a finite difference technique optimized for solving two-dimensional parabolic PDEs like the heat equation. It alternates the direction of implicitness in r and z at each half time-step, leading to better stability and faster computation for 2D problems.

## ▶️ Run the Code

You can view and run the ADI notebook on Google Colab here:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xR2b5yx1x2lQzJp84Jn3cQBnALhDRGVt?usp=sharing)

## 📊 Results

The following visualizations illustrate how the temperature evolves over time in the tissue during cryosurgery, modeled using the ADI method.

### 🖼️ 2D Temperature Plots

These 2D contour plots show how the freezing region expands over time(t:30,60,90,120), r(r:0-5), z(z:0-10).

#### 🔹 Automatic scaling of the vertical axis by matplot

![Auto Scale](./results/ADI%202d%20auto.jpg)

#### 🔹 Fixed Scaling of the vertical axis (-200,0)

![Step 10](./results/ADI%202d%20fixed.jpg)

---

### 🧊 3D Surface Plots

The 3D plots below provide a depth perspective of how the temperature profile evolves through the tissue layers over time(t:30,60,90,120), r(r:0-5), z(z:0-10).

![3D](./results/ADI%203d.jpg)

>

---
