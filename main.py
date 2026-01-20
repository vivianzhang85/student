# main.py - Combined Museum Scraper API with Full Flask Application
from flask import Flask, jsonify, abort, redirect, render_template, request, send_from_directory, url_for, current_app, g
from flask_cors import CORS
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from flask.cli import AppGroup
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import urljoin, urlparse
import os
import requests
from bs4 import BeautifulSoup
import re
import random  # ADDED FOR RANDOM LANDMARKS

# Import database and models
from __init__ import app, db, login_manager

# Import API blueprints
from api.user import user_api 
from api.python_exec_api import python_exec_api
from api.javascript_exec_api import javascript_exec_api
from api.section import section_api
from api.pfp import pfp_api
from api.stock import stock_api
from api.analytics import analytics_api
from api.student import student_api
from api.groq_api import groq_api
from api.gemini_api import gemini_api
from api.microblog_api import microblog_api
from api.classroom_api import classroom_api
from hacks.joke import joke_api
from hacks.lyric import lyric_api
from hacks.lyrics import initLyrics
from api.post import post_api
from api.study import study_api
from api.feedback_api import feedback_api
from api.jwt_authorize import token_required

# Import models
from model.user import User, Section, initUsers
from model.github import GitHubUser
from model.feedback import Feedback
from model.study import Study, initStudies
from model.classroom import Classroom
from model.post import Post, init_posts
from model.microblog import MicroBlog, Topic, init_microblogs
from hacks.jokes import initJokes

# Load environment variables
load_dotenv()

# Initialize CORS for all origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuration
app.config['KASM_SERVER'] = os.getenv('KASM_SERVER')
app.config['KASM_API_KEY'] = os.getenv('KASM_API_KEY')
app.config['KASM_API_KEY_SECRET'] = os.getenv('KASM_API_KEY_SECRET')

# Register all API blueprints
app.register_blueprint(python_exec_api)
app.register_blueprint(javascript_exec_api)
app.register_blueprint(user_api)
app.register_blueprint(section_api)
app.register_blueprint(pfp_api) 
app.register_blueprint(stock_api)
app.register_blueprint(groq_api)
app.register_blueprint(gemini_api)
app.register_blueprint(microblog_api)
app.register_blueprint(analytics_api)
app.register_blueprint(student_api)
app.register_blueprint(study_api)
app.register_blueprint(classroom_api)
app.register_blueprint(feedback_api)
app.register_blueprint(joke_api)
app.register_blueprint(lyric_api)
app.register_blueprint(post_api)

# Initialize jokes
with app.app_context():
    initJokes()
    initLyrics()

# Flask-Login configuration
login_manager.login_view = "login"

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login', next=request.path))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

# ============================================================================
# MUSEUM SCRAPER CLASS
# ============================================================================

