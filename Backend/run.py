from Backend import app, socketio

print(__name__)
if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)

