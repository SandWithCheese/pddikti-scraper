import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import json

universitas = "INSTITUT TEKNOLOGI BANDUNG"

options = Options()
options.add_argument("--headless")

with open("list_fakultas.json") as f:
    content = f.read()
    fakultas = json.loads(content)

angkatan = input("Angkatan: ")
nama_file = f"data/batch/angkatan_{angkatan}.csv"

start = time.time()

for kode in fakultas.keys():
    nim = 1
    count = 0
    kode_nim = kode + angkatan

    results = []
    while count < 3:
        print(f"Processing {kode_nim}{nim:03d}...")

        driver = webdriver.Firefox(options=options)
        url = "https://pddikti.kemdikbud.go.id/search/" + kode_nim + f"{nim:03d}"
        driver.get(url)
        time.sleep(1)

        span = driver.find_elements(By.XPATH, "//td//span//span")

        result = []
        temp_result = []

        ada_itb = False
        for tag in span:
            if tag.text == universitas:
                ada_itb = True
                temp_result = result.copy()
                result = []
                continue
            result.append(tag.text.title())

            if ada_itb:
                break

        if not ada_itb:
            count += 1
        else:
            nim_nama = list(filter(None, temp_result[-4:]))
            results.append(nim_nama + result)

            # Autosave tiap 20 NIM
            if nim % 20 == 0:
                df = pd.DataFrame(results)
                df.to_csv(nama_file, index=False, header=["NAMA", "NIM", "FAKULTAS"])

            nim += 1
        driver.close()

    if results != []:
        df = pd.DataFrame(results)
        df.to_csv(nama_file, index=False, header=["NAMA", "NIM", "FAKULTAS"])

end = time.time()
hours, rem = divmod(end - start, 3600)
minutes, seconds = divmod(rem, 60)
print(
    "Time Elapsed:",
    "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds),
)
