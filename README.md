This project presents a simple HTTP server written in Flask, designed to visualize current weather conditions using images. The server provides access to .png files representing various meteorological phenomena based on synoptic codes from weather stations. It is designed to be easily integrable, for example, into Grafana for dynamic weather display.

Key Features:

HTTP Server: Developed using the Flask web framework, the server handles requests for weather images.

Synop Code Visualization: Converts synoptic codes into corresponding images, allowing for a visual representation of data from weather stations.

PNG Image Support: The server is configured to securely serve .png files.

Security Mechanisms: Includes basic checks to prevent access to unauthorized files and directories.

Easy Deployment: The application runs on port 5000 and is ready for deployment.

The project is minimalistic and serves as an example of a simple application for visualizing meteorological data.
