from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit
import eventlet
import logging
import sys
import random

# eventlet.monkey_patch()

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

ROOM = "main_room"
user_colors = {}  # Store colors for each connected user

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    sid = request.sid
    join_room(ROOM)
    color = random_color()
    user_colors[sid] = color
    app.logger.info(f'User connected: {sid}, color: {color}')

    # Notify others of the new user and their color
    emit('user_joined', {'sid': sid, 'color': color}, room=ROOM, include_self=False)

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    app.logger.info(f'User disconnected: {sid}')
    emit('user_left', {'sid': sid}, room=ROOM, include_self=False)
    user_colors.pop(sid, None)

@socketio.on('mouse_move')
def handle_mouse_move(data):
    sid = request.sid
    x = data.get('x')
    y = data.get('y')
    app.logger.debug(f'Mouse move from {sid}: x={x}, y={y}')
    emit('mouse_update', {'sid': sid, 'x': x, 'y': y}, room=ROOM, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
