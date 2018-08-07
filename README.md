# Bolder Style

This is a client-side map style for use with OpenStreetMap data. The style can be broken down into two parts: the client-side rendering rules, and the server-side vector tile definitions. As such, it's like two projects in one, which are closely coupled.

## Installation

1. Load the data and install the software as instructed [in the vector README](/vector/README.md). Run Tegola.

2. Check that [`http://localhost:8080/`](http://localhost:8080/) has a Tegola preview page.

3. Serve the client style with `cd client && ./serve.py` and open [`http://localhost:8081/`](http://localhost:8081/) in a web browser. Detailed instructions can be found [in the client README](client/README.md).
