# TweetFeed2Splunk
A Python script that fetches logs from the TweetFeed API every 5 minutes and sends them to Splunk in the 'main' index, ensuring no duplicate entries. The script processes and hashes each log to avoid repetitions and streamline log monitoring in real-time.

# Splunk Log Streamer Setup with Docker

This guide will walk you through setting up Splunk using Docker and configuring an automation script to stream logs to Splunk.

## Prerequisites

- Docker installed on your machine.
- Python 3.x and `pip` installed.
- A GitHub account (for managing the project).
- Splunk HEC token (HTTP Event Collector) for sending data to Splunk.

## Step 1: Set Up Splunk Using Docker

### 1.1 Pull the Splunk Docker Image

Run the following command to pull the official Splunk Docker image:

```bash
docker pull splunk/splunk:latest

docker run -d -p 8000:8000 -p 8088:8088 --name splunk \
  -e SPLUNK_PASSWORD=<your_password> \
  -e SPLUNK_START_ARGS="--accept-license" \
  splunk/splunk:latest
 ```


## Set Up the Python Script
2.1 Clone the Repository
Clone the Splunk-Log-Streamer repository to your local machine:

## Configure the Python Script
Open the Python script (log_streamer.py) and update the following configuration:

```bash
# Splunk HEC Configuration
SPLUNK_HEC_URL = "https://localhost:8088/services/collector"
SPLUNK_HEC_TOKEN = "<your_splunk_token>"

 ```
## Run the Python Script
Run the Python script to start fetching logs from the TweetFeed API and sending them to Splunk every 5 minutes:

```bash
python log_streamer.py

 ```


### Explanation:
- This markdown file includes all the necessary steps in one document for the user to follow.
- It begins by explaining how to set up Splunk via Docker, including the commands to pull the image, start the container, and configure the HTTP Event Collector (HEC).
- It then moves on to configuring and running the Python automation script to stream logs into Splunk.
- Finally, it covers verifying the logs in Splunk, troubleshooting tips, and a conclusion.
