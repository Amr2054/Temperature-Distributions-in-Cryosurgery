# 🧊🔥 Modeling Temperature Distributions in Cryosurgery

This project explores the numerical solution of the heat equation applied to **cryosurgery temperature modeling**, using three numerical methods and one machine learning approach.

---

## 📚 Table of Contents

- [🔍 Project Overview](#-project-overview)
- [📂 Solving Methods](#-solving-methods)
- [📊 Error Comparison](#-error-comparison)
- [📝 Project Report](#-project-report)
- [🧠 Author](#-author)
- [📜 License](#-license)

---

## 🔍 Project Overview

Cryosurgery is a minimally invasive medical technique that destroys unwanted or diseased tissues by exposing them to extremely low temperatures, often achieved using liquid nitrogen or argon gas. Accurate prediction of the temperature distribution during cryosurgery is crucial for effective treatment planning and avoiding damage to surrounding healthy tissue.

This project aims to model and solve the **bio-heat transfer equation** (heat equation with perfusion and metabolic terms) that governs the temperature evolution in biological tissues during cryosurgery. The core challenge lies in solving this partial differential equation (PDE) efficiently and accurately under varying boundary and initial conditions, which mimic the freezing process in realistic tissue environments.

---

## 📂 Solving Methods

| 🧪 Method                            | 🌿 Branch                                                            |
| ------------------------------------ | -------------------------------------------------------------------- |
| Method of Lines (MOL)                | [`mol-method`](https://github.com/yourusername/repo/tree/mol-method) |
| Alternating Direction Implicit (ADI) | [`adi-method`](https://github.com/yourusername/repo/tree/adi-method) |
| Finite Volume Method (FVM)           | [`fvm-method`](https://github.com/yourusername/repo/tree/fvm-method) |
| Machine Learning (ML) Prediction     | [`ml-model`](https://github.com/yourusername/repo/tree/ml-model)     |

Each method is implemented and analyzed individually, with a focus on comparing their accuracy, computational performance, and applicability to real-world cryosurgical scenarios. The results are visualized through temperature plots and error analyses to offer insights into how each method performs under identical physical parameters.

---

## 📊 Error Comparison

This table compares the error metrics (e.g., L2 norm or maximum absolute error) between different solution methods under the same initial and boundary conditions.

| ⚙️ Method | 📈 Max Error (°C) | 📉 Mean Error (°C) |
| --------- | ----------------- | ------------------ |
| MOL       | 2.13              | 1.04               |
| ADI       | 1.67              | 0.89               |
| FVM       | 1.90              | 0.96               |
| ML Model  | 2.45              | 1.12               |

📁 Raw data available in [`error_comparison.csv`](./results_overview/error_comparison.csv)

📊 [Optional: View Error Plot](./results_overview/error_plot.png)

---

## 📝 Project Report

The full report explains the motivation, mathematical modeling, numerical methods, implementation details, and result interpretation.

📄 [Download Project Report (PDF)](./Report/Cryosurgery_Report.pdf)

The report includes:

- ✅ Problem formulation and governing equations
- 🔁 Details of ADI, FVM, MOL, and ML approaches
- 🧠 Implementation highlights
- 📊 Performance comparison and discussion
- 🔮 Conclusions and future improvements

---

## 🧠 Author

**Amr Ahmed**  
🔗 [LinkedIn](#) | 🐦 [Twitter](#)

---

## 📜 License

Released under the MIT License.
