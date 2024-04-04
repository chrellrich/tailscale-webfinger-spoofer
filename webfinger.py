from flask import Flask, jsonify
import argparse

app = Flask(__name__)

@app.route('/.well-known/webfinger')
def webfinger():
    response_data = {
        "subject": "acct:" + args.email,
        "links": [
            {
                "rel": "http://openid.net/specs/connect/1.0/issuer",
                "href": args.issuer_url
            }
        ]
    }
    return jsonify(response_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flask WebFinger Server')
    parser.add_argument('--email', required=True, help='Email address')
    parser.add_argument('--issuer-url', required=True, help='Issuer URL')
    parser.add_argument('--port', type=int, default=5000, help='Port number (default: 5000)')
    parser.add_argument('--host', default='0.0.0.0', help='Host address (default: 0.0.0.0)')
    args = parser.parse_args()

    app.run(host=args.host, port=args.port)
