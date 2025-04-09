import os
from opengateway_sandbox_sdk import numberverification, devicelocation, ClientCredentials
from flask import Flask
import requests

application = Flask(__name__)
phone_number = "+34654178356"

credentials = ClientCredentials(
    client_id="dde9ced8-3851-4555-9678-4aabd67463dd",
    client_secret="32b79d3e-5304-4998-876a-e99b49821a27"
)


if __name__ == "__main__":
    application.run(debug=True)