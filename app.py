from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
from helper import *

matplotlib.use('Agg')

app = Flask(__name__)

data = load_data()

@app.route("/")
def index():
	# generate value for cards

	percent_fraud = float(pd.crosstab(index=data['fraud_reported'],columns='count',normalize=True).loc['Y']*100)
	fraud_loss = data.groupby('fraud_reported').sum()['total_claim_amount'].loc['Y']
	average_claim = data.groupby('fraud_reported').median()['total_claim_amount'].loc['Y']

	# compile card values as card_data
	 
	card_data = dict(
		percent_fraud = f'{percent_fraud}%',
		fraud_loss = f'US$ {fraud_loss:,}',
		average_claim = f'US$ {average_claim:,}'
	)

	# generate plot
	plot_age_res = plot_age(data)
	plot_premium_res = plot_premium(data)
	plot_incident_res = plot_incident(data)
	plot_report_res = plot_report(data)
	plot_hourgroup_res = plot_hourgroup(data)
	plot_incidenthour_res = plot_incidenthour(data)    
    
	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_age_res=plot_age_res,
		plot_premium_res=plot_premium_res,
		plot_incident_res=plot_incident_res,
		plot_report_res=plot_report_res,                          
		plot_hourgroup_res=plot_hourgroup_res,
		plot_incidenthour_res=plot_incidenthour_res                           
		)


if __name__ == "__main__": 
    app.run(debug=True)
