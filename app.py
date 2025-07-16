from sanic import Sanic
from sanic.response import json
from datastar_py import ServerSentEventGenerator as SSE
from datastar_py.sanic import datastar_response

app = Sanic("datastar_app")

# @app.route("/")
# async def hello(request):
#     return json({"message": "Hello, Sanic!"})

app.static("/", "index.html", name="index")
app.static("/static", "./static/", name="static")

@app.get("/init")
@datastar_response
async def init(request):
    # Initialize the DataStar SSE generator
    sse = SSE()
    html = "<main id='main' class='playfair-display-500'><h1>DataStar SSE Example</h1></main>"
    return  sse.patch_elements(html)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)