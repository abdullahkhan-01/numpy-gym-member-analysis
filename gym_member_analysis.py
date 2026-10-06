# ============================================================
# Gym Member Analysis using NumPy
# ============================================================

import numpy as np


# ------------------------------------------------------------
# 1. Dataset
# ------------------------------------------------------------
# Columns:
# 0 -> Member ID
# 1 -> Age
# 2 -> Weight (kg)
# 3 -> Workouts per Month
# 4 -> Average Workout Hours

data = np.array([
    [101, 19, 62,  4, 7.2],
    [102, 24, 78,  6, 8.1],
    [103, 31, 85,  5, 6.8],
    [104, 27, 70,  8, 9.0],
    [105, 22, 55,  3, 7.5],
    [106, 35, 92,  7, 8.7],
    [107, 29, 68,  4, 6.5],
    [108, 42, 88,  9, 7.9],
    [109, 26, 74,  6, 8.4],
    [110, 38, 95, 10, 9.2],
    [111, 21, 60,  5, 7.0],
    [112, 33, 82,  7, 8.0]
])


# ------------------------------------------------------------
# 2. Separate Columns
# ------------------------------------------------------------

member_id = data[:, 0]
age = data[:, 1]
weight = data[:, 2]
workouts = data[:, 3]
workout_hours = data[:, 4]


# ------------------------------------------------------------
# Q1. Find Average Age and Average Workout Hours
# ------------------------------------------------------------

average_age = np.mean(age)
average_workout_hours = np.mean(workout_hours)

print("\n--- Q1: Average ---")
print("Average Age:", average_age)
print("Average Workout Hours:", average_workout_hours)


# ------------------------------------------------------------
# Q2. Find Member with Highest Workouts per Month
# ------------------------------------------------------------

highest_workout_index = np.argmax(workouts)

print("\n--- Q2: Highest Workouts ---")
print("Member ID:", member_id[highest_workout_index])
print("Workouts per Month:", workouts[highest_workout_index])


# ------------------------------------------------------------
# Q3. Find Members with 7 or More Workouts per Month
# ------------------------------------------------------------

condition = workouts >= 7

result = member_id[condition]

print("\n--- Q3: Workouts >= 7 ---")
print("Member IDs:", result)


# ------------------------------------------------------------
# Q4. Find Members Whose:
# Age > 30 AND Average Workout Hours > 8
# ------------------------------------------------------------

condition = (age > 30) & (workout_hours > 8)

result = member_id[condition]

print("\n--- Q4: Age > 30 and Workout Hours > 8 ---")
print("Member IDs:", result)


# ------------------------------------------------------------
# Q5. Among Members with Workout Hours >= 8,
# Find the Member with the Highest Weight
# ------------------------------------------------------------

condition = workout_hours >= 8

highest_weight_index = np.argmax(weight[condition])

filtered_member_id = member_id[condition]
filtered_weight = weight[condition]
filtered_workout_hours = workout_hours[condition]

print("\n--- Q5: Highest Weight among Workout Hours >= 8 ---")
print("Member ID:", filtered_member_id[highest_weight_index])
print("Weight:", filtered_weight[highest_weight_index], "kg")
print("Workout Hours:", filtered_workout_hours[highest_weight_index])


# ------------------------------------------------------------
# Q6. Among Members Whose:
# Age > 25 AND Workouts >= 6,
# Find the Member with the Lowest Workout Hours
# ------------------------------------------------------------

condition = (age > 25) & (workouts >= 6)

lowest_workout_hours_index = np.argmin(workout_hours[condition])

filtered_member_id = member_id[condition]
filtered_age = age[condition]
filtered_workouts = workouts[condition]
filtered_workout_hours = workout_hours[condition]

print("\n--- Q6: Lowest Workout Hours ---")
print("Member ID:", filtered_member_id[lowest_workout_hours_index])
print("Age:", filtered_age[lowest_workout_hours_index])
print("Workouts per Month:", filtered_workouts[lowest_workout_hours_index])
print("Workout Hours:", filtered_workout_hours[lowest_workout_hours_index])
