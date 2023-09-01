# Multi-label Question Category Classifier
Here I attached multi-label question categories/tags classifier models huggingface API as a flask app.

# Features
1. `index.html` page contains the code for submitting the programming related question. 
2. On the other hand, `result.html` will show the question categories reagrding that question.

`app.py` contains the backend process of the above processes.

# Build and Run
Run `python app.py` command to run the app. Go to the required localhost url. Now submit a programming related question and see the predicted category/categories.

# To deploy on `render.com`

1. Create the docker file as `Dockerfile` and write those code as it is.
2. Create a `requirements.txt` file and make you this file contains these two libraries-

    `Flask==2.0.1` and `gunicorn==20.1.0`

3. Build the Docker Image with `docker build -t flask-app .` command.
4. Run the Docker Container with `docker run -p 8000:8000 flask-app` command. 
5. Access Your Application on `http://localhost:8000`
6. Deploy the app on render. Use `gunicorn app:app` on the `Start Command` field. Here, the left app `app:app` indicates the `app.py` file.
7. Go the render url of you app. See the app live on [here.](https://multilabel-question-category-classifier.onrender.com/)
