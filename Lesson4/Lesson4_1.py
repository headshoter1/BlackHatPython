import os

new_extension = input().strip()
old_extension = input().strip()

folder = input().strip()

# old_ext -> new_ext

if not os.path.isdir(folder):
    exit()

for obj in os.listdir(folder):
    if not os.path.isfile(os.path.join(folder, obj)):
        continue
    path, ext = os.path.splitext(os.path.join(folder, obj))
    if ext.lstrip(".") == old_extension:
        os.rename(os.path.join(folder, obj), ".".join([path, new_extension]))
