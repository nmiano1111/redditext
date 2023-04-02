from flask import jsonify, request, Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from redditext.clients.reddit import Reddit
from redditext.config.utils.configreader import YAMLConfigReader
from redditext.util import process_url
from redditext.text_to_speech import SpeechGenerator

import logging
from logging import Logger

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # just for dev!

CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

conf = YAMLConfigReader()
subs = conf.read_config()
subs = subs['subs']

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
logging.info("FUCK")
redditext_logger = logging.getLogger(__name__)

redditext_logger.info("WHAT THE FUCK")

reddit = Reddit(subs=subs, logger=redditext_logger)

speech_generator = SpeechGenerator(logger=redditext_logger)


def emit_audio(title):
    file = speech_generator.generate_speech(title)
    socketio.emit('audio', {'file_path': f'/{file}.wav'})


@app.route("/reddit_post")
def json_api():
    sub = request.args.get('sub')
    cat = request.args.get('cat', default='hot')
    window = request.args.get('window')

    post = reddit.get_post(sub=sub, cat=cat, window=window)
    post['url'] = process_url(post)

    socketio.start_background_task(emit_audio, post['title'])

    return jsonify(post)


@socketio.on('connect')
def handle_connect():
    app.logger.info('Client connected')

    def send_message():
        socketio.emit('message', {'data': 'Hello, there!'})

    socketio.start_background_task(send_message)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
