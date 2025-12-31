import requests
api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased"
headers = {
    "Authorization": "Bearer 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"
}
text_input = input("Enter text for sentiment analysis: ")
response = requests.post(api_url,headers=headers,json={"inputs": text_input})
if response.status_code==200:
    result=response.json()
    print(f"sentiment: {result[0]['label']} with confidence score:{result[0]['score']}")
else:
    print(f"error: {response.status_code}")