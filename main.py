import os

from flask import Flask, jsonify, request
from data.db_session import *
from data.models import QueryState

app = Flask(__name__)
os.mkdir("database")
global_init('database/querystate.db')
session = create_session()
session.add(QueryState(state_yellow=False, state_red=False))
session.commit()


@app.route('/new_signal', methods=['POST'])
def new_signal():
    res = {'status': 'ok'}
    state_yellow, state_red = request.json['first'], request.json['second']
    q_state = session.get(QueryState, 1)
    q_state.state_yellow = state_yellow
    q_state.state_red = state_red
    session.commit()
    return jsonify(res)


@app.route('/get_state', methods=['GET'])
def get_state():
    res = {}
    query_state = session.query(QueryState).first()
    res['state_yellow'] = query_state.state_yellow
    res['state_red'] = query_state.state_red
    return jsonify(res)


if __name__ == '__main__':
    app.run()
