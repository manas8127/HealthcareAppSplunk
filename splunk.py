import pandas as pd
import requests
import json
import time

SPLUNK_HEC_URL = "http://<HEC-URL>:8088/services/collector"
SPLUNK_TOKEN = "<HEC-TOKEN>"

headers = {
    "Authorization": f"Splunk {SPLUNK_TOKEN}",
    "Content-Type": "application/json"
}

df = pd.read_csv("dataset.csv")
df = df.where(pd.notnull(df), None) 
df = df.dropna()
df.head(10)

df_stroke_1 = df[df["stroke"] == 1]
df_stroke_0 = df[df["stroke"] == 0]

df_sampled_1 = df_stroke_1.sample(n=45, random_state=20)
df_sampled_0 = df_stroke_0.sample(n=45, random_state=20)

df_balanced = pd.concat([df_sampled_1, df_sampled_0]).sample(frac=1, random_state=42).reset_index(drop=True)

df_balanced.head(), df_balanced["stroke"].value_counts()

stroke_counts = df['stroke'].value_counts()

print("Stroke value counts:")
print(stroke_counts)

for idx, row in df.iterrows():
    row_dict = row.dropna().to_dict()
    row_dict["sensor"] = "ECG-01"  # Add sensor name

    payload = {
        "event": row_dict,
        "sourcetype": "_json",
        "index": "main",
        "source": "ecg_stream",
        "host": "manas_laptop"
    }

    # payload = {
    #     "event": json.dumps(row_dict),  # Serialize inner dict
    #     "sourcetype": "_json",
    #     "index": "main",
    #     "source": "ecg_stream",
    #     "host": "scde-cxgwzw5yl1r0ayqbu"
    # }

    try:
        response = requests.post(SPLUNK_HEC_URL, headers=headers, data=json.dumps(payload), verify=True)
        if response.status_code == 200:
            print(f"✅ Row {idx} sent successfully")
        else:
            print(f"❌ Row {idx} failed: {response.text}")
    except Exception as e:
        print(f"❌ Exception on row {idx}: {str(e)}")

    time.sleep(0.2)  # Optional delay

