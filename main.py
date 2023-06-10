import random
import string

logo = """
█       ▄   ▄█▄    ▄█ ██▄   ▄█ ██   █     
█        █  █▀ ▀▄  ██ █  █  ██ █ █  █     
█     █   █ █   ▀  ██ █   █ ██ █▄▄█ █     
███▄  █   █ █▄  ▄▀ ▐█ █  █  ▐█ █  █ ███▄  
    ▀ █▄ ▄█ ▀███▀   ▐ ███▀   ▐    █     ▀ 
       ▀▀▀                       █        
                                ▀
"""

# Generate a random string of uppercase characters
random_string = ''.join(random.choices(string.ascii_uppercase, k=712))

# Warning text
warning_text = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"

# Combine the warning text and random string
final_string = warning_text + random_string

print(logo)

# Ask user if they want to save the final_string to a file
save_to_file = input("Do you want to save the generated cookie to a file? (Y/N): ")

if save_to_file.upper() == "Y":
    # Save final_string to a file
    with open("cookie.txt", "w") as file:
        file.write(final_string)
    print("Cookie saved to 'cookie.txt'.")
else:
    print("Cookie not saved to a file.")
print(final_string)
