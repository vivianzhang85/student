---
layout: post
title: About
permalink: /about/
comments: true
---
<h2 class="sparkle-text">Hi, I'm Vivian</h2>

<style>
  .sparkle-text {
    position: relative;
    font-size: 3rem;
    font-family: Arial, sans-serif;
    color: white;
    text-align: center;
    z-index: 2;
  }

  .sparkle {
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: white;
    animation: twinkle 1.5s infinite ease-in-out;
    pointer-events: none;
  }

  @keyframes twinkle {
    0%, 100% {
      transform: scale(0.2);
      opacity: 0;
    }
    50% {
      transform: scale(1.2);
      opacity: 1;
    }
  }
</style>

<script>
  const colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8F00FF"];
  const text = document.querySelector(".sparkle-text");

  function createSparkle() {
    const rect = text.getBoundingClientRect();
    const sparkle = document.createElement("div");
    sparkle.classList.add("sparkle");

    // Position randomly around the text
    const angle = Math.random() * 2 * Math.PI;
    const radius = rect.width * 0.6;
    const x = rect.left + rect.width / 2 + Math.cos(angle) * (Math.random() * radius);
    const y = rect.top + rect.height / 2 + Math.sin(angle) * (Math.random() * radius);

    sparkle.style.left = `${x}px`;
    sparkle.style.top = `${y}px`;
    sparkle.style.background = colors[Math.floor(Math.random() * colors.length)];
    sparkle.style.animationDuration = `${1 + Math.random()}s`;

    document.body.appendChild(sparkle);

    setTimeout(() => {
      sparkle.remove();
    }, 2000);
  }

  setInterval(createSparkle, 200);
</script>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Moving Cat</title>
  <style>
    body {
      background: #f5f5f5;
      height: 100vh;
      margin: 0;
      overflow: hidden;
      position: relative;
    }
    .cat {
      position: absolute;
      width: 100px;
      transition: transform 2s ease;
    }
  </style>
</head>
<body>
  <img src="https://i.imgur.com/Jg3U3eG.png" alt="cat" class="cat" id="cat">

  <script>
    const cat = document.getElementById("cat");
    const screenW = window.innerWidth;
    const screenH = window.innerHeight;

    function moveCat() {
      const x = Math.random() * (screenW - 100);
      const y = Math.random() * (screenH - 100);
      cat.style.transform = `translate(${x}px, ${y}px)`;
    }

    // Move every 2 seconds
    setInterval(moveCat, 2000);

    // Start somewhere random
    moveCat();
  </script>
</body>
</html>

### Fun facts about me:
- I have a cat
- I love to travel
- I love spending time with my family
- Favorite food: good ramen
- Favorite subject: science

### Journey through Life

- born in Atlanta, Georgia
- moved to San Diego in elementary school
- went to SRES for elementary school
- went to OVMS for middle school
- currently attending DNHS for high school

### Photo Gallery
![Photo on 2-28-25 at 7 44 PM #2](https://github.com/user-attachments/assets/cdb474b9-8a7b-4149-9161-9ec1e0ccde93)
