# climate-learn

In this project, I implemented the paper "ClimateLearn: Benchmarking Machine Learning for Weather and Climate Modeling." I developed four different models (ResNet, ResNetBig, UNet, and VIT) to predict the temperature at 2 meters (t2m), the temperature at 850 hPa (t850), and the geopotential at 500 hPa (g500) for the next day. I also compared different forecasting approaches: Direct, Iterative, and Continuous.


To run the code, I recommend running only the notebook (ClimateLearn Implementation) and not the managedData file in the Starting_Data folder, as I cannot upload that much data (almost 30GB). The managedData file is only used for cleaning and merging all the datasets into one.


I used Kaggle to train the models and load the datasets. After downloading the notebook, please import the following two datasets if you want to skip the first part of the notebook:

Data Train X:  "https://www.kaggle.com/datasets/fabiofraschetti/data-train-x"

Data Train Y:  "https://www.kaggle.com/datasets/fabiofraschetti/data-train-y"

Otherwise,if you have enought memory to run the notebook, upload this other Datasets and the run all the Notebook:

Tensor: https://www.kaggle.com/datasets/fabiofraschetti/tensor

Constants: https://www.kaggle.com/datasets/fabiofraschetti/constants

These datasets are the results of the first part of the notebook, which might cause memory errors due to the large data size. To address this, I separated each data processing step with a download script, allowing the workflow to resume from the last saved point without restarting the entire process. So starting from the second part you can load the models that are in the folder "model" (or you can add directly from kaggle at this link https://www.kaggle.com/models/fabiofraschetti/models) that I describe in detail in the Report file. Now you can see the outcome of my forecasts.
