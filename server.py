from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'mySecret'
import random

@app.route('/')
def index():
    if 'gold' in session:
        session['gold'] = session['gold']
    else:
        session['gold'] = 0
    if 'activities' in session:
        session['activities'] = session['activities']
    else:
        session['activities'] = []
    return render_template("index.html", gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building_map = {
        "farm":random.randint(0,20),
        "cave":random.randint(5,10),
        "house":random.randint(2,5),
        "casino":random.randint(-50,50)
    }
    if request.form['building'] == 'farm':
        building = "farm"
        new_gold = building_map[building]
        activity = {
            "content":"Earned " + str(new_gold) + " gold at the farm!",
            "color":"text-success"
        }
        session['activities'].append(activity)
        session['gold'] = session['gold'] + new_gold
    if request.form['building'] == 'cave':
        building = "cave"
        new_gold = building_map[building]
        activity = {
            "content":"Earned " + str(new_gold) + " gold at the cave!",
            "color":"text-success"
        }
        session['activities'].append(activity)
        session['gold'] = session['gold'] + new_gold
    if request.form['building'] == 'house':
        building = "house"
        new_gold = building_map[building]
        activity = {
            "content":"Earned " + str(new_gold) + " gold at the house!",
            "color":"text-success"
        }
        session['activities'].append(activity)
        session['gold'] = session['gold'] + new_gold
    if request.form['building'] == 'casino':
        building = "casino"
        new_gold = building_map[building]
        if new_gold > 0:
            activity = {
                "content":"Earned " + str(new_gold) + " gold at the casino!",
                "color":"text-success"
            }
        if new_gold < 0:
            activity = {
                "content":"Entered a casino and lost " + str(new_gold) + " gold... Ouch...",
                "color":"text-danger"
            }
        session['activities'].append(activity)
        session['gold'] = session['gold'] + new_gold
    session.modified = True
    print(session['activities'])
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)