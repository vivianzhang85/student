# main.py - Production-Ready Flask App with Database Backend
# INTEGRATED WITH EXISTING FLASK-SQLALCHEMY SETUP
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
import json
import uuid
from datetime import timedelta
from typing import Dict, List, Optional, Any

# Import database and models - USE EXISTING db INSTANCE
from __init__ import app, db, login_manager

# Import SQLAlchemy components
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, JSON, func
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError

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

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

# Get database configuration from environment variables or use defaults
DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite').lower()

# Configure additional database settings if needed
if DATABASE_TYPE == 'postgresql':
    # Update Flask app config for PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('DATABASE_USER', 'postgres')}:"
        f"{os.getenv('DATABASE_PASSWORD', '')}@"
        f"{os.getenv('DATABASE_HOST', 'localhost')}:"
        f"{os.getenv('DATABASE_PORT', '5432')}/"
        f"{os.getenv('DATABASE_NAME', 'itinerary_db')}"
    )
elif DATABASE_TYPE == 'mysql':
    # Update for MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('DATABASE_USER', 'root')}:"
        f"{os.getenv('DATABASE_PASSWORD', '')}@"
        f"{os.getenv('DATABASE_HOST', 'localhost')}:"
        f"{os.getenv('DATABASE_PORT', '3306')}/"
        f"{os.getenv('DATABASE_NAME', 'itinerary_db')}"
    )
# For SQLite, keep existing configuration from __init__.py

# Add connection pool settings
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'pool_recycle': 300,
    'pool_pre_ping': True,
}

# Initialize CORS for all origins
CORS(app, 
     resources={r"/*": {"origins": "*"}},
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization", "X-Origin"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"])

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
# DATABASE MODELS - WEBSITE BACKEND TABLES
# ============================================================================

