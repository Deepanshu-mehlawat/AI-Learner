from openai import OpenAI
from dotenv import load_dotenv
import os
import json

f = open('a_training_data.json','r')
data = json.load(f)
load_dotenv()

client = OpenAI(
  api_key=os.getenv('API_KEY'),
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": '''I am making a AI learner system, i get course details including performance criterias required for a student to qualify,
knowledge evidences that contains the topics one needs to learn to clear the performance criterias.
You have to add related knowledge evidences to the performance criterias i provide in json format. add a key named topics and add the related knowledge evidences to each criteria.'''},
    {"role": "user", "content": f"i am giving you the performance criterias, return me formatted json data after adding the topics for each criteria,{data['elements_and_performance_criteria']}, here are the knowledge evidences: {data['knowledge_evidence']}.........also, some evidences have the word 'including' in them....  remove the word 'including' from them.......also return the data not in a code block...i am using API and i want to use the data you sent me directly."}
  ]
)

print(completion.choices[0].message.content)
updated_performance_criteria = json.loads(completion.choices[0].message.content)

# Update the original data
data['elements_and_performance_criteria'] = updated_performance_criteria

# Save the updated data back to the JSON file
with open('updated_training_data_updated.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Updated data saved to a_training_data_updated.json")
