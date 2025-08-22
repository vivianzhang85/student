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
  <title>Sparkle Text</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background: black;
    }

    .sparkle-text {
      font-size: 3rem;
      font-weight: bold;
      color: white;
      position: relative;
      overflow: hidden;
    }

    /* Shimmer gradient */
    .sparkle-text::before {
      content: "Hi, I’m Vivian";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(
        120deg,
        transparent 0%,
        rgba(255, 255, 255, 0.8) 40%,
        transparent 80%
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: shimmer 2s infinite linear;
    }

    /* Sparkle stars */
    .sparkle {
      position: absolute;
      width: 6px;
      height: 6px;
      background: white;
      border-radius: 50%;
      box-shadow: 0 0 8px white, 0 0 15px yellow;
      opacity: 0;
      animation: sparkle 3s infinite;
    }

    @keyframes shimmer {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(100%); }
    }

    @keyframes sparkle {
      0%, 100% { opacity: 0; transform: scale(0); }
      50% { opacity: 1; transform: scale(1.5); }
    }
  </style>
</head>
<body>
  <div class="sparkle-text">Hi, I’m Vivian</div>

  <script>
    const text = document.querySelector('.sparkle-text');

    // Create random sparkles
    setInterval(() => {
      const sparkle = document.createElement('div');
      sparkle.classList.add('sparkle');
      sparkle.style.left = Math.random() * text.offsetWidth + 'px';
      sparkle.style.top = Math.random() * text.offsetHeight + 'px';
      text.appendChild(sparkle);

      setTimeout(() => sparkle.remove(), 3000);
    }, 500);
  </script>
</body>
</html>


### Journey through Life

- born in Atlanta, Georgia
- moved to San Diego in elementary school
- went to SRES for elementary school
- went to OVMS for middle school
- currently attending DNHS for high school

### Photo Gallery
![Photo on 2-28-25 at 7 44 PM #2](https://github.com/user-attachments/assets/cdb474b9-8a7b-4149-9161-9ec1e0ccde93)
