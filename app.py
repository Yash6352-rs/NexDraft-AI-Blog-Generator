from flask import Flask, render_template, request, send_file
from agents_logic import run_blog_creation
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    blog_post = None
    topic = None

    if request.method == 'POST':
        topic = request.form.get('topic')
        if topic:
            blog_post = run_blog_creation(topic)

    return render_template('index.html', blog_post=blog_post, topic=topic)

@app.route('/download', methods=['POST'])
def download():
    content = request.form.get('content')
    topic = request.form.get('topic', 'blog')
    filename = f"{topic.strip().replace(' ', '_')}.txt"

    file_stream = BytesIO()
    file_stream.write(content.encode('utf-8'))
    file_stream.seek(0)

    return send_file(file_stream, as_attachment=True, download_name=filename, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
