# pddikti-scraper
This is a Python script that utilizes Selenium and Pandas libraries to scrape data from the website https://pddikti.kemdikbud.go.id. The script retrieves student information based on a given starting NIM (Nomor Induk Mahasiswa) and a specific faculty or department code.

## Prerequisites
+ Python 3.x
+ Selenium library
+ Pandas library

## Installation
```pip install selenium```
```pip install pandas```

## Usage
1. Run the script using the following command:
```python scraper.py```
2. Enter the requested information when prompted:
  1. Kode Fakultas Atau Jurusan: Enter the code for the desired faculty or department.
  2. Angkatan: Enter the academic year.
  3. NIM Awal Pencarian: Enter the starting NIM for the search.
  4. Nama Folder (Format fakultas_22 atau jurusan_21): Enter the name of the folder where the data will be saved. Use the format "fakultas_22" or "jurusan_21".
  5. Part (Format 'part2' atau kosongkan): Enter the part number for the data if applicable, otherwise leave it blank.
3. The script will start scraping the data from the website, and the progress will be displayed on the console. The scraped data will be saved in a CSV file named according to the provided information.

## Output
The script generates a CSV file containing the following columns:
+ NAMA: Student's name
+ NIM: Student's NIM
+ FAKULTAS: Name of the faculty or department

If the script encounters an error or reaches the end of available data, it will display the NIM which the error occurs.

At the end of the execution, the script will also display the elapsed time and the average time taken per NIM.

Note: 
+ The script is set to run in headless mode by default, which means it won't open a browser window during the execution. If you want to see the browser window, you can remove the "--headless" argument from the code.
+ Sometimes the process stops due to internet issues or pages not loading properly. In such cases, simply run the script again starting from the latest processed NIM.
