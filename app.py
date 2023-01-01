from flask import Flask, jsonify
import socket

app = Flask(__name__)


@app.route('/even/<int:n>')
def even(n):
    if n % 2 == 0:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        result = {
            "Number": n,
            "Even": True,
            "Server IP": f"{local_ip}"
        }

    else:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        result = {
            "Number": n,
            "Even": False,
            "Server IP": f"{local_ip}"
        }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
