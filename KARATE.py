import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# KARATE STUDENT PERFORMANCE ANALYSIS
# ==========================================


# Student Data
data = {
    "Name": [
        "Arun",
        "Priya",
        "Kumar",
        "Divya",
        "Rahul",
        "Vijay",
        "Meena",
        "Karthik"
    ],

    "Belt": [
        "White",
        "Yellow",
        "Orange",
        "Green",
        "Blue",
        "Yellow",
        "Green",
        "Orange"
    ],

    "Attendance": [
        92, 88, 95, 90, 85, 94, 91, 87
    ],

    "Kata": [
        85, 78, 92, 88, 75, 90, 95, 82
    ],

    "Kumite": [
        88, 82, 90, 85, 80, 92, 89, 84
    ],

    "Fitness": [
        90, 85, 94, 88, 78, 95, 92, 86
    ]
}


# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(data)


# ==========================================
# PERFORMANCE CATEGORIES
# ==========================================

performance = [
    "Kata",
    "Kumite",
    "Fitness"
]


# ==========================================
# TOTAL SCORE
# ==========================================

df["Total"] = np.sum(
    df[performance],
    axis=1
)


# ==========================================
# AVERAGE SCORE
# ==========================================

df["Average"] = np.mean(
    df[performance],
    axis=1
)


# ==========================================
# PERFORMANCE LEVEL
# ==========================================

df["Performance"] = np.where(
    df["Average"] >= 90,
    "Excellent",
    np.where(
        df["Average"] >= 80,
        "Good",
        "Needs Improvement"
    )
)


# ==========================================
# DISPLAY STUDENT DATA
# ==========================================

print("\n==========================================")
print("     KARATE STUDENT PERFORMANCE ANALYSIS")
print("==========================================")

print("\n===== STUDENT DETAILS =====")

print(df.to_string(index=False))


# ==========================================
# TOP PERFORMER
# ==========================================

top_student = df.loc[
    df["Average"].idxmax()
]

print("\n===== TOP PERFORMER =====")

print("Name        :", top_student["Name"])
print("Belt        :", top_student["Belt"])
print("Total       :", top_student["Total"])
print("Average     :", round(top_student["Average"], 2))
print("Performance :", top_student["Performance"])


# ==========================================
# BEST KATA PERFORMER
# ==========================================

best_kata = df.loc[
    df["Kata"].idxmax()
]

print("\n===== BEST KATA PERFORMER =====")

print("Name :", best_kata["Name"])
print("Score:", best_kata["Kata"])


# ==========================================
# BEST KUMITE PERFORMER
# ==========================================

best_kumite = df.loc[
    df["Kumite"].idxmax()
]

print("\n===== BEST KUMITE PERFORMER =====")

print("Name :", best_kumite["Name"])
print("Score:", best_kumite["Kumite"])


# ==========================================
# BEST FITNESS PERFORMER
# ==========================================

best_fitness = df.loc[
    df["Fitness"].idxmax()
]

print("\n===== BEST FITNESS PERFORMER =====")

print("Name :", best_fitness["Name"])
print("Score:", best_fitness["Fitness"])


# ==========================================
# CATEGORY AVERAGES
# ==========================================

category_average = np.mean(
    df[performance],
    axis=0
)

print("\n===== CATEGORY AVERAGES =====")

for category, average in zip(
    performance,
    category_average
):
    print(
        category,
        ":",
        round(average, 2)
    )


# ==========================================
# BAR CHART
# ==========================================

plt.figure(figsize=(10, 6))

plt.bar(
    df["Name"],
    df["Average"]
)

plt.title(
    "Karate Student Average Performance",
    fontsize=16
)

plt.xlabel("Students")
plt.ylabel("Average Score")

plt.ylim(0, 100)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()

plt.show()


# ==========================================
# KATA VS KUMITE
# ==========================================

x = np.arange(len(df))

width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    x - width / 2,
    df["Kata"],
    width,
    label="Kata"
)

plt.bar(
    x + width / 2,
    df["Kumite"],
    width,
    label="Kumite"
)

plt.title(
    "Karate Kata vs Kumite Performance",
    fontsize=16
)

plt.xlabel("Students")
plt.ylabel("Score")

plt.xticks(
    x,
    df["Name"]
)

plt.ylim(0, 100)

plt.legend()

plt.tight_layout()

plt.show()


# ==========================================
# ATTENDANCE CHART
# ==========================================

plt.figure(figsize=(10, 6))

plt.bar(
    df["Name"],
    df["Attendance"]
)

plt.title(
    "Karate Student Attendance",
    fontsize=16
)

plt.xlabel("Students")
plt.ylabel("Attendance (%)")

plt.ylim(0, 100)

plt.axhline(
    75,
    linestyle="--",
    label="Minimum 75%"
)

plt.legend()

plt.tight_layout()

plt.show()


# ==========================================
# SEABORN HEATMAP
# ==========================================

plt.figure(figsize=(10, 6))

heatmap_data = df[
    [
        "Attendance",
        "Kata",
        "Kumite",
        "Fitness"
    ]
]

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu",
    linewidths=0.5,
    linecolor="white",
    xticklabels=[
        "Attendance",
        "Kata",
        "Kumite",
        "Fitness"
    ],
    yticklabels=df["Name"]
)

plt.title(
    "Karate Student Performance Heatmap",
    fontsize=16
)

plt.xlabel("Performance Categories")
plt.ylabel("Students")

plt.tight_layout()

plt.show()


# ==========================================
# BELT DISTRIBUTION
# ==========================================

belt_count = df["Belt"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    belt_count.index,
    belt_count.values
)

plt.title(
    "Karate Belt Distribution",
    fontsize=16
)

plt.xlabel("Belt Level")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.show()


# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n==========================================")
print("             FINAL SUMMARY")
print("==========================================")

print(
    "Total Students       :",
    len(df)
)

print(
    "Average Kata         :",
    round(df["Kata"].mean(), 2)
)

print(
    "Average Kumite       :",
    round(df["Kumite"].mean(), 2)
)

print(
    "Average Fitness      :",
    round(df["Fitness"].mean(), 2)
)

print(
    "Average Attendance   :",
    round(df["Attendance"].mean(), 2),
    "%"
)

print(
    "Top Performer        :",
    top_student["Name"]
)

print("\n===== ANALYSIS COMPLETED =====")