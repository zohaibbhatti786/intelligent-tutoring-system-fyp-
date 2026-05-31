from flask import Blueprint, render_template, request

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

# Route: Homepage
@main.route('/')
def index():
    return render_template('index.html')

# Route: Learning Page
@main.route('/start')
def learning():
    return render_template('learning.html')

# Route: Lesson Page with a topic
@main.route('/lesson/<topic>')
def lesson(topic):
    # Dummy content for now
    content = f"This is the content for the topic: {topic}"
    return render_template('lesson.html', topic=topic, content=content)
