## AI-Learner
### Dependencies
Before running the files, install these dependencies using pip:

```bash
pip install requests beautifulsoup4 flask flask-cors openai python-dotenv
```
### Running the App
To run the app, simply type this in your command prompt:

```bash
python API.py
```

### API Endpoints
#### 1. Scraping Training Data
##### Endpoint: /training-data
##### Method: GET
##### Description: Scrapes training data for the specified competency ID.

Request:

```bash
curl http://localhost:5000/training-data?competency_id=ueeel0025
```
You can replace competency_id with any ID you want.

##### Response:

Success (200): Returns the training data in JSON format.
Error (400): Returns an error message if the competency_id parameter is missing.
Error (404): Returns an error message if data for the provided competency_id could not be retrieved.


#### 2. Updating Performance Criteria
##### Endpoint: /performance_criteria
##### Method: POST
##### Description: Updates the performance criteria with related knowledge evidences and removes the word "including" from the evidences.

##### Request Payload:

```json
{
    "custom_prompt": "Your custom prompt here"
}
```

##### Request Example:

```bash
curl -X POST "http://localhost:5000/performance_criteria" -H "Content-Type: application/json" -d "{\"custom_prompt\": \"Your custom prompt here\"}"
```

##### Response:

Success (200): Returns the updated training data in JSON format.
Error (400): Returns an error message if the JSON payload is invalid or missing the custom_prompt field.
Error (500): Returns an error message if no training data is available or if there is an issue with updating the data.


#### 3. Extracting Topics from Knowledge Evidences
##### Endpoint: /extract-topics
##### Method: POST
##### Description: Extracts main topics from the provided knowledge evidences.

##### Request Payload:

```json
{
    "custom_prompt": "Your custom prompt here"
}
```

##### Request Example:

```bash
curl -X POST "http://localhost:5000/extract-topics" -H "Content-Type: application/json" -d "{\"custom_prompt\": \"Your custom prompt here\"}"
```

##### Response:

Success (200): Returns a list of topics extracted from the knowledge evidences.
Error (400): Returns an error message if the JSON payload is invalid.
Error (500): Returns an error message if there is an issue with extracting the topics.


#### 4. Generating Topic Descriptions
##### Endpoint: /generate-description
##### Method: POST
##### Description: Generates a 500-word description for the provided topic name.

##### Request Payload:

```json
{
    "topic_name": "Your topic name here",
    "custom_prompt": "Your custom prompt here"
}
```

##### Request Example:

```bash
curl -X POST "http://localhost:5000/generate-description" -H "Content-Type: application/json" -d "{\"topic_name\": \"Transformer Operation\", \"custom_prompt\": \"\"}"
```
##### Response:

Success (200): Returns the topic name and its 500-word description.
Error (400): Returns an error message if the JSON payload is invalid or missing the topic_name field.
Error (500): Returns an error message if there is an issue with generating the topic description.
