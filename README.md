# redditext

A simple web app that lets you click a button to get a random reddit post (title read
by yours truly). The project includes a server and a web app. The server is written in [Python](https://www.python.org/), 
using [Flask](https://flask.palletsprojects.com/en/2.2.x/). The web app is written in [TypeScript](https://www.typescriptlang.org/) 
using [React](https://react.dev/). 'Text to speech' is handled using the [TTS library](https://github.com/coqui-ai/TTS/).

Here is a [demo video](https://www.loom.com/share/d6219272ce7541d9a00f9dcd4dbb6ac3).

_note: this project is not currently suitable for production use!_ 

### Server

Dependencies are managed using [Pipenv](https://pipenv.pypa.io/en/latest/). The version of Python used is
3.8.16 (check out [Pyenv](https://github.com/pyenv/pyenv) for managing Python versions). 

To install dependencies, run:
```
pipenv install
```


To start server, run:

```
pipenv run python main.py
```

from the root of the project.

Server can be accessed at `http://127.0.0.1:5000`.


### Web App

Dependencies are managed using [Yarn](https://yarnpkg.com/). Building is managed using [Vite](https://vitejs.dev/).
To run app, navigate to `./redditext-frontend`, and run:

```
yarn dev

```

The app can be accessed via `http://localhost:5173`.

_note: I'm not really a front end developer. I just needed a UI for this._

### Text to Speech

As stated above, the [TTS](https://github.com/coqui-ai/TTS) text-to-speech library was used to generate
speech from text. I provided a sample of my voice a pretrained model that came with the library. 

### Project Layout
* `redditext` backend module (Python / Flask)
* `redditext-frontend` web app (TypeScript / React)
* `main.py` flask server / routes 
