import os
import markdown
from flask import Flask, render_template,abort

app = Flask(__name__)
POSTS_FOLDER = os.path.join(os.path.dirname(__file__), 'posts')

def get_post_list():
    files = [f for f in os.listdir(POSTS_FOLDER) if f.endswith('.md')]
    posts = []
    for file in files:
        title = file.replace('.md','').replace('-','').title()
        posts.append({
            'title' : title,
            'filename': file
        })
    return posts
 
def load_post(filename):
    """Load a Markdown file and convert it to HTML."""
    filepath = os.path.join(POSTS_FOLDER, filename)
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Convert Markdown to HTML
    post_content = markdown.markdown(content)

    return post_content   

def get_post_preview(filename, max_length=200):
    """Load a Markdown file, convert it to HTML, and return a preview."""
    content = load_post(filename)
    if not content:
        return None
    
    # Strip HTML tags for the preview
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()    
    # Truncate the text and add ellipsis if necessary
    if len(text) > max_length:
        preview = text[:max_length].rsplit(' ', 1)[0] + '...'
    else:
        preview = text
    
    return preview

@app.route('/')
def index():
    posts = get_post_list()
    for post in posts:
        post['preview'] = get_post_preview(post['filename'])
    return render_template('index.html', posts=posts)


@app.route('/post/<filename>')
def post(filename):    
    content = load_post(filename)
    if not content:
        # return render_template('404.html'), 404
        abort(404)
    # title = filename.replace('.md', '').replace('-', ' ').title()
    return render_template('post.html',content=content)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')