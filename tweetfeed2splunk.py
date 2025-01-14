import requests
import hashlib
import time
import json

SPLUNK_HEC_URL = "YOUR_SPLUNK_HOST"
SPLUNK_HEC_TOKEN = "YOUR_HEC_KEY"


def send_to_splunk(log_data):
    headers = {
        'Authorization': f'Splunk {SPLUNK_HEC_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "event": log_data,
        "index": "twitterstream",  
        "sourcetype": "_json" 
    }

    response = requests.post(SPLUNK_HEC_URL, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print("Log enviado com sucesso!")
    else:
        print(f"Erro ao enviar log: {response.status_code} - {response.text}")

def generate_hash(log):
    log_str = json.dumps(log, sort_keys=True)
    return hashlib.md5(log_str.encode('utf-8')).hexdigest()

def fetch_logs():
    url = "https://api.tweetfeed.live/v1/today"
    response = requests.get(url)
    logs = response.json()
    
    seen_hashes = set()
    unique_logs = []

    for log in logs:
        log_hash = generate_hash(log)
        if log_hash not in seen_hashes:
            seen_hashes.add(log_hash)
            unique_logs.append(log)

    return unique_logs

def main():
    processed_hashes = set()  
    
    while True:
        print("Consultando API...")
        logs = fetch_logs()

        for log in logs:
            log_hash = generate_hash(log)
            if log_hash not in processed_hashes:
                print("Enviando log para o Splunk...")
                send_to_splunk(log)
                processed_hashes.add(log_hash)
        
        time.sleep(300)

if __name__ == "__main__":
    main()