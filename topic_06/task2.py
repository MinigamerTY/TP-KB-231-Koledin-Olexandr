students = [
    {"name": "Олександр", "score": 85},
    {"name": "Ялад", "score": 92},
    {"name": "Дмитро", "score": 98},
    {"name": "Олена", "score": 88}
]

# Сортування за іменем
sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Сортування за іменем:", sorted_by_name)

# Сортування за оцінкою
sorted_by_score = sorted(students, key=lambda x: x["score"])
print("Сортування за оцінкою:", sorted_by_score)
