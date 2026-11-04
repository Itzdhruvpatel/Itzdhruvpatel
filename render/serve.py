"""Local render server: serves this repo and saves the frames the render page POSTs. Not used by the profile itself."""
import base64
import re
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent.parent
FRAMES = Path(__file__).parent / "frames"


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        match = re.fullmatch(r"/frame/([a-z0-9-]+)/(\d+)", self.path)
        if not match:
            self.send_error(404)
            return
        data = self.rfile.read(int(self.headers["Content-Length"]))
        folder = FRAMES / match[1]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / f"{int(match[2]):03}.png").write_bytes(base64.b64decode(data.split(b",", 1)[1]))
        self.send_response(204)
        self.end_headers()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 5180), partial(Handler, directory=str(ROOT))).serve_forever()
