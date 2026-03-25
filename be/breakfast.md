---
layout: post
title: "Step 1 Breakfast"
description: "Breakfast time hits, and in NYC that means one thing: pick your spot and dive in."
permalink: /new-york/breakfast/
parent: "Analytics/Admin"
team: "Insightful Innovators"
submodule: 1
author: "Insightful Innovators"
date: 2025-11-20
microblog: true
footer:
 previous: /new-york/landmarks/
 home: /nyc/home/
 next: /new-york/shopping/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NYC Breakfast Explorer</title>
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

        /* Fixed Sidebar - LANDMARK THEMED */
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

        /* Main Content Area */
        .main-content {
            margin-left: 280px;
            margin-right: 0;
            padding: 30px 60px 30px 20px;
            min-height: 100vh;
            max-width: 1100px;
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
            border: 2px solid #f59e0b;
        }

        .header h1 {
            font-size: 48px;
            margin: 0 0 10px 0;
            color: #fbbf24;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .header p {
            font-size: 1.2rem;
            color: #cbd5e1;
        }

        .trip-dates-banner {
            background: rgba(255, 215, 0, 0.15);
            border: 2px solid #ffd700;
            border-radius: 10px;
            padding: 15px 25px;
            margin: 20px 0 30px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 15px;
        }

        .trip-dates-banner .label {
            color: #ffd700;
            font-weight: bold;
            font-size: 1.1rem;
        }

        .trip-dates-banner .dates {
            color: white;
            font-size: 1.2rem;
            background: rgba(0, 0, 0, 0.3);
            padding: 8px 16px;
            border-radius: 8px;
        }

        .trip-dates-banner .days {
            color: #10b981;
            font-size: 1rem;
            background: rgba(16, 185, 129, 0.1);
            padding: 8px 16px;
            border-radius: 8px;
        }

        .live-hours-container {
            margin: 30px 0;
            padding: 25px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            border-left: 5px solid #10b981;
        }

        .live-hours-container h2 {
            color: #10b981;
            margin-bottom: 20px;
            font-size: 1.8rem;
        }

        /* Restaurant Cards Section */
        .restaurant-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid transparent;
            transition: all 0.3s;
            width: 100%;
        }

        .restaurant-card:hover {
            transform: translateY(-5px);
            border-color: #f59e0b;
            box-shadow: 0 10px 30px rgba(245, 158, 11, 0.3);
        }

        .restaurant-card h3 {
            margin: 0 0 15px 0;
            font-size: 28px;
            color: #f59e0b;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .restaurant-card .badge {
            display: inline-block;
            padding: 5px 15px;
            background: rgba(245, 158, 11, 0.2);
            border-radius: 20px;
            font-size: 12px;
            margin: 10px 0;
        }

        .restaurant-card p {
            line-height: 1.6;
            color: #cbd5e1;
            margin: 10px 0;
            font-size: 1.05rem;
        }

        .hours-display {
            background: rgba(0, 0, 0, 0.2);
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }

        .day-hour {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .day-hour:last-child {
            border-bottom: none;
        }

        .day-hour .day {
            font-weight: bold;
            color: #fbbf24;
        }

        .day-hour .time {
            color: #10b981;
            font-weight: bold;
        }

        .day-hour.filtered-highlight {
            background: rgba(255, 215, 0, 0.1);
            border-radius: 6px;
            padding: 10px;
            margin: 5px 0;
            border-left: 4px solid #ffd700;
        }

        /* Location Grid */
        .location-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 25px;
            margin: 30px 0;
            width: 100%;
        }

        .step h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #fbbf24;
            font-size: 2rem;
            max-width: 100%;
        }

        .location-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            transition: all 0.3s;
            border: 2px solid transparent;
            position: relative;
            width: 100%;
            min-height: 280px;
        }

        .location-card:hover {
            transform: translateY(-5px);
            border-color: #f59e0b;
            box-shadow: 0 10px 30px rgba(245, 158, 11, 0.3);
        }

        .location-card h3 {
            margin: 0 0 10px 0;
            font-size: 26px;
            color: #f59e0b;
        }

        .location-card p {
            margin: 8px 0;
            font-size: 1.05rem;
            line-height: 1.5;
        }

        .restaurant-cuisine {
            background: rgba(139, 92, 246, 0.2);
            color: #c4b5fd;
            padding: 8px 15px;
            border-radius: 12px;
            font-size: 0.9rem;
            display: inline-block;
            margin: 10px 0;
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin: 20px 0;
        }

        .menu-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 20px;
            transition: transform 0.3s;
        }

        .menu-item:hover {
            transform: scale(1.02);
        }

        .menu-item h4 {
            margin: 0 0 5px 0;
            color: #fbbf24;
            font-size: 1.2rem;
        }

        .menu-item .price {
            color: #10b981;
            font-weight: bold;
            font-size: 20px;
            margin: 5px 0;
        }

        .menu-item p {
            color: #94a3b8;
            font-size: 14px;
            margin: 10px 0;
        }

        .btn {
            background: linear-gradient(90deg, #f59e0b, #f97316);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(245, 158, 11, 0.4);
        }

        .btn-primary {
            background: linear-gradient(90deg, #10b981, #059669);
            width: 100%;
            margin-top: 20px;
            justify-content: center;
        }

        .refresh-btn {
            background: linear-gradient(90deg, #8b5cf6, #7c3aed);
            margin-top: 10px;
        }

        .step {
            display: none;
        }

        .step.active {
            display: block;
        }

        .back-btn {
            background: transparent;
            border: 1px solid #64748b;
            color: #94a3b8;
            margin-bottom: 20px;
        }

        .back-btn:hover {
            border-color: white;
            color: white;
        }

        .order-section {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
        }

        .order-item {
            background: rgba(0, 0, 0, 0.3);
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .custom-input {
            width: 100%;
            padding: 12px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid #475569;
            border-radius: 8px;
            color: white;
            font-size: 16px;
            margin: 10px 0;
        }

        .custom-input:focus {
            outline: none;
            border-color: #a855f7;
        }

        .remove-btn {
            background: #ef4444;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
        }

        .total {
            font-size: 28px;
            text-align: right;
            margin: 20px 0;
            color: #fbbf24;
        }

        .restaurant-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .restaurant-location {
            color: #f59e0b;
            font-weight: bold;
        }

        .location-card-footer {
            margin-top: 25px;
            display: flex;
            gap: 15px;
        }

        .view-menu-btn {
            flex: 1;
            background: linear-gradient(90deg, #f59e0b, #f97316);
            color: white;
            border: none;
            padding: 14px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 1rem;
        }

        .view-menu-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(245, 158, 11, 0.4);
        }

        .quick-add-btn {
            background: linear-gradient(90deg, #ffd700, #ffed4e);
            color: #1a1a2e;
            border: none;
            padding: 14px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 1rem;
        }

        .quick-add-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(255, 215, 0, 0.5);
        }

        .quick-add-btn.added {
            background: linear-gradient(90deg, #10b981, #059669);
            color: white;
        }

        .nav-to-landmarks {
            margin-top: 50px;
            margin-bottom: 50px;
            text-align: center;
            padding: 40px;
            background: rgba(255, 215, 0, 0.1);
            border-radius: 15px;
            border: 2px solid #ffd700;
            width: 100%;
        }

        .nav-to-landmarks h2 {
            color: #fbbf24;
            margin-bottom: 20px;
            font-size: 2rem;
        }

        .nav-to-landmarks p {
            color: #cbd5e1;
            font-size: 1.2rem;
            margin-bottom: 30px;
        }

        .landmarks-btn {
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

        .landmarks-btn:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 40px rgba(255, 215, 0, 0.6);
            background: linear-gradient(135deg, #ffed4e 0%, #ffd700 100%);
        }

        /* Itinerary Tracker Sidebar */
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
            backdrop-filter: blur(10px);
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
            transition: all 0.3s ease;
        }

        .itinerary-item:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: translateX(-5px);
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

        .add-to-itinerary-btn {
            background: linear-gradient(90deg, #ffd700, #ffed4e);
            color: #1a1a2e;
            margin-top: 15px;
            font-weight: bold;
            width: 100%;
            justify-content: center;
        }

        .add-to-itinerary-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(255, 215, 0, 0.5);
        }

        .add-to-itinerary-btn.added {
            background: linear-gradient(90deg, #10b981, #059669);
            color: white;
        }

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

        .live-data-indicator.updating {
            background: #FF9800;
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
            border-top: 4px solid #f59e0b;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px auto;
        }

        .hours-header {
            margin: 30px 0 20px 0;
            color: #fbbf24;
            font-size: 1.8rem;
            border-bottom: 2px solid #f59e0b;
            padding-bottom: 10px;
        }

        .no-dates-warning {
            background: rgba(239, 68, 68, 0.2);
            border: 2px solid #ef4444;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            text-align: center;
        }

        .no-dates-warning p {
            color: #ef4444;
            font-size: 1.2rem;
            margin-bottom: 15px;
        }

        .no-dates-warning .btn {
            background: linear-gradient(90deg, #ef4444, #dc2626);
            display: inline-block;
            width: auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }

        .update-note {
            font-style: italic;
            color: #94a3b8;
            font-size: 0.9rem;
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        @media (max-width: 1400px) {
            .main-content {
                margin-right: 0;
                max-width: 900px;
            }
            
            .itinerary-tracker {
                width: 280px;
            }
        }

        @media (max-width: 1024px) {
            .sidebar {
                width: 200px;
            }
            
            .main-content {
                margin-left: 220px;
                margin-right: 0;
                padding: 20px;
                max-width: 800px;
            }
            
            .location-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
            }
            
            .itinerary-tracker {
                display: none;
            }
            
            .itinerary-tracker.hidden {
                display: none;
            }
        }

        @media (max-width: 900px) {
            .location-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .sidebar {
                width: 60px;
                padding: 10px;
            }
            
            .sidebar-header h2 {
                font-size: 0;
            }
            
            .sidebar-header h2::after {
                content: "🗽";
                font-size: 1.5rem;
                color: #FFD700;
            }
            
            .sidebar-header p {
                display: none;
            }
            
            .nav-button {
                padding: 10px;
                font-size: 0;
                justify-content: center;
                text-align: center;
            }
            
            .nav-button::before {
                font-size: 1.2rem;
            }
            
            .nav-button.breakfast::before {
                content: "🍳";
            }
            
            .nav-button.landmarks::before {
                content: "🗽";
            }
            
            .nav-button.shopping::before {
                content: "🛍️";
            }
            
            .nav-button.broadway::before {
                content: "🎭";
            }
            
            .main-content {
                margin-left: 70px;
                margin-right: 10px;
                padding: 15px;
                max-width: 100%;
            }
            
            .location-grid,
            .menu-grid {
                grid-template-columns: 1fr;
                gap: 15px;
            }
            
            .header h1 {
                font-size: 36px;
            }
            
            .restaurant-card h3 {
                font-size: 24px;
            }
            
            .landmarks-btn {
                padding: 15px 35px;
                font-size: 1.1rem;
            }

            .itinerary-tracker {
                width: 90%;
                right: 5%;
                left: 5%;
            }
            
            .location-card {
                padding: 20px;
            }
            
            .location-card h3 {
                font-size: 22px;
            }
        }

        @media (max-width: 480px) {
            .main-content {
                padding: 10px;
            }
            
            .header {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 28px;
            }
            
            .location-card {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
<!-- Fixed Left Sidebar -->
<div class="sidebar">
    <div class="sidebar-header">
        <h2>NYC Trip Planner Menu</h2>
        <p>Click a button to move to the next module</p>
    </div>
    <div class="nav-menu">
        <button class="nav-button breakfast active" onclick="navigateTo('breakfast')">
            🍳 Breakfast
        </button>
        <button class="nav-button landmarks" onclick="navigateTo('landmarks')">
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

<!-- Main Content -->
<div class="main-content">
    <button class="toggle-tracker-btn" onclick="toggleItineraryTracker()">
        📋 My Itinerary
    </button>

    <div class="container">

        <!-- Restaurant Selection Grid -->
        <div id="step1" class="step active">
            <h2>Choose Your Breakfast Spot</h2>
            <div class="location-grid">
                <div class="location-card">
                    <h3>Sarabeth's</h3>
                    <div class="badge">Elegant & Classic</div>
                    <p>📍 Upper West Side</p>
                    <p>A beloved NYC institution known for its legendary homemade jams and elegant brunch classics. Perfect for a refined, upscale breakfast experience.</p>
                    <div class="restaurant-cuisine">Breakfast & Pastries</div>
                    <div class="location-card-footer">
                        <button class="view-menu-btn" onclick="selectRestaurant('sarabeths')">
                            <span>📖</span> View Menu
                        </button>
                        <button class="quick-add-btn" onclick="quickAddToItinerary('sarabeths', event)" data-restaurant="sarabeths">
                            <span>⭐</span> Add
                        </button>
                    </div>
                </div>
                <div class="location-card">
                    <h3>Jack's Wife Frida</h3>
                    <div class="badge">Bold & Trendy</div>
                    <p>📍 SoHo</p>
                    <p>Mediterranean-inspired breakfast with bold Mexican flavors. A trendy spot with colorful dishes and creative twists on morning favorites.</p>
                    <div class="restaurant-cuisine">Mediterranean</div>
                    <div class="location-card-footer">
                        <button class="view-menu-btn" onclick="selectRestaurant('jacks')">
                            <span>📖</span> View Menu
                        </button>
                        <button class="quick-add-btn" onclick="quickAddToItinerary('jacks', event)" data-restaurant="jacks">
                            <span>⭐</span> Add
                        </button>
                    </div>
                </div>
                <div class="location-card">
                    <h3>Ess a Bagel</h3>
                    <div class="badge">Authentic & Iconic</div>
                    <p>📍 Midtown East</p>
                    <p>The ultimate NYC bagel experience. Hand-rolled, kettle-boiled bagels that are crispy outside and pillowy inside. A true New York classic.</p>
                    <div class="restaurant-cuisine">Bagels & Deli</div>
                    <div class="location-card-footer">
                        <button class="view-menu-btn" onclick="selectRestaurant('ess')">
                            <span>📖</span> View Menu
                        </button>
                        <button class="quick-add-btn" onclick="quickAddToItinerary('ess', event)" data-restaurant="ess">
                            <span>⭐</span> Add
                        </button>
                    </div>
                </div>
                <div class="location-card">
                    <h3>Shuka</h3>
                    <div class="badge">Fresh & Vibrant</div>
                    <p>📍 East Village</p>
                    <p>Modern Mediterranean cuisine with Israeli breakfast specialties. Fresh, vibrant dishes featuring tahini, hummus, and perfectly spiced shakshuka.</p>
                    <div class="restaurant-cuisine">Mediterranean</div>
                    <div class="location-card-footer">
                        <button class="view-menu-btn" onclick="selectRestaurant('shuka')">
                            <span>📖</span> View Menu
                        </button>
                        <button class="quick-add-btn" onclick="quickAddToItinerary('shuka', event)" data-restaurant="shuka">
                            <span>⭐</span> Add
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Restaurant Details & Menu -->
        <div class="step" id="step2">
            <button class="btn back-btn" onclick="goToStep(1)">
                <span>←</span> Back to Restaurants
            </button>
            <div class="restaurant-card" id="restaurantDetails">
                <div class="restaurant-info">
                    <h3 id="restaurantName">Loading...</h3>
                    <div class="restaurant-location" id="restaurantLocation"></div>
                </div>
                <p id="restaurantDescription"></p>
        
                <!-- Hours section moved here (AFTER restaurant selection) -->
                <div id="hoursSection">
                    <h2 class="hours-header">🕒 Live Restaurant Hours</h2>
                    <div id="restaurantHours">
                        <div class="hours-loading">
                            <div class="live-loading-spinner"></div>
                            <div>Fetching live hours...</div>
                        </div>
                    </div>
                    <button class="btn refresh-btn" onclick="refreshCurrentRestaurant()">
                        <span>🔄</span> Update Live Hours
                    </button>
                </div>
            </div>
            <h3 style="margin: 30px 0 20px 0; color: #fbbf24; font-size: 1.8rem;">Menu Highlights</h3>
            <div class="menu-grid" id="menuGrid"></div>
            <button class="btn add-to-itinerary-btn" id="addToItineraryBtn" onclick="addBreakfastToItinerary()">
                <span>⭐</span> Add to My Itinerary
            </button>

            <button class="btn btn-primary" onclick="goToStep(3)">
                <span>📝</span> Continue to Order
                <span>→</span>
            </button>
        </div>

        <!-- Order Section -->
        <div class="step" id="step3">
            <button class="btn back-btn" onclick="goToStep(2)">
                <span>←</span> Back to Menu
            </button>
            <div class="order-section">
                <h2 style="color: #fbbf24; margin-bottom: 20px;">Your Order</h2>
                <div id="orderList"></div>
        
                <h3 style="margin-top: 30px; color: #fbbf24;">Add Custom Item</h3>
                <input type="text" class="custom-input" id="customInput" placeholder="E.g., Gluten-free waffle with almond butter">
                <button class="btn" onclick="addCustom()">
                    <span>➕</span> Add Custom Item
                </button>
            </div>
            <button class="btn btn-primary" onclick="goToStep(4)">
                <span>✅</span> Review Order
                <span>→</span>
            </button>
        </div>

        <!-- Order Confirmation -->
        <div class="step" id="step4">
            <div class="order-section">
                <h2 style="color: #fbbf24; margin-bottom: 20px;">Order Confirmation</h2>
                <div id="reviewHeader"></div>
                <div id="reviewList"></div>
                <div class="total" id="totalPrice">Total: $0</div>
        
                <button class="btn back-btn" onclick="goToStep(3)">
                    <span>←</span> Edit Order
                </button>
                <button class="btn btn-primary" onclick="confirmOrder()">
                    <span>📦</span> Confirm Order
                </button>
            </div>
        </div>

        <!-- Navigation to Landmarks Page -->
        <div class="nav-to-landmarks">
            <h2>Ready for the Next Adventure?</h2>
            <p>With a full stomach, let's move on to picking your ideal attraction to sight see!</p>
            <a href="/Insightful-Innovators-/new-york/landmarks/" class="landmarks-btn">
                🗽 Explore NYC Landmarks
            </a>
        </div>
    </div>
</div>

<!-- Itinerary Tracker -->
<div class="itinerary-tracker hidden" id="itineraryTracker">
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

<script>
    // ============================================
    // SIDEBAR NAVIGATION
    // ============================================
    
    function navigateTo(section) {
        if (section === 'breakfast') {
            // Already on breakfast page
            console.log('Navigating to breakfast section');
        } else if (section === 'landmarks') {
            window.location.href = '/Insightful-Innovators-/new-york/landmarks/';
        } else if (section === 'shopping') {
            window.location.href = '/Insightful-Innovators-/new-york/shopping/';
        } else if (section === 'broadway') {
            window.location.href = '/Insightful-Innovators-/new-york/broadway/';
        }
    }

    // ============================================
    // LOCAL STORAGE FUNCTIONS (FIXED)
    // ============================================

    function getItineraryFromStorage() {
        const stored = localStorage.getItem('nycItinerary');
        return stored ? JSON.parse(stored) : {
            tripInfo: null,
            breakfast: null,
            landmarks: null,
            shopping: null,
            broadway: null
        };
    }

    function saveItineraryToStorage(itinerary) {
        localStorage.setItem('nycItinerary', JSON.stringify(itinerary));
        updateItineraryDisplay(itinerary);
    }

    function updateItineraryDisplay(itinerary) {
        // Update trip info
        if (itinerary.tripInfo) {
            document.getElementById('tripDatesValue').innerHTML = 
                `${itinerary.tripInfo.month || ''} ${itinerary.tripInfo.startDate || ''} - ${itinerary.tripInfo.endDate || ''}`;
            document.getElementById('tripInfoItem').classList.remove('incomplete');
        } else {
            document.getElementById('tripDatesValue').innerHTML = '<span class="itinerary-empty">Not set yet</span>';
            document.getElementById('tripInfoItem').classList.add('incomplete');
        }
        
        // Update breakfast
        if (itinerary.breakfast) {
            if (typeof itinerary.breakfast === 'object') {
                document.getElementById('breakfastValue').innerHTML = itinerary.breakfast.name || 'Breakfast selected';
            } else {
                document.getElementById('breakfastValue').innerHTML = itinerary.breakfast;
            }
            document.getElementById('breakfastItem').classList.remove('incomplete');
        } else {
            document.getElementById('breakfastValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
            document.getElementById('breakfastItem').classList.add('incomplete');
        }
        
        // Update landmarks
        if (itinerary.landmarks) {
            if (typeof itinerary.landmarks === 'object') {
                document.getElementById('landmarksValue').innerHTML = itinerary.landmarks.name || 'Landmark selected';
            } else {
                document.getElementById('landmarksValue').innerHTML = itinerary.landmarks;
            }
            document.getElementById('landmarksItem').classList.remove('incomplete');
        } else {
            document.getElementById('landmarksValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
            document.getElementById('landmarksItem').classList.add('incomplete');
        }
        
        // Update shopping
        if (itinerary.shopping) {
            if (typeof itinerary.shopping === 'object') {
                document.getElementById('shoppingValue').innerHTML = 
                    `${itinerary.shopping.center || 'Shopping'}<br><small>${itinerary.shopping.gender || ''}'s Fashion</small>`;
            } else {
                document.getElementById('shoppingValue').innerHTML = itinerary.shopping;
            }
            document.getElementById('shoppingItem').classList.remove('incomplete');
        } else {
            document.getElementById('shoppingValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
            document.getElementById('shoppingItem').classList.add('incomplete');
        }
        
        // Update broadway
        if (itinerary.broadway) {
            if (typeof itinerary.broadway === 'object') {
                document.getElementById('broadwayValue').innerHTML = 
                    `${itinerary.broadway.theater || 'Broadway'}<br><small>${itinerary.broadway.show || ''}</small>`;
            } else {
                document.getElementById('broadwayValue').innerHTML = itinerary.broadway;
            }
            document.getElementById('broadwayItem').classList.remove('incomplete');
        } else {
            document.getElementById('broadwayValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
            document.getElementById('broadwayItem').classList.add('incomplete');
        }
    }

    function clearItinerary() {
        if (confirm('Are you sure you want to clear your entire itinerary?')) {
            localStorage.removeItem('nycItinerary');
            location.reload();
        }
    }

    function toggleItineraryTracker() {
        const tracker = document.getElementById('itineraryTracker');
        tracker.classList.toggle('hidden');
    }

    function updateBreakfastInItinerary(restaurantData) {
        const itinerary = getItineraryFromStorage();
        itinerary.breakfast = restaurantData;
        saveItineraryToStorage(itinerary);
        updateQuickAddButtons();
    }

    // ============================================
    // DATE FILTERING FUNCTIONS (FIXED - USING LOCAL STORAGE)
    // ============================================

    function getSelectedDays() {
        const itinerary = getItineraryFromStorage();
        
        if (!itinerary.tripInfo || !itinerary.tripInfo.startDate || !itinerary.tripInfo.endDate) {
            return null;
        }
    
        const month = itinerary.tripInfo.month;
        const dateRange = parseDateRange(month, itinerary.tripInfo.startDate, itinerary.tripInfo.endDate);
    
        if (!dateRange) return null;
    
        const selectedDays = new Set();
        const currentDate = new Date(dateRange.start);

        while (currentDate <= dateRange.end) {
            const dayName = currentDate.toLocaleDateString('en-US', { weekday: 'long' });
            selectedDays.add(dayName);
            currentDate.setDate(currentDate.getDate() + 1);
        }
    
        return Array.from(selectedDays);
    }

    function parseDateRange(month, startStr, endStr) {
        try {
            const currentYear = new Date().getFullYear();
            
            // Extract numeric values
            const startDay = parseInt(startStr.toString().match(/\d+/)[0]);
            const endDay = parseInt(endStr.toString().match(/\d+/)[0]);
            
            const startDate = new Date(`${month} ${startDay}, ${currentYear}`);
            const endDate = new Date(`${month} ${endDay}, ${currentYear}`);
            
            // If end date is before start date, assume it's next month/year
            if (endDate < startDate) {
                endDate.setFullYear(endDate.getFullYear() + 1);
            }
        
            return { start: startDate, end: endDate };
        } catch (error) {
            console.error('Error parsing dates:', error);
            return null;
        }
    }

    // ============================================
    // BREAKFAST HOURS FUNCTIONS
    // ============================================

    // Format hours with date filtering
    function formatHoursInChronologicalOrder(hoursData, selectedDays = null) {
        const dayOrder = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        let html = '';
        
        if (hoursData.hours && typeof hoursData.hours === 'object') {
            // Filter days based on selected itinerary dates
            let daysToDisplay = dayOrder;
            if (selectedDays && selectedDays.length > 0) {
                daysToDisplay = dayOrder.filter(day => selectedDays.includes(day));
            }
        
            // Display only filtered days
            daysToDisplay.forEach(day => {
                if (hoursData.hours[day]) {
                    html += `
                        <div class="day-hour">
                            <span class="day">${day}:</span>
                            <span class="time">${hoursData.hours[day]}</span>
                        </div>
                    `;
                }
            });
        
            // Show message if no hours for selected days
            if (html === '' && Object.keys(hoursData.hours).length > 0) {
                html = `
                    <div class="day-hour">
                        <span class="day">Note:</span>
                        <span class="time">No hours available for selected dates</span>
                    </div>
                `;
            }
        } else if (typeof hoursData.hours === 'string') {
            html += `<div class="day-hour"><span class="time">${hoursData.hours}</span></div>`;
        }
        
        return html;
    }

    // Fallback hours for when API is offline
    function getFallbackHours(restaurantKey) {
        const fallbackHours = {
            sarabeths: {
                hours: {
                    Sunday: "8:00 AM - 4:00 PM",
                    Monday: "8:00 AM - 4:00 PM",
                    Tuesday: "8:00 AM - 4:00 PM",
                    Wednesday: "8:00 AM - 4:00 PM",
                    Thursday: "8:00 AM - 4:00 PM",
                    Friday: "8:00 AM - 5:00 PM",
                    Saturday: "8:00 AM - 5:00 PM"
                }
            },
            jacks: {
                hours: {
                    Monday: "8:00 AM - 4:00 PM",
                    Tuesday: "8:00 AM - 4:00 PM",
                    Wednesday: "8:00 AM - 4:00 PM",
                    Thursday: "8:00 AM - 4:00 PM",
                    Friday: "8:00 AM - 5:00 PM",
                    Saturday: "9:00 AM - 5:00 PM",
                    Sunday: "9:00 AM - 5:00 PM"
                }
            },
            ess: {
                hours: {
                    Monday: "6:00 AM - 8:00 PM",
                    Tuesday: "6:00 AM - 8:00 PM",
                    Wednesday: "6:00 AM - 8:00 PM",
                    Thursday: "6:00 AM - 8:00 PM",
                    Friday: "6:00 AM - 8:00 PM",
                    Saturday: "6:00 AM - 6:00 PM",
                    Sunday: "6:00 AM - 4:00 PM"
                }
            },
            shuka: {
                hours: {
                    Monday: "8:00 AM - 11:00 PM",
                    Tuesday: "8:00 AM - 11:00 PM",
                    Wednesday: "8:00 AM - 11:00 PM",
                    Thursday: "8:00 AM - 11:00 PM",
                    Friday: "8:00 AM - 12:00 AM",
                    Saturday: "10:00 AM - 12:00 AM",
                    Sunday: "10:00 AM - 11:00 PM"
                }
            }
        };

        return fallbackHours[restaurantKey] || fallbackHours.sarabeths;
    }

    // ============================================
    // TRIP DATES BANNER FUNCTIONS
    // ============================================

    function updateTripDatesBanner() {
        const itinerary = getItineraryFromStorage();
        const banner = document.getElementById('tripDatesBanner');
        const noDatesWarning = document.getElementById('noDatesWarning');
        const tripDatesDisplay = document.getElementById('tripDatesDisplay');
        const tripDaysDisplay = document.getElementById('tripDaysDisplay');
        
        if (itinerary.tripInfo && itinerary.tripInfo.month && itinerary.tripInfo.startDate && itinerary.tripInfo.endDate) {
            // Show banner with dates
            banner.style.display = 'flex';
            noDatesWarning.style.display = 'none';
            
            tripDatesDisplay.textContent = `${itinerary.tripInfo.month} ${itinerary.tripInfo.startDate} - ${itinerary.tripInfo.endDate}`;
            
            const selectedDays = getSelectedDays();
            if (selectedDays && selectedDays.length > 0) {
                tripDaysDisplay.textContent = `📆 Visiting on: ${selectedDays.join(', ')}`;
            } else {
                tripDaysDisplay.textContent = '';
            }
        } else {
            // Show warning
            banner.style.display = 'none';
            noDatesWarning.style.display = 'block';
        }
    }

    // ============================================
    // BREAKFAST DATA
    // ============================================

    const MENU_DATA = {
        sarabeths: {
            name: "Sarabeth's",
            location: "Upper West Side",
            description: "A beloved NYC institution known for its legendary homemade jams and elegant brunch classics. Perfect for a refined, upscale breakfast experience.",
            items: [
                {name: 'Lemon Ricotta Pancakes', price: 18, desc: 'Fluffy pancakes with fresh lemon zest'},
                {name: 'Eggs Benedict', price: 22, desc: 'Poached eggs on English muffin'},
                {name: 'French Toast', price: 16, desc: 'Challah bread with maple syrup'},
                {name: 'Fresh Squeezed OJ', price: 8, desc: 'Orange juice made to order'}
            ]
        },
        jacks: {
            name: "Jack's Wife Frida",
            location: "SoHo",
            description: "Mediterranean-inspired breakfast with bold Mexican flavors. A trendy spot with colorful dishes and creative twists on morning favorites.",
            items: [
                {name: 'Shakshuka', price: 19, desc: 'Poached eggs in spicy tomato sauce'},
                {name: 'Avocado Toast', price: 16, desc: 'Sourdough with smashed avocado'},
                {name: 'Mexican Omelet', price: 18, desc: 'With chorizo and peppers'},
                {name: 'Cold Brew Coffee', price: 6, desc: 'Smooth and refreshing'}
            ]
        },
        ess: {
            name: "Ess a Bagel",
            location: "Midtown East",
            description: "The ultimate NYC bagel experience. Hand-rolled, kettle-boiled bagels that are crispy outside and pillowy inside. A true New York classic.",
            items: [
                {name: 'Everything Bagel', price: 5, desc: 'With cream cheese'},
                {name: 'Lox and Bagel', price: 18, desc: 'Nova lox with cream cheese'},
                {name: 'Egg Sandwich', price: 12, desc: 'Fried egg and cheese'},
                {name: 'Hot Coffee', price: 3, desc: 'Fresh brewed'}
            ]
        },
        shuka: {
            name: "Shuka",
            location: "East Village",
            description: "Modern Mediterranean cuisine with Israeli breakfast specialties. Fresh, vibrant dishes featuring tahini, hummus, and perfectly spiced shakshuka.",
            items: [
                {name: 'Israeli Breakfast', price: 22, desc: 'Eggs, hummus, tahini, salad'},
                {name: 'Halloumi Scramble', price: 19, desc: 'With grilled halloumi cheese'},
                {name: 'Quinoa Bowl', price: 17, desc: 'Roasted vegetables and egg'},
                {name: 'Turkish Coffee', price: 5, desc: 'Strong and aromatic'}
            ]
        }
    };

    // Restaurant mapping for API calls
    const RESTAURANT_MAP = {
        'sarabeths': { name: "Sarabeth's", endpoint: 'sarabeths' },
        'jacks': { name: "Jack's Wife Frida", endpoint: 'jacks' },
        'ess': { name: "Ess a Bagel", endpoint: 'bagel' },
        'shuka': { name: "Shuka", endpoint: 'shuka' }
    };

    let currentRestaurant = null;
    let cart = [];

    // ============================================
    // API FUNCTIONS
    // ============================================

    async function fetchRestaurantHours(restaurantKey) {
        const restaurant = RESTAURANT_MAP[restaurantKey];
        if (!restaurant) return null;

        try {
            // Try to fetch from backend API
            const response = await fetch(`/api/breakfast/${restaurant.endpoint}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include'
            });
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            
            const data = await response.json();
        
            if (data.success && data.data) {
                return data.data;
            } else {
                console.error(`Error fetching ${restaurant.name}:`, data.error);
                // Return fallback data
                return getFallbackHours(restaurantKey);
            }
        } catch (error) {
            console.error(`Network error for ${restaurant.name}:`, error);
            return getFallbackHours(restaurantKey);
        }
    }

    async function testAPIConnection() {
        try {
            const response = await fetch(`/api/breakfast/test`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include'
            });
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            
            const data = await response.json();
        
            const statusIndicator = document.getElementById('apiStatus');
            if (data.success) {
                statusIndicator.textContent = '✅ API Connected';
                statusIndicator.className = 'live-data-indicator';
                return true;
            } else {
                statusIndicator.textContent = '⚠️ API Error';
                statusIndicator.className = 'live-data-indicator offline';
                return false;
            }
        } catch (error) {
            console.error('API connection failed:', error);
            const statusIndicator = document.getElementById('apiStatus');
            statusIndicator.textContent = '❌ API Offline (Using Fallback Hours)';
            statusIndicator.className = 'live-data-indicator offline';
            return false;
        }
    }

    // ============================================
    // UI FUNCTIONS
    // ============================================

    function goToStep(n) {
        document.querySelectorAll('.step').forEach(step => {
            step.classList.remove('active');
        });
        document.getElementById('step' + n).classList.add('active');
        if (n === 2) {
            updateAddButton();
        }
    }

    async function selectRestaurant(restaurantKey) {
        // Check if trip dates are selected
        const itinerary = getItineraryFromStorage();
        if (!itinerary.tripInfo || !itinerary.tripInfo.month) {
            alert('Please set your trip dates first!');
            window.location.href = '/Insightful-Innovators-/newyork/tripinfo/';
            return;
        }

        currentRestaurant = restaurantKey;
        
        // Update restaurant details
        const restaurantData = MENU_DATA[restaurantKey];
        document.getElementById('restaurantName').textContent = restaurantData.name;
        document.getElementById('restaurantLocation').textContent = `📍 ${restaurantData.location}`;
        document.getElementById('restaurantDescription').textContent = restaurantData.description;
        
        // Fetch live hours
        await refreshCurrentRestaurant();
        
        // Show menu
        showMenu();
        goToStep(2);
    }

    async function refreshCurrentRestaurant() {
        if (!currentRestaurant) return;
        
        const restaurantData = MENU_DATA[currentRestaurant];
        const hoursContainer = document.getElementById('restaurantHours');
        
        // Show loading
        hoursContainer.innerHTML = `
            <div class="hours-loading">
                <div class="live-loading-spinner"></div>
                <div>Fetching live hours for ${restaurantData.name}...</div>
            </div>
        `;
        
        try {
            const hoursData = await fetchRestaurantHours(currentRestaurant);
            const selectedDays = getSelectedDays();
        
            if (hoursData) {
                let hoursHtml = `<div class="hours-display">`;
            
                // Add subtle indicator if filtering is active
                if (selectedDays && selectedDays.length > 0) {
                    hoursHtml += `
                        <div style="margin-bottom: 10px; padding: 8px; background: rgba(255, 215, 0, 0.05); border-radius: 6px; font-size: 0.9rem; color: #ffd700;">
                            📅 Showing hours for: ${selectedDays.join(', ')}
                        </div>
                    `;
                }
            
                // Use filtered chronological order formatting
                hoursHtml += formatHoursInChronologicalOrder(hoursData, selectedDays);
            
                hoursHtml += `</div>`;
            
                // Add timestamp
                const now = new Date();
                const currentTime = now.toLocaleTimeString('en-US', {
                    hour: '2-digit',
                    minute: '2-digit',
                    hour12: true
                });
                const currentDate = now.toLocaleDateString('en-US', {
                    month: 'short',
                    day: 'numeric',
                    year: 'numeric'
                });
            
                hoursHtml += `
                    <div class="update-note">
                        <strong>Source:</strong> ${hoursData.source || 'Live API'}
                        | <strong>Updated:</strong> ${currentTime} on ${currentDate}
                        ${selectedDays ? ` | <strong>Filtered by your trip dates</strong>` : ''}
                    </div>
                `;
            
                hoursContainer.innerHTML = hoursHtml;
            } else {
                throw new Error('No hours data');
            }
        } catch (error) {
            console.error('Error fetching hours:', error);

            // Get selected days for error message
            const selectedDays = getSelectedDays();
            let errorMessage = 'Unable to fetch live hours';
            if (selectedDays) {
                errorMessage += ` for selected dates`;
            }

            const fallbackHours = getFallbackHours(currentRestaurant);
            
            const now = new Date();
            const currentTime = now.toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit',
                hour12: true
            });
            const currentDate = now.toLocaleDateString('en-US', {
                month: 'short',
                day: 'numeric',
                year: 'numeric'
            });
            
            hoursContainer.innerHTML = `
                <div class="hours-display">
                    <div class="day-hour">
                        <span class="day">Status:</span>
                        <span class="time" style="color: #ef4444;">${errorMessage}</span>
                    </div>
                    ${Object.entries(fallbackHours.hours).map(([day, time]) => `
                        <div class="day-hour">
                            <span class="day">${day}:</span>
                            <span class="time">${time}</span>
                        </div>
                    `).join('')}
                </div>
                <div class="update-note">
                    ⚠️ Showing fallback hours. API connection failed.
                    | <strong>Last checked:</strong> ${currentTime} on ${currentDate}
                </div>
            `;
        }
    }

    function showMenu() {
        const menuGrid = document.getElementById('menuGrid');
        const items = MENU_DATA[currentRestaurant].items;
        
        menuGrid.innerHTML = items.map(item => `
            <div class="menu-item">
                <h4>${item.name}</h4>
                <div class="price">$${item.price}</div>
                <p>${item.desc}</p>
                <button class="btn" onclick="addToCart('${item.name}', ${item.price})" style="width: 100%; margin-top: 10px;">
                    <span>➕</span> Add to Order
                </button>
            </div>
        `).join('');
    }

    // Order functions (cart management)
    function addToCart(name, price) {
        cart.push({ name, price });
        updateOrderList();
    }

    function updateOrderList() {
        const orderList = document.getElementById('orderList');
        if (cart.length === 0) {
            orderList.innerHTML = '<p style="color: #94a3b8;">Your order is empty. Add items from the menu!</p>';
            return;
        }
        
        orderList.innerHTML = cart.map((item, index) => `
            <div class="order-item">
                <div>
                    <strong>${item.name}</strong>
                    <div style="color: #10b981;">$${item.price}</div>
                </div>
                <button class="remove-btn" onclick="removeFromCart(${index})">Remove</button>
            </div>
        `).join('');
    }

    function removeFromCart(index) {
        cart.splice(index, 1);
        updateOrderList();
    }

    function addCustom() {
        const input = document.getElementById('customInput');
        const customItem = input.value.trim();
        
        if (customItem) {
            cart.push({ name: customItem, price: 0 });
            input.value = '';
            updateOrderList();
        }
    }

    function showReview() {
        const reviewHeader = document.getElementById('reviewHeader');
        const reviewList = document.getElementById('reviewList');
        const totalPrice = document.getElementById('totalPrice');
        
        reviewHeader.innerHTML = `<h3 style="color: #f59e0b; margin-bottom: 20px;">${MENU_DATA[currentRestaurant].name}</h3>`;
        
        if (cart.length === 0) {
            reviewList.innerHTML = '<p style="color: #94a3b8;">No items in order</p>';
            totalPrice.textContent = 'Total: $0';
            return;
        }
        
        reviewList.innerHTML = cart.map(item => `
            <div class="order-item">
                <div>
                    <strong>${item.name}</strong>
                </div>
                <div style="color: #10b981; font-size: 20px; font-weight: bold;">$${item.price}</div>
            </div>
        `).join('');
        
        const total = cart.reduce((sum, item) => sum + item.price, 0);
        totalPrice.textContent = `Total: $${total}`;
    }

    function confirmOrder() {
        alert(`Order confirmed at ${MENU_DATA[currentRestaurant].name}! Total: $${cart.reduce((sum, item) => sum + item.price, 0)}`);
        cart = [];
        goToStep(1);
    }

    // ============================================
    // ITINERARY BUTTON FUNCTIONS
    // ============================================

    function addBreakfastToItinerary() {
        if (!currentRestaurant) return;

        const restaurantData = MENU_DATA[currentRestaurant];
        
        // Save to localStorage
        const breakfastInfo = {
            name: restaurantData.name,
            location: restaurantData.location,
            selected_at: new Date().toISOString(),
            restaurant_id: currentRestaurant,
            type: 'breakfast'
        };
        
        updateBreakfastInItinerary(breakfastInfo);
        
        // Update button state
        const btn = document.getElementById('addToItineraryBtn');
        btn.classList.add('added');
        btn.innerHTML = '<span>✓</span> Added to Itinerary';

        // Update quick add buttons
        updateQuickAddButtons();
        
        // Revert button after 2 seconds
        setTimeout(() => {
            updateAddButton();
        }, 2000);
    }

    function updateAddButton() {
        const itinerary = getItineraryFromStorage();
        const btn = document.getElementById('addToItineraryBtn');
        
        if (btn && itinerary.breakfast && currentRestaurant) {
            const restaurantData = MENU_DATA[currentRestaurant];
            
            // Check if this restaurant is the one saved
            let isCurrentRestaurant = false;
            if (typeof itinerary.breakfast === 'object') {
                isCurrentRestaurant = itinerary.breakfast.name === restaurantData.name;
            } else {
                isCurrentRestaurant = itinerary.breakfast === restaurantData.name;
            }
            
            if (isCurrentRestaurant) {
                btn.classList.add('added');
                btn.innerHTML = '<span>✓</span> Added to Itinerary';
            } else {
                btn.classList.remove('added');
                btn.innerHTML = '<span>⭐</span> Add to My Itinerary';
            }
        }
    }

    function updateQuickAddButtons() {
        const itinerary = getItineraryFromStorage();
        const buttons = document.querySelectorAll('.quick-add-btn');

        buttons.forEach((btn) => {
            const restaurantKey = btn.getAttribute('data-restaurant');
            const restaurantData = MENU_DATA[restaurantKey];
            
            // Check if this restaurant is saved
            let isSaved = false;
            if (itinerary.breakfast) {
                if (typeof itinerary.breakfast === 'object') {
                    isSaved = itinerary.breakfast.name === restaurantData.name;
                } else {
                    isSaved = itinerary.breakfast === restaurantData.name;
                }
            }
        
            if (isSaved) {
                btn.classList.add('added');
                btn.innerHTML = '<span>✓</span> Added';
            } else {
                btn.classList.remove('added');
                btn.innerHTML = '<span>⭐</span> Add';
            }
        });
    }

    function quickAddToItinerary(restaurantKey, event) {
        event.stopPropagation();

        // Check if trip dates are selected
        const itinerary = getItineraryFromStorage();
        if (!itinerary.tripInfo || !itinerary.tripInfo.month) {
            alert('Please set your trip dates first!');
            window.location.href = '/Insightful-Innovators-/newyork/tripinfo/';
            return;
        }

        const restaurantData = MENU_DATA[restaurantKey];
        
        // Save to localStorage
        const breakfastInfo = {
            name: restaurantData.name,
            location: restaurantData.location,
            selected_at: new Date().toISOString(),
            restaurant_id: restaurantKey,
            type: 'breakfast'
        };
        
        updateBreakfastInItinerary(breakfastInfo);
        updateQuickAddButtons();
        
        // Show confirmation
        const btn = event.target.closest('.quick-add-btn');
        if (btn) {
            const originalHTML = btn.innerHTML;
            btn.innerHTML = '<span>✓</span> Saved!';
            setTimeout(() => {
                btn.innerHTML = '<span>✓</span> Added';
            }, 1000);
        }
    }

    // ============================================
    // INITIALIZATION
    // ============================================

    // Expose functions to global window scope
    window.navigateTo = navigateTo;
    window.toggleItineraryTracker = toggleItineraryTracker;
    window.clearItinerary = clearItinerary;
    window.goToStep = goToStep;
    window.selectRestaurant = selectRestaurant;
    window.refreshCurrentRestaurant = refreshCurrentRestaurant;
    window.addBreakfastToItinerary = addBreakfastToItinerary;
    window.quickAddToItinerary = quickAddToItinerary;
    window.addToCart = addToCart;
    window.updateOrderList = updateOrderList;
    window.removeFromCart = removeFromCart;
    window.addCustom = addCustom;
    window.showReview = showReview;
    window.confirmOrder = confirmOrder;

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        // Load itinerary from localStorage
        const itinerary = getItineraryFromStorage();
        updateItineraryDisplay(itinerary);
        updateTripDatesBanner();
        updateQuickAddButtons();
        
        // Test API connection
        testAPIConnection();
    });
</script>
</body>
</html>