import numpy as np
import matplotlib.pyplot as plt

# данные: несколько повторных измерений для каждой группы
groups = {"A": [4.8, 5.1, 5.0, 4.7, 5.3],
          "B": [5.9, 6.3, 6.1, 5.8, 6.4],
          "C": [7.2, 6.8, 7.5, 7.0, 7.1]}

fig, ax = plt.subplots(figsize=(5, 4))
for i, (name, y) in enumerate(groups.items()):
    y = np.array(y)
    mean = y.mean()
    sd = y.std(ddof=1)            # ddof=1 — выборочное СКО (n-1)
    sem = sd / np.sqrt(len(y))    # ошибка среднего

    # отдельные измерения с небольшим разбросом по x
    ax.scatter(np.random.normal(i, 0.04, len(y)), y,
               color="gray", alpha=0.6, s=20, zorder=2)
    # среднее ± SD (широкие планки)
    ax.errorbar(i, mean, yerr=sd, fmt="o", color="C0",
                capsize=6, lw=1.5, zorder=3, label="среднее ± SD" if i == 0 else "")
    # среднее ± SEM (узкие планки поверх)
    ax.errorbar(i, mean, yerr=sem, fmt="none", ecolor="C3",
                capsize=3, lw=3, zorder=4, label="± SEM" if i == 0 else "")

ax.set_xticks(range(len(groups)), groups.keys())
ax.set_ylabel("Величина, ед.")
ax.legend()
plt.tight_layout()
plt.show()
