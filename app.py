import os

from flask import Flask, jsonify, request
from data.db_session import *
from data.query_state_model import QueryState

app = Flask(__name__)
if not os.path.isdir("database"):
    os.mkdir("database")
global_init('database/queue_state.db')
session = create_session()
session.add(QueryState(old_state_yellow=False, old_state_red=False, new_state_yellow=False, new_state_red=False))
session.commit()


@app.route('/new_signal', methods=['POST'])
def new_signal():
    res = {'status': 'ok'}
    state_yellow, state_red = request.json['first'], request.json['second']
    q_state = session.get(QueryState, 1)
    q_state.old_state_yellow = q_state.new_state_yellow
    q_state.old_state_red = q_state.new_state_red
    q_state.new_state_red = state_red
    q_state.new_state_yellow = state_yellow
    session.commit()
    session.close()
    return jsonify(res)


@app.route('/get_state', methods=['GET', 'POST'])
def get_state():
    res = {}
    queue_state = session.query(QueryState).first()
    res['old_state_yellow'] = queue_state.old_state_yellow
    res['old_state_red'] = queue_state.old_state_red
    res['new_state_yellow'] = queue_state.new_state_yellow
    res['new_state_red'] = queue_state.new_state_red
    queue_state.old_state_yellow = queue_state.new_state_yellow
    queue_state.old_state_yellow = queue_state.new_state_red
    session.close()
    return jsonify(res)


if __name__ == '__main__':
    app.run()
