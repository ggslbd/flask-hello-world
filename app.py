from flask import Flask
from flask import render_template
import tag_reader


app = Flask(__name__)


@app.route('/')
def index():
    # Replace 'tag2' with the tag name you want to display as the header
    searched_tag_name_h = 'header'
    tag_description_header = tag_reader.find_tag_description(searched_tag_name_h)
    
    searched_tag_name_w = 'welcome'
    tag_description_welcome = tag_reader.find_tag_description(searched_tag_name_w)
    
    return render_template('index.html', header_text=tag_description_header,welcome_text=tag_description_welcome)
    
    
 
app.run(host='0.0.0.0', port=81)