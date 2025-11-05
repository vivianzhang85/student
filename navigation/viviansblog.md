---
layout: post
title: Vivian's Blog
permalink: /student/viviansblog
---

<style>
  /* General body styling */
  body {
    background-color: #365563;
    color: white;
    font-family: 'Poppins', sans-serif;
    line-height: 1.7;
    padding: 2em;
    overflow-x: hidden;
  }

  /* Sparkle and twinkling stars */
  .sparkle, .star {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    animation: floatStars linear infinite;
  }
  @keyframes floatStars {
    0% { transform: translateY(-20px) rotate(0deg); opacity:0.8; }
    100% { transform: translateY(110vh) rotate(360deg); opacity:0; }
  }

  /* Rainbow glowing headings */
  h1, h2, h3 {
    background: linear-gradient(90deg, #ff69b4, #ffb6c1, #ffa500, #ffff00, #00ffcc, #8a2be2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.8), 0 0 20px rgba(255, 105, 180, 0.6);
    animation: rainbowMove 5s linear infinite;
  }
  @keyframes rainbowMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  h2 {
    border-bottom: 2px dashed white;
    padding-bottom: 5px;
    margin-top: 30px;
  }

  h3 {
    background-color: rgba(255, 255, 255, 0.15);
    padding: 8px 12px;
    border-radius: 8px;
  }

  p {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 10px 15px;
    border-radius: 8px;
    margin-bottom: 15px;
    transition: 0.3s;
  }
  p:hover {
    background-color: rgba(255, 255, 255, 0.25);
    transform: scale(1.02);
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
  }

  strong {
    color: #fff8dc;
  }

  .highlight {
    background-color: rgba(255, 255, 255, 0.25);
    padding: 5px 10px;
    border-radius: 5px;
    font-style: italic;
  }

  /* Surprise button styling */
  #surpriseBtn {
    background-color: #ff69b4;
    color: white;
    border: none;
    padding: 15px 35px;
    font-size: 22px;
    border-radius: 15px;
    cursor: pointer;
    box-shadow: 0 0 25px #ffb6c1, 0 0 50px #ff69b4;
    transition: 0.3s;
    margin: 30px 0;
  }
  #surpriseBtn:hover {
    transform: scale(1.15) rotate(-5deg);
    box-shadow: 0 0 40px #ffb6c1, 0 0 60px #ff69b4;
  }

  #surpriseMsg {
    margin-top: 20px;
    font-size: 24px;
    font-weight: bold;
    color: #ffff66;
    text-shadow: 0 0 10px #fff;
  }
</style>


<!-- Binary Joke Button (fresh jokes) -->
<div id="binaryJokeContainer" style="text-align:center; margin-top:20px;">
  <button id="binaryJokeButton" 
          style="
            padding: 12px 24px;
            font-size: 1.2em;
            cursor: pointer;
            border: none;
            border-radius: 12px;
            background-color: #00bfff;
            color: white;
            box-shadow: 0 0 20px #00bfff, 0 0 40px #00bfff, 0 0 60px #00bfff;
            transition: 0.3s;
            font-weight: bold;
          "
          onmouseover="this.style.boxShadow='0 0 30px #00ffff, 0 0 60px #00ffff, 0 0 90px #00ffff'; this.style.transform='scale(1.05)';"
          onmouseout="this.style.boxShadow='0 0 20px #00bfff, 0 0 40px #00bfff, 0 0 60px #00bfff'; this.style.transform='scale(1)';"
  >
    Click for a Binary Joke!
  </button>
  <div id="binaryJokeText" style="margin-top:15px; font-size:1.2em; max-width:400px; margin-left:auto; margin-right:auto;"></div>
</div>

<script>
  const freshBinaryJokes = [
    "Why did the computer sit in the sun? It wanted to become a hot byte.",
    "I told a binary joke… but it didn’t get a bit of laughter.",
    "Why do bits always travel in pairs? Because they can’t handle single life.",
    "What’s a programmer’s favorite snack? Microchips and dip.",
    "How do computers eat popcorn? One byte at a time.",
  ];

  document.getElementById('binaryJokeButton').addEventListener('click', () => {
    const joke = freshBinaryJokes[Math.floor(Math.random() * freshBinaryJokes.length)];
    document.getElementById('binaryJokeText').textContent = joke;
  });
</script>

