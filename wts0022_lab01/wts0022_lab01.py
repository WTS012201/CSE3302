import os

def get_size(path):
    total = 0
    for elem in os.listdir(path):
        if os.path.isfile(f"{path}/{elem}"):
            total += os.path.getsize(f"{path}/{elem}")
        else:
            total += get_size(f"{path}/{elem}")
    return total

total_size = get_size(".")
print(f"{total_size} bytes")