---
layout: post
title: About
permalink: /about/
comments: true
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sparkling Stars Text</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background: black;
      overflow: hidden;
    }

    .sparkle-container {
      position: relative;
      display: inline-block;
      font-size: 3rem;
      font-weight: bold;
      color: white;
    }

    /* Twinkling star base */
    .star {
      position: absolute;
      width: 6px;
      height: 6px;
      background: white;
      transform: rotate(45deg);
      animation: twinkle 2s infinite ease-in-out;
      opacity: 0.8;
    }

    /* Star cross arms */
    .star::before,
    .star::after {
      content: "";
      position: absolute;
      background: white;
      border-radius: 50%;
    }

    .star::before {
      width: 12px;
      height: 2px;
      top: 2px;
      left: -3px;
    }

    .star::after {
      width: 2px;
      height: 12px;
      top: -3px;
      left: 2px;
    }

    @keyframes twinkle {
      0%, 100% { opacity: 0.2; transform: scale(0.8) rotate(45deg); }
      50% { opacity: 1; transform: scale(1.3) rotate(45deg); }
    }
  </style>
</head>
<body>
  <div class="sparkle-container">Hi, I’m Vivian</div>

  <script>
    const container = document.querySelector('.sparkle-container');

    // Generate stars randomly around the text
    for (let i = 0; i < 25; i++) {
      const star = document.createElement('div');
      star.classList.add('star');
      star.style.left = (Math.random() * 250 - 50) + 'px'; // spread left/right
      star.style.top = (Math.random() * 120 - 40) + 'px';  // spread up/down
      star.style.animationDuration = (1 + Math.random() * 2) + 's'; // random twinkle speed
      star.style.animationDelay = (Math.random() * 2) + 's';
      container.appendChild(star);
    }
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
