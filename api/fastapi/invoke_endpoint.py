import requests

# Set the base URL for the FastAPI server running on localhost:8000
base_url = "http://localhost:8000"
img_file_path = '/home/nakul74/Desktop/templates/streamlit/streamlit_demo_apps/sample.jpeg'
csv_file_path = '/home/nakul74/Downloads/sample.csv'

# Define the sample data for the /data endpoint
data_payload = {
    "HSN": ["3304", "123456", "12"],
    "title": "Example Title",
    "email": "example@example.com",
    "password": "example_password",
    "confirm_password": "example_password",
    "code": 123
}

# Define the sample data for the /translate/ endpoint
translate_payload = {
    "brand_name": "ExampleBrand",
    "receiver_email_list": ["email1@example.com", "email2@example.com"],
    # Assuming you have a CSV file named "example.csv" in the same directory as this script
    "file": ("example.csv", open(csv_file_path, "rb"))
}

# Define the sample data for the /uploadfile/ endpoint
upload_file_payload = {
    "file": ("example.png", open(img_file_path, "rb"))
}

def invoke_api_routes():
    # Invoke the / endpoint
    response_home = requests.get(f"{base_url}/")
    print("Response from / endpoint:", response_home.json())

    # Invoke the /data endpoint
    response_data = requests.post(f"{base_url}/data", json=data_payload)
    print("Response from /data endpoint:", response_data.json())

    # Invoke the /translate/ endpoint
    response_translate = requests.post(f"{base_url}/translate/", files=translate_payload)
    print("Response from /translate/ endpoint:", response_translate.json())

    # Invoke the /uploadfile/ endpoint
    response_upload = requests.post(f"{base_url}/uploadfile/", files=upload_file_payload)
    content_type = response_upload.headers.get("content-type")
    extension = content_type.split("/")[-1]

    # Save the file locally with the same extension
    with open(f"downloaded_file.{extension}", "wb") as local_file:
        local_file.write(response_upload.content)

# Invoke the API routes
invoke_api_routes()
