

from flask import Flask, render_template, jsonify
import threading
import main


app = Flask(__name__)

current_status = "Ready to start"

iris_thread = None
iris_event = threading.Event()

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify({"status": current_status})

    

@app.route("/start", methods=["POST"])
def start_assistant():
    global iris_thread, current_status
    
    iris_event.set() 
    current_status = "Say 'Irish'..."
    # iris_running = True

    if iris_thread is None or not iris_thread.is_alive():
        iris_thread = threading.Thread(target=main.start_iris, args=(iris_event,))
        iris_thread.daemon = True
        iris_thread.start()

    return jsonify({"status": "Irish started"})

@app.route("/stop", methods=["POST"])
def stop_assistant():
    global current_status
    iris_event.clear()
    current_status = "Idle"
    return jsonify({"status": "Irish stopped"})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)