class MuseumScraper:
    """Web scraper for museum hours with improved parsing"""
    
    def scrape_met_museum(self):
        """Scrape MET Museum hours"""
        try:
            url = "https://www.metmuseum.org/visit/plan-your-visit/metropolitan-museum-of-art"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            hours = "Sun-Thu: 10:00 AM - 5:30 PM, Fri-Sat: 10:00 AM - 9:00 PM"
            
            # Look for hours in MET page with multiple strategies
            hour_sections = soup.find_all(['p', 'div', 'span', 'li'], 
                                         text=re.compile(r'[Hh]ours?|[Oo]pen|[Cc]losed|10.*AM.*5.*PM', re.IGNORECASE))
            
            for section in hour_sections:
                text = section.get_text().strip()
                if '10' in text and ('AM' in text or 'am' in text) and ('PM' in text or 'pm' in text):
                    hours = text[:200]
                    break
            
            # Also check for structured hours data
            hour_divs = soup.find_all(['div', 'section'], class_=re.compile(r'hour|time|schedule', re.IGNORECASE))
            for div in hour_divs:
                text = div.get_text().strip()
                if len(text) > 50 and ('AM' in text or 'PM' in text):
                    hours = text[:200]
                    break
            
            return {
                'museum': 'MET Museum',
                'hours': hours,
                'address': '1000 5th Ave, New York, NY 10028',
                'phone': '(212) 535-7710',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'source': 'metmuseum.org'
            }
            
        except Exception as e:
            return {
                'museum': 'MET Museum',
                'hours': 'Sun-Thu: 10:00 AM - 5:30 PM, Fri-Sat: 10:00 AM - 9:00 PM',
                'address': '1000 5th Ave, New York, NY 10028',
                'phone': '(212) 535-7710',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'error': str(e)[:100],
                'source': 'fallback'
            }
    
    def scrape_ice_cream_museum(self):
        """Scrape Museum of Ice Cream hours"""
        try:
            url = "https://www.museumoficecream.com/new-york"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for hours with multiple patterns
            hours = "Mon-Sun: 10:00 AM - 9:00 PM"
            all_text = soup.get_text()
            
            # Pattern 1: Direct hour patterns
            hour_patterns = [
                r'([A-Za-z]{3,9}[-\s]*\d{1,2}(?::\d{2})?\s*[APap][Mm]\s*[-–]\s*\d{1,2}(?::\d{2})?\s*[APap][Mm])',
                r'(\d{1,2}(?::\d{2})?\s*[APap][Mm]\s*[-–]\s*\d{1,2}(?::\d{2})?\s*[APap][Mm])',
                r'[Hh]ours?[:\s]*([^\n]{10,80})'
            ]
            
            for pattern in hour_patterns:
                match = re.search(pattern, all_text)
                if match:
                    hours = match.group(1).strip()
                    break
            
            # Pattern 2: Look for opening hours sections
            hour_sections = soup.find_all(['p', 'div', 'span'], 
                                         text=re.compile(r'[Oo]pen|[Hh]ours?|[Mm]on.*[Ss]un', re.IGNORECASE))
            for section in hour_sections:
                text = section.get_text().strip()
                if 'AM' in text or 'PM' in text:
                    hours = text[:150]
                    break
            
            return {
                'museum': 'Museum of Ice Cream',
                'hours': hours,
                'address': '558 Broadway, New York, NY 10012',
                'phone': '(646) 459-3515',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'source': 'museumoficecream.com'
            }
            
        except Exception as e:
            return {
                'museum': 'Museum of Ice Cream',
                'hours': 'Mon-Sun: 10:00 AM - 9:00 PM',
                'address': '558 Broadway, New York, NY 10012',
                'phone': '(646) 459-3515',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'error': str(e)[:100],
                'source': 'fallback'
            }
    
    def scrape_ukrainian_museum(self):
        """Scrape Ukrainian Museum hours"""
        try:
            url = "https://www.ukrainianmuseum.org/"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            hours = "Wed-Sun: 11:30 AM - 5:00 PM"
            
            # Multiple search strategies
            patterns = [
                r'[Hh]ours?[:\s]*([^\n]{10,100})',
                r'[Oo]pen[:\s]*([^\n]{10,100})',
                r'(\d{1,2}:\d{2}\s*[APap][Mm]\s*[-–]\s*\d{1,2}:\d{2}\s*[APap][Mm])'
            ]
            
            all_text = soup.get_text()
            for pattern in patterns:
                match = re.search(pattern, all_text)
                if match:
                    hours = match.group(1).strip()[:100]
                    break
            
            # Also search in footer or specific sections
            footer = soup.find(['footer', 'div'], class_=re.compile(r'footer|hours|visit', re.IGNORECASE))
            if footer:
                footer_text = footer.get_text()
                for pattern in patterns:
                    match = re.search(pattern, footer_text)
                    if match:
                        hours = match.group(1).strip()[:100]
                        break
            
            return {
                'museum': 'Ukrainian Museum',
                'hours': hours,
                'address': '222 East 6th Street, New York, NY 10003',
                'phone': '(212) 228-0110',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'source': 'ukrainianmuseum.org'
            }
            
        except Exception as e:
            return {
                'museum': 'Ukrainian Museum',
                'hours': 'Wed-Sun: 11:30 AM - 5:00 PM',
                'address': '222 East 6th Street, New York, NY 10003',
                'phone': '(212) 228-0110',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'error': str(e)[:100],
                'source': 'fallback'
            }
    
    def scrape_empire_state(self):
        """Scrape Empire State Building hours"""
        try:
            url = "https://www.esbnyc.com/"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            hours = "Daily: 8:00 AM - 2:00 AM"
            
            # Multiple search strategies
            hour_text = soup.get_text()
            
            # Pattern 1: Direct time patterns
            hour_patterns = [
                r'(\d{1,2}(?::\d{2})?\s*[APap][Mm]\s*[-–]\s*\d{1,2}(?::\d{2})?\s*[APap][Mm])',
                r'[Hh]ours?[:\s]*([^\n]{10,80})',
                r'[Oo]pen[:\s]*([^\n]{10,80})'
            ]
            
            for pattern in hour_patterns:
                match = re.search(pattern, hour_text)
                if match:
                    found = match.group(1).strip()
                    if 'AM' in found or 'PM' in found:
                        hours = f"Daily: {found}" if 'daily' not in found.lower() else found
                        break
            
            # Pattern 2: Look in specific sections
            visit_sections = soup.find_all(['div', 'section'], 
                                          text=re.compile(r'[Vv]isit|[Hh]ours?|[Oo]bservatory', re.IGNORECASE))
            for section in visit_sections:
                text = section.get_text()
                for pattern in hour_patterns:
                    match = re.search(pattern, text)
                    if match:
                        found = match.group(1).strip()
                        if 'AM' in found or 'PM' in found:
                            hours = found
                            break
            
            return {
                'museum': 'Empire State Building',
                'hours': hours,
                'address': '20 W 34th St, New York, NY 10001',
                'phone': '(212) 736-3100',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'source': 'esbnyc.com'
            }
            
        except Exception as e:
            return {
                'museum': 'Empire State Building',
                'hours': 'Daily: 8:00 AM - 2:00 AM',
                'address': '20 W 34th St, New York, NY 10001',
                'phone': '(212) 736-3100',
                'status': 'open',
                'last_updated': datetime.now().strftime("%I:%M %p"),
                'error': str(e)[:100],
                'source': 'fallback'
            }

