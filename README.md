# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Setting up secrets.py
To link the app to your own Trello board, create an API key and token [here](https://trello.com/app-key) and paste them in a file called secrets.py which should look like this:
```python
TRELLO_API_KEY = "32c28cb9001dc2b9c5d926645a3bf835"
TRELLO_API_TOKEN = "7ff7347e9c264e348adce9432b27b23b6b35f5d200941d08445a5095083d5669"
```
