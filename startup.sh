echo "*/5 * * * *  blob_reading.py" | crontab -
service cron start
pip install -r requirements.txt && python app.py

