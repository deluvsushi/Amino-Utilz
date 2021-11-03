import pyfiglet
from tabulate import tabulate
from configs import menu_configs, main_functions
from colored import fore, back, style, attr
attr(0)
print(fore.DEEP_SKY_BLUE_1 + style.BOLD)
print("""Script by DeLuvSushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("AminoUtilz", font="cosmike", width=58))
print(tabulate(menu_configs.main_menu, tablefmt="fancy_grid"))
select = input("Select >> ")

if select == "1":
    main_functions.spam_utilz()
elif select == "2":
    main_functions.active_utilz()
elif select == "3":
    main_functions.other_utilz()
elif select == "4":
    main_functions.profile_utilz()
