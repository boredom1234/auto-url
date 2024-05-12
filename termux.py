import subprocess
import time
import re
import requests
import os

url = "https://api.dub.co/links/cls5034o1000ujw08tk1ne6am"

def start_shell_script(script_path):
    try:
        os.system(f"bash {script_path}")
        print("Shell script started successfully.")
    except Exception as e:
        print(f"Error starting shell script: {e}")

shell_script_path1 = "tunnel.sh"
shell_script_path2 = "jiotv.sh"

start_shell_script(shell_script_path1)
time.sleep(5)

# Assuming output.txt is generated by the shell script
with open("output.txt", "r") as file:
    content = file.read()
    urls = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    filtered_urls = [url for url in urls if url !=
                     "https://developers.cloudflare.com/cloudflare-one/connections/connect-apps"]
    filtered_urls_str = ", ".join(filtered_urls)
    print("Link Generated: " + filtered_urls_str)

time.sleep(5)

start_shell_script(shell_script_path2)

time.sleep(2)

querystring = {"workspaceId": "ws_clri4hgs3000yvss0zyevebic"}

payload = {"url": filtered_urls_str + "/playlist.m3u"}
headers = {
    "Authorization": "Bearer 8GOorADoP8RA7jDOPFqtUEGf",
    "Content-Type": "application/json"
}

response = requests.request("PATCH", url, json=payload, headers=headers, params=querystring)

print(response.text)
print("Your Final URL is: https://dub.sh/jiotv")