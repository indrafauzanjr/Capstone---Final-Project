# Data Analysis Capstone:<br> Auto Insurance Fraud Analysis
[![](assets/algoritma-autoinsurance.PNG)](https://algoritma-autoinsurance.herokuapp.com/)

This project is developed as one of [Algoritma Academy](https://algorit.ma/) Data Analytics Specialization using capstone Projects. The deliverables of this project is a simple analytic dashboard using Flask framework.

The skeleton for this application is separated into 2 different files: [app.py](app.py) and [helper.py](helper.py), in which the first one handles the routing and within [helper](helper.py) you would define function to be called in [app](app.py).

The **Auto Insurance Fraud Analysis.ipynb** notebook contains all the tasks and explanation which will guide you to complete the given skeleton.

## Rubrics

To get the full 16 points, you will need to complete the following tasks:
- Load and pre-process data (*2pts*)
- Extract quick summary (*3pts*)
- Generate the plot (*4pts*)
- Create your own analysis (*4pts*)
- Make the flask app run properly (*3pts*)

## Dependencies

You'll find a file called [requirements.txt](requirements.txt). The file contains dependencies for this project.

Run the following command to create a new conda environment from requirements.txt:

**Step 1**: Prepare a new "blank" environment then activate it

```
conda env create -n <ENV_NAME> python=<PYTHON_VERSION>
conda activate <ENV_NAME>
```

**Step 2**: Navigate to the folder with your `requirements.txt`

```
cd <PATH_TO_REQUIREMENTS>
```

**Step 3**: Install the requirements

```
pip install -r requirements.txt
```

Now you have successfuly installed all the requirements needed on this project! For your convenience, don't forget to link your new environment to jupyter-notebook by installing the kernel:

```
pip install ipykernel
python -m ipykernel install --user --name=<ENV_NAME>
```

## Dataset Details

The data set is taken from [fraud-detection-insurance](https://www.kaggle.com/sanjeevkallepalli/fraud-detection-insurance) for autoinsurance fraud detection. 

> "The autoinsurance data contains information about a fictional auto insurance company that provided insurance for car incident, this data have 1000 sample data that an insurance claim which labeled as fraud claim or non fraud claim. 


### Data Glossary

- 'months_as_customer' : months as policy holder
- 'age' : umur pemegang polis
- 'policy_number' : nomor polis
- 'policy_bind_date' : date when policy made
- 'policy_state' : state where the policy made
- 'policy_deductable': Policy deductable 
- 'policy_annual_premium' : Yearly policy premium
- 'umbrella_limit: umbrella limit of the premium
- 'insured_zip': zip code of insured
- 'insured_sex' : insured sex
- 'insured_education_level' : insured education level
- 'insured_occupation' : insured occupation
- 'insured_hobbies' : insured hobbies
- 'insured_relationship' : insured relationship status
- 'incident_date' : reported incident date
- 'incident_type' : reported incident type
- 'collision_type' : reported collision type
- 'incident_severity': reported incident severity
- 'authorities_contacted' : contacted autorities
- 'incident_state' : reported incident state 
- 'incident_city' : reported incident city
- 'incident_location' : reported incident location
- 'incident_hour_of_the_day' : reported hour of incident
- 'number_of_vehicles_involved' : number of vehicles involved
- 'property_damage' : number of property damage reported
- 'bodily_injuries' : number of bodily injuries reported
- 'witnesses' : number of witnesses 
- 'police_report_available' : police report avaiability 
- 'total_claim_amount' : total claim amount
- 'injury_claim' : total injury claim 
- 'property_claim' : total property claim 
- 'vehicle_claim' : total vehicle claim 
- 'auto_make' : vehicle brand
- 'auto_model' : vehicle model
- 'auto_year' : vehicle year made 
- 'fraud_reported' : fraud label



