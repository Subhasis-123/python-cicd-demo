from flask import Flask, jsonify

app = Flask(__name__)


def add_numbers(a, b):
    return a + b


@app.route("/")
def home():
    return jsonify({
        "message": "Hello! My Python app is running in Docker. this is first docker code",
        "result": add_numbers(10, 20)
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

