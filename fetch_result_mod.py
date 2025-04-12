import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL pattern
base_url = "https://results.beup.ac.in/ResultsBTechSPLSem2024_B2020Pub.aspx?Sem=III&RegNo={}"

# Range of registration numbers
start_reg = 22105111901
end_reg = 22105111920

# Output CSV file
output_file = "BEU_Results.csv"

# Write headers to CSV file
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Registration Number", "Name", "Father's Name", "Mother's Name", "SGPA", "Cur. CGPA"])

# Loop through each registration number
for reg_no in range(start_reg, end_reg + 1):
    result_url = base_url.format(reg_no)  # Construct result URL
    response = requests.get(result_url)

    # Check if the page was retrieved successfully
    if response.status_code != 200:
        print(f"Failed to fetch {reg_no}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Student Name
    name_tag = soup.find("span", {"id": "ContentPlaceHolder1_DataList1_StudentNameLabel_0"})
    name = name_tag.text.strip() if name_tag else "Not Found"

    # Extract Father's Name
    father_tag = soup.find("span", {"id": "ContentPlaceHolder1_DataList1_FatherNameLabel_0"})
    father_name = father_tag.text.strip() if father_tag else "Not Found"

    # Extract Mother's Name
    mother_tag = soup.find("span", {"id": "ContentPlaceHolder1_DataList1_MotherNameLabel_0"})
    mother_name = mother_tag.text.strip() if mother_tag else "Not Found"

    # Extract SGPA
    sgpa_tag = soup.find("span", {"id": "ContentPlaceHolder1_DataList5_GROSSTHEORYTOTALLabel_0"})
    sgpa = sgpa_tag.text.strip() if sgpa_tag else "Not Found"

    # Extract Cur. CGPA from the last <td> in the table
    cur_cgpa = "Not Found"
    table = soup.find("table", {"id": "ContentPlaceHolder1_GridView3"})
    if table:
        rows = table.find_all("tr")
        if len(rows) > 1:
            last_row = rows[1]  # The second row contains CGPA values
            cells = last_row.find_all("td")
            if cells:
                cur_cgpa = cells[-1].text.strip()  # Last column is "Cur. CGPA"

    # Save extracted data to CSV
    with open(output_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([reg_no, name, father_name, mother_name, sgpa, cur_cgpa])

    # Print progress
    print(f"Registration No.: {reg_no} | Name: {name} | Father: {father_name} | Mother: {mother_name} | SGPA: {sgpa} | Cur. CGPA: {cur_cgpa}")

    # Delay to prevent getting blocked
    time.sleep(0.1)

print(f"\nResults saved in {output_file}")