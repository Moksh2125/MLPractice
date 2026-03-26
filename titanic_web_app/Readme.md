# Titanic Survival prediction application
A simple pipeline created model, integreated with flask html css for web application.

## Process of making model ([TitanicPipelineTraining](TitanicPipelineTraining.ipynb)):
- Loaded the dataset, removed the unwanted columns.
- Created a pipe for numerical data  Imputed the age and scaled the data through **SimpleImputer** and **MinMaxScaler**.
- Created another pipeline for categorical data, first to impute through **SimpleImputer** and then **OneHotEncoding**.
- Pipelines will work parellel through a **ColumnTransform**
- A final pipeline containing the above **column transformer, feature selection and DecisionTreeClassifier**  
- Lastly fiting it with train data and dumping it in pkl file.

## Using the model oin the web application
- Using different tech stack like flask to create backend and html css for landing page. I have created a simple pipeline model to better understand different flows.

