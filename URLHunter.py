import requests

author = "Karan Bhateja"
github_link = "https://github.com/karanbhateja/"
version = "1.0"

# Function to display a custom ASCII art banner
def display_banner():
    banner = f"""

    \033[31m██╗   ██╗██████╗ ██╗         ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
    \033[31m██║   ██║██╔══██╗██║         ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
    \033[33m██║   ██║██████╔╝██║         ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
    \033[33m██║   ██║██╔══██╗██║         ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
    \033[91m╚██████╔╝██║  ██║███████╗    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
    \033[91m ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                                                   
                    \033[93m Author: {author}  
                    \033[93m Github: {github_link}
                    \033[93m Version: V{version}  
    """                                                        
    print(banner)
    print("            Welcome to URLHunter - Web Path and File Brute-Forcing Tool\n")                                                   
    

# Function to format the URL with a trailing slash if missing and add "http://" or "https://"
def format_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url  # Add "http://" by default if missing
    if not url.endswith("/"):
        url += "/"
    return url

# Display the custom banner
display_banner()

# Target URL and wordlists for directories and filenames
target_url = input("Enter the target URL (e.g., example.com): ")
target_url = format_url(target_url)  # Ensure URL has "http://" or "https://" and a trailing slash

# Prompt the user for their choice
print("\nSelect an option:")
print("1. Directory Brute-Forcing")
print("2. File Brute-Forcing")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    directory_wordlist_file = input("\nEnter the name of the Directory Wordlist File (e.g., directory_wordlist.txt): ")
    wordlist_file = directory_wordlist_file
    print("\nPerforming Directory Brute-Forcing...")
elif choice == "2":
    file_wordlist_file = input("\nEnter the name of the File Wordlist File (e.g., file_wordlist.txt): ")
    wordlist_file = file_wordlist_file
    print("\nPerforming File Brute-Forcing...")
else:
    print("\nInvalid choice. Please enter 1 for directory brute-forcing or 2 for file brute-forcing.")
    exit()

# Read the selected wordlist
with open(wordlist_file, "r") as file:
    wordlist = [line.strip() for line in file.readlines()]

# Perform brute-forcing based on the user's choice
for item in wordlist:
    url = target_url + item
    response = requests.get(url)
    
    if response.status_code in [200, 301, 401, 403]:
        if choice == "1":
            print(f"==> {url} (Status Code: {response.status_code})")
        elif choice == "2":
            print(f"==> {url} (Status Code: {response.status_code})")

# Close the file
file.close()
