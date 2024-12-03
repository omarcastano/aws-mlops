# import python iamge
FROM python:3.10.15-slim AS app

#move to the working directory
WORKDIR /app

COPY . ./

# Install dependencies
RUN pip install --upgrade pip && pip install poetry
RUN poetry install

# esport ports
EXPOSE 8000

#Run the app
CMD poetry run python src/app/app.py