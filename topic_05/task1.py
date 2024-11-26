import random

choices = ["камінь", "ножиці", "папір"]

# Функція для визначення переможця
def game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Нічия!"
    elif (
         player_choice == "камінь" and computer_choice == "ножиці" or 
         player_choice == "ножиці" and computer_choice == "папір" or 
         player_choice == "папір" and computer_choice == "камінь"
         ):
        return "Ви виграли!"
    else:
        return "Переміг комп'ютер!"

# Запитуємо користувача на вибір
player_choice = input("Оберіть камінь, ножиці чи папір: \n").lower()

# Перевіряємо, чи є введення в списку виборів
if player_choice not in choices:
    print("Некоректний вибір! Будь ласка, оберіть камінь, ножиці чи папір.")
else:
    computer_choice = random.choice(choices)
    print("Комп'ютер вибрав: ", computer_choice)

    # Визначаємо результат гри
    result = game(player_choice, computer_choice)
    print(result)