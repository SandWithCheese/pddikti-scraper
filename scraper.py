import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import json

options = Options()
options.add_argument("--headless")

with open("list_fakultas.json") as f:
    content = f.read()
    fakultas = json.loads(content)

kode_fakultas = input("Kode Fakultas Atau Jurusan: ")

if kode_fakultas in fakultas:
    nama_fakultas = f"{fakultas[kode_fakultas]}"
else:
    print("Tidak ada fakultas atau jurusan dengan kode tersebut")
    quit()

angkatan = input("Angkatan: ")
nama_fakultas += f"_{angkatan}"

nim = int(input("NIM Awal Pencarian: "))
nim_awal = nim

kode_nim = kode_fakultas + angkatan
universitas = "INSTITUT TEKNOLOGI BANDUNG"

nama_folder = input("Nama Folder (Format fakultas_22 atau jurusan_21): ")

part = input("Part (Format 'part2' atau kosongkan): ")

if part != "":
    part = "_" + part

nama_file = f"data/{nama_folder}/{nama_fakultas}{part}.csv"

start = time.time()

results = []
while True:
    print(f"Processing NIM {nim:03d}...")

    driver = webdriver.Firefox(options=options)
    url = "https://pddikti.kemdikbud.go.id/search/" + kode_nim + f"{nim:03d}"
    driver.get(url)
    time.sleep(0.5)

    span = driver.find_elements(
        By.XPATH, "//td//span//span")

    result = []
    temp_result = []

    ada_itb = False
    for tag in span:
        if tag.text == universitas:
            ada_itb = True
            temp_result = result.copy()
            result = []
            continue
        result.append(tag.text)

        if ada_itb:
            break

    if not ada_itb:
        break

    nim_nama = list(filter(None, temp_result[-4:]))
    results.append(nim_nama + result)

    # Autosave tiap 20 NIM
    if nim % 20 == 0:
        df = pd.DataFrame(results)
        df.to_csv(nama_file, index=False, header=["NAMA", "NIM", "FAKULTAS"])

    nim += 1
    driver.close()

print(f"NIM error: {nim}")


if results != []:
    end = time.time()

    df = pd.DataFrame(results)
    df.to_csv(nama_file, index=False, header=["NAMA", "NIM", "FAKULTAS"])

    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("Time Elapsed:", "{:0>2}:{:0>2}:{:05.2f}".format(
        int(hours), int(minutes), seconds))

    avg = (end - start)/(nim-nim_awal)
    print(f"Average time per NIM: {avg} seconds")
