from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest
import random
import time
import threading

app = Flask(__name__)

# Define view counter metrics for pages
view_main_metric = Counter('view_main', 'Number of views on main page')
view_other_metric = Counter('view_other', 'Number of views on other page')

# Define a gauge metric
random_metric = Gauge('random_metric', 'A random metric')

def update_random_metric():
    while True:
        random_metric.set(random.uniform(0, 100))
        time.sleep(5)  # Update the metric every 5 seconds

# Start the thread to update the random metric
thread = threading.Thread(target=update_random_metric)
thread.daemon = True  # So the thread dies when the main thread dies
thread.start()

## Create route for main page
@app.route('/')
def index():
    view_main_metric.inc()  # Increment the view counter
    return "Hello, World!"

## Create route for /other page
@app.route('/other')
def other_page():
    view_other_metric.inc()  # Increment the view counter
    return "This is the other page!"
    
@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

