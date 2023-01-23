from io import StringIO

import requests



data={"file": o,"args": StringIO(json.dumps(kwargs))}
requests.post("http://localhost:8080",data=data)
