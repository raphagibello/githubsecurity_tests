import requests
import os
import sys

def get_data_from_url(url):
    # Insecure: directly using input URL without validation
    response = requests.get(url)
    return response.text

def dangerous_eval(user_input):
    # Insecure: eval used with untrusted input
    return eval(user_input)

def run_command(command):
    # Insecure: possible command injection
    os.system("ping -c 1 " + command)

def main():
    # Hardcoded API token (bad practice)
    API_TOKEN = "ghp_1234567890abcdefSECRET"

    # User input from CLI args (not validated)
    if len(sys.argv) < 2:
        print("Usage: python vulnerable_script.py <hostname>")
        return

    hostname = sys.argv[1]

    print("Querying globo.com...")
    data = get_data_from_url("https://www.globo.com/")
    print(data[:200])  # Just show part of the result

    print("Running dangerous eval...")
    dangerous_eval("2 + 2")  # Simulate unsafe use

    print("Running shell command...")
    run_command(hostname)

if __name__ == "__main__":
    main()