# Create scraper instance
scraper = MuseumScraper()

# ============================================================================
# MUSEUM SCRAPER API ENDPOINTS
# ============================================================================

@app.route('/api/met')
def get_met_hours():
    """GET MET Museum hours"""
    data = scraper.scrape_met_museum()
    return jsonify({'success': True, 'data': data})

@app.route('/api/icecream')
def get_icecream_hours():
    """GET Ice Cream Museum hours"""
    data = scraper.scrape_ice_cream_museum()
    return jsonify({'success': True, 'data': data})

@app.route('/api/ukrainian')
def get_ukrainian_hours():
    """GET Ukrainian Museum hours"""
    data = scraper.scrape_ukrainian_museum()
    return jsonify({'success': True, 'data': data})

@app.route('/api/empire')
def get_empire_hours():
    """GET Empire State Building hours"""
    data = scraper.scrape_empire_state()
    return jsonify({'success': True, 'data': data})

@app.route('/api/all')
def get_all_hours():
    """GET all museum hours at once"""
    data = {
        'met': scraper.scrape_met_museum(),
        'icecream': scraper.scrape_ice_cream_museum(),
        'ukrainian': scraper.scrape_ukrainian_museum(),
        'empire': scraper.scrape_empire_state(),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify({'success': True, 'data': data})

@app.route('/api/test')
def test_api():
    """Test endpoint to verify API is working"""
    return jsonify({
        'success': True,
        'message': 'Museum Hours API is running!',
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'endpoints': {
            '/api/met': 'MET Museum hours',
            '/api/icecream': 'Ice Cream Museum hours',
            '/api/ukrainian': 'Ukrainian Museum hours',
            '/api/empire': 'Empire State Building hours',
            '/api/all': 'All museums at once',
            '/api/test': 'Test endpoint'
        }
    })

# ============================================================================
# NYC MODULES ROUTES - ADDED FOR RANDOM LANDMARKS
# ============================================================================

@app.route('/nyc/home/')
def nyc_home():
    """NYC Home Page - Interactive Adventure"""
    return render_template('nyc_home.html')

@app.route('/new-york/shopping/')
def shopping():
    """Shopping module"""
    return render_template('shopping.html')

@app.route('/new-york/broadway/')
def broadway():
    """Broadway module"""
    return render_template('broadway.html')

@app.route('/new-york/breakfast/')
def breakfast():
    """Breakfast module"""
    return render_template('breakfast.html')

@app.route('/new-york/landmarks/')
def landmarks_random():
    """Randomly select one of four landmarks"""
    landmarks = ['met', 'icecream', 'empire', 'ukrainian']
    chosen = random.choice(landmarks)
    return redirect(f'/new-york/landmarks/{chosen}/')

@app.route('/new-york/landmarks/met/')
def landmarks_met():
    """The Metropolitan Museum of Art"""
    return render_template('landmarks_met.html')

@app.route('/new-york/landmarks/icecream/')
def landmarks_icecream():
    """Museum of Ice Cream"""
    return render_template('landmarks_icecream.html')

@app.route('/new-york/landmarks/empire/')
def landmarks_empire():
    """Empire State Building"""
    return render_template('landmarks_empire.html')

@app.route('/new-york/landmarks/ukrainian/')
def landmarks_ukrainian():
    """Ukrainian Museum"""
    return render_template('landmarks_ukrainian.html')

# ============================================================================
# EXISTING FLASK ROUTES (from your second file)
# ============================================================================

def is_safe_url(target):
    """Check if URL is safe for redirects"""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    error = None
    next_page = request.args.get('next', '') or request.form.get('next', '')
    if request.method == 'POST':
        user = User.query.filter_by(_uid=request.form['username']).first()
        if user and user.is_password(request.form['password']):
            login_user(user)
            if not is_safe_url(next_page):
                return abort(400)
            return redirect(next_page or url_for('index'))
        else:
            error = 'Invalid username or password.'
    return render_template("login.html", error=error, next=next_page)

@app.route('/studytracker')
def studytracker():
    """Study tracker page"""
    return render_template("studytracker.html")

@app.route('/logout')
def logout():
    """Logout user"""
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

@app.route('/')
def index():
    """Home page"""
    print("Home:", current_user)
    return render_template("index.html")

@app.route('/users/table2')
@login_required
def u2table():
    """User table page"""
    users = User.query.all()
    return render_template("u2table.html", user_data=users)

@app.route('/sections/')
@login_required
def sections():
    """Sections page"""
    sections = Section.query.all()
    return render_template("sections.html", sections=sections)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    """Delete user"""
    user = User.query.get(user_id)
    if user:
        user.delete()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/reset_password/<int:user_id>', methods=['POST'])
@login_required
def reset_password(user_id):
    """Reset user password"""
    if current_user.role != 'Admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if user.update({"password": app.config['DEFAULT_PASSWORD']}):
        return jsonify({'message': 'Password reset successfully'}), 200
    return jsonify({'error': 'Password reset failed'}), 500

@app.route('/kasm_users')
def kasm_users():
    """KASM users page"""
    SERVER = current_app.config.get('KASM_SERVER')
    API_KEY = current_app.config.get('KASM_API_KEY')
    API_KEY_SECRET = current_app.config.get('KASM_API_KEY_SECRET')

    if not SERVER or not API_KEY or not API_KEY_SECRET:
        return render_template('error.html', message='KASM keys are missing'), 400

    try:
        url = f"{SERVER}/api/public/get_users"
        data = {
            "api_key": API_KEY,
            "api_key_secret": API_KEY_SECRET
        }

        response = requests.post(url, json=data, timeout=10)

        if response.status_code != 200:
            return render_template(
                'error.html', 
                message='Failed to get users', 
                code=response.status_code
            ), response.status_code

        users = response.json().get('users', [])

        for user in users:
            last_session = user.get('last_session')
            try:
                user['last_session'] = datetime.fromisoformat(last_session) if last_session else None
            except ValueError:
                user['last_session'] = None

        sorted_users = sorted(
            users, 
            key=lambda x: x['last_session'] or datetime.min, 
            reverse=True
        )

        return render_template('kasm_users.html', users=sorted_users)

    except requests.RequestException as e:
        return render_template(
            'error.html', 
            message=f"Error connecting to KASM API: {str(e)}"
        ), 500

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user_kasm(user_id):
    """Delete KASM user"""
    if current_user.role != 'Admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    SERVER = current_app.config.get('KASM_SERVER')
    API_KEY = current_app.config.get('KASM_API_KEY')
    API_KEY_SECRET = current_app.config.get('KASM_API_KEY_SECRET')

    if not SERVER or not API_KEY or not API_KEY_SECRET:
        return {'message': 'KASM keys are missing'}, 400

    try:
        url = f"{SERVER}/api/public/delete_user"
        data = {
            "api_key": API_KEY,
            "api_key_secret": API_KEY_SECRET,
            "target_user": {"user_id": user_id},
            "force": False
        }
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'message': 'Failed to delete user'}, response.status_code

    except requests.RequestException as e:
        return {'message': 'Error connecting to KASM API', 'error': str(e)}, 500

