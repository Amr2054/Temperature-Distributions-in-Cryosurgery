# Modeling Temperature Distributions in Cryosurgery 🧊🔥

This project explores the numerical solution of the heat equation applied to **cryosurgery temperature modeling**, using three numerical methods and one machine learning approach.

---

## 📚 Table of Contents

- [🔍 Project Overview](#-project-overview)
- [📂 Solving Methods](#-solving-methods)
- [📊 Error Comparison](#-error-comparison)
- [📝 Project Report](#-project-report)
- [📜 License](#-license)

---

## 🔍 Project Overview

Cryosurgery is a minimally invasive medical technique that destroys unwanted or diseased tissues by exposing them to extremely low temperatures, often achieved using liquid nitrogen or argon gas. Accurate prediction of the temperature distribution during cryosurgery is crucial for effective treatment planning and avoiding damage to surrounding healthy tissue.

This project aims to model and solve the **bio-heat transfer equation** (heat equation with perfusion and metabolic terms) that governs the temperature evolution in biological tissues during cryosurgery. The core challenge lies in solving this partial differential equation (PDE) efficiently and accurately under varying boundary and initial conditions, which mimic the freezing process in realistic tissue environments.

---

## 📂 Solving Methods

| 🧪 Method                            | 🌿 Branch                                                                                                       |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Method of Lines (MOL)                | [`mol-method`](https://github.com/Amr2054/Temperature-Distributions-in-Cryosurgery/tree/MOL?tab=readme-ov-file) |
| Alternating Direction Implicit (ADI) | [`adi-method`](https://github.com/Amr2054/Temperature-Distributions-in-Cryosurgery/blob/ADI)                    |
| Finite Volume Method (FVM)           | [`fvm-method`](https://github.com/Amr2054/Temperature-Distributions-in-Cryosurgery/blob/FV)                     |
| Machine Learning (ML) Prediction     | [`ml-model`](https://github.com/Amr2054/Temperature-Distributions-in-Cryosurgery/tree/ML?tab=readme-ov-file)    |

Each method is implemented and analyzed individually, with a focus on comparing their accuracy, computational performance, and applicability to real-world cryosurgical scenarios. The results are visualized through temperature plots and error analyses to offer insights into how each method performs under identical physical parameters.

---

## 📊 Error Comparison

This table compares the error metrics between different solution methods under the same initial and boundary conditions.

| ⚙️ Method | 📈 MAE  | 📈 Max Error (°C) | 📉 Execution time(seconds) |
| --------- | ------- | ----------------- | -------------------------- |
| MOL       | -       | -                 | 0.1599                     |
| ADI       | 0.3627  | 16.8947           | 8.99                       |
| FVM       | 0.679   | 27.4366           | 0.3091                     |
| ML Model  | 0.51088 | 15.3535           | 0.22                       |

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

## 📜 License

Released under the MIT License.
