from flask import Flask, request, jsonify
import os
import random
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello user this is a api. <a href=\"/api?type=main&sub=main\">For the main page add \"/api?type=main?sub=main\" to the end of the url thank you! 🍩🍩 😄</a>"

@app.route('/api')
def api():
    type_ = request.args.get('type')
    sub = request.args.get('sub')
    
    # Check if type and sub parameters are provided
    if not type_ or not sub:
        return jsonify({'error': 'Please provide both type and sub parameters in the URL'})
    
    data_path = os.path.join(os.getcwd(), 'lists', type_ + '.txt')
    
    # Check if the data file exists
    if not os.path.exists(data_path):
        return jsonify({'error': 'No elements found for type "{}"'.format(type_)})
    
    with open(data_path, 'r') as f:
        lines = f.readlines()
        
    sub_start = '--' + sub + '--\n'
    sub_end = '--end ' + sub + '--\n'
    sub_data = []
    
    # Check if sub exists in the data file
    if sub_start not in lines or sub_end not in lines:
        return jsonify({'error': 'No elements found for type "{}" and sub "{}"'.format(type_, sub)})
    
    start_index = lines.index(sub_start)
    end_index = lines.index(sub_end)
    
    sub_data = lines[start_index+1:end_index]
    
    # Choose a random element from the sub data
    chosen_element = random.choice(sub_data)
    
    return jsonify({'data': chosen_element.strip()})


if __name__ == '__main__':
    sudo_command = "sudo python onlineHandler.py"
    process = subprocess.Popen(sudo_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    app.run(port=1237, host="localhost")
    
    # 109 lines of code!