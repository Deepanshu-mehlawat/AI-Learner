import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("API_KEY"))

# Define the base system message
base_system_message = '''I am making an AI learner system, I get course details including performance criteria required for a student to qualify,
knowledge evidences that contain the topics one needs to learn to clear the performance criteria.
You have to add related knowledge evidences to the performance criteria I provide in JSON format. Add a key named topics and add the related knowledge evidences to each criterion.'''

def get_user_prompt(data, custom_prompt=None):
    if custom_prompt:
        return f"i am giving you the performance criteria, return me formatted json performance criteria only after adding the topics for each criteria, here are the performance crietias :{data['elements_and_performance_criteria']}, here are the knowledge evidences: {data['knowledge_evidence']}.........also, some evidences have the word 'including' in them.... remove the word 'including' from them.......also, dont return the data in a code block....i am using API and i want to use the data you sent me directly. {custom_prompt}"
    else:
        return f"i am giving you the performance criteria, return me formatted json data after adding the topics for each criteria, {data['elements_and_performance_criteria']}, here are the knowledge evidences: {data['knowledge_evidence']}.........also, some evidences have the word 'including' in them.... remove the word 'including' from them.......also return the data not in a code block...i am using API and i want to use the data you sent me directly "

def update_training_data(data, custom_prompt=None):
    messages = [
        {"role": "system", "content": base_system_message},
        {"role": "user", "content": get_user_prompt(data, custom_prompt)}
    ]

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    try:
        updated_performance_criteria = json.loads(completion.choices[0].message.content)
    except json.JSONDecodeError as e:
        return {"error": "Failed to parse response from OpenAI"}

    # Update the original data
    data['elements_and_performance_criteria'] = updated_performance_criteria

    # Save the updated data back to the JSON file
    with open('updated_training_data.json', 'w') as f:
        json.dump(data, f, indent=4)

    return data

def extract_topics_from_evidences(knowledge_evidence,custom_prompt = ""):
    topics = []
    if len(knowledge_evidence)>1:
        print('its here')

    try:
        messages = [
        {"role": "system", "content": '''i am making an API that recieves a JSON based KNowledge evidence data that contains a list of subjects one needs to learn to pass
a course, i want you to read the knowledge evidences and return to me a list of topics, return only comma separated topic names, no code block, no nothing.'''},
        {"role": "user", "content": f"here are the knowledge evidences:\n{knowledge_evidence}\nreturn the major topic names." + custom_prompt}
        ]

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
        )

        # Extract topics from the completion response
        topics.extend(completion.choices[0].message.content.split(','))
        return topics

    except Exception as e:
        print(f"Error extracting topics: {str(e)}")

def generate_topic_description(topic_name,custom_prompt):
    try:
        # Construct a prompt for GPT-3.5 to generate a description of the topic
        prompt = f"Generate a 500-word description of '{topic_name}'. Include details, examples, and relevant information."+custom_prompt

        messages = [
        {"role": "user", "content": prompt}
        ]

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error generating topic description: {str(e)}")
        return None
    
    return topics
