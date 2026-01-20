---
layout: post
title: "Step 3 Landmarks"
description: "Time to shop! Let's make a new outfit."
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

<!-- Upper East Side MET Museum Animation -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Metropolitan Museum of Art - NYC</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Garamond', 'Georgia', serif;
            background: linear-gradient(180deg, #87CEEB 0%, #B0E0E6 40%, #FFE4B5 100%);
            min-height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* Ground and street */
        .ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 35%;
            background: linear-gradient(180deg, #4a4a4a 0%, #2c2c2c 50%, #1a1a1a 100%);
            z-index: 2;
        }

        .sidewalk {
            position: absolute;
            bottom: 35%;
            width: 100%;
            height: 8%;
            background: linear-gradient(180deg, #d3d3d3 0%, #a9a9a9 100%);
            z-index: 3;
        }

        .grass {
            position: absolute;
            bottom: 43%;
            width: 100%;
            height: 5%;
            background: linear-gradient(180deg, #90EE90 0%, #2E8B57 100%);
            z-index: 3;
        }

        /* Animated clouds */
        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 100px;
            animation: cloudFloat 40s linear infinite;
            filter: blur(1px);
        }

        .cloud::before, .cloud::after {
            content: '';
            position: absolute;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 100px;
        }

        .cloud1 {
            width: 120px;
            height: 50px;
            top: 8%;
            left: -150px;
        }

        .cloud1::before {
            width: 60px;
            height: 60px;
            top: -30px;
            left: 15px;
        }

        .cloud1::after {
            width: 70px;
            height: 50px;
            top: -20px;
            right: 15px;
        }

        .cloud2 {
            width: 140px;
            height: 55px;
            top: 15%;
            left: -180px;
            animation-duration: 50s;
            animation-delay: 8s;
        }

        .cloud2::before {
            width: 70px;
            height: 70px;
            top: -35px;
            left: 20px;
        }

        .cloud2::after {
            width: 80px;
            height: 55px;
            top: -25px;
            right: 20px;
        }

        .cloud3 {
            width: 100px;
            height: 45px;
            top: 25%;
            left: -120px;
            animation-duration: 45s;
            animation-delay: 15s;
        }

        .cloud3::before {
            width: 50px;
            height: 50px;
            top: -25px;
            left: 12px;
        }

        .cloud3::after {
            width: 60px;
            height: 45px;
            top: -18px;
            right: 12px;
        }

        /* NYC Skyline background */
        .skyline-bg {
            position: absolute;
            bottom: 48%;
            left: 0;
            right: 0;
            height: 250px;
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            opacity: 0.25;
            z-index: 1;
            gap: 15px;
            padding: 0 50px;
        }

        .bg-building {
            background: linear-gradient(180deg, #2c3e50 0%, #1a252f 100%);
            position: relative;
            animation: buildingRise 1.5s ease-out both;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3);
        }

        .bg-building::after {
            content: '';
            position: absolute;
            top: 0;
            left: 8%;
            right: 8%;
            height: 100%;
            background: repeating-linear-gradient(
                to bottom,
                transparent 0px,
                transparent 12px,
                rgba(255, 215, 0, 0.15) 12px,
                rgba(255, 215, 0, 0.15) 14px
            );
        }

        .bg-building1 { width: 80px; height: 180px; animation-delay: 0.1s; }
        .bg-building2 { width: 70px; height: 220px; animation-delay: 0.2s; }
        .bg-building3 { width: 90px; height: 160px; animation-delay: 0.3s; }
        .bg-building4 { width: 75px; height: 240px; animation-delay: 0.4s; }
        .bg-building5 { width: 85px; height: 190px; animation-delay: 0.5s; }
        .bg-building6 { width: 80px; height: 210px; animation-delay: 0.6s; }

        /* The Met Building - Main Structure */
        .met-complex {
            position: absolute;
            bottom: 48%;
            left: 50%;
            transform: translateX(-50%);
            z-index: 5;
            animation: metAppear 2s ease-out 0.8s both;
        }

        /* Main building */
        .met-main {
            width: 700px;
            height: 320px;
            background: linear-gradient(180deg, #f5e6d3 0%, #d9c7b0 50%, #c9b79c 100%);
            position: relative;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.5);
        }

        /* Roof */
        .met-roof {
            position: absolute;
            top: -25px;
            left: -15px;
            right: -15px;
            height: 25px;
            background: linear-gradient(180deg, #8b7355 0%, #6b5845 100%);
            clip-path: polygon(0 100%, 5% 0, 95% 0, 100% 100%);
        }

        /* Pediment (triangular top) */
        .pediment {
            position: absolute;
            top: -80px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            border-left: 200px solid transparent;
            border-right: 200px solid transparent;
            border-bottom: 60px solid #c9b79c;
            filter: drop-shadow(0 5px 10px rgba(0, 0, 0, 0.3));
        }

        /* Classical columns */
        .colonnade {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 280px;
            display: flex;
            justify-content: space-evenly;
            padding: 0 40px;
            align-items: flex-end;
        }

        .column {
            width: 50px;
            height: 100%;
            background: linear-gradient(90deg, #e8dcc8 0%, #f5f5f0 50%, #e8dcc8 100%);
            position: relative;
            box-shadow: 
                inset 3px 0 8px rgba(0, 0, 0, 0.15),
                inset -3px 0 8px rgba(0, 0, 0, 0.15);
            border-radius: 3px 3px 0 0;
        }

        .column::before {
            content: '';
            position: absolute;
            top: -15px;
            left: -5px;
            right: -5px;
            height: 18px;
            background: linear-gradient(180deg, #f5f5f0 0%, #e8dcc8 100%);
            border-radius: 3px;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
        }

        .column::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: -5px;
            right: -5px;
            height: 15px;
            background: #d9c7b0;
            border-radius: 2px;
        }

        /* Fluting on columns */
        .column-flute {
            position: absolute;
            top: 20px;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            background: repeating-linear-gradient(
                90deg,
                transparent 0px,
                transparent 8px,
                rgba(0, 0, 0, 0.05) 8px,
                rgba(0, 0, 0, 0.05) 9px
            );
        }

        /* Entrance */
        .met-entrance {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 180px;
            height: 240px;
            background: linear-gradient(180deg, #3a2f24 0%, #1a1410 100%);
            border-radius: 8px 8px 0 0;
            box-shadow: inset 0 10px 30px rgba(0, 0, 0, 0.8);
            z-index: 10;
        }

        .entrance-arch {
            position: absolute;
            top: 10px;
            left: 10px;
            right: 10px;
            height: 220px;
            background: linear-gradient(180deg, #2c2416 0%, #0a0806 100%);
            border-radius: 80px 80px 0 0;
        }

        /* Windows */
        .window {
            position: absolute;
            width: 35px;
            height: 45px;
            background: linear-gradient(135deg, #4a6fa5 0%, #2c4870 100%);
            border: 3px solid #8b7355;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
        }

        .window1 { top: 40px; left: 60px; }
        .window2 { top: 40px; right: 60px; }
        .window3 { top: 120px; left: 60px; }
        .window4 { top: 120px; right: 60px; }

        /* Grand stairs */
        .grand-stairs {
            position: absolute;
            bottom: -120px;
            left: 50%;
            transform: translateX(-50%);
            width: 750px;
            z-index: 4;
        }

        .stair-level {
            width: 100%;
            height: 15px;
            background: linear-gradient(180deg, #c9c5ba 0%, #a49f94 100%);
            margin-bottom: 5px;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.4);
            position: relative;
        }

        .stair-level::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: rgba(255, 255, 255, 0.3);
        }

        /* Banner flags */
        .banner {
            position: absolute;
            width: 100px;
            height: 180px;
            background: linear-gradient(180deg, #8B0000 0%, #6B0000 100%);
            top: 60px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.4);
            animation: bannerWave 4s ease-in-out infinite;
        }

        .banner-left {
            left: 20px;
        }

        .banner-right {
            right: 20px;
            animation-delay: 2s;
        }

        .banner::after {
            content: 'MET';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(90deg);
            color: #FFD700;
            font-size: 2rem;
            font-weight: bold;
            letter-spacing: 0.3rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        /* Street lamps */
        .street-lamp {
            position: absolute;
            bottom: 48%;
            width: 8px;
            height: 100px;
            background: linear-gradient(180deg, #2c2c2c 0%, #1a1a1a 100%);
            z-index: 6;
        }

        .lamp-top {
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 30px;
            background: radial-gradient(circle, #ffe87c 0%, #ffb347 70%);
            border-radius: 50%;
            box-shadow: 0 0 40px rgba(255, 232, 124, 0.9);
            animation: lampFlicker 3s ease-in-out infinite;
        }

        .lamp-left { left: 15%; }
        .lamp-right { right: 15%; }

        /* Yellow taxis */
        .taxi {
            position: absolute;
            bottom: 35%;
            width: 80px;
            height: 40px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 5px 5px 3px 3px;
            animation: taxiDrive 20s linear infinite;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
            z-index: 7;
        }

        .taxi-top {
            position: absolute;
            top: -12px;
            left: 25px;
            width: 40px;
            height: 15px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 3px 3px 0 0;
        }

        .taxi-sign {
            position: absolute;
            top: -18px;
            left: 32px;
            width: 26px;
            height: 8px;
            background: #FF6B6B;
            border-radius: 2px;
            font-size: 5px;
            text-align: center;
            color: white;
            font-weight: bold;
            line-height: 8px;
        }

        .taxi-wheels {
            position: absolute;
            bottom: -8px;
            width: 100%;
        }

        .wheel {
            position: absolute;
            width: 16px;
            height: 16px;
            background: #2c2c2c;
            border-radius: 50%;
            border: 2px solid #1a1a1a;
        }

        .wheel-front { left: 10px; }
        .wheel-back { right: 10px; }

        .taxi1 { 
            animation-duration: 18s; 
        }
        
        .taxi2 { 
            animation-duration: 22s; 
            animation-delay: 6s;
            bottom: 36%;
        }

        /* Trees */
        .tree {
            position: absolute;
            bottom: 48%;
            z-index: 4;
        }

        .tree-trunk {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 15px;
            height: 60px;
            background: linear-gradient(90deg, #5c4033 0%, #8B4513 50%, #5c4033 100%);
        }

        .tree-foliage {
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 80px;
            background: radial-gradient(circle, #228B22 0%, #006400 100%);
            border-radius: 50%;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        }

        .tree-left { left: 8%; }
        .tree-right { right: 8%; }

        /* People silhouettes */
        .person {
            position: absolute;
            bottom: 43%;
            width: 15px;
            height: 35px;
            background: linear-gradient(180deg, #2c2c2c 0%, #1a1a1a 60%, #2c2c2c 100%);
            border-radius: 8px 8px 3px 3px;
            animation: personWalk 15s linear infinite;
            z-index: 6;
        }

        .person-head {
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 12px;
            height: 12px;
            background: #d4a574;
            border-radius: 50%;
        }

        .person1 { animation-duration: 25s; left: -20px; }
        .person2 { animation-duration: 30s; animation-delay: 8s; left: -20px; }
        .person3 { animation-duration: 28s; animation-delay: 15s; left: -20px; }

        /* Title */
        .title-container {
            position: absolute;
            top: 8%;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            z-index: 10;
            animation: titleFade 2.5s ease-out both;
        }

        .main-title {
            font-size: 5rem;
            color: #8B0000;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4), 0 0 40px rgba(255, 215, 0, 0.3);
            letter-spacing: 0.8rem;
            margin-bottom: 15px;
            font-weight: 300;
        }

        .subtitle {
            font-size: 1.8rem;
            color: #2c4870;
            letter-spacing: 0.5rem;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
            font-weight: 400;
        }

        /* Animations */
        @keyframes cloudFloat {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(100vw + 200px)); }
        }

        @keyframes buildingRise {
            0% { transform: scaleY(0); opacity: 0; }
            100% { transform: scaleY(1); opacity: 1; }
        }

        @keyframes metAppear {
            0% { opacity: 0; transform: translateX(-50%) translateY(100px) scale(0.9); }
            100% { opacity: 1; transform: translateX(-50%) translateY(0) scale(1); }
        }

        @keyframes taxiDrive {
            0% { left: -100px; }
            100% { left: calc(100% + 100px); }
        }

        @keyframes personWalk {
            0% { left: -20px; }
            100% { left: calc(100% + 20px); }
        }

        @keyframes titleFade {
            0% { opacity: 0; transform: translateX(-50%) translateY(-50px); }
            100% { opacity: 1; transform: translateX(-50%) translateY(0); }
        }

        @keyframes bannerWave {
            0%, 100% { transform: scaleX(1); }
            50% { transform: scaleX(1.02); }
        }

        @keyframes lampFlicker {
            0%, 100% { opacity: 1; box-shadow: 0 0 40px rgba(255, 232, 124, 0.9); }
            50% { opacity: 0.85; box-shadow: 0 0 30px rgba(255, 232, 124, 0.7); }
        }
    </style>
</head>
<body>
    <!-- Clouds -->
    <div class="cloud cloud1"></div>
    <div class="cloud cloud2"></div>
    <div class="cloud cloud3"></div>

    <!-- Title -->
    <div class="title-container">
        <h1 class="main-title">THE MET</h1>
        <p class="subtitle">METROPOLITAN MUSEUM OF ART</p>
    </div>

    <!-- Background NYC Skyline -->
    <div class="skyline-bg">
        <div class="bg-building bg-building1"></div>
        <div class="bg-building bg-building2"></div>
        <div class="bg-building bg-building3"></div>
        <div class="bg-building bg-building4"></div>
        <div class="bg-building bg-building5"></div>
        <div class="bg-building bg-building6"></div>
    </div>

    <!-- Trees -->
    <div class="tree tree-left">
        <div class="tree-trunk"></div>
        <div class="tree-foliage"></div>
    </div>
    <div class="tree tree-right">
        <div class="tree-trunk"></div>
        <div class="tree-foliage"></div>
    </div>

    <!-- The Met Building Complex -->
    <div class="met-complex">
        <div class="met-main">
            <div class="pediment"></div>
            <div class="met-roof"></div>
            
            <!-- Banner flags -->
            <div class="banner banner-left"></div>
            <div class="banner banner-right"></div>
            
            <!-- Windows -->
            <div class="window window1"></div>
            <div class="window window2"></div>
            <div class="window window3"></div>
            <div class="window window4"></div>
            
            <!-- Colonnade -->
            <div class="colonnade">
                <div class="column"><div class="column-flute"></div></div>
                <div class="column"><div class="column-flute"></div></div>
                <div class="column"><div class="column-flute"></div></div>
                <div class="column"><div class="column-flute"></div></div>
                <div class="column"><div class="column-flute"></div></div>
                <div class="column"><div class="column-flute"></div></div>
                <div class="column"><div class="column-flute"></div></div>
                <div class="column"><div class="column-flute"></div></div>
            </div>
            
            <!-- Main entrance -->
            <div class="met-entrance">
                <div class="entrance-arch"></div>
            </div>
        </div>
        
        <!-- Grand stairs -->
        <div class="grand-stairs">
            <div class="stair-level"></div>
            <div class="stair-level"></div>
            <div class="stair-level"></div>
            <div class="stair-level"></div>
            <div class="stair-level"></div>
            <div class="stair-level"></div>
        </div>
    </div>

    <!-- Street lamps -->
    <div class="street-lamp lamp-left">
        <div class="lamp-top"></div>
    </div>
    <div class="street-lamp lamp-right">
        <div class="lamp-top"></div>
    </div>

    <!-- Yellow taxis -->
    <div class="taxi taxi1">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="taxi-wheels">
            <div class="wheel wheel-front"></div>
            <div class="wheel wheel-back"></div>
        </div>
    </div>
    <div class="taxi taxi2">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="taxi-wheels">
            <div class="wheel wheel-front"></div>
            <div class="wheel wheel-back"></div>
        </div>
    </div>

    <!-- Walking people -->
    <div class="person person1">
        <div class="person-head"></div>
    </div>
    <div class="person person2">
        <div class="person-head"></div>
    </div>
    <div class="person person3">
        <div class="person-head"></div>
    </div>

    <!-- Ground layers -->
    <div class="grass"></div>
    <div class="sidewalk"></div>
    <div class="ground"></div>
</body>
</html>


<!-- SOHO Ice Cream Mueseum Animation -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Museum of Ice Cream - Soho</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(180deg, #87CEEB 0%, #B0E0E6 50%, #FFE4B5 100%);
            min-height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* Ground */
        .ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 30%;
            background: linear-gradient(180deg, #6B6B6B 0%, #404040 100%);
            z-index: 2;
        }

        .sidewalk {
            position: absolute;
            bottom: 30%;
            width: 100%;
            height: 6%;
            background: linear-gradient(180deg, #D3D3D3 0%, #A9A9A9 100%);
            z-index: 3;
        }

        /* NYC buildings background */
        .nyc-skyline {
            position: absolute;
            bottom: 36%;
            left: 0;
            right: 0;
            height: 250px;
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            opacity: 0.2;
            z-index: 1;
            gap: 20px;
            padding: 0 30px;
        }

        .nyc-building {
            background: linear-gradient(180deg, #2c2c2c 0%, #1a1a1a 100%);
            animation: buildingGrow 1.5s ease-out both;
        }

        .nyc-building::after {
            content: '';
            position: absolute;
            top: 0;
            left: 10%;
            right: 10%;
            height: 100%;
            background: repeating-linear-gradient(
                to bottom,
                transparent 0px,
                transparent 15px,
                rgba(255, 215, 0, 0.2) 15px,
                rgba(255, 215, 0, 0.2) 17px
            );
        }

        .nyc1 { width: 70px; height: 150px; animation-delay: 0.1s; }
        .nyc2 { width: 60px; height: 200px; animation-delay: 0.2s; }
        .nyc3 { width: 80px; height: 130px; animation-delay: 0.3s; }
        .nyc4 { width: 65px; height: 180px; animation-delay: 0.4s; }
        .nyc5 { width: 75px; height: 160px; animation-delay: 0.5s; }

        /* Ice Cream Museum Building */
        .museum {
            position: absolute;
            bottom: 36%;
            left: 50%;
            transform: translateX(-50%);
            width: 500px;
            height: 350px;
            background: linear-gradient(180deg, #FFE5F1 0%, #FFD1E8 100%);
            border-left: 15px solid #FF69B4;
            border-right: 15px solid #FF69B4;
            z-index: 5;
            animation: museumAppear 2s ease-out 0.6s both;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        /* Top sign */
        .top-sign {
            position: absolute;
            top: 30px;
            left: 50%;
            transform: translateX(-50%);
            width: 400px;
            padding: 20px;
            background: #FF1493;
            text-align: center;
            box-shadow: 0 8px 25px rgba(255, 20, 147, 0.4);
        }

        .sign-text {
            color: white;
            font-size: 2.2rem;
            font-weight: bold;
            letter-spacing: 0.2rem;
        }

        /* Windows */
        .window {
            position: absolute;
            width: 70px;
            height: 90px;
            background: linear-gradient(135deg, #87CEEB 0%, #4682B4 100%);
            border: 4px solid #FF69B4;
        }

        .w1 { top: 140px; left: 40px; }
        .w2 { top: 140px; right: 40px; }
        .w3 { top: 240px; left: 40px; }
        .w4 { top: 240px; right: 40px; }

        /* Door */
        .door {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 130px;
            height: 160px;
            background: linear-gradient(180deg, #FF1493 0%, #C71585 100%);
            border-left: 4px solid #FFB6D9;
            border-right: 4px solid #FFB6D9;
        }

        /* Ice cream cone on top */
        .roof-cone {
            position: absolute;
            top: -100px;
            left: 50%;
            transform: translateX(-50%);
            animation: coneFloat 3s ease-in-out infinite;
        }

        .cone {
            width: 0;
            height: 0;
            border-left: 50px solid transparent;
            border-right: 50px solid transparent;
            border-bottom: 100px solid #D2691E;
            position: relative;
            overflow: hidden;
        }

        .cone::before {
            content: '';
            position: absolute;
            top: 0;
            left: -50px;
            width: 100px;
            height: 100px;
            background: 
                linear-gradient(45deg, transparent 48%, #8B4513 48%, #8B4513 51%, transparent 51%),
                linear-gradient(-45deg, transparent 48%, #8B4513 48%, #8B4513 51%, transparent 51%);
            background-size: 12px 12px;
        }

        .scoop {
            position: absolute;
            top: -45px;
            left: 50%;
            transform: translateX(-50%);
            width: 85px;
            height: 85px;
            background: linear-gradient(135deg, #FFB6D9 0%, #FF69B4 100%);
            border-radius: 50%;
            box-shadow: 0 8px 25px rgba(255, 105, 180, 0.4);
        }

        .cherry {
            position: absolute;
            top: -60px;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 20px;
            background: #FF0000;
            border-radius: 50%;
            animation: cherryBob 2s ease-in-out infinite;
        }

        /* Taxis */
        .taxi {
            position: absolute;
            bottom: 36%;
            width: 70px;
            height: 35px;
            background: #FFD700;
            animation: taxiMove 18s linear infinite;
            z-index: 6;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }

        .taxi-top {
            position: absolute;
            top: -10px;
            left: 22px;
            width: 35px;
            height: 12px;
            background: #FFD700;
        }

        .taxi-sign {
            position: absolute;
            top: -15px;
            left: 27px;
            width: 25px;
            height: 6px;
            background: #FF6B6B;
            font-size: 5px;
            color: white;
            text-align: center;
            font-weight: bold;
        }

        .wheels {
            position: absolute;
            bottom: -6px;
            width: 100%;
        }

        .wheel {
            position: absolute;
            width: 14px;
            height: 14px;
            background: #333;
            border-radius: 50%;
            border: 2px solid #1a1a1a;
        }

        .wheel-f { left: 8px; }
        .wheel-b { right: 8px; }

        .taxi1 { animation-duration: 16s; }
        .taxi2 { animation-duration: 20s; animation-delay: 5s; bottom: 37%; }

        /* Title */
        .title {
            position: absolute;
            top: 8%;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            z-index: 10;
            animation: titleDrop 1.8s ease-out both;
        }

        .big-text {
            font-size: 3.5rem;
            color: #FF1493;
            font-weight: bold;
            letter-spacing: 0.3rem;
            text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);
        }

        .small-text {
            font-size: 1.5rem;
            color: #333;
            letter-spacing: 0.4rem;
            margin-top: 5px;
        }

        /* Clouds */
        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 100px;
            animation: cloudMove 40s linear infinite;
        }

        .cloud::before, .cloud::after {
            content: '';
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 100px;
        }

        .cloud1 {
            width: 100px;
            height: 40px;
            top: 10%;
            left: -120px;
        }

        .cloud1::before {
            width: 50px;
            height: 50px;
            top: -25px;
            left: 12px;
        }

        .cloud1::after {
            width: 60px;
            height: 40px;
            top: -15px;
            right: 12px;
        }

        .cloud2 {
            width: 120px;
            height: 45px;
            top: 20%;
            left: -140px;
            animation-duration: 50s;
            animation-delay: 8s;
        }

        .cloud2::before {
            width: 60px;
            height: 60px;
            top: -30px;
            left: 15px;
        }

        .cloud2::after {
            width: 70px;
            height: 45px;
            top: -20px;
            right: 15px;
        }

        /* Animations */
        @keyframes buildingGrow {
            0% { transform: scaleY(0); }
            100% { transform: scaleY(1); }
        }

        @keyframes museumAppear {
            0% {
                opacity: 0;
                transform: translateX(-50%) translateY(60px);
            }
            100% {
                opacity: 1;
                transform: translateX(-50%) translateY(0);
            }
        }

        @keyframes coneFloat {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-12px); }
        }

        @keyframes cherryBob {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-8px); }
        }

        @keyframes taxiMove {
            0% { left: -80px; }
            100% { left: calc(100% + 80px); }
        }

        @keyframes titleDrop {
            0% {
                opacity: 0;
                transform: translateX(-50%) translateY(-60px);
            }
            100% {
                opacity: 1;
                transform: translateX(-50%) translateY(0);
            }
        }

        @keyframes cloudMove {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(100vw + 150px)); }
        }

        /* Floating ice creams */
        .float-cone {
            position: absolute;
            animation: floatUp 12s ease-in-out infinite;
            z-index: 1;
        }

        .mini-cone {
            width: 0;
            height: 0;
            border-left: 20px solid transparent;
            border-right: 20px solid transparent;
            border-bottom: 40px solid #D2691E;
            position: relative;
        }

        .mini-cone::before {
            content: '';
            position: absolute;
            top: 0;
            left: -20px;
            width: 40px;
            height: 40px;
            background: 
                linear-gradient(45deg, transparent 48%, #8B4513 48%, #8B4513 51%, transparent 51%),
                linear-gradient(-45deg, transparent 48%, #8B4513 48%, #8B4513 51%, transparent 51%);
            background-size: 8px 8px;
        }

        .mini-scoop {
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            width: 35px;
            height: 35px;
            border-radius: 50%;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        .fc1 {
            top: 15%;
            left: 12%;
            animation-duration: 10s;
        }
        .fc1 .mini-scoop { background: linear-gradient(135deg, #FFB6D9 0%, #FF69B4 100%); }

        .fc2 {
            top: 50%;
            left: 8%;
            animation-duration: 13s;
            animation-delay: 2s;
        }
        .fc2 .mini-scoop { background: linear-gradient(135deg, #87CEEB 0%, #4682B4 100%); }

        .fc3 {
            top: 20%;
            right: 15%;
            animation-duration: 11s;
            animation-delay: 1s;
        }
        .fc3 .mini-scoop { background: linear-gradient(135deg, #98FB98 0%, #00FA9A 100%); }

        .fc4 {
            top: 55%;
            right: 10%;
            animation-duration: 14s;
            animation-delay: 3s;
        }
        .fc4 .mini-scoop { background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); }

        .fc5 {
            top: 35%;
            left: 20%;
            animation-duration: 12s;
            animation-delay: 4s;
        }
        .fc5 .mini-scoop { background: linear-gradient(135deg, #DDA0DD 0%, #BA55D3 100%); }

        .fc6 {
            top: 42%;
            right: 18%;
            animation-duration: 13s;
            animation-delay: 5s;
        }
        .fc6 .mini-scoop { background: linear-gradient(135deg, #FF6347 0%, #DC143C 100%); }

        /* Sprinkles */
        .sprinkle {
            position: absolute;
            width: 8px;
            height: 25px;
            border-radius: 4px;
            animation: sprinkleFall 7s linear infinite;
            box-shadow: 0 0 8px rgba(0, 0, 0, 0.4);
            z-index: 8;
        }

        @keyframes floatUp {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            50% {
                transform: translateY(-30px) rotate(10deg);
            }
        }

        @keyframes sprinkleFall {
            0% {
                transform: translateY(-50px) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translateY(100vh) rotate(360deg);
                opacity: 0.5;
            }
        }
    </style>
</head>
<body>
    <!-- Clouds -->
    <div class="cloud cloud1"></div>
    <div class="cloud cloud2"></div>

    <!-- Floating ice creams -->
    <div class="float-cone fc1">
        <div class="mini-scoop"></div>
        <div class="mini-cone"></div>
    </div>
    <div class="float-cone fc2">
        <div class="mini-scoop"></div>
        <div class="mini-cone"></div>
    </div>
    <div class="float-cone fc3">
        <div class="mini-scoop"></div>
        <div class="mini-cone"></div>
    </div>
    <div class="float-cone fc4">
        <div class="mini-scoop"></div>
        <div class="mini-cone"></div>
    </div>
    <div class="float-cone fc5">
        <div class="mini-scoop"></div>
        <div class="mini-cone"></div>
    </div>
    <div class="float-cone fc6">
        <div class="mini-scoop"></div>
        <div class="mini-cone"></div>
    </div>



    <!-- NYC Skyline -->
    <div class="nyc-skyline">
        <div class="nyc-building nyc1"></div>
        <div class="nyc-building nyc2"></div>
        <div class="nyc-building nyc3"></div>
        <div class="nyc-building nyc4"></div>
        <div class="nyc-building nyc5"></div>
    </div>

    <!-- Museum Building -->
    <div class="museum">
        <!-- Ice cream on roof -->
        <div class="roof-cone">
            <div class="cherry"></div>
            <div class="scoop"></div>
            <div class="cone"></div>
        </div>

        <!-- Sign -->
        <div class="top-sign">
            <div class="sign-text">ICE CREAM MUSEUM</div>
        </div>

        <!-- Windows -->
        <div class="window w1"></div>
        <div class="window w2"></div>
        <div class="window w3"></div>
        <div class="window w4"></div>

        <!-- Door -->
        <div class="door"></div>
    </div>

    <!-- Taxis -->
    <div class="taxi taxi1">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="wheels">
            <div class="wheel wheel-f"></div>
            <div class="wheel wheel-b"></div>
        </div>
    </div>
    <div class="taxi taxi2">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="wheels">
            <div class="wheel wheel-f"></div>
            <div class="wheel wheel-b"></div>
        </div>
    </div>

    <!-- Ground -->
    <div class="sidewalk"></div>
    <div class="ground"></div>

    <script>
        // Create lots of sprinkles
        function createSprinkles() {
            const colors = ['#FF69B4', '#FFD700', '#00CED1', '#98FB98', '#DDA0DD', '#FF6347', '#87CEEB', '#FFA500', '#FF1493', '#00FF00', '#9370DB', '#FF4500'];
            const sprinkleCount = 120;
            
            for (let i = 0; i < sprinkleCount; i++) {
                const sprinkle = document.createElement('div');
                sprinkle.className = 'sprinkle';
                sprinkle.style.left = Math.random() * 100 + '%';
                sprinkle.style.top = (Math.random() * -30) + '%';
                sprinkle.style.background = colors[Math.floor(Math.random() * colors.length)];
                sprinkle.style.animationDelay = Math.random() * 7 + 's';
                sprinkle.style.animationDuration = (Math.random() * 4 + 4) + 's';
                sprinkle.style.transform = `rotate(${Math.random() * 360}deg)`;
                document.body.appendChild(sprinkle);
            }
        }

        createSprinkles();
    </script>
</body>
</html>

<!--- Midtown Empire State Building Animation -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Empire State Building</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(180deg, #0a1628 0%, #1a2a4a 30%, #2d4a7c 60%, #4a6fa5 100%);
            min-height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* Stars */
        .star {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s ease-in-out infinite;
            box-shadow: 0 0 4px white;
        }

        /* Ground */
        .ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 15%;
            background: linear-gradient(180deg, #2c2c2c 0%, #1a1a1a 100%);
            z-index: 2;
        }

        .street {
            position: absolute;
            bottom: 15%;
            width: 100%;
            height: 5%;
            background: linear-gradient(180deg, #4a4a4a 0%, #2c2c2c 100%);
            z-index: 3;
        }

        /* Street lines */
        .street::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            height: 3px;
            background: repeating-linear-gradient(
                90deg,
                #FFD700 0px,
                #FFD700 40px,
                transparent 40px,
                transparent 80px
            );
        }

        /* Background buildings */
        .skyline {
            position: absolute;
            bottom: 20%;
            left: 0;
            right: 0;
            height: 300px;
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            opacity: 0.4;
            z-index: 1;
            gap: 25px;
            padding: 0 40px;
        }

        .bg-building {
            background: linear-gradient(180deg, #1a1a2e 0%, #0f0f1e 100%);
            position: relative;
            animation: buildingRise 2s ease-out both;
            box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.5);
        }

        .bg-building::after {
            content: '';
            position: absolute;
            top: 0;
            left: 8%;
            right: 8%;
            height: 100%;
            background: repeating-linear-gradient(
                to bottom,
                transparent 0px,
                transparent 18px,
                rgba(255, 215, 0, 0.3) 18px,
                rgba(255, 215, 0, 0.3) 20px
            );
        }

        .bg1 { width: 90px; height: 200px; animation-delay: 0.1s; }
        .bg2 { width: 80px; height: 260px; animation-delay: 0.2s; }
        .bg3 { width: 100px; height: 180px; animation-delay: 0.3s; }
        .bg4 { width: 85px; height: 240px; animation-delay: 0.4s; }
        .bg5 { width: 95px; height: 220px; animation-delay: 0.5s; }
        .bg6 { width: 90px; height: 200px; animation-delay: 0.6s; }

        /* Empire State Building */
        .empire-state {
            position: absolute;
            bottom: 15%;
            left: 50%;
            transform: translateX(-50%) scale(0.75);
            z-index: 5;
            animation: empireRise 3s ease-out 0.5s both;
        }

        /* Base section */
        .base {
            width: 280px;
            height: 120px;
            background: linear-gradient(180deg, #c9b79c 0%, #a89885 100%);
            position: relative;
            margin: 0 auto;
            box-shadow: 
                0 0 40px rgba(255, 215, 0, 0.3),
                inset 0 0 30px rgba(0, 0, 0, 0.2);
        }

        /* Mid section */
        .mid-section {
            width: 220px;
            height: 180px;
            background: linear-gradient(180deg, #d4c4b0 0%, #c9b79c 100%);
            margin: 0 auto;
            position: relative;
            box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.2);
        }

        /* Main tower */
        .main-tower {
            width: 160px;
            height: 320px;
            background: linear-gradient(180deg, #e8dcc8 0%, #d4c4b0 100%);
            margin: 0 auto;
            position: relative;
            box-shadow: 
                inset 5px 0 15px rgba(0, 0, 0, 0.3),
                inset -5px 0 15px rgba(0, 0, 0, 0.3);
        }

        /* Top section */
        .top-section {
            width: 100px;
            height: 80px;
            background: linear-gradient(180deg, #f5e6d3 0%, #e8dcc8 100%);
            margin: 0 auto;
            position: relative;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.2);
        }

        /* Spire */
        .spire {
            width: 40px;
            height: 120px;
            background: linear-gradient(180deg, #8b8b8b 0%, #5c5c5c 100%);
            margin: 0 auto;
            position: relative;
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
        }

        /* Antenna */
        .antenna {
            width: 8px;
            height: 60px;
            background: linear-gradient(180deg, #d4d4d4 0%, #8b8b8b 100%);
            margin: 0 auto;
            position: relative;
        }

        .antenna-top {
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 20px;
            background: radial-gradient(circle, #ff0000 0%, #cc0000 100%);
            border-radius: 50%;
            box-shadow: 0 0 30px #ff0000, 0 0 60px #ff0000;
            animation: antennaBlink 2s ease-in-out infinite;
        }

        /* Windows pattern */
        .windows {
            position: absolute;
            top: 0;
            left: 10%;
            right: 10%;
            height: 100%;
            background: repeating-linear-gradient(
                to bottom,
                transparent 0px,
                transparent 8px,
                rgba(255, 215, 0, 0.6) 8px,
                rgba(255, 215, 0, 0.6) 10px
            );
        }

        .windows-vertical {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 100%;
            background: repeating-linear-gradient(
                90deg,
                transparent 0px,
                transparent 15px,
                rgba(0, 0, 0, 0.2) 15px,
                rgba(0, 0, 0, 0.2) 17px
            );
        }

        /* Top lighting */
        .top-lights {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 100px;
            background: linear-gradient(180deg, 
                rgba(135, 206, 250, 0.8) 0%,
                rgba(135, 206, 250, 0.4) 50%,
                transparent 100%
            );
            animation: lightsPulse 3s ease-in-out infinite;
            box-shadow: 0 -20px 60px rgba(135, 206, 250, 0.6);
        }

        /* Searchlights */
        .searchlight {
            position: absolute;
            bottom: 20%;
            width: 200px;
            height: 600px;
            background: linear-gradient(180deg, 
                rgba(255, 255, 255, 0.1) 0%,
                transparent 100%
            );
            transform-origin: bottom center;
            animation: searchlightSweep 8s ease-in-out infinite;
            z-index: 1;
        }

        .searchlight1 {
            left: 35%;
            animation-delay: 0s;
        }

        .searchlight2 {
            right: 35%;
            animation-delay: 4s;
        }

        /* Planes */
        .plane {
            position: absolute;
            width: 60px;
            height: 20px;
            z-index: 6;
            animation: planeFly 15s linear infinite;
        }

        .plane-body {
            width: 100%;
            height: 100%;
            background: linear-gradient(180deg, #d4d4d4 0%, #8b8b8b 100%);
            border-radius: 30px 5px 5px 30px;
            position: relative;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.5);
        }

        .plane-wing {
            position: absolute;
            width: 40px;
            height: 8px;
            background: linear-gradient(180deg, #d4d4d4 0%, #a0a0a0 100%);
            top: 50%;
            left: 20%;
            transform: translateY(-50%);
        }

        .plane1 {
            top: 20%;
            left: -80px;
            animation-duration: 18s;
        }

        .plane2 {
            top: 35%;
            left: -80px;
            animation-duration: 22s;
            animation-delay: 6s;
        }

        /* Clouds */
        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 100px;
            animation: cloudFloat 50s linear infinite;
            filter: blur(2px);
        }

        .cloud::before, .cloud::after {
            content: '';
            position: absolute;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 100px;
        }

        .cloud1 {
            width: 140px;
            height: 50px;
            top: 15%;
            left: -160px;
        }

        .cloud1::before {
            width: 70px;
            height: 70px;
            top: -35px;
            left: 20px;
        }

        .cloud1::after {
            width: 80px;
            height: 50px;
            top: -20px;
            right: 20px;
        }

        .cloud2 {
            width: 160px;
            height: 55px;
            top: 25%;
            left: -180px;
            animation-duration: 60s;
            animation-delay: 10s;
        }

        .cloud2::before {
            width: 80px;
            height: 80px;
            top: -40px;
            left: 25px;
        }

        .cloud2::after {
            width: 90px;
            height: 55px;
            top: -25px;
            right: 25px;
        }

        /* Yellow cabs */
        .taxi {
            position: absolute;
            bottom: 20%;
            width: 80px;
            height: 40px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 5px;
            animation: taxiDrive 20s linear infinite;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
            z-index: 7;
        }

        .taxi-top {
            position: absolute;
            top: -12px;
            left: 25px;
            width: 40px;
            height: 15px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 3px 3px 0 0;
        }

        .taxi-sign {
            position: absolute;
            top: -20px;
            left: 32px;
            width: 26px;
            height: 10px;
            background: #FF6B6B;
            border-radius: 2px;
            font-size: 6px;
            text-align: center;
            color: white;
            font-weight: bold;
            line-height: 10px;
        }

        .taxi-wheels {
            position: absolute;
            bottom: -8px;
            width: 100%;
        }

        .wheel {
            position: absolute;
            width: 16px;
            height: 16px;
            background: #2c2c2c;
            border-radius: 50%;
            border: 2px solid #1a1a1a;
        }

        .wheel-front { left: 12px; }
        .wheel-back { right: 12px; }

        .taxi1 { animation-duration: 18s; }
        .taxi2 { animation-duration: 24s; animation-delay: 8s; bottom: 21%; }
        .taxi3 { animation-duration: 20s; animation-delay: 4s; }

        /* Animations */
        @keyframes buildingRise {
            0% { transform: scaleY(0); opacity: 0; }
            100% { transform: scaleY(1); opacity: 1; }
        }

        @keyframes empireRise {
            0% {
                opacity: 0;
                transform: translateX(-50%) translateY(200px) scale(0.8);
            }
            100% {
                opacity: 1;
                transform: translateX(-50%) translateY(0) scale(1);
            }
        }

        @keyframes antennaBlink {
            0%, 100% {
                opacity: 1;
                box-shadow: 0 0 30px #ff0000, 0 0 60px #ff0000;
            }
            50% {
                opacity: 0.3;
                box-shadow: 0 0 15px #ff0000, 0 0 30px #ff0000;
            }
        }

        @keyframes lightsPulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.6;
            }
        }

        @keyframes searchlightSweep {
            0%, 100% {
                transform: rotate(-15deg);
            }
            50% {
                transform: rotate(15deg);
            }
        }

        @keyframes planeFly {
            0% { left: -100px; }
            100% { left: calc(100% + 100px); }
        }

        @keyframes cloudFloat {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(100vw + 200px)); }
        }

        @keyframes taxiDrive {
            0% { left: -100px; }
            100% { left: calc(100% + 100px); }
        }

        @keyframes twinkle {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
    </style>
</head>
<body>
    <!-- Stars -->
    
    <!-- Clouds -->
    <div class="cloud cloud1"></div>
    <div class="cloud cloud2"></div>

    <!-- Searchlights -->
    <div class="searchlight searchlight1"></div>
    <div class="searchlight searchlight2"></div>

    <!-- Background skyline -->
    <div class="skyline">
        <div class="bg-building bg1"></div>
        <div class="bg-building bg2"></div>
        <div class="bg-building bg3"></div>
        <div class="bg-building bg4"></div>
        <div class="bg-building bg5"></div>
        <div class="bg-building bg6"></div>
    </div>

    <!-- Planes -->
    <div class="plane plane1">
        <div class="plane-body">
            <div class="plane-wing"></div>
        </div>
    </div>
    <div class="plane plane2">
        <div class="plane-body">
            <div class="plane-wing"></div>
        </div>
    </div>

    <!-- Empire State Building -->
    <div class="empire-state">
        <div class="antenna">
            <div class="antenna-top"></div>
        </div>
        <div class="spire"></div>
        <div class="top-section">
            <div class="top-lights"></div>
            <div class="windows"></div>
            <div class="windows-vertical"></div>
        </div>
        <div class="main-tower">
            <div class="windows"></div>
            <div class="windows-vertical"></div>
        </div>
        <div class="mid-section">
            <div class="windows"></div>
            <div class="windows-vertical"></div>
        </div>
        <div class="base">
            <div class="windows"></div>
            <div class="windows-vertical"></div>
        </div>
    </div>

    <!-- Taxis -->
    <div class="taxi taxi1">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="taxi-wheels">
            <div class="wheel wheel-front"></div>
            <div class="wheel wheel-back"></div>
        </div>
    </div>
    <div class="taxi taxi2">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="taxi-wheels">
            <div class="wheel wheel-front"></div>
            <div class="wheel wheel-back"></div>
        </div>
    </div>
    <div class="taxi taxi3">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="taxi-wheels">
            <div class="wheel wheel-front"></div>
            <div class="wheel wheel-back"></div>
        </div>
    </div>

    <!-- Ground -->
    <div class="street"></div>
    <div class="ground"></div>

    <script>
        // Create twinkling stars
        function createStars() {
            const starCount = 100;
            for (let i = 0; i < starCount; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 50 + '%';
                star.style.animationDelay = Math.random() * 3 + 's';
                star.style.animationDuration = (Math.random() * 2 + 2) + 's';
                document.body.appendChild(star);
            }
        }

        createStars();
    </script>
</body>
</html>

<!-- East Village Ukranian Mueseum Animation -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ukrainian Museum - East Village</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(180deg, #87CEEB 0%, #B0E0E6 40%, #FFE4B5 100%);
            min-height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* Ground and street */
        .ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 35%;
            background: linear-gradient(180deg, #5a5a5a 0%, #333333 50%, #1a1a1a 100%);
            z-index: 2;
        }

        .sidewalk {
            position: absolute;
            bottom: 35%;
            width: 100%;
            height: 8%;
            background: linear-gradient(180deg, #e0e0e0 0%, #b0b0b0 100%);
            z-index: 3;
        }

        .grass {
            position: absolute;
            bottom: 43%;
            width: 100%;
            height: 5%;
            background: linear-gradient(180deg, #7BC043 0%, #2E8B57 100%);
            z-index: 3;
        }

        /* Animated clouds */
        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 100px;
            animation: cloudFloat 45s linear infinite;
            filter: blur(1px);
        }

        .cloud::before, .cloud::after {
            content: '';
            position: absolute;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 100px;
        }

        .cloud1 {
            width: 120px;
            height: 50px;
            top: 8%;
            left: -150px;
        }

        .cloud1::before {
            width: 60px;
            height: 60px;
            top: -30px;
            left: 15px;
        }

        .cloud1::after {
            width: 70px;
            height: 50px;
            top: -20px;
            right: 15px;
        }

        .cloud2 {
            width: 140px;
            height: 55px;
            top: 18%;
            left: -180px;
            animation-duration: 50s;
            animation-delay: 10s;
        }

        .cloud2::before {
            width: 70px;
            height: 70px;
            top: -35px;
            left: 20px;
        }

        .cloud2::after {
            width: 80px;
            height: 55px;
            top: -25px;
            right: 20px;
        }

        /* NYC Skyline background */
        .skyline-bg {
            position: absolute;
            bottom: 48%;
            left: 0;
            right: 0;
            height: 250px;
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            opacity: 0.2;
            z-index: 1;
            gap: 15px;
            padding: 0 50px;
        }

        .bg-building {
            background: linear-gradient(180deg, #2c3e50 0%, #1a252f 100%);
            animation: buildingRise 1.5s ease-out both;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3);
        }

        .bg-building1 { width: 80px; height: 180px; animation-delay: 0.1s; }
        .bg-building2 { width: 70px; height: 220px; animation-delay: 0.2s; }
        .bg-building3 { width: 90px; height: 160px; animation-delay: 0.3s; }
        .bg-building4 { width: 75px; height: 240px; animation-delay: 0.4s; }
        .bg-building5 { width: 85px; height: 190px; animation-delay: 0.5s; }
        .bg-building6 { width: 80px; height: 210px; animation-delay: 0.6s; }

        /* Ukrainian Museum Building */
        .museum-complex {
            position: absolute;
            bottom: 48%;
            left: 50%;
            transform: translateX(-50%);
            z-index: 5;
            animation: museumAppear 2.2s ease-out 0.7s both;
        }

        .museum-main {
            width: 550px;
            height: 400px;
            background: linear-gradient(180deg, #D4464F 0%, #A8373F 50%, #8B2E33 100%);
            position: relative;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
            border: 3px solid #6B1F24;
        }

        /* Main entrance with Ukrainian-inspired arch */
        .entrance-section {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 220px;
            background: linear-gradient(180deg, #A8373F 0%, #6B1F24 100%);
            display: flex;
            justify-content: center;
            align-items: flex-end;
            border-top: 4px solid #FFD700;
        }

        .entrance-door {
            width: 140px;
            height: 200px;
            background: linear-gradient(90deg, #2c2c2c 0%, #1a1a1a 100%);
            border-radius: 8px 8px 0 0;
            position: relative;
            box-shadow: inset 0 5px 20px rgba(0, 0, 0, 0.8);
        }

        .door-handle {
            position: absolute;
            top: 50%;
            right: 15px;
            width: 10px;
            height: 10px;
            background: #FFD700;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
        }

        /* Windows with Ukrainian pattern */
        .window-section {
            position: absolute;
            top: 30px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-around;
            padding: 0 50px;
            height: 150px;
        }

        .window {
            width: 60px;
            height: 80px;
            background: linear-gradient(135deg, #87CEEB 0%, #4682B4 100%);
            border: 4px solid #FFD700;
            box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 215, 0, 0.4);
            position: relative;
            animation: windowGlow 3s ease-in-out infinite;
        }

        .window::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 80%;
            height: 80%;
            background: repeating-linear-gradient(
                45deg,
                transparent,
                transparent 10px,
                rgba(255, 215, 0, 0.2) 10px,
                rgba(255, 215, 0, 0.2) 11px
            );
        }

        /* Ukrainian decorative elements */
        .ornament {
            position: absolute;
            background: #FFD700;
            border-radius: 50%;
            animation: ornamentBob 3s ease-in-out infinite;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.7);
        }

        .ornament1 { width: 15px; height: 15px; top: 25px; left: 60px; animation-delay: 0s; }
        .ornament2 { width: 15px; height: 15px; top: 25px; right: 60px; animation-delay: 0.5s; }
        .ornament3 { width: 12px; height: 12px; top: 150px; left: 70px; animation-delay: 1s; }
        .ornament4 { width: 12px; height: 12px; top: 150px; right: 70px; animation-delay: 1.5s; }

        /* Roof detail with Ukrainian flag colors */
        .roof {
            position: absolute;
            top: -25px;
            left: -15px;
            right: -15px;
            height: 25px;
            background: linear-gradient(180deg, #005EB8 0%, #004A99 100%);
            clip-path: polygon(0 100%, 5% 0, 95% 0, 100% 100%);
            box-shadow: 0 -5px 15px rgba(0, 0, 0, 0.3);
        }

        .roof::after {
            content: '';
            position: absolute;
            top: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 15px;
            background: #FFD700;
            clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }

        /* Flag pole with Ukrainian flag */
        .flag {
            position: absolute;
            top: -60px;
            left: 40px;
            width: 80px;
            height: 50px;
            background: linear-gradient(180deg, #005EB8 0%, #FFD700 50%);
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.4);
            animation: flagWave 2.5s ease-in-out infinite;
            z-index: 6;
        }

        .flag-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 10px;
            font-weight: bold;
            white-space: nowrap;
        }

        /* Taxis */
        .taxi {
            position: absolute;
            bottom: 35%;
            width: 80px;
            height: 40px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 5px 5px 3px 3px;
            animation: taxiDrive 20s linear infinite;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
            z-index: 7;
        }

        .taxi-top {
            position: absolute;
            top: -12px;
            left: 25px;
            width: 40px;
            height: 15px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 3px 3px 0 0;
        }

        .taxi-sign {
            position: absolute;
            top: -18px;
            left: 32px;
            width: 26px;
            height: 8px;
            background: #FF6B6B;
            border-radius: 2px;
            font-size: 5px;
            text-align: center;
            color: white;
            font-weight: bold;
            line-height: 8px;
        }

        .wheel {
            position: absolute;
            width: 16px;
            height: 16px;
            background: #2c2c2c;
            border-radius: 50%;
            border: 2px solid #1a1a1a;
            bottom: -8px;
        }

        .wheel-front { left: 10px; }
        .wheel-back { right: 10px; }

        .taxi1 { animation-duration: 18s; }
        .taxi2 { animation-duration: 22s; animation-delay: 6s; bottom: 36%; }

        /* People walking */
        .person {
            position: absolute;
            bottom: 43%;
            width: 15px;
            height: 35px;
            background: linear-gradient(180deg, #2c2c2c 0%, #1a1a1a 60%, #2c2c2c 100%);
            border-radius: 8px 8px 3px 3px;
            animation: personWalk 18s linear infinite;
            z-index: 6;
        }

        .person-head {
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 12px;
            height: 12px;
            background: #d4a574;
            border-radius: 50%;
        }

        .person1 { animation-duration: 25s; left: -20px; }
        .person2 { animation-duration: 30s; animation-delay: 8s; left: -20px; }
        .person3 { animation-duration: 28s; animation-delay: 15s; left: -20px; }

        /* Title */
        .title-container {
            position: absolute;
            top: 10%;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            z-index: 10;
            animation: titleFade 2.8s ease-out both;
        }

        .main-title {
            font-size: 3.5rem;
            color: #005EB8;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4), 0 0 30px rgba(0, 94, 184, 0.3);
            letter-spacing: 0.5rem;
            margin-bottom: 10px;
            font-weight: bold;
        }

        .subtitle {
            font-size: 1.5rem;
            color: #D4464F;
            letter-spacing: 0.3rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            font-weight: 500;
        }

        /* Animations */
        @keyframes cloudFloat {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(100vw + 200px)); }
        }

        @keyframes buildingRise {
            0% { transform: scaleY(0); opacity: 0; }
            100% { transform: scaleY(1); opacity: 1; }
        }

        @keyframes museumAppear {
            0% { opacity: 0; transform: translateX(-50%) translateY(80px) scale(0.95); }
            100% { opacity: 1; transform: translateX(-50%) translateY(0) scale(1); }
        }

        @keyframes windowGlow {
            0%, 100% { box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 215, 0, 0.4); }
            50% { box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3), 0 0 35px rgba(255, 215, 0, 0.7); }
        }

        @keyframes ornamentBob {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        @keyframes flagWave {
            0%, 100% { transform: scaleX(1) rotate(0deg); }
            50% { transform: scaleX(0.95) rotate(2deg); }
        }

        @keyframes taxiDrive {
            0% { left: -100px; }
            100% { left: calc(100% + 100px); }
        }

        @keyframes personWalk {
            0% { left: -20px; }
            100% { left: calc(100% + 20px); }
        }

        @keyframes titleFade {
            0% { opacity: 0; transform: translateX(-50%) translateY(-50px); }
            100% { opacity: 1; transform: translateX(-50%) translateY(0); }
        }
    </style>
</head>
<body>
    <!-- Clouds -->
    <div class="cloud cloud1"></div>
    <div class="cloud cloud2"></div>

    <!-- Title -->
    <div class="title-container">
        <h1 class="main-title">UKRAINIAN MUSEUM</h1>
        <p class="subtitle">EAST VILLAGE</p>
    </div>

    <!-- Background NYC Skyline -->
    <div class="skyline-bg">
        <div class="bg-building bg-building1"></div>
        <div class="bg-building bg-building2"></div>
        <div class="bg-building bg-building3"></div>
        <div class="bg-building bg-building4"></div>
        <div class="bg-building bg-building5"></div>
        <div class="bg-building bg-building6"></div>
    </div>

    <!-- The Ukrainian Museum Building -->
    <div class="museum-complex">
        <div class="museum-main">
            <!-- Roof -->
            <div class="roof"></div>
            
            <!-- Flag -->
            <div class="flag">
                <div class="flag-text">🇺🇦</div>
            </div>
            
            <!-- Ornaments -->
            <div class="ornament ornament1"></div>
            <div class="ornament ornament2"></div>
            <div class="ornament ornament3"></div>
            <div class="ornament ornament4"></div>
            
            <!-- Windows -->
            <div class="window-section">
                <div class="window"></div>
                <div class="window"></div>
                <div class="window"></div>
            </div>
            
            <!-- Entrance Section -->
            <div class="entrance-section">
                <div class="entrance-door">
                    <div class="door-handle"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Taxis -->
    <div class="taxi taxi1">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="wheel wheel-front"></div>
        <div class="wheel wheel-back"></div>
    </div>
    <div class="taxi taxi2">
        <div class="taxi-top"></div>
        <div class="taxi-sign">TAXI</div>
        <div class="wheel wheel-front"></div>
        <div class="wheel wheel-back"></div>
    </div>

    <!-- Walking people -->
    <div class="person person1">
        <div class="person-head"></div>
    </div>
    <div class="person person2">
        <div class="person-head"></div>
    </div>
    <div class="person person3">
        <div class="person-head"></div>
    </div>

    <!-- Ground layers -->
    <div class="grass"></div>
    <div class="sidewalk"></div>
    <div class="ground"></div>
</body>
</html>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ landmark.name }} - NYC Landmarks</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }

        /* NAVBAR */
        nav {
            background: white;
            padding: 1rem 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-left {
            display: flex;
            gap: 2rem;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: #005EB8;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav a:hover {
            color: #005EB8;
        }

        .nav-right {
            display: flex;
            gap: 1rem;
        }

        .btn-secondary {
            padding: 0.5rem 1rem;
            background: #f0f0f0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
        }

        .btn-secondary:hover {
            background: #e0e0e0;
        }

        /* MAIN CONTAINER */
        .container {
            display: flex;
            height: calc(100vh - 80px);
            background: white;
        }

        /* LEFT COLUMN - ANIMATION (65%) */
        .animation-column {
            flex: 0 0 65%;
            background: linear-gradient(180deg, #87CEEB 0%, #B0E0E6 40%, #FFE4B5 100%);
            position: relative;
            overflow: hidden;
        }

        .animation-wrapper {
            width: 100%;
            height: 100%;
            position: relative;
        }

        /* ANIMATION STYLES - Ukrainian Museum */
        .ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 35%;
            background: linear-gradient(180deg, #5a5a5a 0%, #333333 50%, #1a1a1a 100%);
            z-index: 2;
        }

        .sidewalk {
            position: absolute;
            bottom: 35%;
            width: 100%;
            height: 8%;
            background: linear-gradient(180deg, #e0e0e0 0%, #b0b0b0 100%);
            z-index: 3;
        }

        .grass {
            position: absolute;
            bottom: 43%;
            width: 100%;
            height: 5%;
            background: linear-gradient(180deg, #7BC043 0%, #2E8B57 100%);
            z-index: 3;
        }

        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 100px;
            animation: cloudFloat 45s linear infinite;
            filter: blur(1px);
        }

        .cloud::before, .cloud::after {
            content: '';
            position: absolute;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 100px;
        }

        .cloud1 {
            width: 120px;
            height: 50px;
            top: 8%;
            left: -150px;
        }

        .cloud1::before {
            width: 60px;
            height: 60px;
            top: -30px;
            left: 15px;
        }

        .cloud1::after {
            width: 70px;
            height: 50px;
            top: -20px;
            right: 15px;
        }

        .cloud2 {
            width: 140px;
            height: 55px;
            top: 18%;
            left: -180px;
            animation-duration: 50s;
            animation-delay: 10s;
        }

        .cloud2::before {
            width: 70px;
            height: 70px;
            top: -35px;
            left: 20px;
        }

        .cloud2::after {
            width: 80px;
            height: 55px;
            top: -25px;
            right: 20px;
        }

        .skyline-bg {
            position: absolute;
            bottom: 48%;
            left: 0;
            right: 0;
            height: 250px;
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            opacity: 0.2;
            z-index: 1;
            gap: 15px;
            padding: 0 50px;
        }

        .bg-building {
            background: linear-gradient(180deg, #2c3e50 0%, #1a252f 100%);
            animation: buildingRise 1.5s ease-out both;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3);
        }

        .bg-building1 { width: 80px; height: 180px; animation-delay: 0.1s; }
        .bg-building2 { width: 70px; height: 220px; animation-delay: 0.2s; }
        .bg-building3 { width: 90px; height: 160px; animation-delay: 0.3s; }
        .bg-building4 { width: 75px; height: 240px; animation-delay: 0.4s; }
        .bg-building5 { width: 85px; height: 190px; animation-delay: 0.5s; }
        .bg-building6 { width: 80px; height: 210px; animation-delay: 0.6s; }

        .museum-complex {
            position: absolute;
            bottom: 48%;
            left: 50%;
            transform: translateX(-50%);
            z-index: 5;
            animation: museumAppear 2.2s ease-out 0.7s both;
        }

        .museum-main {
            width: 550px;
            height: 400px;
            background: linear-gradient(180deg, #D4464F 0%, #A8373F 50%, #8B2E33 100%);
            position: relative;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.6);
            border: 3px solid #6B1F24;
        }

        .entrance-section {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 220px;
            background: linear-gradient(180deg, #A8373F 0%, #6B1F24 100%);
            display: flex;
            justify-content: center;
            align-items: flex-end;
            border-top: 4px solid #FFD700;
        }

        .entrance-door {
            width: 140px;
            height: 200px;
            background: linear-gradient(90deg, #2c2c2c 0%, #1a1a1a 100%);
            border-radius: 8px 8px 0 0;
            position: relative;
            box-shadow: inset 0 5px 20px rgba(0, 0, 0, 0.8);
        }

        .door-handle {
            position: absolute;
            top: 50%;
            right: 15px;
            width: 10px;
            height: 10px;
            background: #FFD700;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
        }

        .window-section {
            position: absolute;
            top: 30px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-around;
            padding: 0 50px;
            height: 150px;
        }

        .window {
            width: 60px;
            height: 80px;
            background: linear-gradient(135deg, #87CEEB 0%, #4682B4 100%);
            border: 4px solid #FFD700;
            box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 215, 0, 0.4);
            position: relative;
            animation: windowGlow 3s ease-in-out infinite;
        }

        .window::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 80%;
            height: 80%;
            background: repeating-linear-gradient(
                45deg,
                transparent,
                transparent 10px,
                rgba(255, 215, 0, 0.2) 10px,
                rgba(255, 215, 0, 0.2) 11px
            );
        }

        .ornament {
            position: absolute;
            background: #FFD700;
            border-radius: 50%;
            animation: ornamentBob 3s ease-in-out infinite;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.7);
        }

        .ornament1 { width: 15px; height: 15px; top: 25px; left: 60px; animation-delay: 0s; }
        .ornament2 { width: 15px; height: 15px; top: 25px; right: 60px; animation-delay: 0.5s; }
        .ornament3 { width: 12px; height: 12px; top: 150px; left: 70px; animation-delay: 1s; }
        .ornament4 { width: 12px; height: 12px; top: 150px; right: 70px; animation-delay: 1.5s; }

        .roof {
            position: absolute;
            top: -25px;
            left: -15px;
            right: -15px;
            height: 25px;
            background: linear-gradient(180deg, #005EB8 0%, #004A99 100%);
            clip-path: polygon(0 100%, 5% 0, 95% 0, 100% 100%);
            box-shadow: 0 -5px 15px rgba(0, 0, 0, 0.3);
        }

        .roof::after {
            content: '';
            position: absolute;
            top: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 15px;
            background: #FFD700;
            clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }

        .flag {
            position: absolute;
            top: -60px;
            left: 40px;
            width: 80px;
            height: 50px;
            background: linear-gradient(180deg, #005EB8 0%, #FFD700 50%);
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.4);
            animation: flagWave 2.5s ease-in-out infinite;
            z-index: 6;
        }

        .flag-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 10px;
            font-weight: bold;
            white-space: nowrap;
        }

        .taxi {
            position: absolute;
            bottom: 35%;
            width: 80px;
            height: 40px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 5px 5px 3px 3px;
            animation: taxiDrive 20s linear infinite;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
            z-index: 7;
        }

        .taxi-top {
            position: absolute;
            top: -12px;
            left: 25px;
            width: 40px;
            height: 15px;
            background: linear-gradient(180deg, #FFD700 0%, #FFC700 100%);
            border-radius: 3px 3px 0 0;
        }

        .taxi-sign {
            position: absolute;
            top: -18px;
            left: 32px;
            width: 26px;
            height: 8px;
            background: #FF6B6B;
            border-radius: 2px;
            font-size: 5px;
            text-align: center;
            color: white;
            font-weight: bold;
            line-height: 8px;
        }

        .wheel {
            position: absolute;
            width: 16px;
            height: 16px;
            background: #2c2c2c;
            border-radius: 50%;
            border: 2px solid #1a1a1a;
            bottom: -8px;
        }

        .wheel-front { left: 10px; }
        .wheel-back { right: 10px; }

        .taxi1 { animation-duration: 18s; }
        .taxi2 { animation-duration: 22s; animation-delay: 6s; bottom: 36%; }

        .person {
            position: absolute;
            bottom: 43%;
            width: 15px;
            height: 35px;
            background: linear-gradient(180deg, #2c2c2c 0%, #1a1a1a 60%, #2c2c2c 100%);
            border-radius: 8px 8px 3px 3px;
            animation: personWalk 18s linear infinite;
            z-index: 6;
        }

        .person-head {
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 12px;
            height: 12px;
            background: #d4a574;
            border-radius: 50%;
        }

        .person1 { animation-duration: 25s; left: -20px; }
        .person2 { animation-duration: 30s; animation-delay: 8s; left: -20px; }
        .person3 { animation-duration: 28s; animation-delay: 15s; left: -20px; }

        /* Overlay buttons on animation */
        .animation-controls {
            position: absolute;
            top: 20px;
            left: 20px;
            display: flex;
            gap: 1rem;
            z-index: 10;
        }

        .btn-overlay {
            padding: 0.6rem 1.2rem;
            background: rgba(255, 255, 255, 0.9);
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s;
        }

        .btn-overlay:hover {
            background: rgba(255, 255, 255, 1);
            transform: translateY(-2px);
        }

        .bottom-controls {
            position: absolute;
            bottom: 20px;
            right: 20px;
            display: flex;
            gap: 1rem;
            z-index: 10;
        }

        /* RIGHT COLUMN - INFO SIDEBAR (35%) */
        .info-column {
            flex: 0 0 35%;
            background: white;
            overflow-y: auto;
            padding: 2rem;
            border-left: 1px solid #e0e0e0;
        }

        .header-section {
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 2px solid #f0f0f0;
        }

        .landmark-title {
            font-size: 2rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 0.5rem;
        }

        .landmark-location {
            color: #666;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .quick-facts {
            background: #f9f9f9;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
        }

        .rating {
            font-size: 1.2rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .stars {
            color: #FFD700;
        }

        .fact-row {
            display: flex;
            justify-content: space-between;
            padding: 0.6rem 0;
            border-bottom: 1px solid #e8e8e8;
            font-size: 0.9rem;
        }

        .fact-row:last-child {
            border-bottom: none;
        }

        .fact-label {
            font-weight: 600;
            color: #666;
        }

        .fact-value {
            color: #333;
        }

        .action-buttons {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.8rem;
            margin-bottom: 1.5rem;
        }

        .btn-primary {
            padding: 0.8rem 1rem;
            background: #005EB8;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s;
            font-size: 0.9rem;
        }

        .btn-primary:hover {
            background: #004495;
            transform: translateY(-2px);
        }

        .btn-secondary-full {
            padding: 0.8rem 1rem;
            background: #f0f0f0;
            border: 2px solid #005EB8;
            color: #005EB8;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s;
            font-size: 0.9rem;
        }

        .btn-secondary-full:hover {
            background: #e8f0ff;
        }

        .btn-full {
            grid-column: 1 / -1;
        }

        .description-section {
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: #f9f9f9;
            border-radius: 4px;
        }

        .section-title {
            font-weight: 700;
            color: #333;
            margin-bottom: 0.8rem;
            font-size: 1.1rem;
        }

        .description-text {
            color: #555;
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .reviews-section {
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 2px solid #f0f0f0;
        }

        .review-item {
            background: #f9f9f9;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
            border-left: 4px solid #005EB8;
        }

        .review-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }

        .review-author {
            font-weight: 600;
            color: #333;
        }

        .review-date {
            color: #999;
            font-size: 0.85rem;
        }

        .review-rating {
            color: #FFD700;
            margin-bottom: 0.5rem;
        }

        .review-text {
            color: #555;
            line-height: 1.5;
            font-size: 0.9rem;
        }

        .write-review-btn {
            padding: 0.8rem 1rem;
            background: #005EB8;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            width: 100%;
            margin-top: 1rem;
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 100;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            width: 90%;
            max-width: 500px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }

        .modal-close {
            float: right;
            font-size: 1.5rem;
            cursor: pointer;
            color: #999;
        }

        .modal-close:hover {
            color: #333;
        }

        .form-group {
            margin-bottom: 1rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #333;
        }

        input, textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: inherit;
            font-size: 0.95rem;
        }

        textarea {
            resize: vertical;
            min-height: 120px;
        }

        input:focus, textarea:focus {
            outline: none;
            border-color: #005EB8;
            box-shadow: 0 0 0 3px rgba(0, 94, 184, 0.1);
        }

        .star-rating {
            display: flex;
            gap: 0.5rem;
            font-size: 1.8rem;
        }

        .star {
            cursor: pointer;
            color: #ddd;
            transition: color 0.2s;
        }

        .star:hover, .star.active {
            color: #FFD700;
        }

        .form-actions {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .form-actions button {
            flex: 1;
            padding: 0.8rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
        }

        .btn-submit {
            background: #005EB8;
            color: white;
        }

        .btn-submit:hover {
            background: #004495;
        }

        .btn-cancel {
            background: #f0f0f0;
            color: #333;
        }

        .btn-cancel:hover {
            background: #e0e0e0;
        }

        /* ANIMATIONS */
        @keyframes cloudFloat {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(100vw + 200px)); }
        }

        @keyframes buildingRise {
            0% { transform: scaleY(0); opacity: 0; }
            100% { transform: scaleY(1); opacity: 1; }
        }

        @keyframes museumAppear {
            0% { opacity: 0; transform: translateX(-50%) translateY(80px) scale(0.95); }
            100% { opacity: 1; transform: translateX(-50%) translateY(0) scale(1); }
        }

        @keyframes windowGlow {
            0%, 100% { box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 215, 0, 0.4); }
            50% { box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.3), 0 0 35px rgba(255, 215, 0, 0.7); }
        }

        @keyframes ornamentBob {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        @keyframes flagWave {
            0%, 100% { transform: scaleX(1) rotate(0deg); }
            50% { transform: scaleX(0.95) rotate(2deg); }
        }

        @keyframes taxiDrive {
            0% { left: -100px; }
            100% { left: calc(100% + 100px); }
        }

        @keyframes personWalk {
            0% { left: -20px; }
            100% { left: calc(100% + 20px); }
        }

        @media (max-width: 1024px) {
            .container {
                flex-direction: column;
            }

            .animation-column {
                flex: 0 0 40vh;
            }

            .info-column {
                flex: 1;
            }

            .action-buttons {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- NAVBAR -->
    <nav>
        <div class="nav-left">
            <div class="logo">🗽 NYC</div>
            <a href="/">Home</a>
            <a href="/#map">Map</a>
        </div>
        <div class="nav-right">
            {% if session.user_id %}
                <a href="/dashboard">Dashboard</a>
                <a href="/auth/logout" class="btn-secondary">Logout</a>
            {% else %}
                <a href="/auth/login" class="btn-secondary">Login</a>
                <a href="/auth/register" class="btn-secondary">Sign Up</a>
            {% endif %}
        </div>
    </nav>

    <!-- MAIN CONTAINER -->
    <div class="container">
        <!-- LEFT COLUMN - ANIMATION (65%) -->
        <div class="animation-column">
            <div class="animation-wrapper">
                <!-- ANIMATION CONTENT -->
                <div class="cloud cloud1"></div>
                <div class="cloud cloud2"></div>

                <div class="skyline-bg">
                    <div class="bg-building bg-building1"></div>
                    <div class="bg-building bg-building2"></div>
                    <div class="bg-building bg-building3"></div>
                    <div class="bg-building bg-building4"></div>
                    <div class="bg-building bg-building5"></div>
                    <div class="bg-building bg-building6"></div>
                </div>

                <div class="museum-complex">
                    <div class="museum-main">
                        <div class="roof"></div>
                        <div class="flag">
                            <div class="flag-text">🇺🇦</div>
                        </div>
                        <div class="ornament ornament1"></div>
                        <div class="ornament ornament2"></div>
                        <div class="ornament ornament3"></div>
                        <div class="ornament ornament4"></div>
                        <div class="window-section">
                            <div class="window"></div>
                            <div class="window"></div>
                            <div class="window"></div>
                        </div>
                        <div class="entrance-section">
                            <div class="entrance-door">
                                <div class="door-handle"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="taxi taxi1">
                    <div class="taxi-top"></div>
                    <div class="taxi-sign">TAXI</div>
                    <div class="wheel wheel-front"></div>
                    <div class="wheel wheel-back"></div>
                </div>
                <div class="taxi taxi2">
                    <div class="taxi-top"></div>
                    <div class="taxi-sign">TAXI</div>
                    <div class="wheel wheel-front"></div>
                    <div class="wheel wheel-back"></div>
                </div>

                <div class="person person1">
                    <div class="person-head"></div>
                </div>
                <div class="person person2">
                    <div class="person-head"></div>
                </div>
                <div class="person person3">
                    <div class="person-head"></div>
                </div>

                <div class="grass"></div>
                <div class="sidewalk"></div>
                <div class="ground"></div>

                <!-- OVERLAY CONTROLS -->
                <div class="animation-controls">
                    <button class="btn-overlay" onclick="alert('Learn more coming soon!')">ℹ️ Info</button>
                    <button class="btn-overlay" onclick="document.getElementById('add-to-itinerary-modal').classList.add('active')">📌 Add to Trip</button>
                </div>

                <div class="bottom-controls">
                    <button class="btn-overlay" onclick="window.open('{{ landmark.website }}', '_blank')">🌐 Visit</button>
                </div>
            </div>
        </div>

        <!-- RIGHT COLUMN - INFO SIDEBAR (35%) -->
        <div class="info-column">
            <!-- HEADER SECTION -->
            <div class="header-section">
                <h1 class="landmark-title">{{ landmark.name }}</h1>
                <div class="landmark-location">
                    📍 landmark.