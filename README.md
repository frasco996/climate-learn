# climate-learn

In this project, I implemented the paper "ClimateLearn: Benchmarking Machine Learning for Weather and Climate Modeling." I developed four different models: ResNet, ResNetBig, UNet, and VIT, to predict the temperature at 2 meters (t2m), the temperature at 850 hPa (t850), and the geopotential at 500 hPa (g500) for the following day. I also compared various forecasting approaches: Direct, Iterative, and Continuous.

To run the code, I recommend executing only the notebook (ClimateLearn Implementation) and not the managedData file in the Starting_Data folder, as I cannot upload such a large amount of data (nearly 30GB). The managedData file is used solely for cleaning and merging all datasets into a single file.

I used Kaggle to train the models and load the datasets. After downloading the notebook, please import the following two datasets if you wish to skip the first part of the notebook:

Data Train X: https://www.kaggle.com/datasets/fabiofraschetti/data-train-x

Data Train Y: https://www.kaggle.com/datasets/fabiofraschetti/data-train-y

Alternatively, if you have enough memory to run the entire notebook, you can upload these other datasets and run everything:

Tensor: https://www.kaggle.com/datasets/fabiofraschetti/tensor

Constants: https://www.kaggle.com/datasets/fabiofraschetti/constants

The first two datasets are the results of the initial part of the notebook, which might cause memory errors due to their size. To mitigate this, I separated each data processing step with a download script, allowing you to resume from the last saved point without restarting the entire process. Starting from the second part, you can load the models, which are available on Kaggle at this link: https://www.kaggle.com/models/fabiofraschetti/models, and I describe them in detail in the report file. Now you can view the outcomes of my forecasts.
