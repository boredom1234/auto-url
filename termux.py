import subprocess
import time
import re
import requests

url = "https://api.dub.co/links/cls5034o1000ujw08tk1ne6am"

def start_shell_script(script_path):
    try:
        process = subprocess.Popen(["bash", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Shell script started successfully...")
        return process
    except Exception as e:
        print(f"Error starting shell script: {e}")
        return None

def kill_process(process):
    if process:
        process.terminate()
        process.wait()

shell_script_path1 = "tunnel.sh"
shell_script_path2 = "jiotv.sh"

process1 = start_shell_script(shell_script_path1)
time.sleep(5)

# Assuming output.txt is generated by the shell script
with open("output.txt", "r") as file:
    content = file.read()
    urls = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    filtered_urls = [url for url in urls if url not in [
        "https://developers.cloudflare.com/cloudflare-one/connections/connect-apps",
        "https://github.com/quic-go/quic-go/wiki/UDP-Buffer-Sizes"
    ]]
    filtered_urls_str = ", ".join(filtered_urls)
    print("Link Generated: " + filtered_urls_str)

time.sleep(5)

process2 = start_shell_script(shell_script_path2)

querystring = {"workspaceId": "ws_clri4hgs3000yvss0zyevebic"}

payload = {"url": filtered_urls_str + "/playlist.m3u"}
headers = {
    "Authorization": "Bearer 8GOorADoP8RA7jDOPFqtUEGf",
    "Content-Type": "application/json"
}

response = requests.request("PATCH", url, json=payload, headers=headers, params=querystring)

print(response.text)
print("Your Final URL is: https://dub.sh/jiotv")

try:
    while True:
        time.sleep(1)  # Check every second for user input
except KeyboardInterrupt:
    print("Ctrl+C detected. Terminating processes...")
    kill_process(process1)
    kill_process(process2)
    print("Processes terminated.")
