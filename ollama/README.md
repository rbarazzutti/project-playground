
accéder au serveur en ligne de commande
```bash
curl -X POST https://llm-01.fever.ch/api/generate \
     -H 'Content-Type: application/json'  -H 'X-API-Key: key1'  \
     -d '{
       "prompt": "combien de patte a un chat",
       "model": "llama3.2:1b"
     }'
```


```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

