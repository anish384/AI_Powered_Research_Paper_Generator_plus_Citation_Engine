from flask import render_template, request, jsonify, send_file
from . import main_bp
from services.paper_service import PaperService
import os

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/generate')
def generate():
    return render_template('generate.html')

@main_bp.route('/result')
def result():
    return render_template('result.html')
