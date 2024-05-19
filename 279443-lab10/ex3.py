import os
import shutil
import zipfile
from ftplib import FTP
from datetime import datetime

local_files = ['/path/to/file1', '/path/to/file2']  # Ścieżki do plików, które mają być zarchiwizowane
backup_dir = '/path/to/backup'  # Katalog, w którym będzie tworzona kopia zapasowa
ftp_server = 'ftp.example.com'
ftp_user = 'your_username'
ftp_password = 'your_password'
ftp_remote_dir = '/remote/backup/directory'


# Funkcja do tworzenia archiwum
def create_backup_zip(files, output_dir):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    zip_filename = os.path.join(output_dir, f'backup_{timestamp}.zip')
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    return zip_filename


# Funkcja do przesyłania pliku na serwer FTP
def upload_to_ftp(ftp_server, ftp_user, ftp_password, file_path, remote_dir):
    with FTP(ftp_server) as ftp:
        ftp.login(ftp_user, ftp_password)
        ftp.cwd(remote_dir)
        with open(file_path, 'rb') as f:
            ftp.storbinary(f'STOR {os.path.basename(file_path)}', f)


def perform_backup():
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    zip_file = create_backup_zip(local_files, backup_dir)
    print(f'Backup created: {zip_file}')

    upload_to_ftp(ftp_server, ftp_user, ftp_password, zip_file, ftp_remote_dir)
    print(f'Backup uploaded to FTP: {ftp_server}/{ftp_remote_dir}/{os.path.basename(zip_file)}')


if __name__ == "__main__":
    perform_backup()
