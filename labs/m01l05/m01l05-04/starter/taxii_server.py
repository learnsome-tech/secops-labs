"""A small stand-in for a TAXII 2.1 server, for the lesson only.

It serves one collection's Get Objects endpoint on 127.0.0.1, honouring
the added_after, limit and next parameters and returning the TAXII
envelope (more, next, objects). A real TAXII server also offers discovery,
API roots, manifests, versions and authentication; this one does not.
The date an object was added to the collection is taken from its
modified time.
"""
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

COLLECTION = "91a7b528-80eb-42ed-a74d-c6fbd5a26116"
TAXII = "application/taxii+json;version=2.1"

with open("intel_bundle.json") as f:
    OBJECTS = sorted(json.load(f)["objects"], key=lambda o: o["modified"])


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def send(self, status, body, headers=()):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", TAXII)
        for name, value in headers:
            self.send_header(name, value)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlsplit(self.path)
        if url.path != f"/api1/collections/{COLLECTION}/objects/":
            return self.send(404, {"title": "Unknown collection"})
        if self.headers.get("Accept", "").replace(" ", "") != TAXII:
            return self.send(406, {"title": "Send Accept: " + TAXII})
        query = parse_qs(url.query)
        after = query.get("added_after", [""])[0].replace("Z", ".000Z")
        limit = int(query.get("limit", ["100"])[0])
        start = int(query.get("next", ["0"])[0])
        rows = [o for o in OBJECTS if o["modified"] > after]
        page = rows[start:start + limit]
        more = start + limit < len(rows)
        body = {"more": more, "objects": page}
        if more:
            body["next"] = str(start + limit)
        headers = []
        if page:
            headers = [("X-TAXII-Date-Added-First", page[0]["modified"]),
                       ("X-TAXII-Date-Added-Last", page[-1]["modified"])]
        self.send(200, body, headers)


def start():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{server.server_address[1]}"