## Vivian Zhang CSP Trimester 1 Final Blog Entry

### CSP Big Idea 3 Reflection
Throughout **Big Idea 3**, I learned how data and algorithms form the foundation of computer science. Each lesson built on the last, helping me see how information can be represented, processed, and used efficiently in code. From variables to loops, every concept showed me how to think more like a programmer and make my code more organized.

### 3.1 – Variables and Assignments  
From this lesson, I learned that **variables** are used to store information. Using variables and assignments helps organize your code and makes it easier to read, update, and reuse.

### 3.2 – Data Abstraction and Lists  
Through this lesson, I learned how **data abstraction** helps make complex information easier to work with in code. I also learned that **lists** are a type of data abstraction—they give many variables one name, helping manage complexity and keep code efficient.

### 3.3 – Mathematical Expressions and Operators  
I learned how to **write and evaluate mathematical expressions** using operators and variables. Practicing the **order of operations** helped me understand how programs calculate and produce correct results.

### 3.4 – Strings  
From this lesson, I learned how **strings** work—they group characters into a single value, making them easier to manage and manipulate. This allows programmers to treat a whole sequence of text as one variable.

### 3.5 – Boolean Expressions (My Lesson!)  
For 3.5, I took the role of a teacher to write and teach the material. I reflected on my experience with integrating resources, organizing the class flow, and creating an **interactive Jeopardy game** to make learning Boolean logic more engaging. Teaching this topic deepened my understanding of how computers make decisions using true and false values. I also had to design homework that both challenged my classmates thinking, and allowed them to effectively apply concepts I taught.

### 3.6 – Conditionals  
I enjoyed this lesson and learned a lot about **conditionals**, especially the differences between Python’s `elif` and JavaScript’s `else if`. Conditionals help programs make decisions based on certain conditions being true or false.

### 3.7 – Nested Conditionals  
I learned that **nested conditionals** stack multiple layers of conditions together. This means the output of the code depends on a combination of many requirements, allowing for more complex logic and outcomes.

### 3.8 – Iteration  
From this lesson, I learned that **iterations** repeat a block of code multiple times. This is useful because it allows the same action to be performed efficiently without writing duplicate code. Loops make programs faster and more concise.

### 3.9 – Algorithms  
I enjoyed this lesson and felt that the instructors were knowledgeable. I learned that **algorithms** take inputs, process them, and produce outputs when the input meets certain criteria. Understanding algorithms helped me see how problem-solving is at the heart of programming.

### 3.10 – Lists  
From this lesson, I learned that **lists** can store multiple values within a single variable. The **popcorn hacks** were especially helpful for practicing how to access, change, and loop through list elements.

### 3.12 – Procedures  
I learned that **procedures** help organize code into reusable blocks instead of rewriting it each time. This makes programs more efficient and easier to debug. The instructors did a great job explaining and demonstrating this concept.

### 3.13 – Random Values  
In this lesson, I learned to **create procedures** to perform specific tasks in a program. I also learned how to use **random values** to make programs unpredictable or simulate real-world scenarios. Even though it was a bit confusing at times, it was engaging, and I appreciated how knowledgeable the instructors were. By the end, I understood how to make my code cleaner and more efficient.

### 3.15 – Random Values  
This lesson reinforced how **randomness** can make programs more dynamic and realistic. I practiced generating random input to produce different outcomes each time the code runs.

### 3.17 – Algorithmic Efficiency  
This lesson was confusing but also engaging. I appreciated the detailed explanations from the instructors and came away with a stronger understanding of how to make my code more efficient and straightforward.

---

### Compare Yourself to the Beginning of the Year
At the beginning of the year, I felt uncertain about how coding really worked. Concepts like algorithms, loops, and conditionals seemed confusing and abstract. Now, after going through Big Idea 3, I’ve noticed a big change in how I think. I’ve become more confident, organized, and logical when solving problems. I’ve also learned to be more patient when debugging and to see mistakes as part of the learning process. Compared to the start of the year, I feel more like a real programmer and a better team player who can take on challenges step by step. Moreover, as my team's scrum master, I've learned a lot about leadership, how to communicate most effectively with my team, and how to keep us all on pace.

---

