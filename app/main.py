import sys
import os

# Dynamically add path to src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from predict import predict_url, predict_email, predict_sender

print("=== PHISHING DETECTOR ===")
print("1. Check URL")
print("2. Check Email Text")
print("3. Check Sender Email ID")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    url = input("Enter URL: ")
    result = predict_url(url)
    print("Result:", result)

elif choice == '2':
    text = input("Paste Email Text: ")
    result = predict_email(text)
    print("Result:", result)

elif choice == '3':
    email = input("Enter Sender Email ID: ")
    result = predict_sender(email)
    print("Result:", result)

else:
    print("❌ Invalid Choice")
