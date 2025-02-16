# Apollo API Data Extraction to CSV

This project utilizes the Apollo API to extract JSON data of professionals and their organizations, transforming it into a CSV file for further analysis.

---

## **Project Structure**
- `1_input_payload.json` – Contains the initial API request payload.
- `apollo_api_script.py` – Python script to fetch data from Apollo API and export it to CSV.
- `output_people.csv` – Output CSV with extracted data.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.x
- `requests` library installed:
  ```bash
  pip install requests
  ```

### **Steps to Run**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/apollo-api-data-extraction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd apollo-api-data-extraction
   ```
3. Add your Apollo API key in `apollo_api_script.py`:
   ```python
   headers = {"x-api-key": "your_api_key"}
   ```
4. Run the script:
   ```bash
   python apollo_api_script.py
   ```

The extracted data will be saved in `output_people.csv`.

---

## **Code Overview**
- Fetches data from Apollo API in pages.
- Extracts fields such as `people_name`, `country`, `organization_name`, and `organization_url`.
- Adds delays to avoid rate limits.

---

## **Best Practices Followed**
- Delays to avoid API limits.
- Secure API key usage.
- Modular and well-documented code.


---

## **Author**
*Your Name*  
*Your Position*  
[LinkedIn Profile](https://www.linkedin.com/in/mekhma-tamang/)  
*Date: February 14, 2025*  

---

*This README provides a comprehensive guide for setting up and running the project.*
