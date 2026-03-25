---
layout: post
title: "Step 4 Broadway & Lyrics"
description: "Experience Broadway magic and vote on show lyrics! Choose your show and participate in lyric voting."
permalink: /new-york/broadway/
parent: "Analytics/Admin"
team: "Insightful Innovators"
submodule: 4
author: "Insightful Innovators"
date: 2025-11-20
microblog: true
footer: 
    previous: /new-york/shopping/
    home: /nyc/home/
    next: /new-york/final
---
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🎭 Broadway Show Selector & Lyrics Voting</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #1a1a2e 0%, #0d0d1a 100%);
      color: white;
      min-height: 100vh;
    }

    /* Fixed Sidebar - SAME AS LANDMARKS PAGE */
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

    /* Main Content Area - SHIFTED LEFT */
    .main-content {
      margin-left: 280px; /* Slightly more space from sidebar */
      margin-right: 0; /* Remove right margin */
      padding: 30px 60px 30px 20px; /* Adjusted padding - more on right, less on left */
      min-height: 100vh;
      max-width: 1100px; /* Constrain max width */
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
      border: 2px solid #8b5cf6;
      position: relative;
      overflow: hidden;
    }
    
    .header::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #8b5cf6, #ec4899, #3b82f6);
    }
    
    .header h1 {
      font-size: 48px;
      margin: 0 0 10px 0;
      color: #f0abfc;
      text-shadow: 2px 2px 4px rgba(139, 92, 246, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 15px;
    }
    
    .header p {
      font-size: 1.2rem;
      color: #cbd5e1;
      max-width: 800px;
      margin: 0 auto;
    }
    
    .tab-container {
      display: flex;
      gap: 10px;
      margin: 30px 0;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 15px;
      padding: 10px;
    }
    
    .tab {
      flex: 1;
      padding: 15px;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      border-radius: 10px;
      color: #cbd5e1;
      font-size: 1.1rem;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.3s;
    }
    
    .tab:hover {
      background: rgba(139, 92, 246, 0.2);
      color: #f0abfc;
    }
    
    .tab.active {
      background: linear-gradient(90deg, #8b5cf6, #7c3aed);
      color: white;
      box-shadow: 0 5px 15px rgba(139, 92, 246, 0.3);
    }
    
    .live-data-container {
      margin: 30px 0;
      padding: 25px;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 15px;
      border-left: 5px solid #8b5cf6;
    }
    
    .live-data-container h2 {
      color: #f0abfc;
      margin-bottom: 20px;
      font-size: 1.8rem;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .date-selector {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
      margin: 20px 0;
    }
    
    .date-card {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 20px;
      text-align: center;
      cursor: pointer;
      transition: all 0.3s;
      border: 2px solid transparent;
    }
    
    .date-card:hover {
      transform: translateY(-5px);
      border-color: #8b5cf6;
      background: rgba(139, 92, 246, 0.1);
    }
    
    .date-card.selected {
      background: rgba(139, 92, 246, 0.2);
      border-color: #f0abfc;
      box-shadow: 0 10px 30px rgba(139, 92, 246, 0.3);
    }
    
    .date-card .date {
      font-size: 1.8rem;
      font-weight: bold;
      color: #f0abfc;
    }
    
    .date-card .day {
      color: #c4b5fd;
      margin-bottom: 5px;
    }
    
    .show-card {
      background: linear-gradient(145deg, rgba(139, 92, 246, 0.1), rgba(0, 0, 0, 0.3));
      border-radius: 15px;
      padding: 25px;
      margin: 20px 0;
      border: 2px solid transparent;
      transition: all 0.3s;
      position: relative;
      overflow: hidden;
    }
    
    .show-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #8b5cf6, #ec4899);
    }
    
    .show-card:hover {
      transform: translateY(-5px);
      border-color: #f0abfc;
      box-shadow: 0 15px 40px rgba(139, 92, 246, 0.4);
    }
    
    .show-card h3 {
      margin: 0 0 15px 0;
      font-size: 28px;
      color: #f0abfc;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .show-badge {
      display: inline-block;
      padding: 5px 15px;
      background: linear-gradient(90deg, #8b5cf6, #7c3aed);
      color: white;
      border-radius: 20px;
      font-size: 12px;
      margin: 10px 0;
      font-weight: bold;
    }
    
    .show-theater {
      color: #c4b5fd;
      margin: 10px 0;
      font-size: 1.1rem;
    }
    
    .show-description {
      line-height: 1.6;
      color: #cbd5e1;
      margin: 15px 0;
    }
    
    .availability-display {
      background: rgba(0, 0, 0, 0.3);
      padding: 25px;
      border-radius: 10px;
      margin: 20px 0;
      border: 1px solid rgba(139, 92, 246, 0.3);
    }
    
    .availability-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid rgba(139, 92, 246, 0.3);
    }
    
    .availability-header h4 {
      color: #f0abfc;
      font-size: 1.3rem;
    }
    
    .price-tag {
      background: linear-gradient(90deg, #10b981, #059669);
      color: white;
      padding: 8px 16px;
      border-radius: 25px;
      font-weight: bold;
      font-size: 1.1rem;
    }
    
    .performance-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
    }
    
    .performance-card {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 20px;
      text-align: center;
      transition: all 0.3s;
      border: 2px solid transparent;
    }
    
    .performance-card:hover {
      transform: scale(1.05);
      border-color: #10b981;
      background: rgba(16, 185, 129, 0.1);
    }
    
    .performance-card.sold-out {
      background: rgba(239, 68, 68, 0.1);
      opacity: 0.7;
    }
    
    .performance-card.sold-out:hover {
      border-color: #ef4444;
    }
    
    .performance-time {
      font-size: 1.5rem;
      font-weight: bold;
      color: #f0abfc;
      margin-bottom: 10px;
    }
    
    .performance-price {
      color: #10b981;
      font-weight: bold;
      font-size: 1.2rem;
      margin: 10px 0;
    }
    
    .performance-status {
      padding: 5px 10px;
      border-radius: 15px;
      font-size: 0.8rem;
      font-weight: bold;
      margin-top: 10px;
    }
    
    .status-available {
      background: rgba(16, 185, 129, 0.2);
      color: #10b981;
    }
    
    .status-sold-out {
      background: rgba(239, 68, 68, 0.2);
      color: #ef4444;
    }
    
    .status-limited {
      background: rgba(245, 158, 11, 0.2);
      color: #f59e0b;
    }
    
    .btn {
      background: linear-gradient(90deg, #8b5cf6, #7c3aed);
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
      box-shadow: 0 5px 15px rgba(139, 92, 246, 0.4);
    }
    
    .btn-primary {
      background: linear-gradient(90deg, #ec4899, #db2777);
      width: 100%;
      margin-top: 20px;
      justify-content: center;
    }
    
    .btn-secondary {
      background: linear-gradient(90deg, #3b82f6, #2563eb);
    }
    
    .refresh-btn {
      background: linear-gradient(90deg, #10b981, #059669);
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
    
    .selection-section {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 15px;
      padding: 30px;
      margin: 20px 0;
    }
    
    .selection-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }
    
    .selection-card {
      background: rgba(0, 0, 0, 0.3);
      border-radius: 12px;
      padding: 20px;
      transition: all 0.3s;
      border: 2px solid transparent;
      cursor: pointer;
    }
    
    .selection-card:hover {
      transform: translateY(-5px);
      border-color: #8b5cf6;
      background: rgba(139, 92, 246, 0.1);
    }
    
    .selection-card.selected {
      background: rgba(139, 92, 246, 0.2);
      border-color: #f0abfc;
      box-shadow: 0 10px 30px rgba(139, 92, 246, 0.3);
    }
    
    .selection-card h4 {
      margin: 0 0 10px 0;
      color: #f0abfc;
      font-size: 1.3rem;
    }
    
    .ticket-quantity {
      display: flex;
      align-items: center;
      gap: 15px;
      margin: 20px 0;
      padding: 20px;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 10px;
    }
    
    .quantity-control {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .quantity-btn {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: #8b5cf6;
      color: white;
      border: none;
      font-size: 1.5rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    .quantity-btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
    
    .quantity-display {
      font-size: 1.8rem;
      font-weight: bold;
      color: #f0abfc;
      min-width: 50px;
      text-align: center;
    }
    
    .total-price {
      font-size: 28px;
      text-align: right;
      margin: 20px 0;
      color: #f0abfc;
      padding: 20px;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 10px;
    }
    
    .show-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
      padding-bottom: 15px;
      border-bottom: 2px solid rgba(139, 92, 246, 0.3);
    }
    
    .show-type {
      background: linear-gradient(90deg, #ec4899, #db2777);
      color: white;
      padding: 5px 10px;
      border-radius: 12px;
      font-size: 0.8rem;
    }
    
    .live-data-indicator {
      display: inline-block;
      padding: 8px 16px;
      background: #8b5cf6;
      color: white;
      border-radius: 4px;
      font-size: 0.9rem;
      margin-left: 10px;
      animation: pulse 2s infinite;
    }
    
    .live-data-indicator.updating {
      background: #f59e0b;
    }
    
    .live-data-indicator.offline {
      background: #ef4444;
    }
    
    .availability-loading {
      text-align: center;
      padding: 40px;
      color: #94a3b8;
    }
    
    .live-loading-spinner {
      width: 40px;
      height: 40px;
      border: 4px solid rgba(255, 255, 255, 0.1);
      border-top: 4px solid #8b5cf6;
      border-radius: 50%;
      animation: spin 1s linear infinite;
      margin: 0 auto 10px auto;
    }
    
    .availability-header {
      margin: 30px 0 20px 0;
      color: #f0abfc;
      font-size: 1.8rem;
      border-bottom: 2px solid #8b5cf6;
      padding-bottom: 10px;
    }
    
    /* Lyrics Voting Section */
    .lyrics-section {
      background: linear-gradient(145deg, rgba(245, 158, 11, 0.1), rgba(0, 0, 0, 0.3));
      border-radius: 15px;
      padding: 30px;
      margin: 30px 0;
      border: 2px solid #f59e0b;
    }
    
    .lyrics-section h2 {
      color: #fbbf24;
      margin-bottom: 20px;
      font-size: 1.8rem;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .lyrics-table {
      width: 100%;
      border-collapse: collapse;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 10px;
      overflow: hidden;
    }
    
    .lyrics-table thead {
      background: rgba(245, 158, 11, 0.2);
    }
    
    .lyrics-table th {
      padding: 15px;
      text-align: left;
      color: #fbbf24;
      font-weight: bold;
      border-bottom: 2px solid #f59e0b;
    }
    
    .lyrics-table td {
      padding: 15px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .lyrics-table tr:hover {
      background: rgba(255, 255, 255, 0.05);
    }
    
    .lyrics-table tr:last-child td {
      border-bottom: none;
    }
    
    .lyric-text {
      color: #f0f0f0;
      font-size: 1.1rem;
      line-height: 1.5;
    }
    
    .vote-btn {
      padding: 8px 16px;
      border: none;
      border-radius: 20px;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.3s;
      min-width: 80px;
    }
    
    .love-btn {
      background: linear-gradient(90deg, #ef4444, #dc2626);
      color: white;
    }
    
    .love-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 5px 15px rgba(239, 68, 68, 0.4);
    }
    
    .dislike-btn {
      background: linear-gradient(90deg, #3b82f6, #2563eb);
      color: white;
    }
    
    .dislike-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);
    }
    
    .vote-count {
      display: inline-block;
      margin-left: 8px;
      font-size: 1.2rem;
      font-weight: bold;
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

    .quick-add-btn {
      background: linear-gradient(90deg, #ffd700, #ffed4e);
      color: #1a1a2e;
      border: none;
      padding: 12px 20px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: bold;
      transition: all 0.3s;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .quick-add-btn:hover {
      transform: scale(1.05);
      box-shadow: 0 5px 20px rgba(255, 215, 0, 0.5);
    }

    .quick-add-btn.added {
      background: linear-gradient(90deg, #10b981, #059669);
      color: white;
    }

    .nav-buttons {
      display: flex;
      justify-content: space-between;
      margin: 40px 0;
      padding: 30px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 15px;
    }

    .nav-btn {
      padding: 15px 30px;
      font-size: 1.1rem;
      font-weight: bold;
      text-decoration: none;
      border-radius: 10px;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.3s;
    }

    .nav-btn-prev {
      background: linear-gradient(90deg, #3b82f6, #2563eb);
      color: white;
    }

    .nav-btn-prev:hover {
      transform: translateX(-5px);
      box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4);
    }

    .nav-btn-next {
      background: linear-gradient(90deg, #10b981, #059669);
      color: white;
    }

    .nav-btn-next:hover {
      transform: translateX(5px);
      box-shadow: 0 10px 20px rgba(16, 185, 129, 0.4);
    }

    .confirmation-section {
      background: linear-gradient(145deg, rgba(16, 185, 129, 0.1), rgba(0, 0, 0, 0.3));
      border-radius: 15px;
      padding: 40px;
      margin: 30px 0;
      text-align: center;
      border: 2px solid #10b981;
    }

    .confirmation-icon {
      font-size: 4rem;
      margin-bottom: 20px;
      display: block;
    }

    .confirmation-title {
      color: #f0abfc;
      font-size: 2rem;
      margin-bottom: 20px;
    }

    .confirmation-details {
      background: rgba(0, 0, 0, 0.3);
      border-radius: 10px;
      padding: 25px;
      margin: 20px 0;
      text-align: left;
    }

    .detail-item {
      display: flex;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .detail-item:last-child {
      border-bottom: none;
    }

    .detail-label {
      color: #c4b5fd;
    }

    .detail-value {
      color: #f0abfc;
      font-weight: bold;
    }

    .tab-content {
      display: none;
    }
    
    .tab-content.active {
      display: block;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.7; }
    }

    /* Responsive Design */
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
      
      .selection-grid,
      .performance-grid {
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
      .selection-grid,
      .performance-grid {
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
        content: "🎭";
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
      
      .selection-grid,
      .performance-grid {
        grid-template-columns: 1fr;
        gap: 15px;
      }
      
      .header h1 {
        font-size: 36px;
      }
      
      .show-card h3 {
        font-size: 24px;
      }

      .itinerary-tracker {
        width: 90%;
        right: 5%;
        left: 5%;
      }
      
      .date-selector {
        grid-template-columns: repeat(2, 1fr);
      }
      
      .lyrics-table {
        display: block;
        overflow-x: auto;
      }
      
      .nav-buttons {
        flex-direction: column;
        gap: 15px;
      }
      
      .nav-btn {
        width: 100%;
        justify-content: center;
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
      
      .date-selector {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <!-- Fixed Left Sidebar - SAME AS LANDMARKS PAGE -->
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
      <button class="nav-button shopping" onclick="navigateTo('shopping')">
        🛍️ Shopping
      </button>
      <button class="nav-button broadway active" onclick="navigateTo('broadway')">
        🎭 Broadway
      </button>
    </div>
  </div>

  <!-- Main Content - SHIFTED LEFT -->
  <div class="main-content">
    <button class="toggle-tracker-btn" onclick="toggleItineraryTracker()">
      📋 My Itinerary
    </button>

    <div class="container">
      <div class="header">
        <h1>🎭 Broadway Experience</h1>
        <p>Choose your Broadway show and vote on famous lyrics from musicals. Experience the magic of theater!</p>
        <div class="live-data-indicator" id="apiStatus">🔌 Connecting to Broadway API...</div>
      </div>

      <!-- Tab Navigation -->
      <div class="tab-container">
        <button class="tab active" onclick="switchTab('shows')">🎟️ Show Selection</button>
        <button class="tab" onclick="switchTab('lyrics')">🎵 Lyrics Voting</button>
      </div>

      <!-- Shows Tab Content -->
      <div id="shows-tab" class="tab-content active">
        <!-- Show Selection Grid -->
        <div id="step1" class="step active">
          <h2 style="text-align: center; margin-bottom: 30px; color: #f0abfc;">Choose Your Broadway Show</h2>
          
          <div class="date-selector">
            <div class="date-card selected" onclick="selectDate('2026-06-05')">
              <div class="day">Friday</div>
              <div class="date">June 5</div>
            </div>
            <div class="date-card" onclick="selectDate('2026-06-06')">
              <div class="day">Saturday</div>
              <div class="date">June 6</div>
            </div>
            <div class="date-card" onclick="selectDate('2026-06-07')">
              <div class="day">Sunday</div>
              <div class="date">June 7</div>
            </div>
            <div class="date-card" onclick="selectDate('2026-06-08')">
              <div class="day">Monday</div>
              <div class="date">June 8</div>
            </div>
            <div class="date-card" onclick="selectDate('2026-06-09')">
              <div class="day">Tuesday</div>
              <div class="date">June 9</div>
            </div>
          </div>
          
          <div class="selection-grid">
            <div class="selection-card" onclick="selectShow('hamilton')">
              <h4>🎭 Hamilton</h4>
              <div class="show-theater">Richard Rodgers Theatre</div>
              <p>The revolutionary musical that tells the story of American Founding Father Alexander Hamilton through a blend of hip-hop, jazz, R&B, and Broadway.</p>
              <div class="show-badge">Most Popular</div>
              <button class="quick-add-btn" onclick="quickAddToItinerary('hamilton', event)" data-show="hamilton">
                <span>⭐</span> Add to Itinerary
              </button>
            </div>
            
            <div class="selection-card" onclick="selectShow('lionking')">
              <h4>🦁 The Lion King</h4>
              <div class="show-theater">Minskoff Theatre</div>
              <p>The groundbreaking musical based on Disney's classic film, featuring breathtaking visuals, stunning costumes, and unforgettable music by Elton John.</p>
              <div class="show-badge">Family Favorite</div>
              <button class="quick-add-btn" onclick="quickAddToItinerary('lionking', event)" data-show="lionking">
                <span>⭐</span> Add to Itinerary
              </button>
            </div>
            
            <div class="selection-card" onclick="selectShow('wicked')">
              <h4>🧙‍♀️ Wicked</h4>
              <div class="show-theater">Gershwin Theatre</div>
              <p>The untold story of the witches of Oz, exploring the friendship between Glinda the Good and the Wicked Witch of the West before Dorothy arrived.</p>
              <div class="show-badge">Longest Running</div>
              <button class="quick-add-btn" onclick="quickAddToItinerary('wicked', event)" data-show="wicked">
                <span>⭐</span> Add to Itinerary
              </button>
            </div>
            
            <div class="selection-card" onclick="selectShow('hadestown')">
              <h4>⚡ Hadestown</h4>
              <div class="show-theater">Walter Kerr Theatre</div>
              <p>An acclaimed musical that intertwines two mythic tales—Orpheus and Eurydice, and King Hades and Persephone—as it journeys to the underworld and back.</p>
              <div class="show-badge">Tony Winner</div>
              <button class="quick-add-btn" onclick="quickAddToItinerary('hadestown', event)" data-show="hadestown">
                <span>⭐</span> Add to Itinerary
              </button>
            </div>
          </div>
          
          <button class="btn btn-primary" onclick="goToStep(2)">
            <span>🎟️</span> Check Live Availability
            <span>→</span>
          </button>
        </div>

        <!-- Show Details & Availability -->
        <div class="step" id="step2">
          <button class="btn back-btn" onclick="goToStep(1)">
            <span>←</span> Back to Shows
          </button>
          
          <div class="show-card">
            <div class="show-info">
              <h3 id="showName">Loading...</h3>
              <div class="show-type" id="showType"></div>
            </div>
            <div class="show-theater" id="showTheater"></div>
            <p id="showDescription"></p>
            
            <!-- Live Availability Section -->
            <div id="availabilitySection">
              <h2 class="availability-header">📅 Live Ticket Availability</h2>
              <div class="availability-display">
                <div class="availability-header">
                  <h4>Available Performances</h4>
                  <div class="price-tag" id="priceRange">Loading...</div>
                </div>
                <div id="availabilityData">
                  <div class="availability-loading">
                    <div class="live-loading-spinner"></div>
                    <div>Checking real-time Broadway.com availability...</div>
                  </div>
                </div>
              </div>
              <button class="btn refresh-btn" onclick="refreshAvailability()">
                <span>🔄</span> Refresh Live Availability
              </button>
            </div>
          </div>
          
          <!-- Ticket Selection -->
          <div class="selection-section">
            <h3 style="color: #f0abfc; margin-bottom: 20px;">Select Your Tickets</h3>
            
            <div class="ticket-quantity">
              <div style="flex: 1;">
                <h4 style="color: #c4b5fd; margin-bottom: 10px;">Number of Tickets</h4>
                <p style="color: #cbd5e1;">Select how many tickets you need for the selected performance.</p>
              </div>
              <div class="quantity-control">
                <button class="quantity-btn" onclick="adjustQuantity(-1)" id="decreaseBtn">-</button>
                <div class="quantity-display" id="ticketQuantity">2</div>
                <button class="quantity-btn" onclick="adjustQuantity(1)" id="increaseBtn">+</button>
              </div>
            </div>
            
            <div class="total-price" id="estimatedTotal">
              Estimated Total: $0
            </div>
          </div>
          
          <button class="btn add-to-itinerary-btn" id="addToItineraryBtn" onclick="addBroadwayToItinerary()">
            <span>⭐</span> Add to My Itinerary
          </button>

          <button class="btn btn-primary" onclick="goToStep(3)">
            <span>✅</span> Confirm Selection
            <span>→</span>
          </button>
        </div>

        <!-- Confirmation Section -->
        <div class="step" id="step3">
          <button class="btn back-btn" onclick="goToStep(2)">
            <span>←</span> Back to Tickets
          </button>
          
          <div class="confirmation-section">
            <div class="confirmation-icon">🎉</div>
            <h2 class="confirmation-title">Broadway Tickets Reserved!</h2>
            
            <div class="confirmation-details">
              <div class="detail-item">
                <span class="detail-label">Show:</span>
                <span class="detail-value" id="confirmShow">Hamilton</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Theater:</span>
                <span class="detail-value" id="confirmTheater">Richard Rodgers Theatre</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Date:</span>
                <span class="detail-value" id="confirmDate">Friday, June 5, 2026</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Tickets:</span>
                <span class="detail-value" id="confirmTickets">2 tickets</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Price per Ticket:</span>
                <span class="detail-value" id="confirmPrice">$250</span>
              </div>
              <div class="detail-item" style="border-top: 2px solid #f0abfc; padding-top: 15px; margin-top: 10px;">
                <span class="detail-label" style="font-size: 1.2rem;">Total Cost:</span>
                <span class="detail-value" style="font-size: 1.2rem; color: #10b981;" id="confirmTotal">$500</span>
              </div>
            </div>
            
            <p style="color: #cbd5e1; margin: 20px 0; font-size: 1.1rem;">
              Your tickets have been added to your itinerary. You'll receive a confirmation email with your e-tickets.
            </p>
            
            <button class="btn btn-primary" onclick="completeReservation()">
              <span>📧</span> Send Confirmation Email
            </button>
          </div>
        </div>
      </div>

      <!-- Lyrics Voting Tab Content -->
      <div id="lyrics-tab" class="tab-content">
        <div class="lyrics-section">
          <h2>🎵 Broadway Lyrics Voting</h2>
          <p style="color: #cbd5e1; margin-bottom: 20px; font-size: 1.1rem;">
            Vote on your favorite lyrics from famous Broadway musicals. Click ❤️ for lyrics you love and 👎 for those you dislike!
          </p>
          
          <table class="lyrics-table">
            <thead>
              <tr>
                <th style="width: 60%">Lyric</th>
                <th style="width: 20%">❤️ Love</th>
                <th style="width: 20%">👎 Dislike</th>
              </tr>
            </thead>
            <tbody id="lyricsResult">
              <!-- JavaScript-generated rows will appear here -->
            </tbody>
          </table>
          
          <div style="margin-top: 20px; padding: 15px; background: rgba(0, 0, 0, 0.2); border-radius: 10px;">
            <h4 style="color: #fbbf24; margin-bottom: 10px;">🎭 Vote for Your Favorites!</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
              Lyrics are automatically refreshed every 5 seconds. Your votes are recorded in real-time!
              Currently showing lyrics from <strong>Hamilton</strong>, <strong>Wicked</strong>, <strong>The Lion King</strong>, and more.
            </p>
          </div>
        </div>
      </div>

      <!-- Navigation Buttons -->
      <div class="nav-buttons">
        <a href="/new-york/shopping/" class="nav-btn nav-btn-prev">
          <span>←</span> Previous: Shopping
        </a>
        <a href="/new-york/breakfast/" class="nav-btn nav-btn-next">
          Next: Breakfast
          <span>→</span>
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
    
    <div class="itinerary-item" id="breakfastItem">
      <div class="itinerary-label">🍳 Breakfast</div>
      <div class="itinerary-value" id="breakfastValue">
        <span class="itinerary-empty">Not selected</span>
      </div>
    </div>
    
    <div class="itinerary-item" id="landmarksItem">
      <div class="itinerary-label">🗽 Landmarks</div>
      <div class="itinerary-value" id="landmarksValue">
        <span class="itinerary-empty">Not selected</span>
      </div>
    </div>
    
    <div class="itinerary-item" id="shoppingItem">
      <div class="itinerary-label">🛍️ Shopping</div>
      <div class="itinerary-value" id="shoppingValue">
        <span class="itinerary-empty">Not selected</span>
      </div>
    </div>
    
    <div class="itinerary-item" id="broadwayItem">
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
        window.location.href = '/Insightful-Innovators-/new-york/shopping/';
      } else if (section === 'broadway') {
        // Already on broadway page
        console.log('Navigating to broadway section');
      }
    }

    // ============================================
    // ITINERARY TRACKER JAVASCRIPT (BACKEND-ENABLED)
    // ============================================

    // Import configuration from config.js
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
    
    console.log('Broadway Config loaded - Python URI:', pythonURI);

    // Initialize itinerary when page loads
    async function initItinerary() {
      try {
        const itinerary = await getItinerary();
        updateItineraryDisplay(itinerary);
        updateQuickAddButtons();
      } catch (error) {
        console.error('Failed to initialize itinerary:', error);
        // Fallback to localStorage during transition
        updateItineraryDisplay({
          tripInfo: null,
          breakfast: null,
          landmarks: null,
          shopping: null,
          broadway: null
        });
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
          return itinerary;
        } else {
          throw new Error(data.error || 'Failed to save itinerary');
        }
      } catch (error) {
        console.error('Error saving itinerary to backend:', error);
        localStorage.setItem('nycItinerary', JSON.stringify(itinerary));
        updateItineraryDisplay(itinerary);
        return itinerary;
      }
    }

    async function updateBroadwayInItinerary(broadwayData) {
      try {
        const requestOptions = {
          ...fetchOptions,
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
          body: JSON.stringify(broadwayData)
        };
        
        const response = await fetch(`${pythonURI}/api/itinerary/section/broadway`, requestOptions);
        
        if (!response.ok) {
          throw new Error(`API error: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.success) {
          const itinerary = await getItinerary();
          updateItineraryDisplay(itinerary);
          return data.data;
        } else {
          throw new Error(data.error || 'Failed to update broadway');
        }
      } catch (error) {
        console.error('Error updating broadway in backend:', error);
        const itinerary = await getItinerary();
        itinerary.broadway = broadwayData;
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
            `${itinerary.broadway.show || 'Broadway'}<br><small>${itinerary.broadway.theater || ''}</small>`;
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

    // ============================================
    // BROADWAY SHOW DATA
    // ============================================

    const SHOW_DATA = {
      hamilton: {
        name: "Hamilton",
        theater: "Richard Rodgers Theatre",
        description: "The revolutionary musical that tells the story of American Founding Father Alexander Hamilton through a blend of hip-hop, jazz, R&B, and Broadway.",
        price: 299,
        priceRange: "$299 - $499",
        type: "Musical Drama"
      },
      lionking: {
        name: "The Lion King",
        theater: "Minskoff Theatre",
        description: "The groundbreaking musical based on Disney's classic film, featuring breathtaking visuals, stunning costumes, and unforgettable music by Elton John.",
        price: 179,
        priceRange: "$179 - $399",
        type: "Family Musical"
      },
      wicked: {
        name: "Wicked",
        theater: "Gershwin Theatre",
        description: "The untold story of the witches of Oz, exploring the friendship between Glinda the Good and the Wicked Witch of the West before Dorothy arrived.",
        price: 189,
        priceRange: "$189 - $359",
        type: "Fantasy Musical"
      },
      hadestown: {
        name: "Hadestown",
        theater: "Walter Kerr Theatre",
        description: "An acclaimed musical that intertwines two mythic tales—Orpheus and Eurydice, and King Hades and Persephone—as it journeys to the underworld and back.",
        price: 159,
        priceRange: "$159 - $329",
        type: "Folk Opera"
      }
    };

    // ============================================
    // BROADWAY SHOW SELECTION LOGIC
    // ============================================

    let currentShow = null;
    let selectedDate = '2026-06-05';
    let ticketQuantity = 2;

    async function addBroadwayToItinerary() {
      if (!currentShow) return;
      
      const showData = SHOW_DATA[currentShow];
      const broadwayData = {
        show: showData.name,
        theater: showData.theater,
        date: selectedDate,
        tickets: ticketQuantity,
        total: ticketQuantity * showData.price,
        selected_at: new Date().toISOString(),
        type: 'broadway'
      };
      
      try {
        await updateBroadwayInItinerary(broadwayData);
        
        // Show success message
        const btn = document.getElementById('addToItineraryBtn');
        btn.classList.add('added');
        btn.innerHTML = '<span>✓</span> Added to Itinerary';
        btn.disabled = true;
        
        setTimeout(() => {
          btn.innerHTML = '<span>⭐</span> Add to My Itinerary';
          btn.disabled = false;
        }, 2000);
        
        updateQuickAddButtons();
        
      } catch (error) {
        console.error('Failed to save Broadway to itinerary:', error);
        alert('Failed to save selection. Please try again.');
      }
    }

    async function quickAddToItinerary(showKey, event) {
      event.stopPropagation();
      
      if (!showKey) return;
      
      const showData = SHOW_DATA[showKey];
      if (!showData) return;
      
      const broadwayData = {
        show: showData.name,
        theater: showData.theater,
        date: selectedDate,
        tickets: 2, // Default quantity
        total: 2 * showData.price,
        selected_at: new Date().toISOString(),
        type: 'broadway'
      };
      
      try {
        await updateBroadwayInItinerary(broadwayData);
        
        // Show success feedback on button
        const btn = event.target;
        btn.classList.add('added');
        btn.innerHTML = '<span>✓</span> Added';
        btn.disabled = true;
        
        setTimeout(() => {
          updateQuickAddButtons();
        }, 2000);
        
      } catch (error) {
        console.error('Failed to save Broadway to itinerary:', error);
        alert('Failed to save selection. Please try again.');
      }
    }

    function updateQuickAddButtons() {
      const buttons = document.querySelectorAll('.quick-add-btn');
      const broadwayBtn = document.getElementById('addToItineraryBtn');
      
      getItinerary().then(itinerary => {
        buttons.forEach((btn) => {
          const showKey = btn.getAttribute('data-show');
          const showData = SHOW_DATA[showKey];
          
          if (itinerary.broadway && itinerary.broadway.show === showData.name) {
            btn.classList.add('added');
            btn.innerHTML = '<span>✓</span> Added';
            btn.disabled = true;
          } else {
            btn.classList.remove('added');
            btn.innerHTML = '<span>⭐</span> Add to Itinerary';
            btn.disabled = false;
          }
        });
        
        // Update main add button
        if (broadwayBtn && currentShow) {
          const showData = SHOW_DATA[currentShow];
          if (itinerary.broadway && itinerary.broadway.show === showData.name) {
            broadwayBtn.classList.add('added');
            broadwayBtn.innerHTML = '<span>✓</span> Added to Itinerary';
            broadwayBtn.disabled = true;
          } else {
            broadwayBtn.classList.remove('added');
            broadwayBtn.innerHTML = '<span>⭐</span> Add to My Itinerary';
            broadwayBtn.disabled = false;
          }
        }
      });
    }

    // ============================================
    // TAB SWITCHING FUNCTIONALITY
    // ============================================

    function switchTab(tabName) {
      // Update tabs
      document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active');
      });
      document.querySelector(`.tab[onclick*="${tabName}"]`).classList.add('active');
      
      // Update content
      document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
      });
      document.getElementById(`${tabName}-tab`).classList.add('active');
    }

    // ============================================
    // LYRICS VOTING SYSTEM (BACKEND-ENABLED)
    // ============================================

    // Reaction keys
    const LOVE = "love";
    const DISLIKE = "dislike";

    // Initialize lyrics voting
    function initLyricsVoting() {
      const requestOptions = {
        ...fetchOptions,
        method: 'GET'
      };
      
      fetch(`${pythonURI}/api/lyrics`, requestOptions)
        .then(response => {
          if (response.status !== 200) {
            error("GET API response failure: " + response.status);
            return;
          }
          response.json().then(data => {
            const resultContainer = document.getElementById("lyricsResult");
            resultContainer.innerHTML = '';
            
            for (const row of data) {
              const tr = document.createElement("tr");

              // Lyric text
              const lyric = document.createElement("td");
              lyric.innerHTML = `<div class="lyric-text">${row.id}. "${row.lyric}"</div>`;

              // Love button
              const love = document.createElement("td");
              const loveBtn = document.createElement("button");
              loveBtn.id = LOVE + row.id;
              loveBtn.className = "vote-btn love-btn";
              loveBtn.innerHTML = `❤️ <span class="vote-count">${row.love}</span>`;
              loveBtn.onclick = () => {
                handleVote(LOVE, row.id, loveBtn.id);
              };
              love.appendChild(loveBtn);

              // Dislike button
              const dislike = document.createElement("td");
              const dislikeBtn = document.createElement("button");
              dislikeBtn.id = DISLIKE + row.id;
              dislikeBtn.className = "vote-btn dislike-btn";
              dislikeBtn.innerHTML = `👎 <span class="vote-count">${row.dislike}</span>`;
              dislikeBtn.onclick = () => {
                handleVote(DISLIKE, row.id, dislikeBtn.id);
              };
              dislike.appendChild(dislikeBtn);

              tr.appendChild(lyric);
              tr.appendChild(love);
              tr.appendChild(dislike);
              resultContainer.appendChild(tr);
            }
          });
        })
        .catch(err => {
          error("Lyrics loading error: " + err);
        });
    }

    // Refresh reactions every 5 seconds
    function refreshLyricsReactions() {
      const requestOptions = {
        ...fetchOptions,
        method: 'GET'
      };
      
      fetch(`${pythonURI}/api/lyrics`, requestOptions)
        .then(response => response.json())
        .then(data => {
          for (const row of data) {
            const loveBtn = document.getElementById(LOVE + row.id);
            if (loveBtn) {
              const countSpan = loveBtn.querySelector('.vote-count');
              if (countSpan) countSpan.textContent = row.love;
            }

            const dislikeBtn = document.getElementById(DISLIKE + row.id);
            if (dislikeBtn) {
              const countSpan = dislikeBtn.querySelector('.vote-count');
              if (countSpan) countSpan.textContent = row.dislike;
            }
          }
        })
        .catch(err => console.error("Refresh error:", err));
    }

    // Handle vote
    function handleVote(type, lyricId, elemID) {
      const requestOptions = {
        ...fetchOptions,
        method: "PUT"
      };
      
      fetch(`${pythonURI}/api/lyrics/${type}/${lyricId}`, requestOptions)
        .then(response => {
          if (response.status !== 200) {
            error("PUT API response failure: " + response.status);
            return;
          }
          response.json().then(data => {
            const btn = document.getElementById(elemID);
            if (btn) {
              const countSpan = btn.querySelector('.vote-count');
              if (countSpan) {
                if (type === LOVE) {
                  countSpan.textContent = data.love;
                } else if (type === DISLIKE) {
                  countSpan.textContent = data.dislike;
                }
              }
              
              // Visual feedback
              btn.style.transform = 'scale(1.2)';
              setTimeout(() => {
                btn.style.transform = 'scale(1)';
              }, 300);
            }
          });
        })
        .catch(err => {
          error(err + " " + url);
        });
    }

    // ============================================
    // BROADWAY SHOW SELECTION FUNCTIONS
    // ============================================

    async function testAPIConnection() {
      try {
        const requestOptions = {
          ...fetchOptions,
          method: 'GET'
        };
        
        const response = await fetch(`${pythonURI}/api/broadway/test`, requestOptions);
        const data = await response.json();
        
        const statusIndicator = document.getElementById('apiStatus');
        if (data.success) {
          statusIndicator.textContent = '✅ Broadway API Connected';
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
        statusIndicator.textContent = '❌ Broadway API Offline';
        statusIndicator.className = 'live-data-indicator offline';
        return false;
      }
    }

    function goToStep(n) {
      document.querySelectorAll('.step').forEach(step => {
        step.classList.remove('active');
      });
      document.getElementById('step' + n).classList.add('active');
      if (n === 3) showConfirmation();
      if (n === 2) updateQuickAddButtons();
    }

    function selectDate(date) {
      selectedDate = date;
      
      // Update UI
      document.querySelectorAll('.date-card').forEach(card => {
        card.classList.remove('selected');
      });
      event.target.closest('.date-card').classList.add('selected');
    }

    function selectShow(showKey) {
      currentShow = showKey;
      
      // Update show details
      const showData = SHOW_DATA[showKey];
      document.getElementById('showName').textContent = showData.name;
      document.getElementById('showTheater').textContent = `📍 ${showData.theater}`;
      document.getElementById('showType').textContent = showData.type;
      document.getElementById('showDescription').textContent = showData.description;
      document.getElementById('priceRange').textContent = showData.priceRange;
      
      // Fetch live availability
      fetchAvailability();
      
      // Calculate initial total
      updateTotal();
      
      goToStep(2);
    }

    async function fetchAvailability() {
      if (!currentShow) return;
      
      const availabilityContainer = document.getElementById('availabilityData');
      
      // Show loading
      availabilityContainer.innerHTML = `
        <div class="availability-loading">
          <div class="live-loading-spinner"></div>
          <div>Fetching live availability for ${SHOW_DATA[currentShow].name}...</div>
        </div>
      `;
      
      try {
        const requestOptions = {
          ...fetchOptions,
          method: 'GET'
        };
        
        const response = await fetch(`${pythonURI}/api/broadway/availability?show=${currentShow}&date=${selectedDate}&quantity=${ticketQuantity}`, requestOptions);
        const data = await response.json();
        
        if (data.success) {
          let availabilityHtml = '<div class="performance-grid">';
          
          if (data.availability && data.availability.length > 0) {
            data.availability.forEach(performance => {
              const statusClass = performance.status === 'sold-out' ? 'sold-out' : '';
              const statusText = performance.status === 'available' ? 'Available' : 
                                performance.status === 'limited' ? 'Limited' : 'Sold Out';
              const statusClassText = performance.status === 'available' ? 'status-available' : 
                                     performance.status === 'limited' ? 'status-limited' : 'status-sold-out';
              
              availabilityHtml += `
                <div class="performance-card ${statusClass}" onclick="selectPerformance('${performance.time}', ${performance.price})">
                  <div class="performance-time">${performance.time}</div>
                  <div class="performance-price">$${performance.price}</div>
                  <div class="performance-status ${statusClassText}">${statusText}</div>
                  <p style="color: #94a3b8; font-size: 0.9rem; margin-top: 8px;">${performance.seats} seats</p>
                </div>
              `;
            });
          } else {
            // Fallback to sample data if no API data
            const performances = [
              { time: '2:00 PM', price: SHOW_DATA[currentShow].price, status: 'available', seats: 'Limited' },
              { time: '7:30 PM', price: SHOW_DATA[currentShow].price + 50, status: 'available', seats: 'Good' },
              { time: '8:00 PM', price: SHOW_DATA[currentShow].price + 100, status: 'limited', seats: 'Few left' },
              { time: '8:30 PM', price: SHOW_DATA[currentShow].price + 150, status: 'sold-out', seats: 'Sold out' }
            ];
            
            performances.forEach(performance => {
              const statusClass = performance.status === 'sold-out' ? 'sold-out' : '';
              const statusText = performance.status === 'available' ? 'Available' : 
                                performance.status === 'limited' ? 'Limited' : 'Sold Out';
              const statusClassText = performance.status === 'available' ? 'status-available' : 
                                     performance.status === 'limited' ? 'status-limited' : 'status-sold-out';
              
              availabilityHtml += `
                <div class="performance-card ${statusClass}">
                  <div class="performance-time">${performance.time}</div>
                  <div class="performance-price">$${performance.price}</div>
                  <div class="performance-status ${statusClassText}">${statusText}</div>
                  <p style="color: #94a3b8; font-size: 0.9rem; margin-top: 8px;">${performance.seats} seats</p>
                </div>
              `;
            });
          }
          
          availabilityHtml += `</div>`;
          
          availabilityContainer.innerHTML = availabilityHtml;
          
          // Add update note
          availabilityContainer.innerHTML += `
            <div class="update-note">
              <strong>Source:</strong> Broadway.com API 
              | <strong>Updated:</strong> ${new Date().toLocaleTimeString()}
            </div>
          `;
        } else {
          throw new Error('No availability data');
        }
      } catch (error) {
        console.error('Error fetching availability:', error);
        availabilityContainer.innerHTML = `
          <div class="availability-display">
            <div style="text-align: center; padding: 20px;">
              <div style="font-size: 2rem; margin-bottom: 10px;">⚠️</div>
              <div style="color: #ef4444; font-weight: bold;">Unable to fetch live availability</div>
              <div style="color: #94a3b8; margin-top: 10px;">Showing sample performance times</div>
            </div>
          </div>
          <div class="update-note">⚠️ Using sample data - API connection failed</div>
        `;
      }
    }

    function refreshAvailability() {
      fetchAvailability();
    }

    function adjustQuantity(change) {
      ticketQuantity += change;
      if (ticketQuantity < 1) ticketQuantity = 1;
      if (ticketQuantity > 10) ticketQuantity = 10;
      
      document.getElementById('ticketQuantity').textContent = ticketQuantity;
      document.getElementById('decreaseBtn').disabled = ticketQuantity === 1;
      document.getElementById('increaseBtn').disabled = ticketQuantity === 10;
      
      updateTotal();
      fetchAvailability(); // Refresh availability with new quantity
    }

    function updateTotal() {
      if (!currentShow) return;
      
      const showData = SHOW_DATA[currentShow];
      const total = ticketQuantity * showData.price;
      document.getElementById('estimatedTotal').textContent = `Estimated Total: $${total}`;
    }

    function showConfirmation() {
      if (!currentShow) return;
      
      const showData = SHOW_DATA[currentShow];
      const total = ticketQuantity * showData.price;
      const dateObj = new Date(selectedDate);
      const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
      const formattedDate = dateObj.toLocaleDateString('en-US', options);
      
      document.getElementById('confirmShow').textContent = showData.name;
      document.getElementById('confirmTheater').textContent = showData.theater;
      document.getElementById('confirmDate').textContent = formattedDate;
      document.getElementById('confirmTickets').textContent = `${ticketQuantity} ticket${ticketQuantity > 1 ? 's' : ''}`;
      document.getElementById('confirmPrice').textContent = `$${showData.price}`;
      document.getElementById('confirmTotal').textContent = `$${total}`;
    }

    function completeReservation() {
      alert(`🎉 Broadway tickets confirmed!\n\n${SHOW_DATA[currentShow].name}\n${ticketQuantity} tickets for ${selectedDate}\nTotal: $${ticketQuantity * SHOW_DATA[currentShow].price}\n\nConfirmation email has been sent!`);
      
      // Reset for next booking
      ticketQuantity = 2;
      updateTotal();
      goToStep(1);
    }

    // ============================================
    // ERROR HANDLING
    // ============================================

    function error(err) {
      console.error(err);
      
      // Create error message in lyrics section
      const resultContainer = document.getElementById("lyricsResult");
      if (resultContainer) {
        const tr = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 3;
        td.innerHTML = `<div style="color: #ef4444; text-align: center; padding: 20px;">Error loading lyrics: ${err}</div>`;
        tr.appendChild(td);
        resultContainer.appendChild(tr);
      }
    }

    // ============================================
    // EXPOSE FUNCTIONS TO WINDOW SCOPE
    // ============================================

    // Expose all functions to global window scope for inline onclick handlers
    window.navigateTo = navigateTo;
    window.initItinerary = initItinerary;
    window.getItinerary = getItinerary;
    window.saveItinerary = saveItinerary;
    window.clearItinerary = clearItinerary;
    window.toggleItineraryTracker = toggleItineraryTracker;
    window.addBroadwayToItinerary = addBroadwayToItinerary;
    window.quickAddToItinerary = quickAddToItinerary;
    window.switchTab = switchTab;
    window.initLyricsVoting = initLyricsVoting;
    window.refreshLyricsReactions = refreshLyricsReactions;
    window.handleVote = handleVote;
    window.testAPIConnection = testAPIConnection;
    window.goToStep = goToStep;
    window.selectDate = selectDate;
    window.selectShow = selectShow;
    window.fetchAvailability = fetchAvailability;
    window.refreshAvailability = refreshAvailability;
    window.adjustQuantity = adjustQuantity;
    window.updateTotal = updateTotal;
    window.showConfirmation = showConfirmation;
    window.completeReservation = completeReservation;
    window.error = error;

    // ============================================
    // INITIALIZATION
    // ============================================

    document.addEventListener('DOMContentLoaded', async () => {
      await initItinerary();
      await testAPIConnection();
      initLyricsVoting();
      
      // Set up interval for refreshing lyrics votes
      setInterval(refreshLyricsReactions, 5000);
      
      // Initialize Broadway show data
      updateTotal();
    });
  </script>
</body>
</html>