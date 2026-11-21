"""ChatGPT generated this Python dashboard and its interface."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent

def load_results():
    frame = pd.read_csv(ROOT / "results/forecasts.csv")
    bundle = joblib.load(ROOT / "results/models.joblib")
    for name, model in bundle["models"].items():
        values = np.maximum(0, frame.lag1 + model.predict(frame[bundle["features"]]))
        np.testing.assert_allclose(values, frame[name])
        frame[name] = values
    w = bundle["weight"]
    stack = w * frame["Random Forest"] + (1-w) * frame["Gradient Boosting"]
    np.testing.assert_allclose(stack, frame.Stacking)
    frame["Stacking"] = stack
    methods = ["Last week", "Random Forest", "Gradient Boosting", "Stacking"]
    scores = frame[methods].sub(frame.actual, axis=0).abs().mean().sort_values()
    return json.dumps(dict(rows=frame.to_dict("records"), scores=scores.to_dict(), weight=w,
                           groups=pd.read_csv(ROOT / "results/movement.csv").to_dict("records")),
                      allow_nan=False).encode()

if __name__ == "__main__":
    payload = load_results()
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/":
                body, kind = (ROOT / "dashboard.html").read_bytes(), "text/html; charset=utf-8"
            elif self.path == "/results":
                body, kind = payload, "application/json"
            else:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", kind)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    port = int(os.environ["PORT"]) if "PORT" in os.environ else 8766
    host = "0.0.0.0" if "PORT" in os.environ else "127.0.0.1"
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"Listening on {host}:{port}", flush=True)
    server.serve_forever()
