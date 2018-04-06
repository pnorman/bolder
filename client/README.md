## Bolder client-side style

This contains the style which makes use of the vector definitions in [`/vector`](/vector). By default it assumes the tiles are being served locally on port 8080, but this can easily be changed if needed.

The style is written as a Tangram scene file, and can be used in Tangram JS or Tangram ES.

### Development

The easiest way to develop is to run the style locally in Tangram JS. You can do this by serving the scene files locally by running `./serve.py` and browsing to [http://localhost:8081/](http://localhost:8081/) with a recent web browser.

After editing the scene file, just hit reload in the browser. `serve.py` is set up to have the browser not cache the scene files.
