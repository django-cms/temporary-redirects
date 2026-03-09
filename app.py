import json

with open("redirects.json") as f:
    redirects = json.load(f)


def application(environ, start_response):
    host = environ.get("HTTP_HOST", "").split(":")[0]
    target = redirects.get(host)

    if target:
        start_response("302 Found", [("Location", target)])
        return [b""]

    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Not found"]
