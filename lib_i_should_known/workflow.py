import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

df = pd.read_csv('resource/d4_loot.csv')
summary = df.groupby('Resource').sum()
plt.clf()
plt.bar(summary.index, summary['tree'])
plt.savefig('static/chart.png')

app = Flask(__name__)

@app.get('/')
def mainp():
    return render_template('chrt.html',chart='static/chart.png')

if __name__ == '__main__':
    app.run()