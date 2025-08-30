from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}],
        )
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
