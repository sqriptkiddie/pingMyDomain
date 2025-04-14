# Raspberry Pi URL Pinger

This project is a simple Python script designed to continuously ping a specified URL using a Raspberry Pi. It sends a request to the URL every 120 seconds and logs the HTTP response status code or any errors. It can be used to monitor the availability or health of a web service.

---

## Features

- Sends a periodic HTTP GET request to a given URL.
- Logs the HTTP response code or error messages.
- Lightweight and easy to set up on a Raspberry Pi.

---

## Requirements

To use this script, ensure the following are installed on your Raspberry Pi:

1. Python 3 installed (pre-installed on Raspberry Pi OS).
2. `pip` package manager installed.
3. Required Python modules:
   - `requests`
   - `time` (built-in with Python and no need to install)

You can install the `requests` module by running the following command:

```shell script
pip install requests
```

---

## Setting Up the Raspberry Pi

Follow these steps to set up and run the URL Pinger on your Raspberry Pi:

1. **Connect to Your Raspberry Pi**
   - Use SSH or directly access your Raspberry Pi via a connected monitor and keyboard.

2. **Update Your System (optional)**
   - It's always good practice to ensure your Raspberry Pi is up to date. Run the commands:
```shell script
sudo apt update
     sudo apt upgrade -y
```

3. **Clone or Download the Script**
   - Save the script on your Raspberry Pi. Use a file editor to create the script file (e.g., `ping_url.py`), or transfer it from your computer.

4. **Edit the Script**
   - Open the script file in any text editor:
```shell script
nano ping_url.py
```
   - Replace `"https://my-URL"` in the code with the actual URL you want to monitor.

5. **Run the Script**
   - Navigate to the directory containing the script and execute it:
```shell script
python3 ping_url.py
```

6. **Automate the Script (Optional)**
   - If you'd like the script to run automatically when the Raspberry Pi boots up, you can add it to `crontab`:
```shell script
crontab -e
```
   - Add the following line to the bottom of the `crontab` file:
```shell script
@reboot python3 /path/to/ping_url.py &
```
   - Replace `/path/to/ping_url.py` with the full path to your script file.

---

## Customization

- **URL Timeout Frequency**: You can change the delay between URL checks by modifying the `time.sleep(120)` line in the script. For example, to ping every minute, change `120` to `60`.
- **Error Logs**: Customize how errors are handled by editing the exception block in the script.

---

## Example Output

When you run the script, you'll see output like this in the terminal:

```shell script
Ping sent: 200
Ping sent: 200
Fehler beim Pingen: HTTPSConnectionPool(host='my-URL', port=443): Max retries exceeded...
```

- `200` indicates the ping was successful.
- Error messages will appear if there are connectivity or server issues.

---

## Troubleshooting

1. **No Internet Connection**:
   - Ensure your Raspberry Pi is connected to the internet (via Wi-Fi or Ethernet).

2. **Permission Denied**:
   - Ensure the script has execution permissions:
```shell script
chmod +x ping_url.py
```

3. **`requests` Module Not Found**:
   - If you see an error about `requests` not being found, install it using pip:
```shell script
pip install requests
```

---

Now, your Raspberry Pi will ping the specified URL and log its status, helping you monitor the availability of your web service. Enjoy!
