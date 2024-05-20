import subprocess

def get_geolocation(file_path):
    result = subprocess.run(['exiftool', file_path], capture_output=True, text=True)
    output = result.stdout
    geolocation_info = {}

    for line in output.split('\n'):
        if 'GPS Latitude' in line:
            geolocation_info['Latitude'] = line.split(': ')[1].strip()
        elif 'GPS Longitude' in line:
            geolocation_info['Longitude'] = line.split(': ')[1].strip()
        elif 'GPS Altitude' in line:
            geolocation_info['Altitude'] = line.split(': ')[1].strip()

    return geolocation_info


file_path = 'path/to/file'
geolocation_info = get_geolocation(file_path)
print(geolocation_info)
