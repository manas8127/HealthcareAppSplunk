Install Python Requirements - pip install -r requirements.txt

Get your HEC Token and Passkey through Splunk

First run:

python main.py

This will run the middleware

Then run:

python splunk.py 

This will start streaming data into Splunk you can search by command index=main source="ecg_stream" on Search & Auditing app and also will populate the Webhook accordingly

Thanks:)