### Remembering Key Things from Tools, Fundamentals of JavaScript/Python, West Coast Quest
**Tools:**  
In the beginning, I learned how to use the essential tools of coding like cloning repositories, navigating VSCode, localhost servers, and basic commads like cd. At first, all the commands felt overwhelming, but over time I realized how these tools work together to help me in debugging and project management. This sprint built my foundation and made me feel more comfortable in a real coding environment.

**Fundamentals of JavaScript and Python:**  
This sprint helped me understand the language of programming. I learned the differences in syntax. Switching between JavaScript and Python also taught me how different languages can express similar ideas in slightly different ways. I became more confident reading and writing code, and I started to think like a problem solver instead of just a note-taker.

**West Coast Travel Quest (UI Design Project):**  
This was the most creative sprints and my personal favorite overall. Despite our class falling slightly behind during the first few days of planning, we all perserved by calling multiple class meetings filled with pasionate discussion. I enjoyed seeing everyone pitch in their ideas, the discussions that ensued, and coming out with a great overall idea: a roadtrip. I loved designing the Travel Module within the West Coast Travel Quest project: a virtual road trip up the West Coast where I applied everything I’d learned to build an interactive user interface. I got to combine coding with creativity by integrating progress bars, buttons, hierarchy, and audio. While coding the module, we ran into some issues with local storage being difficult to integrate, but after a 2-hour long Cool Collaborators team meeting, we figured it out! This sprint helped me see how programming connects to real-world design and how front-end coding can make information both useful and beautiful. 

Overall, these three sprints connected technical learning with creativity and teamwork. They showed me that computer science isn’t just about writing code — it’s about designing experiences, solving problems, and building something meaningful from the ground up.

### Night at the Museum Reflection
Our **Night at the Museum** event went really well! My parents came, and it was exciting to share what I’ve been working on in computer science. There were a lot of people walking around, and I got to explain my project and the coding behind it — especially how I built the **progress bar** feature. It felt good to see others interested in my work and to realize how much I’ve


<div id="photo-carousel" class="carousel" style="max-width:400px; margin: 20px auto; position:relative; text-align:center;">
  <img src="../media/assets/IMG_7600.png" alt="Image 1" style="width:100%; height:300px; object-fit:cover; display:block; border-radius:12px;">
  <img src="../media/assets/IMG_7609.png" alt="Image 2" style="width:100%; height:300px; object-fit:cover; display:none; border-radius:12px;">
  <img src="../media/assets/IMG_7608.png" alt="Image 3" style="width:100%; height:300px; object-fit:cover; display:none; border-radius:12px;">

  <button class="prev" style="position:absolute; top:50%; left:10px; transform:translateY(-50%); background:rgba(0,0,0,0.4); border:none; color:white; font-size:1.8em; cursor:pointer; border-radius:50%; width:35px; height:35px;">❮</button>
  <button class="next" style="position:absolute; top:50%; right:10px; transform:translateY(-50%); background:rgba(0,0,0,0.4); border:none; color:white; font-size:1.8em; cursor:pointer; border-radius:50%; width:35px; height:35px;">❯</button>

  <p style="margin-top:10px; font-style:italic; color:white;">The Collaborators at The Night at the Museum!</p>
</div>

<script>
const carousel = document.getElementById('photo-carousel');
const images = carousel.querySelectorAll('img');
let index = 0;

function showImage(i) {
  images.forEach((img, n) => img.style.display = (n === i) ? 'block' : 'none');
}

carousel.querySelector('.prev').onclick = () => {
  index = (index - 1 + images.length) % images.length;
  showImage(index);
};

carousel.querySelector('.next').onclick = () => {
  index = (index + 1) % images.length;
  showImage(index);
};
</script>

---
### What I Want to Learn Next in Computer Science
Next, I want to learn **data science** and explore how data can reveal hidden patterns and insights. I’m want to learn more about tools like pandas, modeling, and visualization libraries to turn large datasets into clear, meaningful information. Learning data science will let me combine coding with real-world problem-solving to create programs that are both smart and impactful.

---

### 66 Question MC Review
### Overview
Score: 48/66
### Q6 – Internet Engineering Task Force (IETF)
- **Your Answer:** C  
- **Correct Answer:** A – Develops standards & protocols for Internet communication  
- **Key Concept:** IETF sets Internet protocols, not security enforcement.  
- **Approach:** Focus on standardization roles.

### Q7 – Program with start, end, current
- **Your Answer:** B  
- **Correct Answer:** C – Displays `3 4`  
- **Key Concept:** Step-by-step tracing of variable assignments.  
- **Approach:** Follow each assignment to see final displayed values.

