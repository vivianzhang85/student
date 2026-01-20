---
layout: post
title: "Step 1 Breakfast"
description: "Breakfast time hits, and in NYC that means one thing: pick your spot and dive in."
permalink: /new-york/breakfast/
parent: "Analytics/Admin"
team: "Insightful Innovators"
submodule: 1
author: "Insightful Innocators"
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
      margin: 0;
      padding: 20px;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
      color: white;
      min-height: 100vh;
    }
    
    .container {
      max-width: 1200px;
      margin: 0 auto;
    }
    
    .header {
      text-align: center;
      margin-bottom: 40px;
      padding: 20px;
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
    
    .restaurant-card {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 15px;
      padding: 25px;
      margin: 20px 0;
      border: 2px solid transparent;
      transition: all 0.3s;
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
      display: flex;
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
    
    .menu-header {
      background: linear-gradient(135deg, #f59e0b, #f97316);
      padding: 30px;
      border-radius: 15px;
      text-align: center;
      margin-bottom: 20px;
    }
    
    /* Live Data Indicators */
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
    
    .restaurant-cuisine {
      background: rgba(139, 92, 246, 0.2);
      color: #c4b5fd;
      padding: 5px 10px;
      border-radius: 12px;
      font-size: 0.8rem;
    }
    
    /* Interactive Selection */
    .location-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin: 20px 0;
    }
    
    .location-card {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 15px;
      padding: 25px;
      cursor: pointer;
      transition: all 0.3s;
      border: 2px solid transparent;
    }
    
    .location-card:hover {
      transform: translateY(-5px);
      border-color: #f59e0b;
      box-shadow: 0 10px 30px rgba(245, 158, 11, 0.3);
    }
    
    .location-card h3 {
      margin: 0 0 10px 0;
      font-size: 24px;
      color: #f59e0b;
    }
    
    /* Navigation Button Styles */
    .nav-to-landmarks {
      margin-top: 50px;
      margin-bottom: 50px;
      text-align: center;
      padding: 40px;
      background: rgba(255, 215, 0, 0.1);
      border-radius: 15px;
      border: 2px solid #ffd700;
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
    
    /* Responsive */
    @media (max-width: 768px) {
      .location-grid,
      .menu-grid {
        grid-template-columns: 1fr;
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
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🍳 NYC Breakfast Explorer</h1>
      <p>Choose your perfect morning meal with live restaurant hours</p>
      <div class="live-data-indicator" id="apiStatus">🔌 Connecting to API...</div>
    </div>

    <!-- Live Hours Section -->
    <div class="live-hours-container">
      <h2>🕒 Live Restaurant Hours</h2>
      <div id="liveHoursContainer">
        <div class="hours-loading">
          <div class="live-loading-spinner"></div>
          <div>Fetching live restaurant hours...</div>
        </div>
      </div>
      <button class="btn refresh-btn" onclick="fetchAllBreakfastHours()">
        <span>🔄</span> Refresh All Hours
      </button>
    </div>

    <!-- Restaurant Selection Grid -->
    <div id="step1" class="step active">
      <h2 style="text-align: center; margin-bottom: 30px; color: #fbbf24;">Choose Your Breakfast Spot</h2>
      <div class="location-grid">
        <div class="location-card" onclick="selectRestaurant('sarabeths')">
          <h3>Sarabeths</h3>
          <div class="badge">Elegant & Classic</div>
          <p>📍 Upper West Side</p>
          <p>A beloved NYC institution known for its legendary homemade jams and elegant brunch classics. Perfect for a refined, upscale breakfast experience.</p>
          <div class="restaurant-cuisine">Breakfast & Pastries</div>
        </div>
        <div class="location-card" onclick="selectRestaurant('jacks')">
          <h3>Jack's Wife Frida</h3>
          <div class="badge">Bold & Trendy</div>
          <p>📍 SoHo</p>
          <p>Mediterranean-inspired breakfast with bold Mexican flavors. A trendy spot with colorful dishes and creative twists on morning favorites.</p>
          <div class="restaurant-cuisine">Mediterranean</div>
        </div>
        <div class="location-card" onclick="selectRestaurant('ess')">
          <h3>Ess a Bagel</h3>
          <div class="badge">Authentic & Iconic</div>
          <p>📍 Midtown East</p>
          <p>The ultimate NYC bagel experience. Hand-rolled, kettle-boiled bagels that are crispy outside and pillowy inside. A true New York classic.</p>
          <div class="restaurant-cuisine">Bagels & Deli</div>
        </div>
        <div class="location-card" onclick="selectRestaurant('shuka')">
          <h3>Shuka</h3>
          <div class="badge">Fresh & Vibrant</div>
          <p>📍 East Village</p>
          <p>Modern Mediterranean cuisine with Israeli breakfast specialties. Fresh, vibrant dishes featuring tahini, hummus, and perfectly spiced shakshuka.</p>
          <div class="restaurant-cuisine">Mediterranean</div>
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
        <div id="restaurantHours"></div>
        <button class="btn refresh-btn" onclick="refreshCurrentRestaurant()">
          <span>🔄</span> Update Live Hours
        </button>
      </div>
      
      <h3 style="margin: 30px 0 20px 0; color: #fbbf24;">Menu Highlights</h3>
      <div class="menu-grid" id="menuGrid"></div>
      
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
      <a href="{{ site.baseurl }}/new-york/landmarks/" class="landmarks-btn">
        🗽 Explore NYC Landmarks
      </a>
    </div>
  </div>

  <script>
    // ============================================
    // LIVE BREAKFAST HOURS INTEGRATION
    // ============================================

    // API Configuration
    const API_BASE_URL = 'http://localhost:8587/api/breakfast';
    
    // Restaurant mapping
    const RESTAURANT_MAP = {
      'sarabeths': { name: "Sarabeth's", endpoint: 'sarabeths' },
      'jacks': { name: "Jack's Wife Freda", endpoint: 'jacks' },
      'ess': { name: "Ess-a-Bagel", endpoint: 'bagel' },
      'shuka': { name: "Shuka", endpoint: 'shuka' }
    };

    // Menu data
    const MENU_DATA = {
      sarabeths: {
        name: "Sarabeth's",
        location: "Upper West Side",
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
        items: [
          {name: 'Israeli Breakfast', price: 22, desc: 'Eggs, hummus, tahini, salad'},
          {name: 'Halloumi Scramble', price: 19, desc: 'With grilled halloumi cheese'},
          {name: 'Quinoa Bowl', price: 17, desc: 'Roasted vegetables and egg'},
          {name: 'Turkish Coffee', price: 5, desc: 'Strong and aromatic'}
        ]
      }
    };

    let currentRestaurant = null;
    let cart = [];

    // ============================================
    // API FUNCTIONS
    // ============================================

    // Test API connection
    async function testAPIConnection() {
      try {
        const response = await fetch(`${API_BASE_URL}/test`);
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
        statusIndicator.textContent = '❌ API Offline';
        statusIndicator.className = 'live-data-indicator offline';
        return false;
      }
    }

    // Fetch hours for a specific restaurant
    async function fetchRestaurantHours(restaurantKey) {
      const restaurant = RESTAURANT_MAP[restaurantKey];
      if (!restaurant) return null;

      try {
        const response = await fetch(`${API_BASE_URL}/${restaurant.endpoint}`);
        const data = await response.json();
        
        if (data.success) {
          return data.data;
        } else {
          console.error(`Error fetching ${restaurant.name}:`, data.error);
          return null;
        }
      } catch (error) {
        console.error(`Network error for ${restaurant.name}:`, error);
        return null;
      }
    }

    // Fetch all restaurant hours
    async function fetchAllBreakfastHours() {
      const container = document.getElementById('liveHoursContainer');
      const originalContent = container.innerHTML;
      
      container.innerHTML = `
        <div class="hours-loading">
          <div class="live-loading-spinner"></div>
          <div>Scraping live hours from restaurant websites...</div>
        </div>
      `;
      
      try {
        const response = await fetch(API_BASE_URL);
        const data = await response.json();
        
        if (data.success && data.data) {
          let html = '';
          
          data.data.forEach(restaurant => {
            const hours = restaurant.hours || {};
            
            html += `
              <div class="restaurant-card">
                <h3>${restaurant.restaurant}</h3>
                <p><strong>📍 Location:</strong> ${restaurant.location}</p>
                <div class="hours-display">
                  ${Object.entries(hours).map(([day, time]) => `
                    <div class="day-hour">
                      <span class="day">${day}:</span>
                      <span class="time">${time}</span>
                    </div>
                  `).join('')}
                </div>
                <div class="update-note">
                  <strong>Source:</strong> ${restaurant.source || 'API'} 
                  | <strong>Last Updated:</strong> ${new Date().toLocaleTimeString()}
                </div>
              </div>
            `;
          });
          
          container.innerHTML = html;
          
          // Highlight animation
          container.style.animation = "pulse 1s ease";
          setTimeout(() => container.style.animation = "", 1000);
          
        } else {
          throw new Error('No data received');
        }
      } catch (error) {
        console.error('Error fetching all hours:', error);
        container.innerHTML = originalContent;
        
        // Show fallback hours
        const fallbackHours = `
          <div class="restaurant-card">
            <h3>Jack's Wife Freda</h3>
            <p>📍 SoHo, New York</p>
            <div class="hours-display">
              <div class="day-hour"><span class="day">Monday - Thursday:</span><span class="time">8:00 AM - 10:00 PM</span></div>
              <div class="day-hour"><span class="day">Friday - Sunday:</span><span class="time">9:00 AM - 11:00 PM</span></div>
            </div>
            <div class="update-note">⚠️ Showing fallback hours - API connection failed</div>
          </div>
        `;
        
        container.innerHTML = fallbackHours;
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
      if (n === 4) showReview();
    }

    async function selectRestaurant(restaurantKey) {
      currentRestaurant = restaurantKey;
      
      // Update restaurant details
      const restaurantData = MENU_DATA[restaurantKey];
      document.getElementById('restaurantName').textContent = restaurantData.name;
      document.getElementById('restaurantLocation').textContent = `📍 ${restaurantData.location}`;
      
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
      const originalContent = hoursContainer.innerHTML;
      
      // Show loading
      hoursContainer.innerHTML = `
        <div class="hours-loading">
          <div class="live-loading-spinner"></div>
          <div>Fetching live hours for ${restaurantData.name}...</div>
        </div>
      `;
      
      try {
        const hoursData = await fetchRestaurantHours(currentRestaurant);
        
        if (hoursData) {
          let hoursHtml = `<div class="hours-display">`;
          
          if (hoursData.hours && typeof hoursData.hours === 'object') {
            Object.entries(hoursData.hours).forEach(([day, time]) => {
              hoursHtml += `
                <div class="day-hour">
                  <span class="day">${day}:</span>
                  <span class="time">${time}</span>
                </div>
              `;
            });
          } else {
            hoursHtml += `<div class="day-hour"><span class="time">${hoursData.hours || 'Hours not available'}</span></div>`;
          }
          
          hoursHtml += `</div>`;
          
          if (hoursData.error) {
            hoursHtml += `<p style="color: #ef4444;">⚠️ Note: ${hoursData.error}</p>`;
          }
          
          hoursHtml += `
            <div class="update-note">
              <strong>Source