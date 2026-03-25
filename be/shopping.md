---
layout: post
title: "Step 2 Shopping"
description: "Time to shop! Let's make a new outfit."
permalink: /new-york/shopping/
parent: "Analytics/Admin"
team: "Insightful Innovators"
submodule: 2
author: "Insightful Innocators"
date: 2025-11-20
microblog: true
footer: 
    previous: /new-york/breakfast/
    home: /nyc/home/
    next: /new-york/landmarks/
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NYC Shopping Centers</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #1a2332 0%, #2c3e50 100%);
            color: white;
            min-height: 100vh;
        }

        /* Fixed Sidebar - SHOPPING THEMED */
        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            width: 260px;
            height: 100vh;
            background: linear-gradient(180deg, #1a1a2e 0%, #2a2a3e 50%, #3a3a4e 100%);
            border-right: 3px solid #ffd700;
            padding: 25px 20px;
            z-index: 1000;
            overflow-y: auto;
            box-shadow: 4px 0 20px rgba(255, 215, 0, 0.3);
        }

        .sidebar-header {
            margin-bottom: 35px;
            padding-bottom: 20px;
            border-bottom: 3px solid #ffd700;
            text-align: center;
        }

        .sidebar-header h2 {
            color: #ffd700;
            font-size: 1.6rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        .sidebar-header p {
            color: #ffed4e;
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
            border-left-color: #ffd700;
            box-shadow: 0 4px 12px rgba(255, 215, 0, 0.4);
        }

        .nav-button.active {
            background: rgba(255, 215, 0, 0.3);
            border-left-color: #ffd700;
            border-color: #ffd700;
            color: #ffd700;
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
            max-width: 1200px;
        }

        .container {
            max-width: 100%;
            margin: 0;
            width: 100%;
        }

        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }

        h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            font-size: 1.2em;
            font-style: italic;
            opacity: 0.95;
        }

        /* Shopping Center Selection */
        .center-selection {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
            width: 100%;
        }

        .center-card {
            background: #1a1a1a;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 3px solid transparent;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .center-card:hover {
            transform: translateY(-10px);
            border-color: #ffd700;
            box-shadow: 0 15px 50px rgba(255, 215, 0, 0.3);
        }

        .center-card.selected {
            border-color: #ffd700;
            background: #2a2a2a;
        }

        .center-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }

        .center-card h2 {
            font-size: 1.5em;
            margin-bottom: 10px;
            color: #ffd700;
        }

        .center-card p {
            color: #ccc;
            font-size: 0.95em;
            flex-grow: 1;
            margin-bottom: 20px;
        }

        /* Gender Selection Screen */
        .gender-selection {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
            margin-top: 40px;
        }

        .gender-card {
            background: #1a1a1a;
            padding: 50px 40px;
            border-radius: 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 3px solid transparent;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            min-width: 250px;
        }

        .gender-card:hover {
            transform: translateY(-10px);
            border-color: #ffd700;
            box-shadow: 0 15px 50px rgba(255, 215, 0, 0.3);
        }

        .gender-card h3 {
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #ffd700;
        }

        .gender-card p {
            color: #ccc;
            font-size: 1.1em;
        }

        .gender-icon {
            font-size: 4em;
            margin-bottom: 20px;
        }

        .hidden {
            display: none !important;
        }

        .back-button {
            display: inline-block;
            background: rgba(255, 215, 0, 0.2);
            color: #ffd700;
            padding: 10px 20px;
            border-radius: 20px;
            border: 1px solid #ffd700;
            cursor: pointer;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            text-decoration: none;
        }

        .back-button:hover {
            background: rgba(255, 215, 0, 0.3);
            transform: translateY(-2px);
        }

        .area-info {
            background: rgba(255, 215, 0, 0.1);
            border: 1px solid #ffd700;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            text-align: center;
        }

        .area-info h2 {
            color: #ffd700;
            margin-bottom: 10px;
        }

        .area-info p {
            color: #ccc;
        }

        .wardrobe-section {
            background: #1a1a1a;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            border-top: 5px solid #ffd700;
            max-width: 600px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 1.8em;
            margin-bottom: 25px;
            text-align: center;
            color: #ffd700;
        }

        .outfit-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }

        .clothing-item {
            background: #2a2a2a;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            transition: transform 0.3s ease;
        }

        .clothing-item:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .item-category {
            font-size: 0.85em;
            color: #ffd700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }

        .item-display {
            width: 100%;
            height: 200px;
            background: #0a0a0a;
            border-radius: 8px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .item-display img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }

        .item-name {
            font-size: 1em;
            color: #ffffff;
            margin-bottom: 12px;
            font-weight: 600;
        }

        .nav-buttons {
            display: flex;
            gap: 8px;
            justify-content: center;
        }

        .nav-btn {
            background: #ffd700;
            color: #1a2332;
            border: none;
            padding: 6px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.85em;
            transition: all 0.3s ease;
        }

        .nav-btn:hover {
            background: #ffed4e;
        }

        .action-buttons {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }

        .btn {
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            color: #1a2332;
            border: none;
            padding: 12px 25px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.95em;
            font-weight: 600;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.3);
        }

        .status-message {
            text-align: center;
            font-size: 1.1em;
            margin-top: 15px;
            font-style: italic;
            min-height: 30px;
            color: #ffd700;
        }

        /* Itinerary Tracker Sidebar - EXACT COPY */
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

        /* Add to Itinerary Button for Shopping Centers */
        .add-to-itinerary-btn {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: 600;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin-top: auto;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            width: 100%;
        }

        .add-to-itinerary-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(16, 185, 129, 0.3);
        }

        .add-to-itinerary-btn.added {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        }

        .add-to-itinerary-btn.added:hover {
            transform: none;
            cursor: default;
        }

        /* Add to Itinerary Button for Shopping Content */
        .add-shopping-itinerary-btn {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.95em;
            font-weight: 600;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin-top: 10px;
            width: 100%;
        }

        .add-shopping-itinerary-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(16, 185, 129, 0.3);
        }

        .add-shopping-itinerary-btn.added {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        }

        .center-card-buttons {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }

        .center-select-btn {
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            color: #1a2332;
            border: none;
            padding: 10px 15px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: 600;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }

        .center-select-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(255, 215, 0, 0.3);
        }

        /* Broadway Navigation Section */
        .nav-to-broadway {
            margin-top: 50px;
            margin-bottom: 50px;
            text-align: center;
            padding: 40px;
            background: rgba(255, 215, 0, 0.1);
            border-radius: 15px;
            border: 2px solid #ffd700;
            width: 100%;
        }
        
        .nav-to-broadway h2 {
            color: #fbbf24;
            margin-bottom: 20px;
            font-size: 2rem;
        }
        
        .nav-to-broadway p {
            color: #cbd5e1;
            font-size: 1.2rem;
            margin-bottom: 30px;
        }
        
        .broadway-btn {
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
        
        .broadway-btn:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 40px rgba(255, 215, 0, 0.6);
            background: linear-gradient(135deg, #ffed4e 0%, #ffd700 100%);
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
            
            .center-selection {
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
            }
        }

        @media (max-width: 900px) {
            .center-selection {
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
                content: "🛍️";
                font-size: 1.5rem;
                color: #ffd700;
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
            
            h1 {
                font-size: 1.8em;
            }

            .center-selection {
                grid-template-columns: 1fr;
            }

            .gender-selection {
                flex-direction: column;
                gap: 20px;
            }

            .gender-card {
                width: 100%;
                max-width: 300px;
            }

            .wardrobe-section {
                padding: 20px;
            }

            .itinerary-tracker {
                width: 90%;
                right: 5%;
                left: 5%;
            }

            .center-card-buttons {
                flex-direction: column;
            }

            .broadway-btn {
                padding: 15px 35px;
                font-size: 1.1rem;
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
            <button class="nav-button breakfast" onclick="navigateTo('breakfast')">
                🍳 Breakfast
            </button>
            <button class="nav-button landmarks" onclick="navigateTo('landmarks')">
                🗽 Landmarks
            </button>
            <button class="nav-button shopping active" onclick="navigateTo('shopping')">
                🛍️ Shopping
            </button>
            <button class="nav-button broadway" onclick="navigateTo('broadway')">
                🎭 Broadway
            </button>
        </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <!-- Itinerary Tracker Toggle Button -->
        <button class="toggle-tracker-btn" onclick="toggleItineraryTracker()">
            📋 My Itinerary
        </button>

        <div class="container">
            <header>
                <h1>NYC Shopping Experience</h1>
                <p class="subtitle">Choose your shopping destination</p>
            </header>

            <!-- Shopping Center Selection -->
            <div id="center-selection-screen">
                <div class="center-selection">
                    <div class="center-card">
                        <div class="center-icon">🏬</div>
                        <h2>East River Plaza</h2>
                        <p>Affordable fashion & everyday essentials</p>
                        <div class="center-card-buttons">
                            <button class="center-select-btn" onclick="selectCenter('east-river')">
                                <span>🛒</span> Shop Here
                            </button>
                            <button class="add-to-itinerary-btn" id="add-east-river" onclick="addShoppingCenterToItinerary('east-river', event)">
                                <span>✅</span> Add to Itinerary
                            </button>
                        </div>
                    </div>

                    <div class="center-card">
                        <div class="center-icon">🏢</div>
                        <h2>Macy's Herald Square</h2>
                        <p>Classic department store elegance</p>
                        <div class="center-card-buttons">
                            <button class="center-select-btn" onclick="selectCenter('macys')">
                                <span>🛒</span> Shop Here
                            </button>
                            <button class="add-to-itinerary-btn" id="add-macys" onclick="addShoppingCenterToItinerary('macys', event)">
                                <span>✅</span> Add to Itinerary
                            </button>
                        </div>
                    </div>

                    <div class="center-card">
                        <div class="center-icon">✨</div>
                        <h2>SoHo Center</h2>
                        <p>Trendy & fashion-forward styles</p>
                        <div class="center-card-buttons">
                            <button class="center-select-btn" onclick="selectCenter('soho')">
                                <span>🛒</span> Shop Here
                            </button>
                            <button class="add-to-itinerary-btn" id="add-soho" onclick="addShoppingCenterToItinerary('soho', event)">
                                <span>✅</span> Add to Itinerary
                            </button>
                        </div>
                    </div>

                    <div class="center-card">
                        <div class="center-icon">💎</div>
                        <h2>Columbus Circle</h2>
                        <p>Luxury designer boutiques</p>
                        <div class="center-card-buttons">
                            <button class="center-select-btn" onclick="selectCenter('columbus')">
                                <span>🛒</span> Shop Here
                            </button>
                            <button class="add-to-itinerary-btn" id="add-columbus" onclick="addShoppingCenterToItinerary('columbus', event)">
                                <span>✅</span> Add to Itinerary
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Gender Selection Screen -->
            <div id="gender-selection-screen" class="hidden">
                <button class="back-button" onclick="backToCenter()">← Change Shopping Center</button>
                
                <div class="area-info">
                    <h2 id="selected-center-name"></h2>
                    <p id="selected-center-desc"></p>
                </div>

                <div class="gender-selection">
                    <div class="gender-card" onclick="selectGender('women')">
                        <div class="gender-icon">👗</div>
                        <h3>Women's</h3>
                        <p>Shop women's fashion</p>
                    </div>

                    <div class="gender-card" onclick="selectGender('men')">
                        <div class="gender-icon">👔</div>
                        <h3>Men's</h3>
                        <p>Shop men's fashion</p>
                    </div>
                </div>
            </div>

            <!-- Shopping Content -->
            <div id="shopping-content" class="hidden">
                <button class="back-button" onclick="backToGender()">← Change Selection</button>

                <div class="area-info">
                    <h2 id="shopping-area-title"></h2>
                    <p id="shopping-area-subtitle"></p>
                </div>

                <div class="wardrobe-section">
                    <h2 class="section-title" id="section-title">Your Look</h2>
                    
                    <div class="outfit-grid">
                        <div class="clothing-item">
                            <div class="item-category">Top</div>
                            <div class="item-display" id="top-display"></div>
                            <div class="item-name" id="top-name">Top</div>
                            <div class="nav-buttons">
                                <button class="nav-btn" onclick="prevItem('top')">← Prev</button>
                                <button class="nav-btn" onclick="nextItem('top')">Next →</button>
                            </div>
                        </div>

                        <div class="clothing-item">
                            <div class="item-category">Bottom</div>
                            <div class="item-display" id="bottom-display"></div>
                            <div class="item-name" id="bottom-name">Bottom</div>
                            <div class="nav-buttons">
                                <button class="nav-btn" onclick="prevItem('bottom')">← Prev</button>
                                <button class="nav-btn" onclick="nextItem('bottom')">Next →</button>
                            </div>
                        </div>

                        <div class="clothing-item">
                            <div class="item-category">Shoes</div>
                            <div class="item-display" id="shoes-display"></div>
                            <div class="item-name" id="shoes-name">Shoes</div>
                            <div class="nav-buttons">
                                <button class="nav-btn" onclick="prevItem('shoes')">← Prev</button>
                                <button class="nav-btn" onclick="nextItem('shoes')">Next →</button>
                            </div>
                        </div>
                    </div>

                    <div class="action-buttons">
                        <button class="btn" onclick="randomOutfit()">✨ Surprise Me!</button>
                        <button class="btn" onclick="saveOutfit()">💾 Save Outfit</button>
                    </div>

                    <!-- Add to Itinerary Button -->
                    <button class="add-shopping-itinerary-btn" id="addShoppingToItineraryBtn" onclick="addShoppingSelectionToItinerary()">
                        ✅ Add Shopping to My Itinerary
                    </button>

                    <div class="status-message" id="status">Ready to shop!</div>
                </div>
            </div>

            <!-- Broadway Navigation Section -->
            <div class="nav-to-broadway">
                <h2>Ready for Broadway?</h2>
                <p>After shopping, enjoy a spectacular Broadway show in NYC!</p>
                <a href="https://vivianzhang85.github.io/Insightful-Innovators-/new-york/broadway/" class="broadway-btn">
                    🎭 See Broadway Shows
                </a>
            </div>
        </div>
    </div>

    <!-- Itinerary Tracker Sidebar -->
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

    <script type="module">
        // ============================================
        // SIDEBAR NAVIGATION
        // ============================================
        
        function navigateTo(section) {
            // Update active button
            document.querySelectorAll('.nav-button').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Navigation logic
            if (section === 'breakfast') {
                window.location.href = '/Insightful-Innovators-/new-york/breakfast/';
            } else if (section === 'landmarks') {
                window.location.href = '/Insightful-Innovators-/new-york/landmarks/';
            } else if (section === 'shopping') {
                // Already on shopping page
                console.log('Navigating to shopping section');
            } else if (section === 'broadway') {
                window.location.href = '/Insightful-Innovators-/new-york/broadway/';
            }
        }

        // ============================================
        // ITINERARY TRACKER JAVASCRIPT (UPDATED FOR BACKEND)
        // ============================================

        // Import configuration from config.js (MODIFIED)
        import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
        
        console.log('Config loaded - Python URI:', pythonURI);

        // Initialize itinerary when page loads
        async function initItinerary() {
            try {
                const itinerary = await getItinerary();
                updateItineraryDisplay(itinerary);
                updateAddToItineraryButtons();
                updateShoppingContentItineraryButton();
            } catch (error) {
                console.error('Failed to initialize itinerary:', error);
                // Fallback to localStorage during transition
                const stored = localStorage.getItem('nycItinerary');
                const itinerary = stored ? JSON.parse(stored) : {
                    tripInfo: null,
                    breakfast: null,
                    landmarks: null,
                    shopping: null,
                    broadway: null
                };
                updateItineraryDisplay(itinerary);
            }
        }

        async function getItinerary() {
            try {
                const requestOptions = {
                    ...fetchOptions,
                    method: 'GET',
                    credentials: 'include'
                };
                
                const response = await fetch(`${pythonURI}/api/itinerary`, requestOptions);
                
                if (!response.ok) {
                    throw new Error(`API error: ${response.status}`);
                }
                
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
                } else {
                    throw new Error(data.error || 'Failed to get itinerary');
                }
            } catch (error) {
                console.error('Error fetching itinerary from backend:', error);
                // Fallback to localStorage
                const stored = localStorage.getItem('nycItinerary');
                return stored ? JSON.parse(stored) : {
                    tripInfo: null,
                    breakfast: null,
                    landmarks: null,
                    shopping: null,
                    broadway: null
                };
            }
        }

        async function saveItinerary(itinerary) {
            try {
                const backendItinerary = {
                    trip_info: itinerary.tripInfo || null,
                    breakfast: itinerary.breakfast || null,
                    landmarks: itinerary.landmarks || null,
                    shopping: itinerary.shopping || null,
                    broadway: itinerary.broadway || null
                };
                
                const requestOptions = {
                    ...fetchOptions,
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                    body: JSON.stringify(backendItinerary)
                };
                
                const response = await fetch(`${pythonURI}/api/itinerary`, requestOptions);
                
                if (!response.ok) {
                    throw new Error(`API error: ${response.status}`);
                }
                
                const data = await response.json();
                
                if (data.success) {
                    updateItineraryDisplay(itinerary);
                    updateAddToItineraryButtons();
                    updateShoppingContentItineraryButton();
                    return itinerary;
                } else {
                    throw new Error(data.error || 'Failed to save itinerary');
                }
            } catch (error) {
                console.error('Error saving itinerary to backend:', error);
                localStorage.setItem('nycItinerary', JSON.stringify(itinerary));
                updateItineraryDisplay(itinerary);
                updateAddToItineraryButtons();
                updateShoppingContentItineraryButton();
                return itinerary;
            }
        }

        async function updateShoppingInItinerary(shoppingData) {
            try {
                const requestOptions = {
                    ...fetchOptions,
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                    body: JSON.stringify(shoppingData)
                };
                
                const response = await fetch(`${pythonURI}/api/itinerary/section/shopping`, requestOptions);
                
                if (!response.ok) {
                    throw new Error(`API error: ${response.status}`);
                }
                
                const data = await response.json();
                
                if (data.success) {
                    const itinerary = await getItinerary();
                    updateItineraryDisplay(itinerary);
                    updateAddToItineraryButtons();
                    updateShoppingContentItineraryButton();
                    return data.data;
                } else {
                    throw new Error(data.error || 'Failed to update shopping');
                }
            } catch (error) {
                console.error('Error updating shopping in backend:', error);
                const itinerary = await getItinerary();
                itinerary.shopping = shoppingData;
                await saveItinerary(itinerary);
                return itinerary;
            }
        }

        async function clearItinerary() {
            if (confirm('Are you sure you want to clear your entire itinerary?')) {
                try {
                    const requestOptions = {
                        ...fetchOptions,
                        method: 'DELETE',
                        credentials: 'include'
                    };
                    
                    const response = await fetch(`${pythonURI}/api/itinerary/clear`, requestOptions);
                    
                    if (!response.ok) {
                        throw new Error(`API error: ${response.status}`);
                    }
                    
                    const data = await response.json();
                    
                    if (data.success) {
                        localStorage.removeItem('nycItinerary');
                        location.reload();
                    } else {
                        throw new Error(data.error || 'Failed to clear itinerary');
                    }
                } catch (error) {
                    console.error('Error clearing itinerary in backend:', error);
                    localStorage.removeItem('nycItinerary');
                    location.reload();
                }
            }
        }

        function updateItineraryDisplay(itinerary) {
            // Update trip info
            if (itinerary.tripInfo) {
                if (typeof itinerary.tripInfo === 'object') {
                    document.getElementById('tripDatesValue').innerHTML =
                        `${itinerary.tripInfo.month || ''} ${itinerary.tripInfo.startDate || ''} - ${itinerary.tripInfo.endDate || ''}`;
                } else {
                    document.getElementById('tripDatesValue').innerHTML = itinerary.tripInfo;
                }
                document.getElementById('tripInfoItem').classList.remove('incomplete');
            } else {
                document.getElementById('tripDatesValue').innerHTML = '<span class="itinerary-empty">Not set yet</span>';
                document.getElementById('tripInfoItem').classList.add('incomplete');
            }

            // Update breakfast
            if (itinerary.breakfast) {
                if (typeof itinerary.breakfast === 'object') {
                    document.getElementById('breakfastValue').textContent = itinerary.breakfast.name || 'Breakfast selected';
                } else {
                    document.getElementById('breakfastValue').textContent = itinerary.breakfast;
                }
                document.getElementById('breakfastItem').classList.remove('incomplete');
            } else {
                document.getElementById('breakfastValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
                document.getElementById('breakfastItem').classList.add('incomplete');
            }

            // Update landmarks
            if (itinerary.landmarks) {
                if (typeof itinerary.landmarks === 'object') {
                    document.getElementById('landmarksValue').textContent = itinerary.landmarks.name || 'Landmark selected';
                } else {
                    document.getElementById('landmarksValue').textContent = itinerary.landmarks;
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
                    document.getElementById('shoppingValue').textContent = itinerary.shopping;
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
                    document.getElementById('broadwayValue').textContent = itinerary.broadway;
                }
                document.getElementById('broadwayItem').classList.remove('incomplete');
            } else {
                document.getElementById('broadwayValue').innerHTML = '<span class="itinerary-empty">Not selected</span>';
                document.getElementById('broadwayItem').classList.add('incomplete');
            }
        }

        function toggleItineraryTracker() {
            const tracker = document.getElementById('itineraryTracker');
            tracker.classList.toggle('hidden');
        }

        // UPDATED: Add shopping center to itinerary (center only, no gender)
        async function addShoppingCenterToItinerary(centerId, event) {
            if (event) event.stopPropagation();
            
            const center = shoppingCenters[centerId];
            const shoppingData = {
                center: center.name,
                gender: null,
                selected_at: new Date().toISOString(),
                center_id: centerId
            };
            
            try {
                await updateShoppingInItinerary(shoppingData);
                
                // Update button state
                const btn = document.getElementById(`add-${centerId}`);
                const originalHTML = btn.innerHTML;
                btn.classList.add('added');
                btn.innerHTML = '<span>✓</span> Added to Itinerary';
                btn.disabled = true;
                
                // Revert button after 2 seconds
                setTimeout(() => {
                    btn.classList.add('added');
                    btn.innerHTML = '<span>✓</span> Added to Itinerary';
                    btn.disabled = true;
                }, 2000);
                
            } catch (error) {
                console.error('Failed to save shopping center to itinerary:', error);
                alert('Failed to save selection. Please try again.');
            }
        }

        // UPDATED: Add full shopping selection to itinerary (with gender)
        async function addShoppingSelectionToItinerary() {
            if (!selectedCenter || !selectedGender) {
                alert('Please select a shopping center and gender first!');
                return;
            }
            
            const center = shoppingCenters[selectedCenter];
            const shoppingData = {
                center: center.name,
                gender: selectedGender === 'women' ? "Women's" : "Men's",
                selected_at: new Date().toISOString(),
                center_id: selectedCenter
            };
            
            // Add outfit items if available
            if (currentSelection && shoppingCenters[selectedCenter][selectedGender]) {
                const wardrobe = shoppingCenters[selectedCenter][selectedGender];
                shoppingData.outfit = {
                    top: wardrobe.top[currentSelection.top].name,
                    bottom: wardrobe.bottom[currentSelection.bottom].name,
                    shoes: wardrobe.shoes[currentSelection.shoes].name
                };
            }
            
            try {
                await updateShoppingInItinerary(shoppingData);
                
                // Update button state
                const btn = document.getElementById('addShoppingToItineraryBtn');
                const originalHTML = btn.innerHTML;
                btn.classList.add('added');
                btn.innerHTML = '✅ Added to Itinerary';
                btn.disabled = true;
                
                // Revert button after 2 seconds
                setTimeout(() => {
                    btn.classList.add('added');
                    btn.innerHTML = '✅ Added to Itinerary';
                    btn.disabled = true;
                }, 2000);
                
            } catch (error) {
                console.error('Failed to save shopping selection to itinerary:', error);
                alert('Failed to save selection. Please try again.');
            }
        }

        async function updateAddToItineraryButtons() {
            try {
                const itinerary = await getItinerary();
                const currentShopping = itinerary.shopping;
                
                // Reset all center buttons first
                const centerIds = ['east-river', 'macys', 'soho', 'columbus'];
                centerIds.forEach(centerId => {
                    const btn = document.getElementById(`add-${centerId}`);
                    if (btn) {
                        btn.classList.remove('added');
                        btn.innerHTML = '<span>✅</span> Add to Itinerary';
                        btn.disabled = false;
                    }
                });
                
                // If there's shopping in the itinerary, mark that specific center button
                if (currentShopping && currentShopping.center) {
                    let centerId = '';
                    if (currentShopping.center.includes('East River')) centerId = 'east-river';
                    else if (currentShopping.center.includes("Macy's")) centerId = 'macys';
                    else if (currentShopping.center.includes('SoHo')) centerId = 'soho';
                    else if (currentShopping.center.includes('Columbus')) centerId = 'columbus';
                    
                    if (centerId) {
                        const btn = document.getElementById(`add-${centerId}`);
                        if (btn) {
                            btn.classList.add('added');
                            btn.innerHTML = '<span>✓</span> Added to Itinerary';
                            btn.disabled = true;
                        }
                    }
                }
            } catch (error) {
                console.error('Error updating add buttons:', error);
            }
        }

        async function updateShoppingContentItineraryButton() {
            const btn = document.getElementById('addShoppingToItineraryBtn');
            
            if (!selectedCenter || !selectedGender) {
                if (btn) btn.style.display = 'none';
                return;
            }
            
            try {
                const itinerary = await getItinerary();
                const center = shoppingCenters[selectedCenter];
                const currentGender = selectedGender === 'women' ? "Women's" : "Men's";
                
                // Check if this specific shopping selection is already in the itinerary
                if (itinerary.shopping && 
                    itinerary.shopping.center === center.name && 
                    itinerary.shopping.gender === currentGender) {
                    btn.classList.add('added');
                    btn.innerHTML = '✅ Added to Itinerary';
                    btn.disabled = true;
                } else {
                    btn.classList.remove('added');
                    btn.innerHTML = '✅ Add Shopping to My Itinerary';
                    btn.disabled = false;
                }
                
                btn.style.display = 'block';
            } catch (error) {
                console.error('Error updating shopping content button:', error);
                if (btn) {
                    btn.style.display = 'block';
                    btn.classList.remove('added');
                    btn.innerHTML = '✅ Add Shopping to My Itinerary';
                    btn.disabled = false;
                }
            }
        }

        // ============================================
        // SHOPPING JAVASCRIPT (Original code - unchanged)
        // ============================================

        const shoppingCenters = {
            'east-river': {
                name: 'East River Plaza',
                description: 'Affordable fashion & everyday essentials',
                women: {
                    top: [
                        { name: 'Red Long-Sleeve', image: 'https://target.scene7.com/is/image/Target/GUEST_49359324-e894-4de5-8dbf-6503e0661b83?wid=1200&hei=1200&qlt=80' },
                        { name: 'Grey Sweater', image: 'https://target.scene7.com/is/image/Target/GUEST_db9c98bf-5cf5-4892-881b-4d81e4e278c9?wid=1000&hei=1000&qlt=80&fmt=webp' },
                        { name: 'Cream Sweater', image: 'https://target.scene7.com/is/image/Target/GUEST_b6932887-f0a4-4a95-ac72-995aac2e4c2b?wid=1000&hei=1000&qlt=80&fmt=webp' },
                        { name: 'White Hoodie', image: 'https://target.scene7.com/is/image/Target/GUEST_31f5583e-e190-483a-a087-92040e57443b?wid=1200&hei=1200&qlt=80' },
                    ],
                    bottom: [
                        { name: 'Grey Sweats', image: 'https://target.scene7.com/is/image/Target/GUEST_21b65932-7ea1-4e82-92b9-79b19ba0caa4?wid=1000&hei=1000&qlt=80&fmt=webp' },
                        { name: 'Flare Pants', image: 'https://target.scene7.com/is/image/Target/GUEST_dff2f97b-febc-4ca3-9ab5-8d6c78ffc557?wid=1000&hei=1000&qlt=80&fmt=webp' },
                        { name: 'Light Blue Jeans', image: 'https://target.scene7.com/is/image/Target/GUEST_8d88d561-dffe-4dae-a7f9-af9c809f054c?wid=1200&hei=1200&qlt=80' },
                        { name: 'Black Jeans', image: 'https://target.scene7.com/is/image/Target/GUEST_25dca9f0-804e-4952-a8be-0fa54c239050?wid=1200&hei=1200&qlt=80' },
                    ],
                    shoes: [
                        { name: 'White Sneakers', image: 'https://target.scene7.com/is/image/Target/GUEST_220298a7-b188-404a-acfe-4f680957ba68?wid=1200&hei=1200&qlt=80' },
                        { name: 'Reebok', image: 'https://target.scene7.com/is/image/Target/GUEST_72ac4900-d657-473c-a708-192c9e81edef?wid=1200&hei=1200&qlt=80' },
                        { name: 'Red Sneakers', image: 'https://target.scene7.com/is/image/Target/GUEST_89089a42-5009-4794-909a-c8a35da75209?qlt=85&fmt=webp&hei=500&wid=500' },
                        { name: 'Clogs', image: 'https://target.scene7.com/is/image/Target/GUEST_a578e0f7-85df-4cca-8d10-a371d0ef863e?qlt=85&fmt=webp&hei=500&wid=500' }
                    ]
                },
                men: {
                    top: [
                        { name: 'Cream Quarter Zip', image: 'https://target.scene7.com/is/image/Target/GUEST_7231c7a4-45a6-4b1b-b153-8b1fb6b2d834?wid=1200&hei=1200&qlt=80' },
                        { name: 'Black Sweater', image: 'https://target.scene7.com/is/image/Target/GUEST_13e94bdd-f53d-41e6-8682-9f4c8f3d7d9d?qlt=85&fmt=webp&hei=500&wid=500' },
                        { name: 'Black Hoodie', image: 'https://target.scene7.com/is/image/Target/GUEST_d32e3820-0485-4d1e-ae24-ef27ffedd289?wid=1200&hei=1200&qlt=80e' },
                        { name: 'Grey Crewneck', image: 'https://target.scene7.com/is/image/Target/GUEST_e48c1890-4761-482c-9cdf-37908d270950?wid=1200&hei=1200&qlt=80' },
                    ],
                    bottom: [
                        { name: 'Dark Blue Jeans', image: 'https://target.scene7.com/is/image/Target/GUEST_d9cf97d8-2f05-4ef3-af6c-1065b649bf4e?wid=1200&hei=1200&qlt=80' },
                        { name: 'Baggy Utility Pants', image: 'https://target.scene7.com/is/image/Target/GUEST_44c96d3a-3ee5-407c-8035-14d1336bb299?wid=1200&hei=1200&qlt=80' },
                        { name: 'Brown Pants', image: 'https://target.scene7.com/is/image/Target/GUEST_ad55d77f-8054-47a0-bd03-a0483d019352?qlt=85&fmt=webp&hei=500&wid=500' },
                        { name: 'Cargo Pants', image: 'https://target.scene7.com/is/image/Target/GUEST_5209e381-b85d-491d-b66c-fe19ec091349?qlt=85&fmt=webp&hei=500&wid=500' },
                    ],
                    shoes: [
                        { name: 'Brown Shoes', image: 'https://target.scene7.com/is/image/Target/GUEST_9d157095-ebd9-4032-8504-9882ec5f683a?wid=1200&hei=1200&qlt=80' },
                        { name: 'Dockers Men Shoes', image: 'https://target.scene7.com/is/image/Target/GUEST_27f79b0c-c324-4e5c-a61d-b0c8709f6989?wid=1200&hei=1200&qlt=80' },
                        { name: 'White Sneakers', image: 'https://target.scene7.com/is/image/Target/GUEST_1933b21b-f55d-4a14-9f65-4c00fcc80134?qlt=85&fmt=webp&hei=500&wid=500' },
                        { name: 'Leather Shoes', image: 'https://target.scene7.com/is/image/Target/GUEST_4bfb83b0-234a-4283-b2ca-c0b415152535?qlt=85&fmt=webp&hei=500&wid=500' }
                    ]
                }
            },
            'macys': {
                name: "Macy's Herald Square",
                description: 'Classic department store elegance',
                women: {
                    top: [
                        { name: 'White Sweater', image: 'https://slimages.macysassets.com/is/image/MCY/products/6/optimized/26347896_fpx.tif?op_sharpen=1&wid=1500&fit=fit%2C1&fmt=webp' },
                        { name: 'Cream Sweater', image: 'https://slimages.macysassets.com/is/image/MCY/products/6/optimized/31049706_fpx.tif?op_sharpen=1&wid=1500&fit=fit%2C1&fmt=webp' },
                        { name: 'Grey Striped Sweater', image: 'https://slimages.macysassets.com/is/image/MCY/products/6/optimized/31049706_fpx.tif?op_sharpen=1&wid=1500&fit=fit%2C1&fmt=webp' },
                        { name: 'Blue Striped Sweater', image: 'https://slimages.macysassets.com/is/image/MCY/products/6/optimized/34690286_fpx.tif?qlt=85,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=240&hei=293' },
                    ],
                    bottom: [
                        { name: 'Bootcut Jeans', image: 'https://slimages.macysassets.com/is/image/MCY/products/8/optimized/34492948_fpx.tif?op_sharpen=1&wid=1500&fit=fit%2C1&fmt=webp' },
                        { name: 'Blue Baggy Jeans', image: 'https://slimages.macysassets.com/is/image/MCY/products/3/optimized/34816643_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Light Wash Baggy Jeans', image: 'https://slimages.macysassets.com/is/image/MCY/products/8/optimized/25060138_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Black Sweatpants', image: 'https://slimages.macysassets.com/is/image/MCY/products/0/optimized/30437390_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                    ],
                    shoes: [
                        { name: 'Adidas', image: 'https://slimages.macysassets.com/is/image/MCY/products/3/optimized/31271463_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Ugg Tasman', image: 'https://slimages.macysassets.com/is/image/MCY/products/8/optimized/33636358_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'White Platform Sneakers', image: 'https://slimages.macysassets.com/is/image/MCY/products/4/optimized/24150204_fpx.tif?op_sharpen=1&wid=700&fit=fit,1&fmt=webp' },
                        { name: 'Nikes', image: 'https://slimages.macysassets.com/is/image/MCY/products/1/optimized/28841871_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' }
                    ]
                },
                men: {
                    top: [
                        { name: 'Blue Sweater', image: 'https://slimages.macysassets.com/is/image/MCY/products/1/optimized/34421941_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Cream Hoodie', image: 'https://slimages.macysassets.com/is/image/MCY/products/9/optimized/28131229_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Red Quarter-Zip', image: 'https://slimages.macysassets.com/is/image/MCY/products/0/optimized/34871670_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Black Sweater', image: 'https://slimages.macysassets.com/is/image/MCY/products/3/optimized/34876543_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' }
                    ],
                    bottom: [
                        { name: 'Medium Blue Jeans', image: 'https://slimages.macysassets.com/is/image/MCY/products/1/optimized/33255971_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Black Jeans', image: 'https://slimages.macysassets.com/is/image/MCY/products/1/optimized/27686001_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Light Blue Jeans', image: 'https://slimages.macysassets.com/is/image/MCY/products/2/optimized/31838162_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Dark Blue Jeans', image: 'https://slimages.macysassets.com/is/image/MCY/products/4/optimized/33159924_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                    ],
                    shoes: [
                        { name: 'White Sneakers', image: 'https://slimages.macysassets.com/is/image/MCY/products/9/optimized/32120719_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Adidas', image: 'https://slimages.macysassets.com/is/image/MCY/products/2/optimized/34109882_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Brown Sneaker', image: 'https://slimages.macysassets.com/is/image/MCY/products/4/optimized/31392084_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' },
                        { name: 'Black and White Nikes', image: 'https://slimages.macysassets.com/is/image/MCY/products/6/optimized/32221626_fpx.tif?qlt=55,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=webp&wid=684&hei=834' }
                    ]
                }
            },
            'soho': {
                name: 'SoHo Center',
                description: 'Trendy & fashion-forward styles',
                women: {
                    top: [
                        { name: 'Cardigan', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw25212bff/hi-res/4KC1263050010T.jpg?sw=720' },
                        { name: 'Grey Sweater', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw7dfae91c/hi-res/UKC4251028080T.jpg?sw=720' },
                        { name: 'Pink Cardigan', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwd8fd1eca/hi-res/1KC3243037680T.jpg?sw=720' },
                        { name: 'Black Sweater', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwa9cf105c/hi-res/1KC3231017001T.jpg?sw=720' },
                    ],
                    bottom: [
                        { name: 'Light Blue Jeans', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwa30a5a88/hi-res/4DC3254819470CT.jpg?sw=720' },
                        { name: 'Black Jeans', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwf91ee7f1/hi-res/4DC1264112031T.jpg?sw=720' },
                        { name: 'Dark Blue Jeans', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwfb11e5f1/hi-res/4DC1264967401B.jpg?sw=680' },
                        { name: 'Denim Skirt', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwf2670642/hi-res/4DC1265107400CT.jpg?sw=720' },
                    ],
                    shoes: [
                        { name: 'Black Heels', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwf3da7778/hi-res/30321S033001F.jpg?sw=720' },
                        { name: 'Black Sandals', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw41bf844d/hi-res/30325S002001F.jpg?sw=1440' },
                        { name: 'Black Loafers', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw4c201ad2/hi-res/30325F004206F.jpg?sw=720' },
                        { name: 'White Sneaker', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwa777f891/hi-res/30325SN033120F.jpg?sw=720' }
                    ]
                },
                men: {
                    top: [
                        { name: 'Cream Zip-Up', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwcaaa8fbc/hi-res/UCC1262300216AT.jpg?sw=720' },
                        { name: 'Black Sweater', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw12927071/hi-res/6KC1261118001T.jpg?sw=720' },
                        { name: 'Grey Quarter Zip', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwbfcc8de1/hi-res/UCC4251864029CT.jpg?sw=720' },
                        { name: 'Grey Sweater', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw76d8db4e/hi-res/6KC1261118085T.jpg?sw=720' },
                    ],
                    bottom: [
                        { name: 'Black Jeans', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw716b5904/hi-res/6DC1264959020AT.jpg?sw=720' },
                        { name: 'Cream Sweats', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw94e4ef28/hi-res/UCC1264441216AT.jpg?sw=720' },
                        { name: 'Dark Blue Jeans', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw872cf4a6/hi-res/6DC3254830473T.jpg?sw=720' },
                        { name: 'Black Sweatpants', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dwa30c8921/hi-res/UCC4254432001T.jpg?sw=720' },
                    ],
                    shoes: [
                        { name: 'Green Jordans', image: 'https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/e90ccffa-5cde-4a15-8eb1-490519e16aa1/WMNS+AIR+JORDAN+1+RETRO+HI+OG.png' },
                        { name: 'White Sneakers', image: 'https://www.alexanderwang.com/dw/image/v2/BCCC_PRD/on/demandware.static/-/Sites-master/default/dw3d9190ab/hi-res/30325SN034120F.jpg?sw=720' },
                        { name: 'Brown Sneakers', image: 'https://kizik.com/cdn/shop/files/MVEG2501_Mens_Vegas_2_Mole-Whitecap_Gray_Lateral-2048x2048-ae00118.png?v=1756927347&width=600' },
                    ]
                }
            },
            'columbus': {
                name: 'Columbus Circle',
                description: 'Luxury designer boutiques',
                women: {
                    top: [
                        { name: 'Cream Knit Sweater', image: 'https://image.hm.com/assets/hm/5a/a9/5aa96ad24ca61307f2fd557199d2c37316495b72.jpg?imwidth=2160' },
                        { name: 'Cream Cardigan', image: 'https://image.hm.com/assets/hm/49/5a/495a728ace736a9858fc0c58d4fd53c1301499c6.jpg?imwidth=2160' },
                        { name: 'Long-Sleaved Jersey Top', image: 'https://image.hm.com/assets/hm/fd/b0/fdb01fd25e177172f290cf7c3cd8b548591f6eb1.jpg?imwidth=2160' },
                        { name: 'Oversized Boatneck Sweater', image: 'https://image.hm.com/assets/hm/07/c8/07c86252327a71cd0a1b97c6b5c6cbaba3f16873.jpg?imwidth=2160' },
                        { name: 'Black Hoodie', image: 'https://image.hm.com/assets/hm/67/c6/67c65b95233364e5c312e4fc7f36eda04251323d.jpg?imwidth=657' }
                    ],
                    bottom: [
                        { name: 'Light Blue Baggy Jeans', image: 'https://image.hm.com/assets/hm/f8/a1/f8a167f63390ecd1df2bc08a500f54a08acac22e.jpg?imwidth=1536' },
                        { name: 'Black Pleated Mini Skirt', image: 'https://image.hm.com/assets/hm/0e/ea/0eea470eab0ef124cc191d3b1e2c8b04e3d4cf80.jpg?imwidth=396' },
                        { name: 'Flared Low Jeans', image: 'https://image.hm.com/assets/hm/1b/67/1b67cbc902c9736c9fa89eb2ebc548062731eb16.jpg?imwidth=657' },
                        { name: 'Dressy Mini Skirt', image: 'https://image.hm.com/assets/hm/4d/1d/4d1d5e2b834d9afe152d7169ae98e8ed77136244.jpg?imwidth=657' },
                        { name: 'Dark Blue Baggy Jeans', image: 'https://image.hm.com/assets/hm/1c/92/1c924704a2fd8de7965831f055c1f421f4e4a02e.jpg?imwidth=1536' }
                    ],
                    shoes: [
                        { name: 'Sneakers', image: 'https://image.hm.com/assets/hm/b8/9e/b89ed253c72a9f66549c31c868340d52e9988477.jpg?imwidth=2160' },
                        { name: 'Warm-lined Boots', image: 'https://image.hm.com/assets/hm/9b/90/9b90c6cbf772d2d8195e0b4359e36d01174147fa.jpg?imwidth=2160' },
                        { name: 'Birkenstock Sandals', image: 'https://cdn.fleetfeet.com/productTile/products/151183_left.jpg' },
                        { name: 'Heeled Slingbacks', image: 'https://image.hm.com/assets/hm/df/2b/df2b10db22e3561154471fafc8ff422098309334.jpg?imwidth=657' }
                    ]
                },
                men: {
                    top: [
                        { name: 'Black Sweater', image: 'https://image.hm.com/assets/hm/9a/77/9a77c0f49d87abe822edcabd76cb25d7ff41044e.jpg?imwidth=2160' },
                        { name: 'Loose Fit Half-Zip Sweatshirt', image: 'https://image.hm.com/assets/hm/1d/9c/1d9cad8c0834c59489037805c885fb5d5a240e2f.jpg?imwidth=2160' },
                        { name: 'Loose Fit Scuba Hoodie', image: 'https://image.hm.com/assets/hm/75/fb/75fb2c3e06bad89c2755f7f76cae3485bfd559d8.jpg?imwidth=2160' },
                        { name: 'Regular-Fit Rib-Knit Cotton Sweater', image: 'https://image.hm.com/assets/hm/e9/94/e99416b0bac9e59a6e3480cba0a242fb44e8db8c.jpg?imwidth=2160' },
                    ],
                    bottom: [
                        { name: 'Baggy Darted Jeans', image: 'https://image.hm.com/assets/hm/89/d8/89d87ebd0a209c702474f3f79c6bbeb24d72d451.jpg?imwidth=657' },
                        { name: 'Light Blue Jeans', image: 'https://image.hm.com/assets/hm/db/5c/db5ca18fca0db5d6a8b6a05a131601a2c0780507.jpg?imwidth=657' },
                        { name: 'Fairfax Baggy Jeans', image: 'https://image.hm.com/assets/hm/dc/98/dc987f075569a9e8afb546dd6288344c6cc7a614.jpg?imwidth=2160' },
                        { name: 'Loose-Fit Sweatpants', image: 'https://image.hm.com/assets/hm/ec/ed/ecedfe5492def4518cbd18ba0946a0215b48a1fe.jpg?imwidth=657' }
                    ],
                    shoes: [
                        { name: 'Brown Sneakers', image: 'https://image.hm.com/assets/hm/d2/80/d280bb63e27922efc6a171e0fb14b93f407abced.jpg?imwidth=2160' },
                        { name: 'Chunky Sneakers', image: 'https://image.hm.com/assets/hm/91/8e/918e07a0ef4eec4b511b269b208a83a790d10dd5.jpg?imwidth=2160' },
                        { name: 'White Sneakers', image: 'https://image.hm.com/assets/hm/fb/8d/fb8d78018ef31d1891a4e96c7ad7b0bb80348db8.jpg?imwidth=2160' }
                    ]
                }
            }
        };

        let selectedCenter = null;
        let selectedGender = null;
        let currentSelection = { top: 0, bottom: 0, shoes: 0 };

        function selectCenter(centerId) {
            selectedCenter = centerId;
            document.getElementById('center-selection-screen').classList.add('hidden');
            document.getElementById('gender-selection-screen').classList.remove('hidden');
            
            const center = shoppingCenters[centerId];
            document.getElementById('selected-center-name').textContent = '📍 ' + center.name;
            document.getElementById('selected-center-desc').textContent = center.description;
        }

        function selectGender(gender) {
            selectedGender = gender;
            document.getElementById('gender-selection-screen').classList.add('hidden');
            document.getElementById('shopping-content').classList.remove('hidden');
            
            const center = shoppingCenters[selectedCenter];
            document.getElementById('shopping-area-title').textContent = center.name;
            document.getElementById('shopping-area-subtitle').textContent = `Shopping ${gender === 'women' ? "Women's" : "Men's"} Fashion`;
            document.getElementById('section-title').textContent = gender === 'women' ? "Her Look" : "His Look";
            
            updateDisplay();
            updateShoppingContentItineraryButton();
        }

        function backToCenter() {
            selectedCenter = null;
            selectedGender = null;
            currentSelection = { top: 0, bottom: 0, shoes: 0 };
            document.getElementById('center-selection-screen').classList.remove('hidden');
            document.getElementById('gender-selection-screen').classList.add('hidden');
            document.getElementById('shopping-content').classList.add('hidden');
            updateShoppingContentItineraryButton();
        }

        function backToGender() {
            selectedGender = null;
            currentSelection = { top: 0, bottom: 0, shoes: 0 };
            document.getElementById('gender-selection-screen').classList.remove('hidden');
            document.getElementById('shopping-content').classList.add('hidden');
            updateShoppingContentItineraryButton();
        }

        function updateDisplay() {
            if (!selectedCenter || !selectedGender) return;

            const wardrobe = shoppingCenters[selectedCenter][selectedGender];
            const topItem = wardrobe.top[currentSelection.top];
            const bottomItem = wardrobe.bottom[currentSelection.bottom];
            const shoesItem = wardrobe.shoes[currentSelection.shoes];

            document.getElementById('top-display').innerHTML = `<img src="${topItem.image}" alt="${topItem.name}">`;
            document.getElementById('bottom-display').innerHTML = `<img src="${bottomItem.image}" alt="${bottomItem.name}">`;
            document.getElementById('shoes-display').innerHTML = `<img src="${shoesItem.image}" alt="${shoesItem.name}">`;

            document.getElementById('top-name').textContent = topItem.name;
            document.getElementById('bottom-name').textContent = bottomItem.name;
            document.getElementById('shoes-name').textContent = shoesItem.name;

            const phrases = [
                "Looking great!",
                "Perfect choice!",
                "Stylish!",
                "Fashion forward!",
                "Excellent taste!",
                "Love it!"
            ];
            const randomPhrase = phrases[Math.floor(Math.random() * phrases.length)];
            document.getElementById('status').textContent = randomPhrase;
        }

        function nextItem(category) {
            const wardrobe = shoppingCenters[selectedCenter][selectedGender];
            currentSelection[category] = (currentSelection[category] + 1) % wardrobe[category].length;
            updateDisplay();
        }

        function prevItem(category) {
            const wardrobe = shoppingCenters[selectedCenter][selectedGender];
            currentSelection[category] = (currentSelection[category] - 1 + wardrobe[category].length) % wardrobe[category].length;
            updateDisplay();
        }

        function randomOutfit() {
            const wardrobe = shoppingCenters[selectedCenter][selectedGender];
            currentSelection.top = Math.floor(Math.random() * wardrobe.top.length);
            currentSelection.bottom = Math.floor(Math.random() * wardrobe.bottom.length);
            currentSelection.shoes = Math.floor(Math.random() * wardrobe.shoes.length);
            updateDisplay();
            document.getElementById('status').textContent = "✨ Surprise! ✨";
        }

        function saveOutfit() {
            const wardrobe = shoppingCenters[selectedCenter][selectedGender];
            const outfit = {
                center: shoppingCenters[selectedCenter].name,
                gender: selectedGender,
                top: wardrobe.top[currentSelection.top].name,
                bottom: wardrobe.bottom[currentSelection.bottom].name,
                shoes: wardrobe.shoes[currentSelection.shoes].name,
                topImage: wardrobe.top[currentSelection.top].image,
                bottomImage: wardrobe.bottom[currentSelection.bottom].image,
                shoesImage: wardrobe.shoes[currentSelection.shoes].image
            };
            try {
                localStorage.setItem('savedOutfit', JSON.stringify(outfit));
                console.log('savedOutfit stored:', localStorage.getItem('savedOutfit'));
                document.getElementById('status').textContent = "💾 Outfit saved! Redirecting to post...";
                setTimeout(() => { window.location.href = '/student/new-york/shopping/post/'; }, 600);
            } catch (e) {
                console.error('Failed to save outfit:', e);
                document.getElementById('status').textContent = "❌ Failed to save outfit locally.";
            }
        }

        // Initialize on page load
        document.addEventListener('DOMContentLoaded', async () => {
            await initItinerary();
        });

        // Make functions available globally
        window.navigateTo = navigateTo;
        window.toggleItineraryTracker = toggleItineraryTracker;
        window.clearItinerary = clearItinerary;
        window.addShoppingCenterToItinerary = addShoppingCenterToItinerary;
        window.addShoppingSelectionToItinerary = addShoppingSelectionToItinerary;
        window.selectCenter = selectCenter;
        window.selectGender = selectGender;
        window.backToCenter = backToCenter;
        window.backToGender = backToGender;
        window.nextItem = nextItem;
        window.prevItem = prevItem;
        window.randomOutfit = randomOutfit;
        window.saveOutfit = saveOutfit;
    </script>
</body>
</html>