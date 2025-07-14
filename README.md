# Grafana Synop Visualization HTTP Server

This project features a simple HTTP server developed with Flask, designed to visualize current weather conditions using images. The server provides access to `.png` files that represent various meteorological phenomena based on synoptic codes received from weather stations. It is built for easy integration, particularly with tools like Grafana, to enable dynamic and visual weather displays.

## Key Features

* **HTTP Server:** Built using the Flask web framework, this server efficiently handles requests for weather-related images.
* **Synop Code Visualization:** The core functionality involves converting standard synoptic codes into their corresponding visual representations (images), thereby allowing for intuitive visualization of meteorological data from observation stations.
* **PNG Image Support:** The server is specifically configured to securely serve `.png` image files from a predefined set of allowed weather icons.
* **Basic Security Mechanisms:** Includes fundamental path validation (`is_safe_path`) and file whitelisting to prevent access to unauthorized files or directory traversal, ensuring that only specified weather icons can be served.
* **Easy Deployment:** The application runs on `0.0.0.0` at port `5000` by default, making it straightforward to deploy and access within a network.

## How to Use

Simply run the `app.py` file to start the server:

```bash
python app.py

Images can then be accessed via the `/Icons/<filename>` endpoint, for example:
`http://your-server-ip:5000/Icons/0.png`
`http://your-server-ip:5000/Icons/21.png`
The allowed filenames (without the `.png` extension in the URL path, but served as `.png`) correspond to specific synop codes.

This project serves as a clear and functional example for visualizing meteorological data.
