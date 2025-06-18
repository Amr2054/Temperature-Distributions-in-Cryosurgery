import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

r_c = 5.0
z_c = 10.0
z_p = 5.0
t_end = 120.0

T_o = 37.0
T_p = -196.0

t_min, t_max = 0, t_end
r_min, r_max = 0, r_c
z_min, z_max = 0, z_c


class PINN(nn.Module):
    def __init__(self):
        super(PINN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, 1),
        )

    def forward(self, t, r, z):
        t_norm = 2 * (t - t_min) / (t_max - t_min) - 1
        r_norm = 2 * (r - r_min) / (r_max - r_min) - 1
        z_norm = 2 * (z - z_min) / (z_max - z_min) - 1

        X = torch.cat([t_norm, r_norm, z_norm], dim=1)
        return self.net(X)


model = PINN().to(device)

model_weights_path = "model_weights_40000_5.0450_.pth"

if device.type == "cpu":
    model.load_state_dict(
        torch.load(
            model_weights_path, weights_only=True, map_location=torch.device("cpu")
        )
    )
else:
    model.load_state_dict(torch.load(model_weights_path, weights_only=True))


def predict_temp(t, r, z):
    t_eval = torch.tensor([[t]], dtype=torch.float32).to(device)
    r_eval = torch.tensor([[r]], dtype=torch.float32).to(device)
    z_eval = torch.tensor([[z]], dtype=torch.float32).to(device)

    model.eval()
    with torch.no_grad():
        temperature_at_point = model(t_eval, r_eval, z_eval)

    return temperature_at_point.item()


def plot_temperature_distribution(model, t):
    print("Visualizing temperature distribution...")
    model.eval()

    if not os.path.exists("pinn_results"):
        os.makedirs("pinn_results")

    vis_times = [i for i in t]

    r = np.linspace(r_min, r_max, 100)
    z = np.linspace(z_min, z_max, 100)
    R, Z = np.meshgrid(r, z)

    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(2, 2, figure=fig, wspace=0.4, hspace=0.3)

    with torch.no_grad():
        for i, t_val in enumerate(vis_times):
            ax = fig.add_subplot(gs[i // 2, i % 2])

            t_slice = torch.full_like(torch.from_numpy(R.flatten()).float(), t_val)
            r_slice = torch.from_numpy(R.flatten()).float()
            z_slice = torch.from_numpy(Z.flatten()).float()

            t_tensor = t_slice.unsqueeze(1).to(device)
            r_tensor = r_slice.unsqueeze(1).to(device)
            z_tensor = z_slice.unsqueeze(1).to(device)

            T_pred = model(t_tensor, r_tensor, z_tensor).cpu().numpy()
            T_grid = T_pred.reshape(R.shape)

            c = ax.pcolormesh(
                R, Z, T_grid, cmap="jet", shading="auto", vmin=T_p, vmax=T_o
            )
            fig.colorbar(c, ax=ax)
            ax.set_title(f"Temperature Distribution at t = {t_val:.2f} s")
            ax.set_xlabel("Radius (r)")
            ax.set_ylabel("Height (z)")
            ax.plot(
                0,
                z_p,
                "r*",
                markersize=12,
                markeredgecolor="white",
                label=f"T={T_p}°C constraint",
            )
            ax.legend()
            ax.set_aspect("equal", "box")

    plt.savefig("pinn_results/temperature_distribution.png", dpi=300)
    plt.show()


def parse_numbers(input_str):
    return [int(num.strip()) for num in input_str.split(",")]


def grid_input():
    times = input(
        "Enter the times at which you'd like to visualize the temperature distribution, separated by commas (e.g., 0, 30, 60):"
    )
    return parse_numbers(times)


while True:
    mode = int(
        input(
            "select one of the following options:\n(1) single point prediction – predict the temperature at a specific time and location (t, r, z).\n(2) slice/grid visualization – visualize the temperature distribution across a spatial slice at selected times.\n"
        )
    )

    if mode == 1:
        t = int(input("time: "))
        r = int(input("r: "))
        z = int(input("z: "))

        print(predict_temp(t=t, r=r, z=z))
    elif mode == 2:
        plot_temperature_distribution(model, grid_input())
    else:
        print("Please choose option (1) or (2)")
        continue

    break
