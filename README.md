# GIS5572BMSBProject

Authors: Holly Leaf and Megan Marsolek

This repository contains python code files that run the Huff Model in order to predict the spread of BMSB across MN cities.

Execute these notebook within an ArcGIS Pro Python Notebook environment and in the following order:

1. 'BMSB_Data': This notebook loads relevant data from MNGeo Commons and then cleans/reorganizes and creates the necessary tables used to run the Huff model simulation (the model used to predict whether a BMSB spreads/moves to cities within MN). If you plan to run the notebook, you should change the designated environment's workspace (Please set it to a GBD!)
2. 'BMSB-Simulation': This notebook runs the 100 Huff simulations for 60 (monthly) timesteps. If you plan to change or calculate multiple different Huff models with varying alpha values this is the notebook you would edit (We ran this notebook 3 times where alpha = 2, alpha =1.75, alpha =1.5). Warning, this notebooks execution can take anywhere from 2 to 6 hours depending on the abilities of the computer running the simulations. 
3. 'BMSB_AccAssessment': This notebook calculates the accuracy evaluations metrics for each city over the 100 simulations (calculates True Positives, True Negatives, False Positives (used to find the cities in most need to BMSB monitoring), False Negatives, Accuracy). This notebook also ranks the list of cities based on the FP and number of observed BMSB traps within a 10 mile radius of each city, so that cities with high FP and low to no traps are prioritized as highest in need to BMSB monitoring. 
4. 'BMSB_PostGis': This last notebook stores each resulting accuracy evaluations for each Huff model to a PostGIS, and the best model's ranked list of cities that need BMSB monitoring. (It also prints the geojson of each saved layer as a preview of what you will see on the web page created in google cloud run). 

These notebooks were executed 3 times where alpha = 2, alpha =1.75, alpha =1.5. Names of saved tables were changed and reflect the current alpha to distinguish it from other model results. After running and saving the resulting tables, we then executed "multi_geojson.py' within Google Cloud Run services to print the geojson layer for each Huff model simulation and ranked cities list. Please refer to the following link for more information on how to deploy google cloud run services: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

Access the geojson for each run model and the ranked list of cities from: 
* https://bmsb-paqfpja6oq-uc.a.run.app/ranked_cities
* https://bmsb-paqfpja6oq-uc.a.run.app/model_alpha2
* https://bmsb-paqfpja6oq-uc.a.run.app/model_alpha1_75
* https://bmsb-paqfpja6oq-uc.a.run.app/model_alpha1_5
