import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

regions = pd.read_csv("Dataset.csv")


def clean_name(region):
    return re.sub(r"[^\w\s-]", "", region)


# Remove unwanted special characters from oblast column values
regions["Oblast"] = regions["Oblast"].apply(clean_name)
# Remove duplicates
regions.drop_duplicates(subset="Oblast", inplace=True)
# Replace missing values in livelihood score column with 0
regions.fillna(0, inplace=True)
# Order from highest to lowest
regions.sort_values("Livelihood_Score", ascending=False, inplace=True)
# Set conditional equation to a new column and call it "Severity"
# If score is >75 then High, if >49 & <76 then Medium, if <50 then Low
conditions = [
    (regions["Livelihood_Score"] > 75),
    (regions["Livelihood_Score"] > 49) & (regions["Livelihood_Score"] <= 75),
    (regions["Livelihood_Score"] <= 49),
]
choices = ["High", "Medium", "Low"]

# Use np.select to create the new column
regions["Severity"] = np.select(conditions, choices, default="Low")

# Visualize the scores by oblast using bar chart or scatter plot
sns.set(style="whitegrid")

palette = {
    "High": "#d73027",  # Dark red
    "Medium": "#fc8d59",  # Orange
    "Low": "#91bfdb",  # Light blue
}

plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(
    data=regions,
    x="Oblast",
    y="Livelihood_Score",
    hue="Severity",
    hue_order=["High", "Medium", "Low"],
    palette=palette,
)

# excluding oblasts with 0 and adding labels
exclude_oblasts = ["Zakarpatska", "Odeska", "Chernivetska", "Vinnytska"]
for p, label in zip(bar_plot.patches, regions["Oblast"]):
    if label not in exclude_oblasts:
        bar_plot.annotate(
            format(p.get_height(), ".1f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 9),
            textcoords="offset points",
        )

bar_plot.set_title("Livelihood Score by Oblast")
bar_plot.set_xlabel("Oblast")
bar_plot.set_ylabel("Livelihood Score")
bar_plot.legend(title="Severity")
bar_plot.grid(True, axis="y", linestyle="--")

sns.despine()

plt.xticks(rotation=45, ha="right")

plt.tight_layout()
# plt.savefig("Livelihood_score.jpg")
plt.show()
