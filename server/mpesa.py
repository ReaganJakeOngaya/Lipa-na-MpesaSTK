import requests
from flask import request, jsonify
from datetime import datetime
import base64
from config import CONSUMER_KEY, CONSUMER_SECRET, LIPA_NA_MPESA_PASSKEY, BUSINESS_SHORTCODE

# Get access token
def get_access_token():
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(api_url, auth=(CONSUMER_KEY, CONSUMER_SECRET))
    token = response.json().get('access_token')
    return jsonify({"access_token": token})

# STK push function
def lipa_na_mpesa():
    access_token = request.headers.get('Authorization')
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer " + access_token}
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(BUSINESS_SHORTCODE.encode() + LIPA_NA_MPESA_PASSKEY.encode() + timestamp.encode()).decode('utf-8')
    
    payload = {
        "BusinessShortCode": BUSINESS_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,  # Example amount
        "PartyA": "2547XXXXXXXX",  # Customer phone number
        "PartyB": BUSINESS_SHORTCODE,
        "PhoneNumber": "2547XXXXXXXX",
        "CallBackURL": "https://yourdomain.com/callback",
        "AccountReference": "Test123",
        "TransactionDesc": "Payment for goods"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return jsonify(response.json())

# Handle Mpesa callback
def mpesa_callback():
    data = request.json
    # Process the callback data
    return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})
