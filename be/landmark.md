---
layout: post
title: "Step 3 Landmarks"
description: "Let's see the sights of the big apple!"
permalink: /new-york/landmarks/
parent: "Analytics/Admin"
team: "Insightful Innovators"
submodule: 4
author: "Insightful Innovators"
date: 2025-11-20
microblog: true
footer: 
    previous: /new-york/shopping/
    home: /nyc/home/
    next: /new-york/broadway/
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NYC Landmarks Experience</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a1a35 0%, #1a2a4a 100%);
            color: white;
            min-height: 100vh;
        }

        /* Fixed Sidebar - EXACT MATCH FROM BREAKFAST PAGE */
        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            width: 260px;
            height: 100vh;
            background: linear-gradient(180deg, #1a365d 0%, #2d4a7c 50%, #4a6fa5 100%);
            border-right: 3px solid #FFD700;
            padding: 25px 20px;
            z-index: 1000;
            overflow-y: auto;
            box-shadow: 4px 0 20px rgba(255, 215, 0, 0.3);
        }

        .sidebar-header {
            margin-bottom: 35px;
            padding-bottom: 20px;
            border-bottom: 3px solid #FFD700;
            text-align: center;
        }

        .sidebar-header h2 {
            color: #FFD700;
            font-size: 1.6rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        .sidebar-header p {
            color: #FFE55C;
            font-size: 0.85rem;
            margin-top: 8px;
            opacity: 0.9;
        }

        .nav-menu {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .nav-button {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 215, 0, 0.3);
            color: #f0fdfa;
            padding: 16px 20px;
            border-radius: 12px;
            font-size: 1.05rem;
            font-weight: 600;
            cursor: pointer;
            text-align: left;
            transition: all 0.3s ease;
            border-left: 5px solid transparent;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }

        .nav-button:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: translateX(8px);
            border-left-color: #FFD700;
            box-shadow: 0 4px 12px rgba(255, 215, 0, 0.4);
        }

        .nav-button.active {
            background: rgba(255, 215, 0, 0.3);
            border-left-color: #FFD700;
            border-color: #FFD700;
            color: #FFD700;
            box-shadow: 0 4px 16px rgba(255, 215, 0, 0.5);
        }

        .nav-button.breakfast {
            border-left-color: #fbbf24;
        }

        .nav-button.landmarks {
            border-left-color: #FFD700;
        }

        .nav-button.shopping {
            border-left-color: #c084fc;
        }

        .nav-button.broadway {
            border-left-color: #34d399;
        }

        /* Main Content Area - Shifted right for sidebar */
        .main-content {
            margin-left: 280px;
            margin-right: 0;
            padding: 30px 60px 30px 20px;
            min-height: 100vh;
            max-width: 1400px;
        }

        .container {
            max-width: 100%;
            margin: 0;
            width: 100%;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            border: 2px solid #FFD700;
        }

        .header h1 {
            font-size: 48px;
            margin: 0 0 10px 0;
            color: #FFD700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .header p {
            font-size: 1.2rem;
            color: #cbd5e1;
        }

        /* Landmark Cards - Full width, all details inside */
        .section {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            margin-bottom: 40px;
            border: 2px solid transparent;
            transition: all 0.3s;
            overflow: hidden;
            width: 100%;
        }

        .section:hover {
            transform: translateY(-5px);
            border-color: #FFD700;
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);
        }

        .animation-container {
            position: relative;
            overflow: hidden;
            height: 40vh;
            min-height: 300px;
            width: 100%;
        }

        .content-container {
            background: rgba(0, 0, 0, 0.3);
            padding: 2rem;
            border-top: 2px solid #FFD700;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            color: #FFD700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            font-weight: 800;
        }

        .section-subtitle {
            font-size: 1.2rem;
            color: #cbd5e1;
            margin-bottom: 2rem;
            font-weight: 600;
        }

        .content-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .info-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.3);
            border: 1px solid #FFD700;
        }

        .info-card h3 {
            margin-bottom: 1rem;
            color: #FFD700;
            border-bottom: 2px solid #FFD700;
            padding-bottom: 0.5rem;
            font-weight: 700;
        }

        .hours-list {
            list-style: none;
        }

        .hours-list li {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            color: #f0fdfa;
            font-weight: 500;
        }

        .highlight-list {
            list-style: none;
        }

        .highlight-list li {
            padding: 0.5rem 0;
            position: relative;
            padding-left: 1.5rem;
            color: #f0fdfa;
            font-weight: 500;
        }

        .highlight-list li::before {
            content: '★';
            position: absolute;
            left: 0;
            color: #FFD700;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }

        .reviews-container {
            margin-top: 2rem;
        }

        .review-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            border-left: 4px solid #FFD700;
        }

        .review-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }

        .review-author {
            font-weight: bold;
            color: #FFD700;
        }

        .review-date {
            color: #cbd5e1;
            font-size: 0.9rem;
        }

        .review-rating {
            color: #FFD700;
            margin-bottom: 0.5rem;
        }

        .review-text {
            color: #f0fdfa;
            line-height: 1.5;
            font-size: 0.9rem;
        }

        .interactive-buttons {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 0.8rem 1.5rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 700;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            box-shadow: 0 3px 8px rgba(0,0,0,0.3);
        }

        .btn-primary {
            background: linear-gradient(90deg, #f59e0b, #f97316);
            color: white;
        }

        .btn-primary:hover {
            background: linear-gradient(90deg, #f97316, #f59e0b);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(245, 158, 11, 0.4);
        }

        .btn-success {
            background: linear-gradient(90deg, #10b981, #059669);
            color: white;
        }

        .btn-success:hover {
            background: linear-gradient(90deg, #059669, #10b981);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4);
        }

        .interactive-section {
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            border: 1px solid #FFD700;
        }

        .interactive-title {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #FFD700;
            text-align: center;
        }

        .game-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }

        .game-instructions {
            color: #cbd5e1;
            text-align: center;
            margin-bottom: 1rem;
        }

        /* Animation Styles */
        .met-animation {
            background: linear-gradient(180deg, #1a3a5f 0%, #2d4a7c 50%, #4a6fa5 100%);
            position: relative;
            height: 100%;
            overflow: hidden;
        }

        .met-building {
            position: absolute;
            bottom: 15%;
            left: 50%;
            transform: translateX(-50%);
            width: 320px;
            height: 200px;
            background: linear-gradient(45deg, #8B7355, #A52A2A);
            border-radius: 15px 15px 0 0;
            box-shadow: 0 0 40px rgba(0,0,0,0.6);
        }

        .met-roof {
            position: absolute;
            top: -40px;
            left: -20px;
            right: -20px;
            height: 50px;
            background: #8B4513;
            clip-path: polygon(0 100%, 5% 0, 95% 0, 100% 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            color: #FFD700;
            font-weight: bold;
            font-size: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        }

        .met-columns {
            position: absolute;
            bottom: 0;
            display: flex;
            justify-content: space-around;
            width: 100%;
            padding: 0 40px;
        }

        .met-column {
            width: 20px;
            height: 150px;
            background: linear-gradient(45deg, #DEB887, #F5F5DC);
            border-radius: 8px 8px 0 0;
            position: relative;
        }

        .met-column::before {
            content: '';
            position: absolute;
            top: -15px;
            left: -5px;
            right: -5px;
            height: 20px;
            background: #F5F5DC;
            border-radius: 5px;
        }

        .art-pieces {
            position: absolute;
            top: 15%;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-around;
        }

        .art-piece {
            width: 60px;
            height: 80px;
            background: linear-gradient(45deg, #FFD700, #FF6347);
            border-radius: 8px;
            animation: floatArt 6s ease-in-out infinite;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
            border: 3px solid #FFD700;
        }

        .icecream-animation {
            background: linear-gradient(180deg, #87CEEB 0%, #FFB6C1 30%, #FF69B4 70%, #FF1493 100%);
            position: relative;
            height: 100%;
            overflow: hidden;
        }

        .icecream-ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 20%;
            background: linear-gradient(45deg, #FFD700, #FFA500);
        }

        .icecream-building {
            position: absolute;
            bottom: 20%;
            left: 50%;
            transform: translateX(-50%);
            width: 300px;
            height: 180px;
            background: linear-gradient(45deg, #FF69B4, #FF1493);
            border-radius: 15px 15px 0 0;
            box-shadow: 0 0 30px rgba(255,105,180,0.6);
            border: 5px solid #FFD700;
        }

        .icecream-sign {
            position: absolute;
            top: -60px;
            left: 50%;
            transform: translateX(-50%);
            color: #FFD700;
            font-weight: bold;
            font-size: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
            white-space: nowrap;
        }

        .floating-cones {
            position: absolute;
            top: 10%;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-around;
        }

        .floating-cone {
            width: 50px;
            height: 70px;
            background: #D2691E;
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            animation: floatCone 8s ease-in-out infinite;
            position: relative;
        }

        .giant-icecream {
            position: absolute;
            top: -120px;
            left: 50%;
            transform: translateX(-50%);
        }

        .empire-animation {
            background: linear-gradient(180deg, #0a1628 0%, #1a2a4a 30%, #2d4a7c 60%, #4a6fa5 100%);
            position: relative;
            height: 100%;
            overflow: hidden;
        }

        .empire-building {
            position: absolute;
            bottom: 5%;
            left: 50%;
            transform: translateX(-50%);
            width: 150px;
            height: 320px;
            background: linear-gradient(45deg, #708090, #2F4F4F);
            box-shadow: 0 0 50px rgba(255,255,255,0.2);
        }

        .empire-antenna {
            position: absolute;
            bottom: 320px;
            left: 50%;
            transform: translateX(-50%);
            width: 3px;
            height: 60px;
            background: #C0C0C0;
        }

        .antenna-light {
            position: absolute;
            bottom: 380px;
            left: 50%;
            transform: translateX(-50%);
            width: 15px;
            height: 15px;
            background: #FF0000;
            border-radius: 50%;
            animation: blinkAntenna 2s ease-in-out infinite;
            box-shadow: 0 0 15px #FF0000;
        }

        .ukrainian-animation {
            background: linear-gradient(180deg, #0057B7 0%, #0057B7 50%, #FFD700 50%, #FFD700 100%);
            position: relative;
            height: 100%;
            overflow: hidden;
        }

        .ukrainian-title {
            position: absolute;
            top: 20%;
            left: 50%;
            transform: translateX(-50%);
            color: #FFD700;
            font-weight: bold;
            font-size: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
            z-index: 10;
        }

        .ukrainian-building {
            position: absolute;
            bottom: 15%;
            left: 50%;
            transform: translateX(-50%);
            width: 250px;
            height: 180px;
            background: linear-gradient(45deg, #8B0000, #A52A2A);
            border-radius: 10px;
            box-shadow: 0 0 30px rgba(0,0,0,0.5);
            border: 4px solid #FFD700;
        }

        .ukrainian-roof {
            position: absolute;
            top: -30px;
            left: -15px;
            right: -15px;
            height: 40px;
            background: #FFD700;
            clip-path: polygon(0 100%, 5% 0, 95% 0, 100% 100%);
        }

        /* Interactive Game Elements */
        .art-game {
            display: flex;
            justify-content: space-around;
            width: 100%;
            margin-top: 1rem;
        }

        .art-sample {
            width: 60px;
            height: 80px;
            border-radius: 5px;
            cursor: pointer;
            transition: transform 0.3s;
            box-shadow: 0 3px 10px rgba(0,0,0,0.3);
        }

        .art-sample:hover {
            transform: scale(1.1);
        }

        .sprinkle-pool {
            width: 100%;
            height: 150px;
            background: #FFB6C1;
            border-radius: 10px;
            margin-top: 1rem;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }

        .sprinkle-game {
            position: absolute;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            animation: fallSprinkle 3s linear forwards;
        }

        .observation-game {
            width: 100%;
            height: 150px;
            background: #2c3e50;
            border-radius: 10px;
            margin-top: 1rem;
            position: relative;
            overflow: hidden;
        }

        .nyc-skyline {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 60px;
            background: #34495e;
        }

        .building {
            position: absolute;
            bottom: 0;
            width: 20px;
            background: #7f8c8d;
        }

        .embroidery-game {
            width: 100%;
            height: 150px;
            background: white;
            border-radius: 10px;
            margin-top: 1rem;
            position: relative;
            overflow: hidden;
            cursor: crosshair;
            background-image: 
                linear-gradient(#f0f0f0 1px, transparent 1px),
                linear-gradient(90deg, #f0f0f0 1px, transparent 1px);
            background-size: 20px 20px;
        }

        .embroidery-line {
            position: absolute;
            background: transparent;
            transform-origin: 0 0;
        }

        @keyframes floatArt {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-25px) rotate(5deg); }
        }

        @keyframes floatCone {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-30px) rotate(15deg); }
        }

        @keyframes blinkAntenna {
            0%, 100% { opacity: 1; box-shadow: 0 0 15px #FF0000; }
            50% { opacity: 0.3; box-shadow: 0 0 8px #FF0000; }
        }

        @keyframes fallSprinkle {
            0% { transform: translateY(-10px) rotate(0deg); opacity: 1; }
            100% { transform: translateY(150px) rotate(360deg); opacity: 0; }
        }

        /* Itinerary Tracker - Right Side */
        .itinerary-tracker {
            position: fixed;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            width: 300px;
            background: rgba(26, 35, 50, 0.95);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            border: 2px solid #ffd700;
            z-index: 9999;
            max-height: 80vh;
            overflow-y: auto;
        }

        .itinerary-tracker h3 {
            color: #ffd700;
            margin-bottom: 15px;
            font-size: 1.3rem;
            text-align: center;
            border-bottom: 2px solid #ffd700;
            padding-bottom: 10px;
        }

        .itinerary-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 10px;
            border-left: 4px solid #ffd700;
        }

        .itinerary-item.incomplete {
            border-left-color: #666;
            opacity: 0.6;
        }

        .itinerary-label {
            font-size: 0.85rem;
            color: #ffd700;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .itinerary-value {
            color: #fff;
            font-size: 1rem;
            font-weight: 500;
        }

        .itinerary-empty {
            color: #999;
            font-style: italic;
            font-size: 0.9rem;
        }

        .clear-itinerary-btn {
            width: 100%;
            background: #ef4444;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            margin-top: 15px;
            transition: all 0.3s;
        }

        .clear-itinerary-btn:hover {
            background: #dc2626;
            transform: translateY(-2px);
        }

        .toggle-tracker-btn {
            position: fixed;
            right: 20px;
            top: 20px;
            background: #ffd700;
            color: #1a2332;
            border: none;
            padding: 12px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
            z-index: 10000;
            box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
            transition: all 0.3s;
        }

        .toggle-tracker-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(255, 215, 0, 0.6);
        }

        .itinerary-tracker.hidden {
            display: none;
        }

        /* Progress Indicator */
        .progress-container {
            position: fixed;
            right: 340px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 1rem;
            z-index: 100;
        }

        .progress-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: rgba(255, 215, 0, 0.5);
            cursor: pointer;
            transition: all 0.3s;
            border: 2px solid #000;
        }

        .progress-dot.active {
            background: #FFD700;
            transform: scale(1.3);
            box-shadow: 0 0 10px rgba(255,215,0,0.8);
        }

        /* Live Hours Styles */
        .live-data-indicator {
            display: inline-block;
            padding: 4px 12px;
            background: #4CAF50;
            color: white;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-left: 10px;
            animation: pulse 2s infinite;
        }

        .live-data-indicator.offline {
            background: #F44336;
        }

        .hours-loading {
            text-align: center;
            padding: 40px;
            color: #94a3b8;
        }

        .live-loading-spinner {
            width: 40px;
            height: 40px;
            border: 4px solid rgba(255, 255, 255, 0.1);
            border-top: 4px solid #FFD700;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px auto;
        }

        .live-hours {
            font-weight: bold;
            color: #FFD700 !important;
        }

        .status-open, .status-closed {
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.85em;
            color: white;
        }

        .status-open { background-color: #2ecc71; }
        .status-closed { background-color: #e74c3c; }

        .update-note {
            font-style: italic;
            color: #94a3b8;
            font-size: 0.9rem;
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes highlight {
            0% { background-color: rgba(255, 215, 0, 0.3); }
            100% { background-color: transparent; }
        }

        /* Navigation to Shopping */
        .nav-to-shopping {
            margin-top: 50px;
            margin-bottom: 50px;
            text-align: center;
            padding: 40px;
            background: rgba(255, 215, 0, 0.1);
            border-radius: 15px;
            border: 2px solid #ffd700;
            width: 100%;
        }

        .nav-to-shopping h2 {
            color: #fbbf24;
            margin-bottom: 20px;
            font-size: 2rem;
        }

        .nav-to-shopping p {
            color: #cbd5e1;
            font-size: 1.2rem;
            margin-bottom: 30px;
        }

        .shopping-btn {
            display: inline-block;
            padding: 20px 50px;
            font-size: 1.3rem;
            font-weight: bold;
            color: #1a1a2e;
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.4);
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .shopping-btn:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 40px rgba(255, 215, 0, 0.6);
        }

        footer {
            background: #0a1a35;
            color: #f0fdfa;
            padding: 3rem 2rem;
            text-align: center;
            border-top: 2px solid #FFD700;
        }

        .copyright {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        @media (max-width: 1024px) {
            .sidebar { width: 200px; }
            .main-content { margin-left: 220px; padding: 20px; }
            .content-grid { grid-template-columns: 1fr; }
            .progress-container { display: none; }
        }

        @media (max-width: 768px) {
            .sidebar { width: 60px; padding: 10px; }
            .sidebar-header h2 { font-size: 0; }
            .sidebar-header h2::after { content: "🗽"; font-size: 1.5rem; color: #FFD700; }
            .sidebar-header p { display: none; }
            .nav-button { padding: 10px; font-size: 0; }
            .nav-button::before { font-size: 1.2rem; }
            .nav-button.breakfast::before { content: "🍳"; }
            .nav-button.landmarks::before { content: "🗽"; }
            .nav-button.shopping::before { content: "🛍️"; }
            .nav-button.broadway::before { content: "🎭"; }
            .main-content { margin-left: 70px; padding: 15px; }
            .interactive-buttons { flex-direction: column; }
            .itinerary-tracker { width: 90%; right: 5%; left: 5%; }
        }
    </style>
</head>
<body>
    <!-- Fixed Left Sidebar - EXACT MATCH FROM BREAKFAST PAGE -->
    <div class="sidebar">
        <div class="sidebar-header">
            <h2>NYC Trip Planner Menu</h2>
            <p>Click a button to move to the next module</p>
        </div>
        <div class="nav-menu">
            <button class="nav-button breakfast" onclick="navigateTo('breakfast')">
                🍳 Breakfast
            </button>
            <button class="nav-button landmarks active" onclick="navigateTo('landmarks')">
                🗽 Landmarks
            </button>
            <button class="nav-button shopping" onclick="navigateTo('shopping')">
                🛍️ Shopping
            </button>
            <button class="nav-button broadway" onclick="navigateTo('broadway')">
                🎭 Broadway
            </button>
        </div>
    </div>

    <!-- Main Content Area -->
    <div class="main-content">
        <button class="toggle-tracker-btn" onclick="toggleItineraryTracker()">
            📋 My Itinerary
        </button>

        <div class="container">
            <div class="header">
                <h1>🗽 NYC Landmarks</h1>
                <p>Explore the iconic sights of the big apple with live hours & interactive games</p>
                <div class="live-data-indicator" id="apiStatus">🔌 Connecting to API...</div>
            </div>

            <!-- Progress Indicator -->
            <div class="progress-container">
                <div class="progress-dot active" data-section="met-section"></div>
                <div class="progress-dot" data-section="icecream-section"></div>
                <div class="progress-dot" data-section="empire-section"></div>
                <div class="progress-dot" data-section="ukrainian-section"></div>
            </div>

            <!-- THE MET - ALL DETAILS + ADD TO ITINERARY BUTTON INSIDE -->
            <section id="met-section" class="section">
                <div class="animation-container">
                    <div class="met-animation">
                        <div class="met-building">
                            <div class="met-roof">THE MET</div>
                            <div class="met-columns">
                                <div class="met-column"></div>
                                <div class="met-column"></div>
                                <div class="met-column"></div>
                                <div class="met-column"></div>
                                <div class="met-column"></div>
                            </div>
                        </div>
                        <div class="art-pieces">
                            <div class="art-piece"></div>
                            <div class="art-piece"></div>
                            <div class="art-piece"></div>
                        </div>
                    </div>
                </div>
                <div class="content-container">
                    <h2 class="section-title">The Metropolitan Museum of Art</h2>
                    <p class="section-subtitle">Upper East Side • Art & Culture</p>
                    
                    <div class="content-grid">
                        <div class="info-card">
                            <h3>Hours & Admission</h3>
                            <ul class="hours-list" id="met-hours">
                                <li><span>Sunday - Thursday</span><span>10:00 AM - 5:30 PM</span></li>
                                <li><span>Friday - Saturday</span><span>10:00 AM - 9:00 PM</span></li>
                                <li><span>General Admission</span><span>$30 (Adults)</span></li>
                                <li><span>Students/Seniors</span><span>$17</span></li>
                            </ul>
                            <button class="btn btn-primary" onclick="updateMuseumHours('met-section')" style="margin-top: 15px; width: 100%;">
                                <span>🔄</span> Update Live Hours
                            </button>
                        </div>
                        <div class="info-card">
                            <h3>Highlights</h3>
                            <ul class="highlight-list">
                                <li>European Paintings Gallery</li>
                                <li>Temple of Dendur</li>
                                <li>American Wing</li>
                                <li>Arms and Armor Collection</li>
                                <li>Costume Institute</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="reviews-container">
                        <h3 style="color: #FFD700; margin-bottom: 1rem;">Visitor Reviews</h3>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">Sarah M.</span>
                                <span class="review-date">March 15, 2023</span>
                            </div>
                            <div class="review-rating">★★★★★</div>
                            <p class="review-text">Absolutely breathtaking! The European paintings collection is world-class. Spent 5 hours and still didn't see everything. Will definitely return.</p>
                        </div>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">James T.</span>
                                <span class="review-date">February 28, 2023</span>
                            </div>
                            <div class="review-rating">★★★★☆</div>
                            <p class="review-text">Incredible museum but very crowded. Go early to avoid lines. The Egyptian wing was my favorite part.</p>
                        </div>
                    </div>
                    
                    <div class="interactive-section">
                        <h3 class="interactive-title">Create Your Masterpiece</h3>
                        <p class="game-instructions">Click on the art samples to create your own gallery arrangement</p>
                        <div class="game-container">
                            <div class="art-game">
                                <div class="art-sample" style="background: linear-gradient(45deg, #FFD700, #FF6347);" onclick="changeArtColor(this)"></div>
                                <div class="art-sample" style="background: linear-gradient(45deg, #4682B4, #87CEEB);" onclick="changeArtColor(this)"></div>
                                <div class="art-sample" style="background: linear-gradient(45deg, #32CD32, #90EE90);" onclick="changeArtColor(this)"></div>
                                <div class="art-sample" style="background: linear-gradient(45deg, #DDA0DD, #EE82EE);" onclick="changeArtColor(this)"></div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="interactive-buttons">
                        <button class="btn btn-success" onclick="saveLandmarkVisit('The Metropolitan Museum of Art')">
                            <span>✅</span> Add to Itinerary
                        </button>
                        <button class="btn btn-primary" onclick="window.open('https://www.metmuseum.org', '_blank')">
                            <span>🌐</span> Visit Website
                        </button>
                    </div>
                </div>
            </section>

            <!-- ICE CREAM MUSEUM - ALL DETAILS + ADD TO ITINERARY BUTTON INSIDE -->
            <section id="icecream-section" class="section">
                <div class="animation-container">
                    <div class="icecream-animation">
                        <div class="icecream-ground"></div>
                        <div class="icecream-building">
                            <div class="icecream-sign">MUSEUM OF ICE CREAM</div>
                            <div class="icecream-facade"></div>
                            <div class="icecream-windows">
                                <div class="icecream-window">
                                    <div class="icecream-pane"></div>
                                    <div class="icecream-pane"></div>
                                </div>
                                <div class="icecream-window">
                                    <div class="icecream-pane"></div>
                                    <div class="icecream-pane"></div>
                                </div>
                            </div>
                            <div class="icecream-door"></div>
                        </div>
                        <div class="floating-cones">
                            <div class="floating-cone">
                                <div class="floating-scoop"></div>
                            </div>
                            <div class="floating-cone">
                                <div class="floating-scoop"></div>
                            </div>
                            <div class="floating-cone">
                                <div class="floating-scoop"></div>
                            </div>
                        </div>
                        <div class="giant-icecream">
                            <div class="giant-scoop"></div>
                            <div class="giant-cherry"></div>
                            <div class="giant-cone"></div>
                        </div>
                    </div>
                </div>
                <div class="content-container">
                    <h2 class="section-title">Museum of Ice Cream</h2>
                    <p class="section-subtitle">Soho • Fun & Interactive</p>
                    
                    <div class="content-grid">
                        <div class="info-card">
                            <h3>Hours & Tickets</h3>
                            <ul class="hours-list" id="icecream-hours">
                                <li><span>Monday - Thursday</span><span>11:00 AM - 7:00 PM</span></li>
                                <li><span>Friday - Sunday</span><span>10:00 AM - 8:00 PM</span></li>
                                <li><span>General Admission</span><span>$39 (All Ages)</span></li>
                                <li><span>Children under 2</span><span>Free</span></li>
                            </ul>
                            <button class="btn btn-primary" onclick="updateMuseumHours('icecream-section')" style="margin-top: 15px; width: 100%;">
                                <span>🔄</span> Update Live Hours
                            </button>
                        </div>
                        <div class="info-card">
                            <h3>Highlights</h3>
                            <ul class="highlight-list">
                                <li>Interactive Sprinkle Pool</li>
                                <li>Ice Cream Tastings</li>
                                <li>Pink Subway Installation</li>
                                <li>Cherry on Top Rooftop</li>
                                <li>Unicorn-themed Rooms</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="reviews-container">
                        <h3 style="color: #FFD700; margin-bottom: 1rem;">Visitor Reviews</h3>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">Jessica L.</span>
                                <span class="review-date">April 2, 2023</span>
                            </div>
                            <div class="review-rating">★★★★★</div>
                            <p class="review-text">So much fun for all ages! The sprinkle pool was a dream come true. The ice cream samples were delicious and creative.</p>
                        </div>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">Michael R.</span>
                                <span class="review-date">March 20, 2023</span>
                            </div>
                            <div class="review-rating">★★★★☆</div>
                            <p class="review-text">Great Instagram spot! Very colorful and playful. A bit pricey for what it is, but the kids loved it.</p>
                        </div>
                    </div>
                    
                    <div class="interactive-section">
                        <h3 class="interactive-title">Virtual Sprinkle Pool</h3>
                        <p class="game-instructions">Click anywhere in the pool to add colorful sprinkles!</p>
                        <div class="game-container">
                            <div class="sprinkle-pool" id="sprinkle-pool"></div>
                        </div>
                    </div>
                    
                    <div class="interactive-buttons">
                        <button class="btn btn-success" onclick="saveLandmarkVisit('Museum of Ice Cream')">
                            <span>✅</span> Add to Itinerary
                        </button>
                        <button class="btn btn-primary" onclick="window.open('https://www.museumoficecream.com', '_blank')">
                            <span>🌐</span> Visit Website
                        </button>
                    </div>
                </div>
            </section>

            <!-- EMPIRE STATE BUILDING - ALL DETAILS + ADD TO ITINERARY BUTTON INSIDE -->
            <section id="empire-section" class="section">
                <div class="animation-container">
                    <div class="empire-animation">
                        <div class="empire-building">
                            <div class="empire-antenna"></div>
                            <div class="antenna-light"></div>
                            <div class="observation-deck"></div>
                        </div>
                        <div class="stars" id="stars-container"></div>
                    </div>
                </div>
                <div class="content-container">
                    <h2 class="section-title">Empire State Building</h2>
                    <p class="section-subtitle">Midtown • Iconic Skyline</p>
                    
                    <div class="content-grid">
                        <div class="info-card">
                            <h3>Hours & Tickets</h3>
                            <ul class="hours-list" id="empire-hours">
                                <li><span>Everyday</span><span>8:00 AM - 2:00 AM</span></li>
                                <li><span>Last Elevator</span><span>1:15 AM</span></li>
                                <li><span>Main Deck (86th)</span><span>$44 (Adults)</span></li>
                                <li><span>Top Deck (102nd)</span><span>+$20</span></li>
                            </ul>
                            <button class="btn btn-primary" onclick="updateMuseumHours('empire-section')" style="margin-top: 15px; width: 100%;">
                                <span>🔄</span> Update Live Hours
                            </button>
                        </div>
                        <div class="info-card">
                            <h3>Highlights</h3>
                            <ul class="highlight-list">
                                <li>86th Floor Observatory</li>
                                <li>102nd Floor Observatory</li>
                                <li>Dare to Dream Exhibit</li>
                                <li>Sustainability Exhibit</li>
                                <li>King Kong Exhibit</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="reviews-container">
                        <h3 style="color: #FFD700; margin-bottom: 1rem;">Visitor Reviews</h3>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">David K.</span>
                                <span class="review-date">May 10, 2023</span>
                            </div>
                            <div class="review-rating">★★★★★</div>
                            <p class="review-text">The view is absolutely spectacular, especially at sunset. The 102nd floor is worth the extra cost for the 360-degree views.</p>
                        </div>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">Amanda P.</span>
                                <span class="review-date">April 28, 2023</span>
                            </div>
                            <div class="review-rating">★★★★☆</div>
                            <p class="review-text">Iconic NYC experience. Lines can be long, so book tickets in advance. The exhibits on the way up are interesting too.</p>
                        </div>
                    </div>
                    
                    <div class="interactive-section">
                        <h3 class="interactive-title">NYC Skyline at Night</h3>
                        <p class="game-instructions">Watch the city lights twinkle in this miniature NYC skyline</p>
                        <div class="game-container">
                            <div class="observation-game" id="observation-game"></div>
                        </div>
                    </div>
                    
                    <div class="interactive-buttons">
                        <button class="btn btn-success" onclick="saveLandmarkVisit('Empire State Building')">
                            <span>✅</span> Add to Itinerary
                        </button>
                        <button class="btn btn-primary" onclick="window.open('https://www.esbnyc.com', '_blank')">
                            <span>🌐</span> Visit Website
                        </button>
                    </div>
                </div>
            </section>

            <!-- UKRAINIAN MUSEUM - ALL DETAILS + ADD TO ITINERARY BUTTON INSIDE -->
            <section id="ukrainian-section" class="section">
                <div class="animation-container">
                    <div class="ukrainian-animation">
                        <div class="flag-pattern"></div>
                        <div class="ukrainian-title">Ukrainian Museum</div>
                        <div class="ukrainian-building">
                            <div class="ukrainian-roof"></div>
                            <div class="ukrainian-windows">
                                <div class="ukrainian-window">
                                    <div class="window-pane"></div>
                                    <div class="window-pane"></div>
                                </div>
                                <div class="ukrainian-window">
                                    <div class="window-pane"></div>
                                    <div class="window-pane"></div>
                                </div>
                            </div>
                            <div class="ukrainian-door">
                                <div class="door-handle"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="content-container">
                    <h2 class="section-title">Ukrainian Museum</h2>
                    <p class="section-subtitle">East Village • Cultural Heritage</p>
                    
                    <div class="content-grid">
                        <div class="info-card">
                            <h3>Hours & Admission</h3>
                            <ul class="hours-list" id="ukrainian-hours">
                                <li><span>Thursday - Sunday</span><span>11:30 AM - 5:00 PM</span></li>
                                <li><span>Monday - Wednesday</span><span>Closed</span></li>
                                <li><span>General Admission</span><span>$12 (Adults)</span></li>
                                <li><span>Students/Seniors</span><span>$8</span></li>
                            </ul>
                            <button class="btn btn-primary" onclick="updateMuseumHours('ukrainian-section')" style="margin-top: 15px; width: 100%;">
                                <span>🔄</span> Update Live Hours
                            </button>
                        </div>
                        <div class="info-card">
                            <h3>Highlights</h3>
                            <ul class="highlight-list">
                                <li>Folk Art Collection</li>
                                <li>Traditional Textiles</li>
                                <li>Fine Arts Exhibitions</li>
                                <li>Historical Artifacts</li>
                                <li>Cultural Events</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="reviews-container">
                        <h3 style="color: #FFD700; margin-bottom: 1rem;">Visitor Reviews</h3>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">Olena S.</span>
                                <span class="review-date">June 5, 2023</span>
                            </div>
                            <div class="review-rating">★★★★★</div>
                            <p class="review-text">Beautiful collection that showcases Ukrainian culture and heritage. The folk art is particularly impressive. A hidden gem in the East Village.</p>
                        </div>
                        <div class="review-card">
                            <div class="review-header">
                                <span class="review-author">Mark T.</span>
                                <span class="review-date">May 22, 2023</span>
                            </div>
                            <div class="review-rating">★★★★☆</div>
                            <p class="review-text">Small but well-curated museum. Learned a lot about Ukrainian history and traditions. The staff was very knowledgeable and friendly.</p>
                        </div>
                    </div>
                    
                    <div class="interactive-section">
                        <h3 class="interactive-title">Create Ukrainian Embroidery</h3>
                        <p class="game-instructions">Click and drag to create traditional Ukrainian embroidery patterns</p>
                        <div class="game-container">
                            <div class="embroidery-game" id="embroidery-game"></div>
                        </div>
                    </div>
                    
                    <div class="interactive-buttons">
                        <button class="btn btn-success" onclick="saveLandmarkVisit('Ukrainian Museum')">
                            <span>✅</span> Add to Itinerary
                        </button>
                        <button class="btn btn-primary" onclick="window.open('https://www.ukrainianmuseum.org', '_blank')">
                            <span>🌐</span> Visit Website
                        </button>
                    </div>
                </div>
            </section>

            <!-- Navigation to Shopping -->
            <div class="nav-to-shopping">
                <h2>Ready to Shop?</h2>
                <p>Time to refresh your wardrobe with some NYC fashion!</p>
                <a href="{{ site.baseurl }}/new-york/shopping/" class="shopping-btn">
                    🛍️ Go Shopping in NYC
                </a>
            </div>

            <footer>
                <div class="copyright">
                    <p>&copy; 2023 NYC Landmarks Experience. All rights reserved.</p>
                </div>
            </footer>
        </div>
    </div>

    <!-- Itinerary Tracker Sidebar -->
    <div class="itinerary-tracker" id="itineraryTracker">
        <h3>🗽 Your NYC Trip</h3>
        <div class="itinerary-item" id="tripInfoItem">
            <div class="itinerary-label">📅 Trip Dates</div>
            <div class="itinerary-value" id="tripDatesValue">
                <span class="itinerary-empty">Not set yet</span>
            </div>
        </div>
        <div class="itinerary-item incomplete" id="breakfastItem">
            <div class="itinerary-label">🍳 Breakfast</div>
            <div class="itinerary-value" id="breakfastValue">
                <span class="itinerary-empty">Not selected</span>
            </div>
        </div>
        <div class="itinerary-item incomplete" id="landmarksItem">
            <div class="itinerary-label">🗽 Landmarks</div>
            <div class="itinerary-value" id="landmarksValue">
                <span class="itinerary-empty">Not selected</span>
            </div>
        </div>
        <div class="itinerary-item incomplete" id="shoppingItem">
            <div class="itinerary-label">🛍️ Shopping</div>
            <div class="itinerary-value" id="shoppingValue">
                <span class="itinerary-empty">Not selected</span>
            </div>
        </div>
        <div class="itinerary-item incomplete" id="broadwayItem">
            <div class="itinerary-label">🎭 Broadway</div>
            <div class="itinerary-value" id="broadwayValue">
                <span class="itinerary-empty">Not selected</span>
            </div>
        </div>
        <button class="clear-itinerary-btn" onclick="clearItinerary()">
            Clear All Selections
        </button>
    </div>

    <script type="module">
        // ============================================
        // SIDEBAR NAVIGATION - EXACT FROM BREAKFAST
        // ============================================
        function navigateTo(section) {
            document.querySelectorAll('.nav-button').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            if (section === 'breakfast') {
                window.location.href = '/Insightful-Innovators-/new-york/breakfast/';
            } else if (section === 'landmarks') {
                console.log('Already on landmarks');
            } else if (section === 'shopping') {
                window.location.href = '/Insightful-Innovators-/new-york/shopping/';
            } else if (section === 'broadway') {
                window.location.href = '/Insightful-Innovators-/new-york/broadway/';
            }
        }

        // ============================================
        // IMPORT CONFIG
        // ============================================
        import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

        // ============================================
        // ITINERARY FUNCTIONS
        // ============================================
        async function getItinerary() {
            try {
                const response = await fetch(`${pythonURI}/api/itinerary`, { ...fetchOptions, method: 'GET', credentials: 'include' });
                if (!response.ok) throw new Error(`API error: ${response.status}`);
                const data = await response.json();
                if (data.success) {
                    const backendData = data.data || {};
                    return {
                        tripInfo: backendData.trip_info || null,
                        breakfast: backendData.breakfast || null,
                        landmarks: backendData.landmarks || null,
                        shopping: backendData.shopping || null,
                        broadway: backendData.broadway || null
                    };
                }
                throw new Error(data.error);
            } catch (error) {
                console.error('Error fetching itinerary:', error);
                const stored = localStorage.getItem('nycItinerary');
                return stored ? JSON.parse(stored) : { tripInfo: null, breakfast: null, landmarks: null, shopping: null, broadway: null };
            }
        }

        async function updateItineraryDisplay(itinerary) {
            // Trip Dates
            if (itinerary.tripInfo) {
                document.getElementById('tripDatesValue').innerHTML = typeof itinerary.tripInfo === 'object' 
                    ? `${itinerary.tripInfo.month || ''} ${itinerary.tripInfo.startDate || ''} - ${itinerary.tripInfo.endDate || ''}`
                    : itinerary.tripInfo;
                document.getElementById('tripInfoItem').classList.remove('incomplete');
            } else {
                document.getElementById('tripDatesValue').innerHTML = '<span class="itinerary-empty">Not set yet</span>';
                document.getElementById('tripInfoItem').classList.add('incomplete');
            }
            // Breakfast
            if (itinerary.breakfast) {
                document.getElementById('breakfastValue').textContent = typeof itinerary.breakfast === 'object' ? itinerary.breakfast.name || 'Breakfast selected' : itinerary.breakfast;
                document.getElementById('breakfastItem').classList.remove('incomplete');
            } else {
                document.getElementById('breakfastValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
                document.getElementById('breakfastItem').classList.add('incomplete');
            }
            // Landmarks
            if (itinerary.landmarks) {
                document.getElementById('landmarksValue').textContent = typeof itinerary.landmarks === 'object' ? itinerary.landmarks.name || 'Landmark selected' : itinerary.landmarks;
                document.getElementById('landmarksItem').classList.remove('incomplete');
            } else {
                document.getElementById('landmarksValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
                document.getElementById('landmarksItem').classList.add('incomplete');
            }
            // Shopping
            if (itinerary.shopping) {
                document.getElementById('shoppingValue').innerHTML = typeof itinerary.shopping === 'object'
                    ? `${itinerary.shopping.center || 'Shopping'}<br><small>${itinerary.shopping.gender || ''}'s Fashion</small>`
                    : itinerary.shopping;
                document.getElementById('shoppingItem').classList.remove('incomplete');
            } else {
                document.getElementById('shoppingValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
                document.getElementById('shoppingItem').classList.add('incomplete');
            }
            // Broadway
            if (itinerary.broadway) {
                document.getElementById('broadwayValue').innerHTML = typeof itinerary.broadway === 'object'
                    ? `${itinerary.broadway.theater || 'Broadway'}<br><small>${itinerary.broadway.show || ''}</small>`
                    : itinerary.broadway;
                document.getElementById('broadwayItem').classList.remove('incomplete');
            } else {
                document.getElementById('broadwayValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
                document.getElementById('broadwayItem').classList.add('incomplete');
            }
        }

        async function initItinerary() {
            try {
                const itinerary = await getItinerary();
                updateItineraryDisplay(itinerary);
            } catch (error) {
                console.error('Failed to initialize itinerary:', error);
                updateItineraryDisplay({ tripInfo: null, breakfast: null, landmarks: null, shopping: null, broadway: null });
            }
        }

        async function saveLandmarkVisit(landmarkName) {
            const landmarkData = {
                name: landmarkName,
                selected_at: new Date().toISOString(),
                type: 'museum'
            };
            const landmarkDetails = {
                'The Metropolitan Museum of Art': { location: 'Upper East Side', hours: '10:00 AM - 5:30 PM', price: '$30 (Adults)' },
                'Museum of Ice Cream': { location: 'Soho', hours: '10:00 AM - 8:00 PM', price: '$39 (All Ages)' },
                'Empire State Building': { location: 'Midtown', hours: '8:00 AM - 2:00 AM', price: '$44 (Adults)' },
                'Ukrainian Museum': { location: 'East Village', hours: '11:30 AM - 5:00 PM', price: '$12 (Adults)' }
            };
            if (landmarkDetails[landmarkName]) Object.assign(landmarkData, landmarkDetails[landmarkName]);

            try {
                const requestOptions = { ...fetchOptions, method: 'POST', headers: { 'Content-Type': 'application/json' }, credentials: 'include', body: JSON.stringify(landmarkData) };
                const response = await fetch(`${pythonURI}/api/itinerary/section/landmarks`, requestOptions);
                if (!response.ok) throw new Error(`API error: ${response.status}`);
                const data = await response.json();
                if (data.success) {
                    const itinerary = await getItinerary();
                    updateItineraryDisplay(itinerary);
                    // Visual feedback on button
                    const buttons = document.querySelectorAll('.btn-success');
                    buttons.forEach(btn => {
                        if (btn.textContent.includes(landmarkName)) {
                            const originalHTML = btn.innerHTML;
                            btn.innerHTML = '<span>✓</span> Added to Itinerary';
                            btn.disabled = true;
                            setTimeout(() => {
                                btn.innerHTML = originalHTML;
                                btn.disabled = false;
                            }, 2000);
                        }
                    });
                }
            } catch (error) {
                console.error('Failed to save landmark:', error);
                alert('Failed to save selection. Please try again.');
            }
        }

        async function clearItinerary() {
            if (confirm('Are you sure you want to clear your entire itinerary?')) {
                try {
                    const response = await fetch(`${pythonURI}/api/itinerary/clear`, { ...fetchOptions, method: 'DELETE', credentials: 'include' });
                    if (!response.ok) throw new Error(`API error: ${response.status}`);
                    const data = await response.json();
                    if (data.success) {
                        localStorage.removeItem('nycItinerary');
                        location.reload();
                    }
                } catch (error) {
                    console.error('Error clearing itinerary:', error);
                    localStorage.removeItem('nycItinerary');
                    location.reload();
                }
            }
        }

        function toggleItineraryTracker() {
            document.getElementById('itineraryTracker').classList.toggle('hidden');
        }

        // ============================================
        // LIVE HOURS FUNCTIONS
        // ============================================
        async function getSelectedDays() {
            try {
                const itinerary = await getItinerary();
                if (!itinerary.tripInfo?.startDate || !itinerary.tripInfo?.endDate) return null;
                const month = itinerary.tripInfo.month;
                const currentYear = new Date().getFullYear();
                const startDay = parseInt(itinerary.tripInfo.startDate.match(/\d+/)[0]);
                const endDay = parseInt(itinerary.tripInfo.endDate.match(/\d+/)[0]);
                const startDate = new Date(`${month} ${startDay}, ${currentYear}`);
                const endDate = new Date(`${month} ${endDay}, ${currentYear}`);
                const selectedDays = new Set();
                const currentDate = new Date(startDate);
                while (currentDate <= endDate) {
                    selectedDays.add(currentDate.toLocaleDateString('en-US', { weekday: 'long' }));
                    currentDate.setDate(currentDate.getDate() + 1);
                }
                return Array.from(selectedDays);
            } catch (error) {
                console.error('Error getting selected days:', error);
                return null;
            }
        }

        async function fetchMuseumHours(museumName) {
            const apiMap = { 'met': `${pythonURI}/api/met`, 'icecream': `${pythonURI}/api/icecream`, 'ukrainian': `${pythonURI}/api/ukrainian`, 'empire': `${pythonURI}/api/empire` };
            try {
                const response = await fetch(apiMap[museumName], { ...fetchOptions, method: 'GET' });
                const data = await response.json();
                return data.data;
            } catch (error) {
                console.error(`Error fetching ${museumName} hours:`, error);
                return null;
            }
        }

        async function updateMuseumHours(museumId) {
            const museumName = museumId.replace('-section', '');
            const hoursList = document.querySelector(`#${museumId} .hours-list`);
            if (!hoursList) return;
            const originalContent = hoursList.innerHTML;
            hoursList.innerHTML = `<li class="hours-loading"><div class="live-loading-spinner"></div><div>Fetching live hours...</div></li>`;
            try {
                const museumData = await fetchMuseumHours(museumName);
                if (museumData) {
                    const selectedDays = await getSelectedDays();
                    let hoursHtml = '';
                    if (selectedDays?.length > 0) {
                        hoursHtml += `<li style="background: rgba(255, 215, 0, 0.1); border-radius: 4px; padding: 8px; margin-bottom: 10px;"><span style="color: #FFD700; font-size: 0.9em;">📅 Showing hours for: ${selectedDays.join(', ')}</span></li>`;
                    }
                    if (museumData.hours && typeof museumData.hours === 'object') {
                        const dayOrder = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
                        const daysToDisplay = selectedDays?.length ? dayOrder.filter(day => selectedDays.includes(day)) : dayOrder;
                        daysToDisplay.forEach(day => {
                            if (museumData.hours[day]) hoursHtml += `<li><span>${day}</span><span class="live-hours">${museumData.hours[day]}</span></li>`;
                        });
                    }
                    if (museumData.status) {
                        const statusClass = museumData.status.toLowerCase().includes('open') ? 'status-open' : 'status-closed';
                        hoursHtml += `<li><span>Status</span><span class="${statusClass}">${museumData.status.toUpperCase()}</span></li>`;
                    }
                    hoursHtml += `<li class="update-note"><span>Last Updated</span><span>${museumData.last_updated || new Date().toLocaleTimeString()}</span></li>`;
                    hoursList.innerHTML = hoursHtml;
                    hoursList.style.animation = "highlight 2s ease";
                    setTimeout(() => hoursList.style.animation = "", 2000);
                } else {
                    hoursList.innerHTML = originalContent;
                }
            } catch (error) {
                console.error('Error updating hours:', error);
                hoursList.innerHTML = originalContent;
            }
        }

        async function testAPIConnection() {
            try {
                const response = await fetch(`${pythonURI}/api/test`, { ...fetchOptions, method: 'GET' });
                const data = await response.json();
                const statusIndicator = document.getElementById('apiStatus');
                if (data.success) {
                    statusIndicator.textContent = '✅ API Connected';
                    statusIndicator.className = 'live-data-indicator';
                } else {
                    statusIndicator.textContent = '⚠️ API Error';
                    statusIndicator.className = 'live-data-indicator offline';
                }
            } catch (error) {
                document.getElementById('apiStatus').textContent = '❌ API Offline';
                document.getElementById('apiStatus').className = 'live-data-indicator offline';
            }
        }

        // ============================================
        // ANIMATIONS & INTERACTIVE GAMES
        // ============================================
        function changeArtColor(element) {
            const colors = [
                'linear-gradient(45deg, #FFD700, #FF6347)',
                'linear-gradient(45deg, #4682B4, #87CEEB)',
                'linear-gradient(45deg, #32CD32, #90EE90)',
                'linear-gradient(45deg, #DDA0DD, #EE82EE)',
                'linear-gradient(45deg, #FFA500, #FF4500)',
                'linear-gradient(45deg, #40E0D0, #00CED1)'
            ];
            element.style.background = colors[Math.floor(Math.random() * colors.length)];
        }

        function initSprinklePool() {
            const pool = document.getElementById('sprinkle-pool');
            if (!pool) return;
            pool.addEventListener('click', function(e) {
                const colors = ['#FF69B4', '#FFD700', '#00CED1', '#98FB98', '#DDA0DD', '#FF6347', '#87CEEB', '#FFA500'];
                const sprinkle = document.createElement('div');
                sprinkle.className = 'sprinkle-game';
                sprinkle.style.background = colors[Math.floor(Math.random() * colors.length)];
                sprinkle.style.left = e.offsetX + 'px';
                sprinkle.style.top = e.offsetY + 'px';
                pool.appendChild(sprinkle);
                setTimeout(() => sprinkle.remove(), 3000);
            });
        }

        function initEmbroideryGame() {
            const canvas = document.getElementById('embroidery-game');
            if (!canvas) return;
            let isDrawing = false, lastX, lastY;
            canvas.addEventListener('mousedown', (e) => { isDrawing = true; [lastX, lastY] = [e.offsetX, e.offsetY]; });
            canvas.addEventListener('mousemove', (e) => {
                if (!isDrawing) return;
                const line = document.createElement('div');
                line.className = 'embroidery-line';
                const x1 = lastX, y1 = lastY, x2 = e.offsetX, y2 = e.offsetY;
                const length = Math.sqrt((x2-x1)**2 + (y2-y1)**2);
                const angle = Math.atan2(y2-y1, x2-x1) * 180 / Math.PI;
                line.style.width = `${length}px`;
                line.style.height = '3px';
                line.style.left = `${x1}px`;
                line.style.top = `${y1}px`;
                line.style.transform = `rotate(${angle}deg)`;
                line.style.background = ['#0057B7', '#FFD700'][Math.floor(Math.random() * 2)];
                canvas.appendChild(line);
                [lastX, lastY] = [x2, y2];
            });
            canvas.addEventListener('mouseup', () => isDrawing = false);
            canvas.addEventListener('mouseleave', () => isDrawing = false);
        }

        function createStars() {
            const container = document.getElementById('stars-container');
            if (!container) return;
            for (let i = 0; i < 80; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.animationDelay = Math.random() * 3 + 's';
                container.appendChild(star);
            }
        }

        function createBuildingSections() {
            const building = document.querySelector('.empire-building');
            if (!building) return;
            for (let i = 0; i < 12; i++) {
                const section = document.createElement('div');
                section.className = 'building-section';
                section.style.bottom = (i * 25) + 'px';
                building.appendChild(section);
            }
        }

        function createSprinkles() {
            const anim = document.getElementById('icecream-animation');
            if (!anim) return;
            const colors = ['#FF69B4', '#FFD700', '#00CED1', '#98FB98', '#DDA0DD', '#FF6347', '#87CEEB', '#FFA500'];
            for (let i = 0; i < 40; i++) {
                const sprinkle = document.createElement('div');
                sprinkle.className = 'sprinkle';
                sprinkle.style.left = Math.random() * 100 + '%';
                sprinkle.style.top = (Math.random() * -30) + '%';
                sprinkle.style.background = colors[Math.floor(Math.random() * colors.length)];
                sprinkle.style.animationDelay = Math.random() * 5 + 's';
                sprinkle.style.animationDuration = (Math.random() * 3 + 3) + 's';
                anim.appendChild(sprinkle);
            }
        }

        function createBuildingLights() {
            const game = document.getElementById('observation-game');
            if (!game) return;
            const skyline = document.createElement('div');
            skyline.className = 'nyc-skyline';
            game.appendChild(skyline);
            for (let i = 0; i < 15; i++) {
                const b = document.createElement('div');
                b.className = 'building';
                b.style.left = (i * 25) + 'px';
                b.style.height = (30 + Math.random() * 70) + 'px';
                skyline.appendChild(b);
                for (let j = 0; j < Math.floor(Math.random() * 5) + 3; j++) {
                    const light = document.createElement('div');
                    light.className = 'light';
                    light.style.left = (Math.random() * 18) + 'px';
                    light.style.top = (10 + Math.random() * (parseInt(b.style.height) - 20)) + 'px';
                    b.appendChild(light);
                }
            }
        }

        function initProgressIndicator() {
            const sections = document.querySelectorAll('.section');
            const dots = document.querySelectorAll('.progress-dot');
            function update() {
                let current = '';
                sections.forEach(s => {
                    if (window.pageYOffset >= s.offsetTop - window.innerHeight / 2) current = s.id;
                });
                dots.forEach(d => {
                    d.classList.remove('active');
                    if (d.dataset.section === current) d.classList.add('active');
                });
            }
            window.addEventListener('scroll', update);
            update();
            dots.forEach(d => d.addEventListener('click', () => {
                document.getElementById(d.dataset.section).scrollIntoView({ behavior: 'smooth' });
            }));
        }

        // ============================================
        // INITIALIZE
        // ============================================
        document.addEventListener('DOMContentLoaded', async () => {
            await initItinerary();
            createStars();
            createBuildingSections();
            createSprinkles();
            createBuildingLights();
            initSprinklePool();
            initEmbroideryGame();
            initProgressIndicator();
            await testAPIConnection();
        });

        // Expose globals
        window.navigateTo = navigateTo;
        window.toggleItineraryTracker = toggleItineraryTracker;
        window.clearItinerary = clearItinerary;
        window.saveLandmarkVisit = saveLandmarkVisit;
        window.updateMuseumHours = updateMuseumHours;
        window.changeArtColor = changeArtColor;
    </script>
</body>
</html>