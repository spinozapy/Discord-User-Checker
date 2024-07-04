import os
import requests
import colorama
from datetime import datetime, timezone

clear_command = "cls" if os.name == "nt" else "clear"

while True:
    os.system(clear_command)
    print(colorama.Fore.GREEN + "[User Checker]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the Discord user ID (type 'exit' to quit):")
    try:
        user_id = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE)
    except KeyboardInterrupt:
        print("")
        continue

    if user_id.lower() == 'exit':
        break

    user_info_url = f"https://discordlookup.mesalytic.moe/v1/user/{user_id}"
    try:
        response = requests.get(user_info_url)

        if response.status_code == 200:
            data = response.json()
            os.system(clear_command)
            print("")
            print(colorama.Fore.YELLOW + f" User ID        : " + colorama.Fore.LIGHTWHITE_EX + str(data.get('id', 'Not found')))
            print(colorama.Fore.YELLOW + f" Username       : " + colorama.Fore.LIGHTWHITE_EX + f"@{data.get('username', 'Not found')}")
            global_name = data.get('global_name')
            print(colorama.Fore.YELLOW + f" Global Name    : " + colorama.Fore.LIGHTWHITE_EX + f"{global_name if global_name is not None else 'Not found.'}")
            print(colorama.Fore.YELLOW + f" Discriminator  : " + colorama.Fore.LIGHTWHITE_EX + f"#{data.get('discriminator', '0')}")
            print("")

            created_at = data.get('created_at')
            if created_at:
                created_at_datetime = datetime.fromisoformat(created_at[:-1] + 'Z').replace(tzinfo=timezone.utc)
                print(colorama.Fore.YELLOW + f" Created At     : " + colorama.Fore.LIGHTWHITE_EX + f"Date: {created_at_datetime.date()} - Time: {created_at_datetime.time()}")
                current_datetime = datetime.now(timezone.utc)
                time_difference = current_datetime - created_at_datetime
                years = time_difference.days // 365
                months = (time_difference.days % 365) // 30
                days = (time_difference.days % 365) % 30
                print(colorama.Fore.YELLOW + f" Joined Discord : " + colorama.Fore.LIGHTWHITE_EX + f"({years} years, {months} months, {days} days ago)")
            else:
                print(colorama.Fore.YELLOW + f" Created At     : " + colorama.Fore.LIGHTWHITE_EX + "Created At not found.")
            print("")
            badges = data.get('badges', [])
            print(colorama.Fore.YELLOW + f" User Badges    : " + colorama.Fore.LIGHTWHITE_EX + (", ".join(badges) if badges else "Badges not found."))

            avatar = data.get('avatar', {})
            avatar_link = avatar.get('link')
            if avatar_link:
                avatar_link += '.gif?size=2048' if avatar.get('is_animated') else '.png?size=2048'
            else:
                avatar_link = "Avatar not found."
            print(colorama.Fore.YELLOW + f" Avatar Link    : " + colorama.Fore.LIGHTWHITE_EX + str(avatar_link))

            banner = data.get('banner', {})
            banner_link = banner.get('link')
            if banner_link:
                banner_link = banner_link.split('?size=')[0]  
                banner_link += '.gif?size=2048' if banner.get('is_animated') else '.png?size=2048'  
            else:
                banner_link = "Banner not found."
            print(colorama.Fore.YELLOW + f" Banner Link    : " + colorama.Fore.LIGHTWHITE_EX + str(banner_link))

            banner_color = banner.get('color', "Banner color not found.")
            print(colorama.Fore.YELLOW + f" Banner Color   : " + colorama.Fore.LIGHTWHITE_EX + str(banner_color))

        else:
            os.system(clear_command)
            print(colorama.Fore.GREEN + "[User Checker]: " + colorama.Fore.RED + "Invalid user ID or unable to fetch data!")

    except KeyboardInterrupt:
        print("")
        continue

    print("")
    try:
        input(colorama.Fore.GREEN + "[User Checker]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")
    except KeyboardInterrupt:
        continue