### Q13 – Social media hypotheses
- **Your Answer:** A  
- **Correct Answer:** D – Mobile app release → shorter messages  
- **Key Concept:** Use data trends after milestones.  
- **Approach:** Compare pre/post mobile app average message lengths.

### Q14 – Comparing loop algorithms
- **Your Answer:** D  
- **Correct Answer:** C – Same number of values, values differ  
- **Key Concept:** Display timing matters (pre/post increment).  
- **Approach:** Trace output sequence carefully.

### Q16 – Downloading licensed music
- **Your Answer:** B  
- **Correct Answer:** D – No DMCA violation  
- **Key Concept:** Licensed downloads are legal.  
- **Approach:** Identify legal vs. illegal actions.

### Q19 – Library e-books metadata
- **Your Answer:** C  
- **Correct Answer:** A – Archives of previous versions  
- **Key Concept:** Metadata includes title, author, genre, publication date.  
- **Approach:** Focus on descriptive/searchable metadata.

### Q21 – Robot algorithms
- **Your Answer:** C  
- **Correct Answer:** B – Move 2 right, 3 up  
- **Key Concept:** Trace robot movements step-by-step.  
- **Approach:** Map each move to the grid.

### Q24 – Byte pair encoding (lossy/lossless)
- **Your Answer:** D  
- **Correct Answer:** C – Lossless, can restore original string  
- **Key Concept:** Lossless = no data discarded.  
- **Approach:** Encoding replaces pairs, doesn’t remove info.

### Q25 – Byte pair encoding (shortening strings)
- **Your Answer:** A  
- **Correct Answer:** D – Only strings with repeating pairs can shorten  
- **Key Concept:** Identify repeated character pairs.  
- **Approach:** Check for multiple occurrences.

### Q26 – Robot IF statement
- **Your Answer:** C  
- **Correct Answer:** B – Properly reaches gray square  
- **Key Concept:** Conditional moves depend on `CAN_MOVE`.  
- **Approach:** Trace IF/ELSE movement logic.

### Q31 – Robot loop comparison
- **Your Answer:** B  
- **Correct Answer:** C – Both programs work  
- **Key Concept:** Simulate all moves.  
- **Approach:** Check if both sequences reach target.

### Q43 – Algorithm runtime
- **Your Answer:** B  
- **Correct Answer:** A – Algorithm runs in reasonable time  
- **Key Concept:** Polynomial runtime = reasonable  
- **Approach:** Recognize O(n²) growth pattern.

### Q52 – Palindrome first letters
- **Your Answer:** B  
- **Correct Answer:** D – II & III work  
- **Key Concept:** Sequence: filter palindromes → shorten → sort  
- **Approach:** Order steps logically.

### Q55 – KeepPlaying procedure
- **Your Answer:** B  
- **Correct Answer:** D – Always returns false  
- **Key Concept:** Logical AND condition prevents true result.  
- **Approach:** Use OR for multiple acceptable inputs.

### Q57 – Generate “Happy” from “Harp” & “Puppy”
- **Your Answer:** A  
- **Correct Answer:** C – Correct substring positions  
- **Key Concept:** Substring indices matter (1-indexed).  
- **Approach:** Map each character position carefully.

### Q63 – isPrime program
- **Your Answer:** Incorrect  
- **Correct Answer:** B & D – Remove line resetting count & extra increment  
- **Key Concept:** Count primes cumulatively; do not reset inside loop.  
- **Approach:** Increment only when prime.

### Q65 – Multiply procedure
- **Your Answer:** Incorrect  
- **Correct Answer:** B & C – Fails for negative y  
- **Key Concept:** Loop termination depends on count = y.  
- **Approach:** Ensure loop handles negative values.

### Q66 – Smallest procedure
- **Your Answer:** Incorrect  
- **Correct Answer:** C & D – Fails if minimum at end  
- **Key Concept:** Return min after scanning entire list.  
- **Approach:** Update min inside loop; return only at end.
 
 ---

### Final Thoughts: Something I Would Like to Share
I really enjoyed working with my teammates this trimester to problem solve and code. Despite the many stressful days and nights filled with coding, I shared lots of laughs and had lots of fun with my classmates. I also am very thankful for Aadit and Avantika's help; without them, I would be very lost.
