import json


def open_json(text):
    with open('candidates.json', 'r', encoding='utf-8') as canditates:
        return json.load(canditates)
    

def format_canditates(canditates_list):
    result = '<pre>'
    for canditate in canditates_list:

        result += (
            f"Имя кандитата - {canditate['name']}\n"
            f"Позиция кандидата {canditate['position']}\n"
            f"Навыки через запятую {canditate['skills']}\n\n"
        )
    result += '<pre>'

    return result


def get_canditate_by_id(canditates_list, canditate_id):

    for canditate in canditates_list:
        if canditate['id'] == canditate_id:
            return canditate


def get_canditate_by_skills(canditates_list, canditate_skill):
    result = []

    for canditate in canditates_list:
        canditate_skills = canditate['skills'].lower().split(', ')

        if canditate_skill in canditate_skills:
            result.append(canditate)

    return result        
