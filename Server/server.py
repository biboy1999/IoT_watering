from sanic import Sanic
from sanic.response import json

app = Sanic("App Name")

@app.get("/save")
async def test(request):    
    return json({"status": "fuck"})

@app.get("/temp")
async def login(request):
    return json({"temp":"99.9"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
