# MultiLabel-Book-Genre-Classifier(QA_Classifier)

A text classification model from data collection, model training, and deployment.
The model can classify 69 different types of questions categories.
The keys of `deployment\category_types_encoded.json` contains the questions categories.

# Data Collection

Data was collected from a Stackoverflow Website's questions segment: https://stackoverflow.com/questions
The data collection process is divided into two steps:

1. **Question URL Scraping:** The question urls were scraped with `scraper\questions_url_scraper.py` and the urls are stored along with question title in `data\questions_urls.csv`

2. **Question Details Scraping:** Using the urls, full question and categories/tags were scraped with `scraper\questions_details_scraper.py` and stored in `data\questions_details.csv`. 

In total, I scraped 22124 book details and 22257 question urls. Some urls didn't contain any valid page. Those details were ignored. 


# Data Preprocessing

Initially there were 640 different genres in the dataset. After some analysis, I found out 499 of them are rare (probably custom genres by users). So, I removed those genres and then I have 141 genres. After that, I removed the description without any genres resulting in 6,104 samples.

# Model Training
Finetuned a distilrobera-base model from HuggingFace Transformers using Fastai and Blurr. The model training notebook can be viewed [here.]()

# Model Compression and ONNX Inference
The trained model has a memory of 300+MB. I compressed this model using ONNX quantization and brought it under 80MB.

# Model Deployment

The compressed model is deployed to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here.]()

<img src="deployment/gradio_app_2.PNG" alt="Girl in a jacket" style="width:500px;height:600px;">


# Web Deployment
Deployed a Flask App built to take descprition and show the genres as output. Check flask  branch. The website is live [here.]()
<img src="deployment/flask_app_home.PNG" alt="Girl in a jacket" style="width:600px;height:400px;">
<img src="deployment/flask_app_result.PNG" alt="Girl in a jacket" style="width:600px;height:400px;">
