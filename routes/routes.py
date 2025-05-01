from flask import Blueprint, request, jsonify, render_template
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename

routes = Blueprint('routes', __name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@routes.route('/post_dog_form')
def post_dog_form():
    return render_template('post_dog.html')

@routes.route('/post_dog', methods=['POST'])
def post_dog():
    data = request.form
    file = request.files.get('dog_image_file')

    # Basic dog info
    dog_name = data.get('dog_name')
    breed = data.get('breed')
    description = data.get('description')
    location = data.get('location')
    contact_info = data.get('contact_info')
    city = data.get('city')
    dog_status = data.get('dog_status')

    # Shelter info
    is_shelter_post = data.get('is_shelter_post') == 'true'
    shelter_name = data.get('shelter_name') if is_shelter_post else None
    shelter_logo_url = data.get('shelter_logo_url') if is_shelter_post else None
    hours_of_operation = data.get('hours_of_operation') if is_shelter_post else None

    # Handle image upload
    image_filename = None
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        image_filename = filename

    new_post = {
        "dog_name": dog_name,
        "breed": breed,
        "description": description,
        "location": location,
        "contact_info": contact_info,
        "city": city,
        "dog_status": dog_status,
        "is_shelter_post": is_shelter_post,
        "shelter_name": shelter_name,
        "shelter_logo_url": shelter_logo_url,
        "hours_of_operation": hours_of_operation,
        "date_posted": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "dog_image_file": image_filename
    }

    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as f:
            posts = json.load(f)
    else:
        posts = []

    posts.append(new_post)

    with open('dog_posts.json', 'w') as f:
        json.dump(posts, f, indent=4)

    return jsonify({"message": "Dog post created successfully!", "post": new_post})

@routes.route('/view_dogs')
def view_dogs():
    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as f:
            posts = json.load(f)
    else:
        posts = []

    now = datetime.utcnow()

    for post in posts:
        try:
            post_time = datetime.strptime(post.get('date_posted'), "%Y-%m-%d %H:%M:%S")
            delta = now - post_time
            post['is_new'] = delta.total_seconds() < 86400  # 24 hours
        except:
            post['is_new'] = False

    return render_template('view_dogs.html', posts=posts)

@routes.route('/view_lost_dogs')
def view_lost_dogs():
    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as f:
            posts = json.load(f)
    else:
        posts = []

    lost_dogs = [post for post in posts if post.get('dog_status') == 'Lost']
    return render_template('view_dogs.html', posts=lost_dogs)

@routes.route('/view_found_dogs')
def view_found_dogs():
    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as f:
            posts = json.load(f)
    else:
        posts = []

    found_or_reunited = [post for post in posts if post.get('dog_status') in ['Found', 'Reunited']]
    return render_template('view_dogs.html', posts=found_or_reunited)

@routes.route('/view_shelters')
def view_shelters():
    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as f:
            posts = json.load(f)
    else:
        posts = []

    shelter_posts = [post for post in posts if post.get('is_shelter_post')]

    return render_template('view_shelters.html', posts=shelter_posts)

@routes.route('/mark_reunited/<dog_name>', methods=['POST'])
def mark_reunited(dog_name):
    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as f:
            posts = json.load(f)
    else:
        posts = []

    updated = False
    for post in posts:
        if post['dog_name'] == dog_name and post.get('dog_status') == 'Lost':
            post['dog_status'] = 'Reunited'
            updated = True
            break

    if updated:
        with open('dog_posts.json', 'w') as f:
            json.dump(posts, f, indent=4)
        return "Dog marked as reunited! 🎉 <a href='/view_dogs'>Go back</a>"
    else:
        return "Dog not found or already reunited.", 404

@routes.route('/success_stories')
def success_stories():
    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as f:
            posts = json.load(f)
    else:
        posts = []

    reunited_posts = [post for post in posts if post.get('dog_status') == 'Reunited']

    return render_template('success_stories.html', posts=reunited_posts)

@routes.route('/post_lost_dog')
def post_lost_dog():
    return render_template('post_dog.html', prefill_status='Lost')

@routes.route('/post_found_dog')
def post_found_dog():
    return render_template('post_dog.html', prefill_status='Found')
