from flask import Flask, jsonify, request
from flask_cors import CORS
import scrapper
import updater

app = Flask(__name__)
CORS(app)
scrapped_data = None  # Initialize as None initially

@app.route('/training-data', methods=['GET'])
def get_training_data():
    global scrapped_data
    competency_id = request.args.get('competency_id')
    if not competency_id:
        return jsonify({"error": "Competency ID parameter is required"}), 400

    data = scrapper.scrape_training_data(competency_id)
    if not data:
        return jsonify({"error": "Failed to retrieve data for the provided competency ID"}), 404
    
    scrapped_data = data  # Update scrapped_data with fetched data
    return jsonify(data)

@app.route('/performance_criteria', methods=['POST'])
def performance_criteria():
    global scrapped_data
    try:
        content = request.get_json()
        if not content or 'custom_prompt' not in content:
            return jsonify({"error": "Invalid JSON payload or missing 'custom_prompt' field"}), 400

        custom_prompt = content.get('custom_prompt', '')
        
        # Ensure scrapped_data is populated and has the required structure
        if not scrapped_data or 'elements_and_performance_criteria' not in scrapped_data:
            return jsonify({"error": "No training data available or invalid data structure"}), 500
        
        data = {
            "elements_and_performance_criteria": scrapped_data['elements_and_performance_criteria'],
            "knowledge_evidence": scrapped_data['knowledge_evidence']
        }

        updated_data = updater.update_training_data(data, custom_prompt)

        if 'error' in updated_data:
            return jsonify({"error": updated_data['error']}), 500

        return jsonify(updated_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/extract-topics', methods=['POST'])
def extract_topics():
    try:
        content = request.get_json()
        if not content:
            return jsonify({"error": "no content found"}), 400

        custom_prompt = content.get('custom_prompt', '')
        knowledge_evidence = scrapped_data['knowledge_evidence']
        topics = updater.extract_topics_from_evidences(knowledge_evidence,custom_prompt)

        return jsonify({"topics": topics})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-description', methods=['POST'])
def generate_description():
    try:
        content = request.get_json()
        if not content or 'topic_name' not in content:
            return jsonify({"error": "JSON payload with 'topic_name' key is required"}), 400

        topic_name = content['topic_name']
        custom_prompt = content.get('custom_prompt','')
        description = updater.generate_topic_description(topic_name,custom_prompt)

        if not description:
            return jsonify({"error": "Failed to generate description for the topic"}), 500

        return jsonify({"topic_name": topic_name, "description": description})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
