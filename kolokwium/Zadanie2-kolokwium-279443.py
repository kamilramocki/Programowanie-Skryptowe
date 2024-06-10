import psutil
import platform
import shutil


def get_ram_count():
    return "Ilość pamięci RAM: " + str(psutil.virtual_memory().total / 1_073_741_824) + " GiB"


def get_disk_usage():
    return "Użycie dysku: " + str(round(shutil.disk_usage("/")[1] / 1_073_741_824, 2)) + " GiB"


def get_hostname():
    return "Nazwa hosta: " + str(psutil.users()[0].name)


def get_os_name():
    return "Nazwa systemu operacyjnego: " + str(platform.system()) + " " + str(platform.release())


print(get_ram_count())
print(get_disk_usage())
print(get_hostname())
print(get_os_name())
