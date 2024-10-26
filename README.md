
This repo contains a few scripts demonstrating poor code that should trigger security alerts, dependencies which should be scanned and reported, and simple metrics observability with Prometheus.

## Setting up a local environment

To run these locally, you will need to have installed:
 - Docker Desktop
 - Prometheus
 - Some git client
    - For a GUI interface, Github Desktop and Fork are good choices.

## Build and Run the Docker image

### Building local image

To build and run a local image:

 - Build an image with `docker build -t justatest .`

 - Run the image with `docker run -it -p 8080:5000/tcp justatest bash -c 'cd /app;. .venv/bin/activate;python3 promtest.py'`

### Running the pre-built image in the repo

With each commit to this repo, Github actions will build and scan a new image, which you can run directly instead of building locally:

`docker run -it -p 8080:5000/tcp ghcr.io/crondaemon001/justatest123:latest bash -c 'cd /app;. .venv/bin/activate;python3 promtest.py'`

### After Running

The commands above will automatically initialize the `promtest.py` python script in the container, which starts up a flask server on port 5000 inside the container, accessible from `localhost:8080` on your local machine.

Accesing the `localhost:8080/` and `localhost:8080/other` endpoints will create OTel metrics, which prometheus can observe.  You can also go to `localhost:8080/events` to see the metrics directly.

## Observing with Prometheus

After installing Prometheus in your local environment, run it with 

`prometheus --config.file=prometheus.yml` 

The configuration will tell prometheus to monitor the `/metrics` endpoint on `localhost:8080`, and gather metrics for the flask app.  

A prometheus GUI will be hosted on `localhost:9090`.  You can type in the event box to select events to montor, and select the "Graph" tab to graph them.  The `view_main_total` metric is associated with the viewcount for the main page (`localhost:8080/`), and the `view_other_total` metric is associated with the `localhost:8080/other` page.  Additionally, the `random_metric` metric is fed by a random number which updates every few seconds.

## Code scanning

This repo (crondaemon001/justatest123) is setup with GitHub actions to monitor and track security issues with committed code and image builds.  Check the Security tab to see enabled security options, and the Code Scanning section to see alerts that were triggered from the `scanthis.py` script.  

Under the Actions tab you can also see CodeQL, Docker Image CI, and trivy actions setup which enforce the code scanning, image builds, and image scans respectively.  You can check the action results and see some failures and security scan results.