class Itinerary(db.Model):
    """Main itinerary table - stores current version for each user"""
    __tablename__ = 'itinerary'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), index=True)
    user_id = db.Column(db.Integer, index=True)
    
    # JSON data for each section
    trip_info = db.Column(db.JSON, nullable=True)
    breakfast = db.Column(db.JSON, nullable=True)
    landmarks = db.Column(db.JSON, nullable=True)
    shopping = db.Column(db.JSON, nullable=True)
    broadway = db.Column(db.JSON, nullable=True)
    
    # Metadata
    version = db.Column(db.Integer, default=1)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    history_entries = relationship('ItineraryHistory', back_populates='itinerary', cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'session_id': self.session_id,
            'user_id': self.user_id,
            'trip_info': self.trip_info,
            'breakfast': self.breakfast,
            'landmarks': self.landmarks,
            'shopping': self.shopping,
            'broadway': self.broadway,
            'version': self.version,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class ItineraryHistory(db.Model):
    """Complete history of itinerary changes"""
    __tablename__ = 'itinerary_history'
    
    id = db.Column(db.Integer, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id', ondelete='CASCADE'))
    user_id = db.Column(db.Integer, index=True)
    session_id = db.Column(db.String(255), index=True)
    
    # JSON data for each section at this historical point
    trip_info = db.Column(db.JSON, nullable=True)
    breakfast = db.Column(db.JSON, nullable=True)
    landmarks = db.Column(db.JSON, nullable=True)
    shopping = db.Column(db.JSON, nullable=True)
    broadway = db.Column(db.JSON, nullable=True)
    
    # Change metadata
    version = db.Column(db.Integer, nullable=False)
    change_type = db.Column(db.String(50), nullable=False)  # 'create', 'update', 'delete', 'restore'
    change_description = db.Column(db.Text, nullable=True)
    changed_by = db.Column(db.String(50), nullable=False)   # 'user', 'guest', 'admin', 'system'
    ip_address = db.Column(db.String(45), nullable=True)    # Supports IPv6
    user_agent = db.Column(db.Text, nullable=True)
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    itinerary = relationship('Itinerary', back_populates='history_entries')
    section_changes = relationship('ItinerarySectionChange', back_populates='history', cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'itinerary_id': self.itinerary_id,
            'user_id': self.user_id,
            'session_id': self.session_id,
            'trip_info': self.trip_info,
            'breakfast': self.breakfast,
            'landmarks': self.landmarks,
            'shopping': self.shopping,
            'broadway': self.broadway,
            'version': self.version,
            'change_type': self.change_type,
            'change_description': self.change_description,
            'changed_by': self.changed_by,
            'ip_address': self.ip_address,
            'user_agent': self.user_agent,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class ItinerarySectionChange(db.Model):
    """Detailed section-by-section change tracking"""
    __tablename__ = 'itinerary_section_changes'
    
    id = db.Column(db.Integer, primary_key=True)
    history_id = db.Column(db.Integer, db.ForeignKey('itinerary_history.id', ondelete='CASCADE'))
    section_name = db.Column(db.String(50), nullable=False)  # 'trip_info', 'breakfast', etc.
    old_value = db.Column(db.JSON, nullable=True)
    new_value = db.Column(db.JSON, nullable=True)
    change_summary = db.Column(db.Text, nullable=True)
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    history = relationship('ItineraryHistory', back_populates='section_changes')
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'history_id': self.history_id,
            'section_name': self.section_name,
            'old_value': self.old_value,
            'new_value': self.new_value,
            'change_summary': self.change_summary,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class BreakfastRestaurant(db.Model):
    """Breakfast restaurant data"""
    __tablename__ = 'breakfast_restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    restaurant = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=True)
    day = db.Column(db.String(20), nullable=False)
    open_time = db.Column(db.String(50), nullable=True)
    close_time = db.Column(db.String(50), nullable=True)
    hours_text = db.Column(db.Text, nullable=True)
    cuisine = db.Column(db.String(100), nullable=True)
    specialty = db.Column(db.String(255), nullable=True)
    scraped_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class BroadwayShow(db.Model):
    """Broadway show data"""
    __tablename__ = 'broadway_shows'
    
    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(255), nullable=False)
    show_date = db.Column(db.String(100), nullable=True)
    price_range = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    scraped_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    source = db.Column(db.String(100), nullable=True)


class CustomEvent(db.Model):
    """User-created custom events"""
    __tablename__ = 'custom_events'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=False, index=True)
    event_name = db.Column(db.String(255), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=True)
    time = db.Column(db.String(100), nullable=True)
    price = db.Column(db.String(100), nullable=True)
    image_url = db.Column(db.Text, nullable=True)
    is_approved = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    # Popularity tracking
    times_added = db.Column(db.Integer, default=0)
    last_added = db.Column(db.DateTime(timezone=True), nullable=True)

# ============================================================================
# DATABASE SERVICE LAYER
# ============================================================================

class DatabaseService:
    """Service layer for database operations"""
    
    @staticmethod
    def create_tables():
        """Create all database tables"""
        with app.app_context():
            db.create_all()
            print(f"✅ Database tables created successfully")
            print(f"   Current database: {db.engine.url}")
            print(f"   Tables created: itinerary, itinerary_history, itinerary_section_changes")
    
    @staticmethod
    def drop_tables():
        """Drop all tables (for testing/reset)"""
        with app.app_context():
            db.drop_all()
            print("⚠️ All tables dropped")
    
    @staticmethod
    def init_database():
        """Initialize database - create tables if they don't exist"""
        with app.app_context():
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            existing_tables = inspector.get_table_names()
            
            # Define required tables
            required_tables = ['itinerary', 'itinerary_history', 'itinerary_section_changes']
            
            # Check if required tables exist
            missing_tables = [table for table in required_tables if table not in existing_tables]
            
            if missing_tables:
                print(f"📊 Creating missing tables: {missing_tables}")
                db.create_all()
                print("✅ Database tables initialized")
            else:
                print(f"📊 Database already has {len(existing_tables)} tables")
    
    @staticmethod
    def get_session():
        """Get a database session"""
        return db.session

# ============================================================================
# ENHANCED ITINERARY SERVICE
# ============================================================================

class EnhancedItineraryService:
    """Service for itinerary operations"""
    
    def create_session(self):
        """Create a new session ID"""
        return str(uuid.uuid4())
    
    def save_itinerary(self, session_id: str, itinerary_data: Dict, user_id: Optional[int] = None,
                      change_description: str = "Created itinerary", request_info: Optional[Dict] = None) -> Dict:
        """Save or update itinerary data with history tracking"""
        try:
            session = DatabaseService.get_session()
            
            # Get request info for audit logging
            ip_address = request_info.get('ip_address', '') if request_info else ''
            user_agent = request_info.get('user_agent', '') if request_info else ''
            
            # Find existing active itinerary
            existing_itinerary = None
            if user_id:
                existing_itinerary = Itinerary.query.filter_by(
                    user_id=user_id,
                    is_active=True
                ).first()
            elif session_id:
                existing_itinerary = Itinerary.query.filter_by(
                    session_id=session_id,
                    is_active=True
                ).first()
            
            if existing_itinerary:
                # Save current state to history before updating
                self._create_history_entry(
                    itinerary=existing_itinerary,
                    change_type='update',
                    change_description=change_description,
                    changed_by='user' if user_id else 'guest',
                    ip_address=ip_address,
                    user_agent=user_agent,
                    save_old_data=True
                )
                
                # Update existing itinerary
                existing_itinerary.trip_info = itinerary_data.get('trip_info')
                existing_itinerary.breakfast = itinerary_data.get('breakfast')
                existing_itinerary.landmarks = itinerary_data.get('landmarks')
                existing_itinerary.shopping = itinerary_data.get('shopping')
                existing_itinerary.broadway = itinerary_data.get('broadway')
                existing_itinerary.version += 1
                
                itinerary_id = existing_itinerary.id
                new_version = existing_itinerary.version
                
            else:
                # Create new itinerary
                new_itinerary = Itinerary(
                    session_id=session_id,
                    user_id=user_id,
                    trip_info=itinerary_data.get('trip_info'),
                    breakfast=itinerary_data.get('breakfast'),
                    landmarks=itinerary_data.get('landmarks'),
                    shopping=itinerary_data.get('shopping'),
                    broadway=itinerary_data.get('broadway'),
                    version=1,
                    is_active=True
                )
                
                session.add(new_itinerary)
                session.flush()
                
                itinerary_id = new_itinerary.id
                new_version = 1
                
                # Create history entry for creation
                self._create_history_entry(
                    itinerary=new_itinerary,
                    change_type='create',
                    change_description='Initial itinerary creation',
                    changed_by='user' if user_id else 'guest',
                    ip_address=ip_address,
                    user_agent=user_agent,
                    save_old_data=False
                )
            
            session.commit()
            
            return {
                'success': True,
                'session_id': session_id,
                'user_id': user_id,
                'itinerary_id': itinerary_id,
                'version': new_version,
                'message': 'Itinerary saved successfully'
            }
            
        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Database error: {e}")
            return {'success': False, 'error': str(e)}
        except Exception as e:
            session.rollback()
            print(f"❌ Error: {e}")
            return {'success': False, 'error': str(e)}
    
    def _create_history_entry(self, itinerary: Itinerary, change_type: str, change_description: str,
                             changed_by: str, ip_address: str, user_agent: str, save_old_data: bool = True):
        """Create a history entry"""
        session = DatabaseService.get_session()
        
        # Get old values if needed
        old_values = None
        if save_old_data and itinerary.id:
            current_state = Itinerary.query.get(itinerary.id)
            if current_state:
                old_values = {
                    'trip_info': current_state.trip_info,
                    'breakfast': current_state.breakfast,
                    'landmarks': current_state.landmarks,
                    'shopping': current_state.shopping,
                    'broadway': current_state.broadway,
                }
        
        # Create history entry
        history_entry = ItineraryHistory(
            itinerary_id=itinerary.id,
            user_id=itinerary.user_id,
            session_id=itinerary.session_id,
            trip_info=itinerary.trip_info,
            breakfast=itinerary.breakfast,
            landmarks=itinerary.landmarks,
            shopping=itinerary.shopping,
            broadway=itinerary.broadway,
            version=itinerary.version,
            change_type=change_type,
            change_description=change_description,
            changed_by=changed_by,
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        session.add(history_entry)
        session.flush()
        
        # Record section changes if we have old values
        if save_old_data and old_values:
            self._record_section_changes(history_entry.id, old_values, {
                'trip_info': itinerary.trip_info,
                'breakfast': itinerary.breakfast,
                'landmarks': itinerary.landmarks,
                'shopping': itinerary.shopping,
                'broadway': itinerary.broadway,
            })
    
    def _record_section_changes(self, history_id: int, old_values: Dict, new_values: Dict):
        """Record section changes"""
        session = DatabaseService.get_session()
        sections = ['trip_info', 'breakfast', 'landmarks', 'shopping', 'broadway']
        
        for section_name in sections:
            old_value = old_values.get(section_name)
            new_value = new_values.get(section_name)
            
            if old_value != new_value:
                change_summary = self._generate_change_summary(section_name, old_value, new_value)
                
                section_change = ItinerarySectionChange(
                    history_id=history_id,
                    section_name=section_name,
                    old_value=old_value,
                    new_value=new_value,
                    change_summary=change_summary
                )
                
                session.add(section_change)
    
    def _generate_change_summary(self, section_name, old_value, new_value):
        """Generate change summary"""
        if not old_value and new_value:
            return f"Added {section_name}"
        elif old_value and not new_value:
            return f"Removed {section_name}"
        elif old_value and new_value:
            if isinstance(old_value, dict) and isinstance(new_value, dict):
                changed_keys = []
                all_keys = set(list(old_value.keys()) + list(new_value.keys()))
                for key in all_keys:
                    if old_value.get(key) != new_value.get(key):
                        changed_keys.append(key)
                if changed_keys:
                    return f"Updated {section_name}: {', '.join(changed_keys[:3])}"
            return f"Modified {section_name}"
        return f"Updated {section_name}"
    
    def get_itinerary(self, session_id=None, user_id=None, version=None):
        """Get itinerary data"""
        try:
            if version and version > 0:
                # Get historical version
                query = ItineraryHistory.query
                
                if user_id:
                    query = query.filter_by(user_id=user_id)
                elif session_id:
                    query = query.filter_by(session_id=session_id)
                else:
                    return {'success': False, 'error': 'No session_id or user_id provided'}
                
                history_entry = query.filter_by(version=version)\
                                   .order_by(ItineraryHistory.created_at.desc())\
                                   .first()
                
                if history_entry:
                    return {
                        'success': True,
                        'session_id': session_id,
                        'user_id': user_id,
                        'version': version,
                        'data': {
                            'trip_info': history_entry.trip_info,
                            'breakfast': history_entry.breakfast,
                            'landmarks': history_entry.landmarks,
                            'shopping': history_entry.shopping,
                            'broadway': history_entry.broadway,
                            'version': history_entry.version,
                            'created_at': history_entry.created_at.isoformat() if history_entry.created_at else None,
                            'change_description': history_entry.change_description,
                            'is_historical': True
                        }
                    }
            
            # Get current version
            query = Itinerary.query.filter_by(is_active=True)
            
            if user_id:
                itinerary = query.filter_by(user_id=user_id).first()
            elif session_id:
                itinerary = query.filter_by(session_id=session_id).first()
            else:
                return {'success': False, 'error': 'No session_id or user_id provided'}
            
            if itinerary:
                return {
                    'success': True,
                    'session_id': session_id,
                    'user_id': user_id,
                    'data': itinerary.to_dict()
                }
            else:
                return {
                    'success': True,
                    'session_id': session_id,
                    'user_id': user_id,
                    'data': {
                        'trip_info': None,
                        'breakfast': None,
                        'landmarks': None,
                        'shopping': None,
                        'broadway': None,
                        'version': 0,
                        'is_active': False,
                        'created_at': None,
                        'updated_at': None,
                        'is_historical': False
                    }
                }
                
        except SQLAlchemyError as e:
            print(f"❌ Database error: {e}")
            return {'success': False, 'error': str(e)}
    
    def get_itinerary_history(self, user_id=None, session_id=None, limit=50):
        """Get itinerary history"""
        try:
            query = ItineraryHistory.query
            
            if user_id:
                query = query.filter_by(user_id=user_id)
            elif session_id:
                query = query.filter_by(session_id=session_id)
            else:
                return {'success': False, 'error': 'No session_id or user_id provided'}
            
            history_entries = query.order_by(ItineraryHistory.created_at.desc())\
                                 .limit(limit)\
                                 .all()
            
            history = [entry.to_dict() for entry in history_entries]
            
            return {
                'success': True,
                'count': len(history),
                'history': history
            }
            
        except SQLAlchemyError as e:
            print(f"❌ Database error: {e}")
            return {'success': False, 'error': str(e)}
    
    def get_version_changes(self, history_id):
        """Get detailed changes for a history entry"""
        try:
            history_entry = ItineraryHistory.query.get(history_id)
            if not history_entry:
                return {'success': False, 'error': 'History entry not found'}
            
            section_changes = ItinerarySectionChange.query\
                .filter_by(history_id=history_id)\
                .all()
            
            changes = [change.to_dict() for change in section_changes]
            
            return {
                'success': True,
                'history': history_entry.to_dict(),
                'changes': changes,
                'change_count': len(changes)
            }
            
        except SQLAlchemyError as e:
            print(f"❌ Database error: {e}")
            return {'success': False, 'error': str(e)}

# Create itinerary service instance
itinerary_service = EnhancedItineraryService()

# ============================================================================
# DATABASE INITIALIZATION - MODERN APPROACH
# ============================================================================

# Use app.before_request for Flask 2.3+
@app.before_request
def initialize_database_on_first_request():
    """Initialize database on first request"""
    # Check if we've already initialized
    if not hasattr(g, 'database_initialized'):
        try:
            print(f"🔧 Initializing database...")
            with app.app_context():
                DatabaseService.init_database()
                print("✅ Database initialized successfully")
            g.database_initialized = True
        except Exception as e:
            print(f"⚠️ Database initialization warning: {e}")
            g.database_initialized = False

# ============================================================================
# ITINERARY API ENDPOINTS
# ============================================================================

@app.route('/api/id')
def get_user_id():
    """Get current user information"""
    try:
        if current_user.is_authenticated:
            user_data = {
                'id': current_user.id,
                'uid': current_user.uid,
                'name': current_user.name if hasattr(current_user, 'name') else current_user.uid,
                'roles': [role.to_dict() for role in current_user.roles] if hasattr(current_user, 'roles') else [],
                'is_authenticated': True
            }
            return jsonify(user_data)
        else:
            return jsonify({'is_authenticated': False, 'message': 'Not authenticated'})
    except Exception as e:
        print(f"Error in /api/id: {e}")
        return jsonify({'is_authenticated': False, 'error': str(e)})

@app.route('/api/itinerary', methods=['GET'])
def get_itinerary():
    """GET itinerary for current session or user"""
    try:
        user_id = current_user.id if current_user.is_authenticated else None
        session_id = request.cookies.get('itinerary_session_id')
        version = request.args.get('version', type=int)
        
        if not session_id:
            session_id = itinerary_service.create_session()
        
        result = itinerary_service.get_itinerary(
            session_id=session_id,
            user_id=user_id,
            version=version
        )
        
        if result['success']:
            response = jsonify(result)
            response.set_cookie('itinerary_session_id', session_id, max_age=30*24*60*60)
            return response
        else:
            return jsonify(result), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/itinerary', methods=['POST', 'PUT'])
def save_itinerary():
    """Save or update itinerary"""
    try:
        user_id = current_user.id if current_user.is_authenticated else None
        session_id = request.cookies.get('itinerary_session_id')
        
        if not session_id:
            session_id = itinerary_service.create_session()
        
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'No itinerary data provided'}), 400
        
        request_info = {
            'ip_address': request.remote_addr,
            'user_agent': request.headers.get('User-Agent', '')
        }
        
        change_description = data.get('change_description', 'Updated itinerary')
        
        result = itinerary_service.save_itinerary(
            session_id=session_id,
            itinerary_data=data,
            user_id=user_id,
            change_description=change_description,
            request_info=request_info
        )
        
        if result['success']:
            response = jsonify(result)
            response.set_cookie('itinerary_session_id', session_id, max_age=30*24*60*60)
            return response
        else:
            return jsonify(result), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/itinerary/history', methods=['GET'])
