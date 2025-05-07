import requests
import json
import time

# Main ETL function
def etl():
    all_data = []  # Stores results from all pages
    page = 0  # Start from page 0

    while True:
        # URL with pagination
        url = f"https://projects.propublica.org/nonprofits/api/v2/search.json?q=chat&page={page}"
        print(f"Requesting page {page}...")

        try:
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                print(f"HTTP Error {response.status_code}")
                break

            data = response.json()

            # If no results, stop
            if not data.get("organizations"):
                print("No more results.")
                break

            # Filter useful data: here, those with a defined city
            filtered_page = [
                org for org in data["organizations"]
                if org.get("city") and org.get("total_revenue", 0) > 0
            ]

            all_data.extend(filtered_page)

            page += 1
            time.sleep(1)  # Pause between requests to avoid spamming the API

        except requests.exceptions.Timeout:
            print("Timeout: server too slow.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    # Write data to a JSON file
    with open("clean_file.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print(f"{len(all_data)} organizations saved in clean_file.json")

if __name__ == "__main__":
    etl()
