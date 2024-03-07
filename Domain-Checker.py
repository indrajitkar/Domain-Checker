import requests
import socket
import time
from tqdm import tqdm
from colorama import Fore, Style

def check_domain(domain):
    try:
        # Check if domain resolves to an IP address
        ip_address = socket.gethostbyname(domain)
        
        # Check if domain responds to HTTP requests
        response = requests.get(f"http://{domain}", timeout=5)
        if response.status_code == 200:
            return True
    except Exception as e:
        pass
    return False

def select_domains_from_file(filename):
    with open(filename, "r") as file:
        domains = [line.strip() for line in file if line.strip()]
    return domains

def save_working_domains(working_domains, output_filename):
    with open(output_filename, "w") as file:
        for domain in working_domains:
            file.write(domain + "\n")

def estimate_time(num_domains):
    # Assuming each domain check takes around 1 second
    return num_domains * 1

def print_colored_message(message, color):
    print(color + message + Style.RESET_ALL)

def display_lolcat():
    print("""
(¯`·¯`·.¸¸.·´¯`·.¸¸.·´¯)
( \                  / )
 ( ) Domain-Checker ( ) 
  (/                \)  
   (.·´¯`·.¸¸.·´¯`·.)                                                                                     
    """)

def main():
    input_filename = input("Enter the filename containing the list of domains: ")
    output_filename = input("Enter the filename to save the working domains: ")

    domains = select_domains_from_file(input_filename)
    num_domains = len(domains)
    working_domains = []

    start_time = time.time()

    for domain in tqdm(domains, desc="Checking domains", unit="domain"):
        if check_domain(domain):
            working_domains.append(domain)

    end_time = time.time()

    display_lolcat()  # Display the LOLCat image

    print_colored_message("\nWorking domains:", Fore.GREEN)
    for domain in working_domains:
        print_colored_message(domain, Fore.GREEN)

    print_colored_message("\nProcess complete!", Fore.BLUE)

    if working_domains:
        save_option = input("Do you want to save the working domains to a file? (y/n): ")
        if save_option.lower() == "y":
            save_working_domains(working_domains, output_filename)
            print_colored_message(f"Working domains saved to {output_filename}", Fore.GREEN)

    elapsed_time = end_time - start_time
    print(f"\nTotal elapsed time: {elapsed_time:.2f} seconds")
    estimated_time = estimate_time(num_domains)
    print(f"Estimated time to complete: {estimated_time:.2f} seconds")

if __name__ == "__main__":
    main()