def get_itinerary_history():
    """Get itinerary history"""
    try:
        user_id = current_user.id if current_user.is_authenticated else None
        session_id = request.cookies.get('itinerary_session_id')
        
        if not user_id and not session_id:
            return jsonify({'success': False, 'error': 'No session or user'}), 400
        
        limit = request.args.get('limit', 50, type=int)
        
        result = itinerary_service.get_itinerary_history(
            user_id=user_id,
            session_id=session_id,
            limit=limit
        )
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/database/info', methods=['GET'])
def get_database_info():
    """Get database information"""
    try:
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        
        info = {
            'database_url': str(db.engine.url).replace('://', '://***:***@') if '://' in str(db.engine.url) else str(db.engine.url),
            'database_type': DATABASE_TYPE,
            'tables': inspector.get_table_names(),
            'connected': True
        }
        
        return jsonify({'success': True, 'database_info': info})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ============================================================================
# EXISTING ROUTES (Add these from your original main.py)
# ============================================================================

# Add all your existing routes here...
# For example:

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
            
            # Sync itinerary from session to user account
            session_id = request.cookies.get('itinerary_session_id')
            if session_id:
                try:
                    # We'll implement this later
                    pass
                except Exception as e:
                    print(f"Note: Could not sync itinerary on login: {e}")
            
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

# Add other existing routes from your original main.py...

# ============================================================================
# MUSEUM SCRAPER CLASSES (Add these from your original main.py)
# ============================================================================

class MuseumScraper:
    """Web scraper for museum hours"""
    
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
        'timestamp': datetime.now().strftime("%Y-%m-d %H:%M:%S"),
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
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 FLASK APPLICATION WITH DATABASE BACKEND")
    print("=" * 70)
    print(f"📊 Database: {DATABASE_TYPE.upper()}")
    print(f"📡 API Endpoints:")
    print(f"   • http://localhost:8303/api/itinerary")
    print(f"   • http://localhost:8303/api/itinerary/history")
    print(f"   • http://localhost:8303/api/database/info")
    print("=" * 70)
    
    port = int(os.environ.get('PORT', 8303))
    host = "0.0.0.0"
    
    # Initialize database before starting
    with app.app_context():
        try:
            DatabaseService.init_database()
            print("✅ Database initialized successfully")
        except Exception as e:
            print(f"⚠️ Database initialization warning: {e}")
    
    app.run(debug=True, host=host, port=port, use_reloader=False)