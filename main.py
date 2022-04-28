import json

from flask import Flask

from utils import format_canditates, get_canditate_by_id, get_canditate_by_skills, open_json

app = Flask(__name__)


@app.route('/')
def page_index():
    canditate_list = open_json('candidates.json')
    
    return format_canditates(canditate_list)


@app.route('/candidates/<int:candite_id>')
def page_candidates(candite_id):
    canditate_list = open_json('candidates.json')

    candidate = get_canditate_by_id(canditate_list, candite_id)

    result = f'<img src="{candidate["picture"]}">'


    return result + format_canditates([candidate])


@app.route('/skills/<skill>')
def page_skills(skill):
    canditate_list = open_json('candidates.json')

    return format_canditates(get_canditate_by_skills(canditate_list, skill))


app.run()    


