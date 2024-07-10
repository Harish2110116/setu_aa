import requests
import time

# Step 1: Generate an access token
auth_url = "https://orgservice-prod.setu.co/v1/users/login"
auth_headers = {
    "client": "bridge",
    "Content-Type": "application/json"
}
auth_payload = {
    "clientID": "0bbe5be3-3983-4364-84eb-af159d775926",
    "grant_type": "client_credentials",
    "secret": "hoaOU9W3ctnGrqpjxhuGv8IltDFi14Nn"
}
auth_response = requests.post(auth_url, headers=auth_headers, json=auth_payload)

# Check if the response contains the access token
if auth_response.status_code == 200:
    auth_data = auth_response.json()
    access_token = auth_data.get("access_token")
    if not access_token:
        print("Error: 'access_token' not found in the response")
        exit(1)
else:
    print(f"Error: Authentication request failed with status code {auth_response.status_code}")
    exit(1)

# Step 2: Create a consent request
consent_url = "https://fiu-sandbox.setu.co/v2/consents"
consent_headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "x-product-instance-id": "5e3d24af-8b2c-403e-bef4-295d28d49872"
}
new_vua = "9894049102@onemoney"  # Replace with the new VUA

consent_payload = {
    "consentDuration": {
        "unit": "MONTH",
        "value": "24"
    },
    "vua": new_vua,
    "dataRange": {
        "from": "2022-12-01T00:00:00Z",
        "to": "2023-08-12T00:00:00Z"
    },
    "context": []
}
consent_response = requests.post(consent_url, headers=consent_headers, json=consent_payload)
consent_data = consent_response.json()

# Extract the consent ID and URL
consent_id = consent_data.get("id")
consent_approval_url = consent_data.get("url")

# Print the consent approval URL for manual approval
print("Consent Approval URL:", consent_approval_url)



# Step 3: Periodically check consent status until it is approved
if consent_id:
    consent_status_url = f"https://fiu-sandbox.setu.co/v2/consents/{consent_id}"
    while True:
        consent_status_response = requests.get(consent_status_url, headers=consent_headers)
        consent_status_data = consent_status_response.json()
        print("Consent Status:", consent_status_data)

        if "status" in consent_status_data:
            if consent_status_data["status"] == "ACTIVE":
                break
            elif consent_status_data["status"] == "FAILED":
                print("Consent request was rejected.")
                exit(1)
            else:
                print("Consent request is not yet approved. Waiting...")
                time.sleep(10)  # Wait for 10 seconds before checking again
        else:
            print("Error: 'status' key not found in the consent status response")
            exit(1)

    # Step 4: Create a data session
    session_url = "https://fiu-sandbox.setu.co/v2/sessions"
    session_payload = {
        "consentId": consent_id,
        "dataRange": {
            "from": "2022-12-01T00:00:00Z",
            "to": "2023-08-12T00:00:00Z"
        },
        "format": "json"
    }
    session_response = requests.post(session_url, headers=consent_headers, json=session_payload)

    # Print the response for debugging
    print("Session Creation Status Code:", session_response.status_code)
    print("Session Creation Response Body:", session_response.text)

    if session_response.status_code == 201:
        session_data = session_response.json()
        session_id = session_data.get("id")
        if not session_id:
            print("Error: 'id' not found in the session creation response")
            exit(1)
    else:
        print(f"Error: Session creation request failed with status code {session_response.status_code}")
        exit(1)

    # Step 5: Fetch financial data
    fetch_data_url = f"https://fiu-sandbox.setu.co/v2/sessions/{session_id}"
    fetch_data_response = requests.get(fetch_data_url, headers=consent_headers)
    financial_data = fetch_data_response.json()
    print("Financial Data:", financial_data)
else:
    print("Error: 'id' not found in the consent creation response")
    exit(1)
