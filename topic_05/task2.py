import requests 

def print_cur_n():
    for elem in nbu_orig.json():
        print(elem['cc'], " | ", elem['txt'])

def print_cur_e():
    for elem in nbu_orig.json():
        print(elem['cc'], " | ", elem['rate'])

def conv():
    cur_code = (input("Введіть код валюти: ")).upper()
    cur_val = float(input("Введіть суму валюти: "))
    try:
        total = cur_val * (nbu[cur_code]["rate"])
        print(f"{total} UAH")
    except:
        print("Неправильно вказано код валюти")

def r_conv():
    cur_code = (input("Введіть код валюти: ")).upper()
    cur_val = float(input("Введіть суму UAH: "))
    try:
        total = cur_val / (nbu[cur_code]["rate"])
        print(f"{total} {cur_code}")
    except:
        print("Неправильно вказано код валюти")

def action():
    while True:
        print("\npn — надрукувати назви валют | pe — роздрукувати курс обміну валют | с — перетворення | rс — зворотне перетворення | ex — вихід із програми")
        q = input("Select an action: ")
        match q:
            case "pn":
                print_cur_n()
            case "pe":
                print_cur_e()
            case "c":
                conv()
            case "rc":
                r_conv()
            case "ex":
                exit(0)

nbu_orig = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")
nbu = {}
for elem in nbu_orig.json():
    nbu.update({elem['cc'] : elem})

action()
