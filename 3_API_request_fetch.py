import requests
import json
import csv
import time  

url = "https://api.apollo.io/v1/mixed_people/search"  

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": "6Nga8qQuRKr34-Xia9hzjA" 
}

with open('1_input_payload.json', 'r') as file:
    payload_template = json.load(file)

def fetch_page(page_number, payload_template):
    payload = payload_template.copy()
    payload["page"] = page_number
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()  
    else:
        print(f"Error fetching page {page_number}: {response.status_code}")
        return None

all_data = []
extracted_data = []

for page in range(1, 6):  
    print(f"Fetching data for page {page}...")
    data = fetch_page(page, payload_template)
    if data:
        for p in data.get('people', []):
            people_name = p.get('name')
            country = p.get('country')
            organization = p.get('organization', {})
            organization_name = organization.get('name', 'N/A')
            organization_url = organization.get('website_url', 'N/A')
            extracted_data.append([people_name, country, organization_name, organization_url])
    
    time.sleep(20) 

csv_filename = './output_people.csv'

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['People_name', 'Country', 'Organization Name', 'Organization URL'])  
    writer.writerows(extracted_data)  
print(f"Successfully saved the data to {csv_filename}")
