# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# # Base URL pattern
# base_url = "https://results.beup.ac.in/ResultsBTech6thSem2024_B2021Pub.aspx?Sem=VI&RegNo={}"

# # Range of registration numbers
# start_reg = 21104108001
# end_reg = 21104108005

# # Output CSV file
# output_file = "BEU_Results.csv"

# # Write headers to CSV file
# with open(output_file, "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Registration Number", "Name", "CGPA"])

# # Loop through each registration number
# for reg_no in range(start_reg, end_reg + 1):
#     result_url = base_url.format(reg_no)  # Construct result URL
#     response = requests.get(result_url)

#     # Check if the page was retrieved successfully
#     if response.status_code != 200:
#         print(f"Failed to fetch {reg_no}")
#         continue

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Extract Student Name
#     name_tag = soup.find("span", {"id": "ContentPlaceHolder1_DataList1_StudentNameLabel_0"})
#     name = name_tag.text.strip() if name_tag else "Not Found"

#     # Extract CGPA
#     cgpa_tag = soup.find("span", {"id": "ContentPlaceHolder1_DataList5_GROSSCGPA_Lbl"})
#     cgpa = cgpa_tag.text.strip() if cgpa_tag else "Not Found"

#     # Save extracted data to CSV
#     with open(output_file, "a", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow([reg_no, name, cgpa])

#     # Print progress
#     print(f"Registration No.: {reg_no} | Name: {name} | CGPA: {cgpa}")

#     # Delay to prevent getting blocked
#     time.sleep(0.1)

# print(f"\n✅ Results saved in {output_file}")





import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL pattern
base_url = "https://results.beup.ac.in/ResultsBTech7thSem2023_B2020Pub.aspx?Sem=VII&RegNo={}"

# Range of registration numbers
start_reg = 20105108001
end_reg = 20105108060

# Output CSV file
output_file = "BEU_Results.csv"

# Write headers to CSV file
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Registration Number", "Name", "Cur. CGPA"])

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
        writer.writerow([reg_no, name, cur_cgpa])

    # Print progress
    print(f"Registration No.: {reg_no} | Name: {name} | Cur. CGPA: {cur_cgpa}")

    # Delay to prevent getting blocked
    time.sleep(0.1)

print(f"\nResults saved in {output_file}")
