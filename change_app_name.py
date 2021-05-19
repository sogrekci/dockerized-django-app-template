import os

target_string = input("Old App Name: ")
replacement = input("New App Name: ")
target_folder = 'docker'
for dname, dirs, files in os.walk(target_folder):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
        s = s.replace(target_string, replacement)
        with open(fpath, "w") as f:
            f.write(s)
print("App name changed")