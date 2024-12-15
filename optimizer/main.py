from flask import Flask, render_template, request
from Artifact import *
import json
import csv

app = Flask(__name__)

@app.get('/')
def form():
    data = get_item_json()
    return render_template('index.html',data=data)

@app.post('/rawdata')
def get_form_data():
    game = request.form['game']
    setArti = request.form['set']
    main_sts = request.form['main']
    arti_type = request.form['arti_type']
    ##
    s1 = request.form['sub1']
    os1 = request.form['opset1']

    s2 = request.form['sub2']
    os2 = request.form['opset2']

    s3 = request.form['sub3']
    os3 = request.form['opset3']

    s4 = request.form['sub4']
    os4 = request.form['opset4']

    main_stat_val = find_main_stat_val(main_sts)

    artifact = Artifact(
        name=arti_type,
        set_name=setArti,
        artifact_type=arti_type,
        main_stat={"name": main_sts, "value": main_stat_val},
        sub_stats=[
            {"name": s1, "value": os1},
            {"name": s2, "value": os2},
            {"name": s3, "value": os3},
            {"name": s4, "value": os4}]
    )


    write_json(artifact)



    return render_template('index.html')
@app.get('/show')
def show():
    data = get_item_json()
    filtered_mixer_box = [box for box in data if box]
    return render_template('show.html',data=filtered_mixer_box)

def write_json(artifact):
    json_str = json.dumps(artifact.__dict__)
    with open("data.json", "r+") as file:
        content = file.read().strip()
        if content:
            file.seek(0)  # Move cursor to the start
            file.write(content[:-1] + ',')  # Write updated content
        else:
            file.write('[')  # Start the JSON array if it's empty
    with open("data.json", "a") as file:
        file.write(json_str + ']')

def find_main_stat_val(main_stat):
    '''
    hp plat 4780//
    atk 311//
    hp%  atk%  46.6 //
    ele 46.6
    def 58.3% //
    em 187
    er 51.8%
    cr 31.1%
    cd 62.2
    heal 35.9%
    '''
    val = False
    if main_stat == 'HP':
        val = 4780
    elif main_stat == 'ATK':
        val = 311
    elif main_stat == 'DEF%':
        val = '58.3%'
    elif main_stat == 'EM':
        val = 187
    elif main_stat == 'ER':
        val = '51.8%'
    elif main_stat == 'CR':
        val = '31.1%'
    elif main_stat == 'CD':
        val = '62.2%'
    elif main_stat == 'HEAL':
        val = '35.9%'
    else:
        val = '46.6%'
    return val

def get_item_json():
    flower_box = []
    feather_box = []
    sand_box = []
    goblet_box = []
    circlet_box = []
    big_box = [flower_box, feather_box, sand_box, goblet_box, circlet_box]
    with open("data.json", "r+") as file:
        items = json.load(file)
        for item in items:
            artifact = Artifact(
                name=item['name'],
                set_name=item['set_name'],
                artifact_type=item['artifact_type'],
                main_stat=item['main_stat'],
                sub_stats=item['sub_stats']
                )

            if item['artifact_type'] == 'Flower':
                flower_box.append(artifact)
            elif item['artifact_type'] == 'Feather':
                feather_box.append(artifact)
            elif item['artifact_type'] == 'Sand':
                sand_box.append(artifact)
            elif item['artifact_type'] == 'Goblet':
                goblet_box.append(artifact)
            elif item['artifact_type'] == 'Circlet':
                circlet_box.append(artifact)

        allPossible(big_box)
        return big_box


def extract():
    import re
    with open('templates/bodyfect.html','r') as file:
        for line in file:
            line = line.strip()
            pattern = r'<b class="a-bold">(.*?)</b>'
            match = re.search(pattern, line)

            if match:
                print(match.group(1))
    



if __name__ == '__main__':
    # get_item_json()
    app.run(debug=True)

'''
web show fact
read json//
cal //
filter val that need//
sort output
delete fact
check fact dup
'''