@app.route('/update_user/<string:uid>', methods=['PUT'])
def update_user(uid):
    """Update user information"""
    if current_user.role != 'Admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    print(f"Request Data: {data}")

    user = User.query.filter_by(_uid=uid).first()
    if user:
        print(f"Found user: {user.uid}")
        user.update(data)
        return jsonify({"message": "User updated successfully."}), 200
    else:
        print("User not found.")
        return jsonify({"message": "User not found."}), 404

# ============================================================================
# MUSEUM SCRAPER WEB INTERFACE
# ============================================================================

@app.route('/museums')
def museums_home():
    """Museum scraper homepage with interactive interface"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🏛️ Museum Hours Scraper API</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            
            .container {
                max-width: 1400px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            }
            
            .header {
                text-align: center;
                margin-bottom: 50px;
            }
            
            .header h1 {
                font-size: 3.5em;
                color: #333;
                margin-bottom: 15px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .header p {
                font-size: 1.2em;
                color: #666;
                max-width: 800px;
                margin: 0 auto;
                line-height: 1.6;
            }
            
            .status-badge {
                display: inline-block;
                padding: 8px 20px;
                background: #4CAF50;
                color: white;
                border-radius: 50px;
                font-weight: bold;
                margin-top: 20px;
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
            
            .endpoints-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                margin-bottom: 50px;
            }
            
            .endpoint-card {
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
                border: 2px solid transparent;
            }
            
            .endpoint-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
                border-color: #667eea;
            }
            
            .endpoint-header {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
            }
            
            .endpoint-icon {
                font-size: 2.5em;
                margin-right: 20px;
                width: 70px;
                height: 70px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            
            .met-icon { background: linear-gradient(45deg, #8B4513, #D2691E); }
            .icecream-icon { background: linear-gradient(45deg, #FF69B4, #FF1493); }
            .ukrainian-icon { background: linear-gradient(45deg, #0057B7, #FFD700); }
            .empire-icon { background: linear-gradient(45deg, #708090, #2F4F4F); }
            .all-icon { background: linear-gradient(45deg, #4CAF50, #45a049); }
            .test-icon { background: linear-gradient(45deg, #2196F3, #21CBF3); }
            
            .endpoint-title {
                font-size: 1.5em;
                font-weight: bold;
                color: #333;
                margin-bottom: 5px;
            }
            
            .endpoint-url {
                font-family: 'Courier New', monospace;
                background: #f5f5f5;
                padding: 10px 15px;
                border-radius: 8px;
                margin: 15px 0;
                font-size: 0.9em;
                color: #333;
                overflow-x: auto;
            }
            
            .endpoint-description {
                color: #666;
                margin-bottom: 20px;
                line-height: 1.5;
            }
            
            .test-btn {
                display: inline-block;
                padding: 12px 30px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                border: none;
                cursor: pointer;
                transition: all 0.3s ease;
                font-size: 1em;
                width: 100%;
                text-align: center;
            }
            
            .test-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
            }
            
            .test-btn.loading {
                background: #999;
                cursor: not-allowed;
            }
            
            .result-container {
                margin-top: 20px;
                max-height: 300px;
                overflow-y: auto;
                background: #1a1a1a;
                border-radius: 8px;
                padding: 15px;
                display: none;
            }
            
            .result-title {
                color: #4CAF50;
                font-weight: bold;
                margin-bottom: 10px;
                font-family: monospace;
            }
            
            .result-data {
                color: #f0f0f0;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
                white-space: pre-wrap;
                word-wrap: break-word;
            }
            
            .api-info {
                background: linear-gradient(45deg, #f8f9fa, #e9ecef);
                border-radius: 15px;
                padding: 30px;
                margin-top: 50px;
            }
            
            .api-info h2 {
                color: #333;
                margin-bottom: 20px;
                font-size: 2em;
            }
            
            .api-info ul {
                list-style: none;
                padding-left: 0;
            }
            
            .api-info li {
                margin: 15px 0;
                padding-left: 30px;
                position: relative;
                color: #555;
            }
            
            .api-info li:before {
                content: '✓';
                position: absolute;
                left: 0;
                color: #4CAF50;
                font-weight: bold;
            }
            
            .quick-test {
                text-align: center;
                margin: 40px 0;
            }
            
            .quick-test-btn {
                display: inline-block;
                padding: 15px 40px;
                background: linear-gradient(45deg, #FF9800, #FF5722);
                color: white;
                text-decoration: none;
                border-radius: 50px;
                font-weight: bold;
                font-size: 1.1em;
                border: none;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            
            .quick-test-btn:hover {
                transform: scale(1.05);
                box-shadow: 0 15px 30px rgba(255, 87, 34, 0.4);
            }
            
            .museum-data {
                background: white;
                border-radius: 15px;
                padding: 25px;
                margin: 20px 0;
                border-left: 5px solid #667eea;
            }
            
            .museum-name {
                font-size: 1.4em;
                font-weight: bold;
                color: #333;
                margin-bottom: 10px;
            }
            
            .museum-hours {
                font-size: 1.1em;
                color: #4CAF50;
                font-weight: bold;
                margin: 10px 0;
            }
            
            .museum-details {
                color: #666;
                font-size: 0.95em;
                margin: 5px 0;
            }
            
            .museum-timestamp {
                color: #999;
                font-size: 0.85em;
                margin-top: 10px;
                font-style: italic;
            }
            
            @media (max-width: 768px) {
                .container {
                    padding: 20px;
                }
                
                .header h1 {
                    font-size: 2.5em;
                }
                
                .endpoints-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🏛️ Museum Hours Scraper API</h1>
                <p>A real-time web scraping API that fetches current hours from major NYC museums. This API makes actual HTTP requests to museum websites and parses the HTML to extract live hours information.</p>
                <div class="status-badge">✅ ACTIVE - Real Web Scraping</div>
            </div>
            
            <div class="quick-test">
                <button class="quick-test-btn" onclick="testAllEndpoints()">
                    🚀 Test All Museum Endpoints
                </button>
            </div>
            
            <div class="endpoints-grid">
                <div class="endpoint-card">
                    <div class="endpoint-header">
                        <div class="endpoint-icon met-icon">🎨</div>
                        <div>
                            <div class="endpoint-title">MET Museum</div>
                            <div class="endpoint-description">The Metropolitan Museum of Art</div>
                        </div>
                    </div>
                    <div class="endpoint-url">GET http://localhost:8587/api/met</div>
                    <div class="endpoint-description">
                        Scrapes hours from metmuseum.org using BeautifulSoup. Returns address, phone, and real-time hours.
                    </div>
                    <button class="test-btn" onclick="testEndpoint('met', this)">
                        Test MET Endpoint
                    </button>
                    <div id="met-result" class="result-container"></div>
                </div>
                
                <div class="endpoint-card">
                    <div class="endpoint-header">
                        <div class="endpoint-icon icecream-icon">🍦</div>
                        <div>
                            <div class="endpoint-title">Ice Cream Museum</div>
                            <div class="endpoint-description">Museum of Ice Cream NYC</div>
                        </div>
                    </div>
                    <div class="endpoint-url">GET http://localhost:858