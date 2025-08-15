---
layout: base
title: I'm [Your Full Name]
hide: true
---

### Me and Team

Hi! My name is [Your Full Name].

| Role         | Name     | Repo Location                       | Stream                | Repo Name |
|--------------|----------|-------------------------------------|-----------------------|-----------|
| Scrum Master | John     | github.com/jm1021/student           | upstream (OCS fork)   | student   |
| Scrummer     | Torin    | github.com/torin/student            | downstream (fork)     | student   |
| Scrummer     | Avantika | github.com/avantika/student         | downstream (fork)     | student   |
| Scrummer     | Aadit    | github.com/aaadit/student           | downstream (fork)     | student   |


## Links to Learning

### Development Environment

> Coding starts with tools, explore these tools and procedures with a click.

<a href="https://github.com/Open-Coding-Society/student">
    <img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white" alt="GitHub">
</a>
<a href="https://open-coding-society.github.io/student">
    <img src="https://img.shields.io/badge/GitHub%20Pages-327FC7?logo=github&logoColor=white" alt="GitHub Pages">
</a>
<a href="https://kasm.opencodingsociety.com/" class="button small" style="background-color: #6b4bd3ff">
    KASM
</a>
<a href="https://vscode.dev/" class="button small" style="background-color: #d38a4bff">
    <span style="color: #FFFFFF">VSCODE</span>
</a>

<br>

### Class Progress

<a href="{{site.baseurl}}/snake" class="button small" style="background-color: #6b4bd3ff">
    Snake Game
</a>
<a href="{{site.baseurl}}/turtle" class="button small" style="background-color: #2A7DB1">
    <span style="color: #000000">Turtle</span>
</a>


<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Push for Confetti</title>
  <style>
    :root {
      --bg: #0f172a;
      --card: #0b1220;
      --accent: #ff7ab6;
    }
    html,body { height:100%; margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial; background:linear-gradient(180deg,var(--bg),#071023); color: #fff;}
    .wrap {
      min-height:100%;
      display:flex;
      align-items:center;
      justify-content:center;
      padding:2rem;
    }
    .card {
      background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
      border-radius:16px;
      padding:28px;
      box-shadow: 0 10px 30px rgba(2,6,23,0.6);
      text-align:center;
      width:100%;
      max-width:480px;
    }
    h1 { margin:0 0 12px; font-size:1.25rem; letter-spacing:0.4px; }
    p { margin:0 0 18px; color: #cbd5e1; font-size:0.95rem; }
    button#confettiBtn {
      appearance:none;
      border:0;
      background: linear-gradient(90deg,var(--accent), #ff9b4b);
      color:#081224;
      font-weight:700;
      padding:12px 18px;
      border-radius:12px;
      cursor:pointer;
      font-size:1rem;
      box-shadow: 0 6px 18px rgba(255,122,182,0.18);
      transition:transform .12s ease, box-shadow .12s ease, opacity .12s;
    }
    button#confettiBtn:active { transform: translateY(1px) scale(.995); }
    button#confettiBtn:focus { outline: 3px solid rgba(255,122,182,0.22); outline-offset:4px; }
    small.hint { display:block; margin-top:12px; color:#94a3b8; }

    /* Fallback DOM confetti styles */
    .dom-confetti {
      position:fixed;
      left:0; top:0; width:100%; height:100%;
      pointer-events:none;
      overflow:hidden;
      z-index:9999;
    }
    .confetti-piece {
      position:absolute;
      width:10px; height:14px;
      opacity:0.95;
      transform-origin:center;
      will-change:transform, top, left;
      animation:confetti-fall linear forwards;
    }
    @keyframes confetti-fall {
      0%   { transform: translateY(-10vh) rotate(0deg); opacity:1; }
      100% { transform: translateY(110vh) rotate(720deg); opacity:0.05; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card" role="region" aria-label="Confetti demo">
      <h1>Push for Confetti 🎉</h1>
      <p>Click the button or press Enter / Space while focused to launch a celebratory confetti burst.</p>
      <button id="confettiBtn" aria-pressed="false">Push for Confetti</button>
      <small class="hint">Accessible & keyboard-friendly</small>
    </div>
  </div>

  <!-- canvas-confetti CDN (served as UMD on window.confetti) -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js" integrity="" crossorigin="anonymous"></script>

  <script>
    (function () {
      const btn = document.getElementById('confettiBtn');

      // Helper: strong confetti burst using canvas-confetti library if available
      function shootWithLibrary() {
        // window.confetti is provided by the CDN UMD bundle
        if (!window.confetti) return false;

        // Multiple bursts for a satisfying effect
        window.confetti({
          particleCount: 40,
          spread: 60,
          origin: { x: 0.25, y: 0.2 },
        });
        window.confetti({
          particleCount: 40,
          spread: 60,
          origin: { x: 0.75, y: 0.2 },
        });
        // A center pop
        window.confetti({
          particleCount: 60,
          spread: 100,
          origin: { x: 0.5, y: 0.25 },
        });

        return true;
      }

      // Fallback: DOM + CSS confetti if the library is unavailable
      function shootDomConfetti() {
        const container = document.createElement('div');
        container.className = 'dom-confetti';
        document.body.appendChild(container);

        const colors = ['#ff7ab6', '#ffd166', '#8be9fd', '#9be7a2', '#b39cff'];
        const total = 40;

        for (let i = 0; i < total; i++) {
          const piece = document.createElement('div');
          piece.className = 'confetti-piece';
          piece.style.background = colors[Math.floor(Math.random() * colors.length)];
          // random starting position across the screen
          const left = Math.random() * 100;
          piece.style.left = left + 'vw';
          // random horizontal drift via animation-duration & delay & transform
          const duration = 2000 + Math.random() * 2400;
          const delay = Math.random() * 120;
          piece.style.top = (-10 - Math.random() * 20) + 'vh';
          piece.style.width = (6 + Math.random() * 12) + 'px';
          piece.style.height = (8 + Math.random() * 18) + 'px';
          piece.style.borderRadius = (Math.random() > 0.5 ? '2px' : '50%');
          piece.style.animationDuration = duration + 'ms';
          piece.style.animationDelay = delay + 'ms';
          piece.style.transform = `rotate(${Math.random()*360}deg)`;
          container.appendChild(piece);

          // Remove the piece after animation finishes
          setTimeout(() => {
            piece.remove();
          }, duration + delay + 100);
        }

        // Cleanup container after the last animation completes
        setTimeout(() => {
          container.remove();
        }, 5000);
      }

      // Main launcher that tries library first, then fallback
      function launchConfetti() {
        const used = shootWithLibrary();
        if (!used) shootDomConfetti();
        // toggle aria-pressed briefly for screen readers
        btn.setAttribute('aria-pressed', 'true');
        setTimeout(()=> btn.setAttribute('aria-pressed','false'), 300);
      }

      // Click handler
      btn.addEventListener('click', launchConfetti);

      // Keyboard activation for Enter and Space while focused
      btn.addEventListener('keydown', function(e) {
        if (e.code === 'Enter' || e.code === 'Space') {
          e.preventDefault();
          launchConfetti();
        }
      });

      // Optional: fire confetti when the page loads (comment out if undesired)
      // window.addEventListener('load', () => setTimeout(launchConfetti, 500));

    })();
  </script>
</body>
</html>


<br>

<!-- Contact Section -->
### Get in Touch

> Feel free to reach out if you'd like to collaborate or learn more about our work.

<p style="color: #2A7DB1;">Open Coding Society: <a href="https://opencodingsociety.com" style="color: #2A7DB1; text-decoration: underline;">Socials</a></p>
