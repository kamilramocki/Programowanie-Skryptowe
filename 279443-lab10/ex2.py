import re
import time

log_file_path = "/var/log/auth.log"

# Wzorzec regex do wykrywania nieudanych prób logowania
failed_login_pattern = re.compile(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+) port \d+ ssh2')

def monitor_ssh_logs():
    with open(log_file_path, 'r') as log_file:
        log_file.seek(0, 2)

        while True:
            line = log_file.readline()
            if not line:
                time.sleep(0.1)
                continue

            match = failed_login_pattern.search(line)
            if match:
                ip_address = match.group(1)
                print(f"Nieudana próba logowania z adresu IP: {ip_address}")


if __name__ == "__main__":
    monitor_ssh_logs()
