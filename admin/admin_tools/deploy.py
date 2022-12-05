from platform import system
import shutil
import os

releaseDirectory = "./release"

for file in os.listdir(releaseDirectory):
    os.remove(os.path.join(releaseDirectory, file))
print("Old Release removed!!")


isfor = {
    'Windows': lambda file: not file.endswith('.db'),
    'Linux': lambda file: file.endswith('.db'),
    '': lambda file: True
}

mainProgram = "./admin/main.py"
programData = [file for file in os.listdir("./admin") if file.startswith("Program Data") and isfor[system()](file)]



shutil.copy(mainProgram, releaseDirectory)

for file in programData:
    shutil.copy("./admin/" + file, releaseDirectory)

print('Program Deployed!!!')
