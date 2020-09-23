import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from io import BytesIO
import base64

def load_data():
    # Read data
    insurance = pd.read_csv('data/autoinsurance.csv')
 
    return(insurance)


def plot_age(data):
    
    # ---- Age group of customer

    def age_grouping(data):
        if(data.age <= 24):
            return '19 - 24'
        elif(data.age > 24 and data.age <= 30) : 
            return '25 - 30'
        elif(data.age > 30 and data.age <= 35) : 
            return '31 - 35'
        elif(data.age > 35 and data.age <= 40) : 
            return '36 - 40'
        elif(data.age > 40 and data.age <= 45) : 
            return '41 - 45'
        elif(data.age > 45 and data.age <= 50) : 
            return '46 - 50'
        elif(data.age > 50 and data.age <= 55) : 
            return '51 - 55'
        elif(data.age > 55 and data.age <= 59) : 
            return '56 - 59'
        else : 
            return '60+'

    data['age_group'] = data.apply(age_grouping,axis = 1)

    fraud_data = data[data['fraud_reported'] == 'Y']
    age_profile = pd.crosstab(index=fraud_data['age_group'],
            columns='total_fraud',
            values=fraud_data['fraud_reported'],
            aggfunc='count').sort_values(by='age_group', ascending=True)

    ax = age_profile.plot.barh(title = "Fraud Reported by Age group", 
    legend= False, 
    color = '#c34454', 
    figsize = (8,6))
 
    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png', transparent=True)
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

def plot_premium(data):

    def tocolor(data):
        if(data.fraud_reported == 'Y'):
            return '#53a4b1'
        else : 
            return '#c34454'
    
    data.fcolor = data.apply(tocolor,axis=1)
    
    # ---- Months as Customer per Policy Annual Premium

    ax = data.plot.scatter(x= "months_as_customer", 
                        y = "policy_annual_premium",
                       c=data.fcolor,title = "Months as Customer per Policy Annual Premium",
                       figsize=(8, 6))

    
    # Plot Configuration
    lab_y = mpatches.Patch(color='#53a4b1', label='Y')
    lab_n = mpatches.Patch(color='#c34454', label='N')
    plt.legend(handles = [lab_y ,lab_n])
    plt.xlabel("Months as Customer")
    plt.ylabel("Policy Annual Premium")

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)



def plot_incident(data):

    def tonum(data):
        if(data.fraud_reported == 'Y'):
            return 1
        else : 
            return 0
    
    data['fnum'] = data.apply(tonum,axis=1)

    timeseries = data.pivot_table(
                 index='incident_date',
                 values='fnum',
                 aggfunc='count').ffill()
    # ---- Number of Report per Day

    ax = timeseries.plot(legend=False, title = "Number of Fraud per Day",color='#c34454', figsize=(8, 6))

    # Plot Configuration
    plt.xlabel('incident_date')

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

def plot_report(data):

    df_fraud = data[data.fraud_reported == 'Y'].pivot_table(index='police_report_available',values='fraud_reported',aggfunc='count')

    df_nfraud = data[data.fraud_reported == 'N'].pivot_table(index='police_report_available',values='fraud_reported',aggfunc='count')

    # ---- Police Report Availability

    ax =  pd.concat([df_fraud,df_nfraud],axis=1).plot.bar(stacked = 'police_report_available',color =['#c34454','#53a4b1'],title = "Police Report Availability", figsize=(8, 6))
    
    # Plot Configuration
    plt.legend(['fraud','not fraud'], bbox_to_anchor=(1, 1))
    plt.xlabel("police report available'")

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

def plot_hourgroup(data):
    
    # ---- Age group of customer

    def hour_grouping(data):
        if(data.incident_hour_of_the_day <= 6):
            return 'Evening'
        elif(data.incident_hour_of_the_day > 6 and data.incident_hour_of_the_day <= 12) : 
            return 'Morning'
        elif(data.incident_hour_of_the_day > 12 and data.incident_hour_of_the_day <= 18) : 
            return 'Afternoon'
        else : 
            return 'Night'
    
    data['hour_group'] = data.apply(hour_grouping,axis = 1)

    fraud_data = data[data['fraud_reported'] == 'Y']
    hourday = pd.crosstab(index=fraud_data['hour_group'],
            columns='total_fraud',
            values=fraud_data['fraud_reported'],
            aggfunc='count').sort_values(by='hour_group', ascending=True)   

    ax = hourday.plot.barh(title = "Number of Fraud in Parts of the Day", 
    legend= False, 
    color = '#c34454', 
    figsize = (8,6))
 
    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png', transparent=True)
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

def plot_incidenthour(data):

    def tonum(data):
        if(data.fraud_reported == 'Y'):
            return 1
        else : 
            return 0
    
    data['fnum'] = data.apply(tonum,axis=1)

    timeseries = data.pivot_table(
                 index='incident_hour_of_the_day',
                 values='fnum',
                 aggfunc='count').ffill()
    # ---- Number of Report per Day

    ax = timeseries.plot(legend=False, title = "Number of Fraud in Incident Hour",color='#c34454', figsize=(8, 6))

    # Plot Configuration
    plt.xlabel('incidenthour')

    # Save png file to IO buffer
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]

    return(result)

