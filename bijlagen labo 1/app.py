from flask import Flask
import os
import redis

redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", "6379"))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

app = Flask(__name__)


@app.route("/")
def index():
    count = redis_client.incr("hits")
    return f"Hello from Flask! This page has been viewed {count} times.\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
