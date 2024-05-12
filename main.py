import subprocess
import time
import re
import requests

url = "https://api.dub.co/links/cls5034o1000ujw08tk1ne6am"

def start_batch_file(file_path):
    try:
        subprocess.Popen(file_path, shell=True)
        print("Batch file started successfully.")
    except Exception as e:
        print(f"Error starting batch file: {e}")


batch_file_path1 = "tunnel.bat"
batch_file_path2 = "jiotv.bat"


start_batch_file(batch_file_path1)
time.sleep(5)


with open("output.txt", "r") as file:
    content = file.read()
    urls = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    filtered_urls = [url for url in urls if url !=
                     "https://developers.cloudflare.com/cloudflare-one/connections/connect-apps"]
    filtered_urls_str = ", ".join(filtered_urls)
    print("Link Generated: " + filtered_urls_str)

time.sleep(5)

start_batch_file(batch_file_path2)

time.sleep(2)

querystring = {"workspaceId":"ws_clri4hgs3000yvss0zyevebic"}

payload = {"url": filtered_urls_str + "/playlist.m3u"}
headers = {
    "Authorization": "Bearer 8GOorADoP8RA7jDOPFqtUEGf",
    "Content-Type": "application/json"
}

response = requests.request("PATCH", url, json=payload, headers=headers, params=querystring)

print(response.text)
print("Your Final URL is: https://dub.sh/jiotv")