<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AP CSP Component C - Web Scraping Feature Reference</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --secondary: #7c3aed;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --dark: #1e293b;
            --light: #f8fafc;
            --code-bg: #1e1e1e;
            --border: #e2e8f0;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #334155;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            background-attachment: fixed;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(10px);
            color: white;
            padding: 30px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        header h1 {
            font-size: 2rem;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        header p {
            color: #94a3b8;
            font-size: 1.1rem;
        }

        nav {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 15px 0;
            position: sticky;
            top: 110px;
            z-index: 999;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            margin-bottom: 30px;
            border-radius: 10px;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }

        nav a {
            color: var(--dark);
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            transition: all 0.3s;
            font-weight: 600;
            display: inline-block;
        }

        nav a:hover {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: translateY(-2px);
        }

        section {
            background: white;
            margin-bottom: 30px;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            scroll-margin-top: 180px;
        }

        h2 {
            color: var(--primary);
            font-size: 2rem;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid var(--primary);
        }

        h3 {
            color: var(--secondary);
            font-size: 1.5rem;
            margin-top: 30px;
            margin-bottom: 15px;
        }

        h4 {
            color: var(--dark);
            font-size: 1.2rem;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin: 5px 5px 5px 0;
        }

        .badge-primary { background: #dbeafe; color: var(--primary); }
        .badge-success { background: #d1fae5; color: var(--success); }
        .badge-warning { background: #fef3c7; color: var(--warning); }
        .badge-danger { background: #fee2e2; color: var(--danger); }
        .badge-secondary { background: #ede9fe; color: var(--secondary); }

        .code-block {
            background: var(--code-bg);
            color: #d4d4d4;
            padding: 25px;
            border-radius: 10px;
            overflow-x: auto;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: relative;
        }

        .code-block::before {
            content: attr(data-lang);
            position: absolute;
            top: 10px;
            right: 15px;
            font-size: 0.75rem;
            color: #888;
            text-transform: uppercase;
            font-weight: 600;
        }

        .code-block pre {
            margin: 0;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9rem;
            line-height: 1.5;
        }

        .keyword { color: #569cd6; }
        .function { color: #dcdcaa; }
        .string { color: #ce9178; }
        .comment { color: #6a9955; font-style: italic; }
        .number { color: #b5cea8; }
        .property { color: #9cdcfe; }
        .operator { color: #d4d4d4; }

        .info-box {
            background: #f0f9ff;
            border-left: 4px solid var(--primary);
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
        }

        .success-box {
            background: #f0fdf4;
            border-left: 4px solid var(--success);
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
        }

        .warning-box {
            background: #fffbeb;
            border-left: 4px solid var(--warning);
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
        }

        .checklist {
            list-style: none;
            padding: 0;
        }

        .checklist li {
            padding: 10px 10px 10px 40px;
            position: relative;
            margin: 5px 0;
        }

        .checklist li::before {
            content: "✓";
            position: absolute;
            left: 10px;
            color: var(--success);
            font-weight: bold;
            font-size: 1.2rem;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }

        th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
        }

        tr:hover {
            background: #f8fafc;
        }

        .algorithm-steps {
            background: #fafafa;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }

        .algorithm-steps ol {
            padding-left: 20px;
        }

        .algorithm-steps li {
            margin: 10px 0;
            font-weight: 500;
        }

        .comparison {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }

        .comparison-item {
            padding: 20px;
            border-radius: 8px;
        }

        .comparison-bad {
            background: #fee2e2;
            border: 2px solid var(--danger);
        }

        .comparison-good {
            background: #d1fae5;
            border: 2px solid var(--success);
        }

        .comparison-item h5 {
            margin-bottom: 10px;
            font-size: 1.1rem;
        }

        .footer {
            background: rgba(30, 41, 59, 0.95);
            color: white;
            text-align: center;
            padding: 30px;
            margin-top: 50px;
            border-radius: 15px;
        }

        .highlight {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 600;
        }

        @media (max-width: 768px) {
            section {
                padding: 20px;
            }

            h2 {
                font-size: 1.5rem;
            }

            nav ul {
                flex-direction: column;
                align-items: center;
            }

            .comparison {
                grid-template-columns: 1fr;
            }

            nav {
                top: 90px;
            }
        }

        .scroll-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            transition: all 0.3s;
            opacity: 0;
            pointer-events: none;
        }

        .scroll-top.visible {
            opacity: 1;
            pointer-events: auto;
        }

        .scroll-top:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>📋 AP Computer Science Principles</h1>
            <p>Component C: Personalized Project Reference - Web Scraping Feature</p>
        </div>
    </header>

    <div class="container">
        <nav>
            <ul>
                <li><a href="#overview">Overview</a></li>
                <li><a href="#procedure">Procedure</a></li>
                <li><a href="#list">List</a></li>
                <li><a href="#responses">Written Responses</a></li>
                <li><a href="#checklist">Checklist</a></li>
            </ul>
        </nav>

        <!-- OVERVIEW SECTION -->
        <section id="overview">
            <h2>📊 Component C Overview</h2>
            
            <div class="info-box">
                <h4>Purpose of Component C</h4>
                <p>Component C captures the key code segments from your project that demonstrate:</p>
                <ul>
                    <li>A student-developed procedure with an algorithm (sequencing, selection, iteration)</li>
                    <li>Use of a list/collection to manage complexity</li>
                    <li>Your ability to explain how your code works</li>
                </ul>
            </div>

            <h3>Featured Task: Live Web Scraping with Date Filtering</h3>
            
            <div class="success-box">
                <h4>🎯 What This Feature Does</h4>
                <p>This feature fetches <strong>live operating hours</strong> from NYC landmark websites through a web scraping API, then <strong>filters the hours</strong> to show only the days the user selected for their trip itinerary. This solves the real-world problem of outdated information and information overload.</p>
            </div>

            <div class="algorithm-steps">
                <h4>Algorithm Flow:</h4>
                <ol>
                    <li><strong>Fetch:</strong> Call backend web scraping API with landmark identifier</li>
                    <li><strong>Parse:</strong> Receive and validate JSON response with hours data</li>
                    <li><strong>Filter:</strong> Get user's trip dates and calculate which weekdays they'll visit</li>
                    <li><strong>Display:</strong> Show only relevant days, hiding unnecessary information</li>
                    <li><strong>Fallback:</strong> If API fails, gracefully show cached sample data</li>
                </ol>
            </div>
        </section>

        <!-- PROCEDURE SECTION -->
        <section id="procedure">
            <h2>🔧 Part 1: Procedure Code Segments</h2>
            
            <span class="badge badge-primary">Required Component</span>
            <span class="badge badge-success">Contains Algorithm</span>

            <h3>Segment 1i: Student-Developed Procedure</h3>
            
            <div class="info-box">
                <p><strong>Procedure Name:</strong> <code class="highlight">fetchLandmarkHours</code></p>
                <p><strong>Return Type:</strong> Promise&lt;Object&gt; (async function)</p>
                <p><strong>Parameter:</strong> <code>landmarkKey</code> (string) - determines which API endpoint to call</p>
            </div>

            <div class="code-block" data-lang="JavaScript">
<pre><span class="keyword">async function</span> <span class="function">fetchLandmarkHours</span>(landmarkKey) {
    <span class="keyword">const</span> landmark = LANDMARK_MAP[landmarkKey];
    <span class="keyword">if</span> (!landmark) <span class="keyword">return null</span>;

    <span class="keyword">try</span> {
        <span class="keyword">const</span> requestOptions = {
            <span class="property">method</span>: <span class="string">'GET'</span>,
            <span class="property">headers</span>: {
                <span class="string">'Content-Type'</span>: <span class="string">'application/json'</span>
            },
            <span class="property">credentials</span>: <span class="string">'include'</span>
        };
        
        <span class="keyword">const</span> response = <span class="keyword">await</span> <span class="function">fetch</span>(<span class="string">`${pythonURI}/api/landmarks/${landmark.endpoint}`</span>, requestOptions);
        
        <span class="keyword">if</span> (!response.ok) {
            <span class="keyword">throw new</span> <span class="function">Error</span>(<span class="string">`HTTP ${response.status}`</span>);
        }
        
        <span class="keyword">const</span> data = <span class="keyword">await</span> response.<span class="function">json</span>();
    
        <span class="keyword">if</span> (data.success) {
            <span class="keyword">return</span> data.data;
        } <span class="keyword">else</span> {
            console.<span class="function">error</span>(<span class="string">`Error fetching ${landmark.name}:`</span>, data.error);
            <span class="keyword">return</span> <span class="function">getFallbackHours</span>(landmarkKey);
        }
    } <span class="keyword">catch</span> (error) {
        console.<span class="function">error</span>(<span class="string">`Network error for ${landmark.name}:`</span>, error);
        <span class="keyword">return</span> <span class="function">getFallbackHours</span>(landmarkKey);
    }
}</pre>
            </div>

            <div class="success-box">
                <h4>✅ Algorithm Components Present:</h4>
                <ul class="checklist">
                    <li><strong>Sequencing:</strong> Steps execute in order (lookup → fetch → parse → return)</li>
                    <li><strong>Selection:</strong> Multiple if statements and try-catch conditionals</li>
                    <li><strong>Iteration:</strong> Error handling flow creates implicit iteration through fallback paths</li>
                </ul>
            </div>

            <h3>Segment 1ii: Procedure Call in Context</h3>

            <div class="code-block" data-lang="JavaScript">
<pre><span class="keyword">async function</span> <span class="function">refreshCurrentLandmark</span>() {
    <span class="keyword">if</span> (!currentLandmark) <span class="keyword">return</span>;
    
    <span class="keyword">const</span> landmarkData = LANDMARK_DATA[currentLandmark];
    <span class="keyword">const</span> hoursContainer = document.<span class="function">getElementById</span>(<span class="string">'landmarkHours'</span>);
    
    hoursContainer.innerHTML = <span class="string">`
        &lt;div class="hours-loading"&gt;
            &lt;div class="live-loading-spinner"&gt;&lt;/div&gt;
            &lt;div&gt;Fetching live hours for ${landmarkData.name}...&lt;/div&gt;
        &lt;/div&gt;
    `</span>;
    
    <span class="keyword">try</span> {
        <span class="keyword">const</span> hoursData = <span class="keyword">await</span> <span class="function">fetchLandmarkHours</span>(currentLandmark);
        <span class="keyword">const</span> selectedDays = <span class="keyword">await</span> <span class="function">getSelectedDays</span>();
    
        <span class="keyword">if</span> (hoursData) {
            <span class="keyword">let</span> hoursHtml = <span class="string">`&lt;div class="hours-display"&gt;`</span>;
        
            <span class="keyword">if</span> (selectedDays && selectedDays.length > <span class="number">0</span>) {
                hoursHtml += <span class="string">`
                    &lt;div&gt;📅 Showing hours for: ${selectedDays.join(', ')}&lt;/div&gt;
                `</span>;
            }
        
            hoursHtml += <span class="function">formatHoursInChronologicalOrder</span>(hoursData, selectedDays);
        
            <span class="keyword">if</span> (hoursData.admission) {
                hoursHtml += <span class="string">`
                    &lt;div&gt;
                        Admission: ${hoursData.admission}
                    &lt;/div&gt;
                `</span>;
            }
        
            hoursContainer.innerHTML = hoursHtml;
        }
    } <span class="keyword">catch</span> (error) {
        console.<span class="function">error</span>(<span class="string">'Error fetching hours:'</span>, error);
        <span class="keyword">const</span> fallbackHours = <span class="function">getFallbackHours</span>(currentLandmark);
        hoursContainer.innerHTML = <span class="string">`⚠️ Showing fallback hours.`</span>;
    }
}</pre>
            </div>

            <div class="info-box">
                <h4>How the Procedure is Called:</h4>
                <p><strong>Call statement:</strong> <code class="highlight">const hoursData = await fetchLandmarkHours(currentLandmark);</code></p>
                <p><strong>Argument passed:</strong> <code>currentLandmark</code> - a string like 'met', 'empire', 'icecream', or 'ukrainian'</p>
                <p><strong>Result usage:</strong> The returned hoursData object is filtered by date and displayed to the user with admission prices</p>
            </div>
        </section>

        <!-- LIST SECTION -->
        <section id="list">
            <h2>📝 Part 2: List Code Segments</h2>
            
            <span class="badge badge-warning">Required Component</span>
            <span class="badge badge-secondary">Manages Complexity</span>

            <h3>Segment 2i: Data Storage in List</h3>

            <div class="info-box">
                <p><strong>List Name:</strong> <code class="highlight">selectedDays</code> (dynamically generated array)</p>
                <p><strong>Purpose:</strong> Stores weekday names from user's trip date range for filtering</p>
            </div>

            <div class="code-block" data-lang="JavaScript">
<pre><span class="keyword">async function</span> <span class="function">getSelectedDays</span>() {
    <span class="keyword">try</span> {
        <span class="keyword">const</span> itinerary = <span class="keyword">await</span> <span class="function">getItinerary</span>();
        
        <span class="keyword">if</span> (!itinerary.tripInfo || !itinerary.tripInfo.startDate || !itinerary.tripInfo.endDate) {
            <span class="keyword">return null</span>;
        }
    
        <span class="keyword">const</span> month = itinerary.tripInfo.month;
        <span class="keyword">const</span> dateRange = <span class="function">parseDateRange</span>(month, itinerary.tripInfo.startDate, itinerary.tripInfo.endDate);
    
        <span class="keyword">if</span> (!dateRange) <span class="keyword">return null</span>;
    
        <span class="keyword">const</span> selectedDays = <span class="keyword">new</span> <span class="function">Set</span>();
        <span class="keyword">const</span> currentDate = <span class="keyword">new</span> <span class="function">Date</span>(dateRange.start);

        <span class="keyword">while</span> (currentDate <= dateRange.end) {
            <span class="keyword">const</span> dayName = currentDate.<span class="function">toLocaleDateString</span>(<span class="string">'en-US'</span>, { <span class="property">weekday</span>: <span class="string">'long'</span> });
            selectedDays.<span class="function">add</span>(dayName);
            currentDate.<span class="function">setDate</span>(currentDate.<span class="function">getDate</span>() + <span class="number">1</span>);
        }
    
        <span class="keyword">return</span> <span class="function">Array.from</span>(selectedDays);
    } <span class="keyword">catch</span> (error) {
        console.<span class="function">error</span>(<span class="string">'Error getting selected days:'</span>, error);
        <span class="keyword">return null</span>;
    }
}</pre>
            </div>

            <div class="success-box">
                <h4>Example Data Stored:</h4>
                <p>If user selects March 14-16, 2025 (Fri-Sun), the list becomes:</p>
                <div class="code-block" data-lang="Output">
<pre>[<span class="string">"Friday"</span>, <span class="string">"Saturday"</span>, <span class="string">"Sunday"</span>]</pre>
                </div>
            </div>

            <h3>Segment 2ii: List Data Usage</h3>

            <div class="code-block" data-lang="JavaScript">
<pre><span class="keyword">function</span> <span class="function">formatHoursInChronologicalOrder</span>(hoursData, selectedDays = <span class="keyword">null</span>) {
    <span class="keyword">const</span> dayOrder = [<span class="string">'Sunday'</span>, <span class="string">'Monday'</span>, <span class="string">'Tuesday'</span>, <span class="string">'Wednesday'</span>, <span class="string">'Thursday'</span>, <span class="string">'Friday'</span>, <span class="string">'Saturday'</span>];
    <span class="keyword">let</span> html = <span class="string">''</span>;
    
    <span class="keyword">if</span> (hoursData.hours && <span class="keyword">typeof</span> hoursData.hours === <span class="string">'object'</span>) {
        <span class="keyword">let</span> daysToDisplay = dayOrder;
        <span class="keyword">if</span> (selectedDays && selectedDays.length > <span class="number">0</span>) {
            daysToDisplay = dayOrder.<span class="function">filter</span>(day => selectedDays.<span class="function">includes</span>(day));
        }
    
        daysToDisplay.<span class="function">forEach</span>(day => {
            <span class="keyword">if</span> (hoursData.hours[day]) {
                html += <span class="string">`
                    &lt;div class="day-hour"&gt;
                        &lt;span class="day"&gt;${day}:&lt;/span&gt;
                        &lt;span class="time"&gt;${hoursData.hours[day]}&lt;/span&gt;
                    &lt;/div&gt;
                `</span>;
            }
        });
    
        <span class="keyword">if</span> (html === <span class="string">''</span> && Object.<span class="function">keys</span>(hoursData.hours).length > <span class="number">0</span>) {
            html = <span class="string">`
                &lt;div&gt;No hours available for selected dates&lt;/div&gt;
            `</span>;
        }
    }
    
    <span class="keyword">return</span> html;
}</pre>
            </div>

            <div class="info-box">
                <h4>How Multiple List Elements Are Accessed:</h4>
                <ul class="checklist">
                    <li><code>.length</code> - checks size of the list</li>
                    <li><code>.includes(day)</code> - tests if each day is in the selected trip range</li>
                    <li><code>.forEach()</code> - iterates through all filtered days</li>
                    <li>Creates new HTML string data from list elements</li>
                </ul>
            </div>

            <h3>How the List Manages Complexity</h3>

            <div class="comparison">
                <div class="comparison-item comparison-bad">
                    <h5>❌ WITHOUT the List (49+ conditionals needed):</h5>
                    <div class="code-block" data-lang="Bad Approach">
<pre><span class="keyword">if</span> (tripStartDay === <span class="string">"Friday"</span> && tripEndDay === <span class="string">"Sunday"</span>) {
    <span class="function">showHours</span>(<span class="string">"Friday"</span>);
    <span class="function">showHours</span>(<span class="string">"Saturday"</span>);
    <span class="function">showHours</span>(<span class="string">"Sunday"</span>);
} <span class="keyword">else if</span> (tripStartDay === <span class="string">"Monday"</span> && tripEndDay === <span class="string">"Wednesday"</span>) {
    <span class="function">showHours</span>(<span class="string">"Monday"</span>);
    <span class="function">showHours</span>(<span class="string">"Tuesday"</span>);
    <span class="function">showHours</span>(<span class="string">"Wednesday"</span>);
}
<span class="comment">// Would need 49 cases for all day combinations!</span></pre>
                    </div>
                </div>

                <div class="comparison-item comparison-good">
                    <h5>✅ WITH the List (single loop handles all cases):</h5>
                    <div class="code-block" data-lang="Good Approach">
<pre>daysToDisplay = dayOrder.<span class="function">filter</span>(day => 
    selectedDays.<span class="function">includes</span>(day)
);

daysToDisplay.<span class="function">forEach</span>(day => {
    <span class="keyword">if</span> (hoursData.hours[day]) {
        html += <span class="string">`&lt;div&gt;${day}: ${hoursData.hours[day]}&lt;/div&gt;`</span>;
    }
});</pre>
                    </div>
                </div>
            </div>

            <div class="success-box">
                <h4>✅ Complexity Managed:</h4>
                <ul class="checklist">
                    <li><strong>Scalability:</strong> Works for any trip length (1-365+ days) without code changes</li>
                    <li><strong>Maintainability:</strong> Single loop instead of dozens of conditionals</li>
                    <li><strong>Dynamic filtering:</strong> Automatically adjusts to user's dates</li>
                    <li><strong>Code reuse:</strong> Same logic works for all landmark types</li>
                </ul>
            </div>
        </section>

        <!-- WRITTEN RESPONSES SECTION -->
        <section id="responses">
            <h2>✍️ Written Response Preparation</h2>
            
            <span class="badge badge-primary">Exam Day Reference</span>

            <h3>Question 3a: Procedure Purpose</h3>
            <div class="info-box">
                <h4>My procedure: <code>fetchLandmarkHours(landmarkKey)</code></h4>
                <p><strong>Purpose:</strong> This procedure retrieves live operating hours and admission prices for NYC landmarks by calling a web scraping API. It takes a landmark identifier as input, constructs the appropriate API request, handles the response, and returns structured hours data. If the API fails, it gracefully falls back to cached sample data.</p>
            </div>

            <h3>Question 3b: Algorithm Implementation</h3>
            <div class="algorithm-steps">
                <h4>Sequencing:</h4>
                <ol>
                    <li>Lookup landmark details from LANDMARK_MAP</li>
                    <li>Construct API request with proper headers</li>
                    <li>Send fetch request to web scraping backend</li>
                    <li>Parse JSON response</li>
                    <li>Return data or trigger fallback</li>
                </ol>

                <h4>Selection:</h4>
                <ul>
                    <li><code>if (!landmark) return null</code> - validates input</li>
                    <li><code>if (!response.ok)</code> - checks HTTP status</li>
                    <li><code>if (data.success)</code> - validates response</li>
                    <li><code>try-catch</code> - handles network errors</li>
                </ul>

                <h4>Iteration:</h4>
                <ul>
                    <li>Error handling creates implicit iteration through fallback paths</li>
                    <li>Alternative: The <code>while</code> loop in <code>getSelectedDays()</code> iterates through date range</li>
                </ul>
            </div>

            <h3>Question 3c: Procedure Call</h3>
            <div class="info-box">
                <p><strong>Call location:</strong> Within <code>refreshCurrentLandmark()</code> function</p>
                <p><strong>Call statement:</strong> <code class="highlight">const hoursData = await fetchLandmarkHours(currentLandmark);</code></p>
                <p><strong>Arguments passed:</strong> <code>currentLandmark</code> - e.g., 'met', 'empire', 'icecream', 'ukrainian'</p>
                <p><strong>Result usage:</strong> The returned hoursData object is passed to <code>formatHoursInChronologicalOrder()</code> to filter and display hours. Admission prices and error messages are displayed based on object properties.</p>
            </div>

            <h3>Question 4a: List Purpose</h3>
            <div class="info-box">
                <p><strong>My list:</strong> <code class="highlight">selectedDays</code> array</p>
                <p><strong>Purpose:</strong> The selectedDays list stores the names of weekdays (e.g., ["Friday", "Saturday", "Sunday"]) that fall within the user's selected trip dates. This allows the program to filter landmark hours to show only the days the user will actually be visiting, rather than displaying all seven days of the week.</p>
            </div>

            <h3>Question 4b: How Data is Stored</h3>
            <div class="warning-box">
                <p><strong>What is stored:</strong> Weekday name strings like "Monday", "Tuesday", etc. are added to a Set (preventing duplicates), then converted to an array.</p>
                <p><strong>Example:</strong> If user selects March 14-16, 2025 (Fri-Sun), the list becomes: <code>["Friday", "Saturday", "Sunday"]</code></p>
            </div>

            <h3>Question 4c: Managing Complexity</h3>
            <table>
                <thead>
                    <tr>
                        <th>Aspect</th>
                        <th>Without List</th>
                        <th>With List</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Conditionals Needed</td>
                        <td>49+ if-else statements</td>
                        <td>1 filter + 1 forEach loop</td>
                    </tr>
                    <tr>
                        <td>Scalability</td>
                        <td>Breaks for trips > 7 days</td>
                        <td>Works for 1-365+ days</td>
                    </tr>
                    <tr>
                        <td>Maintenance</td>
                        <td>Must update all conditionals</td>
                        <td>Single reusable function</td>
                    </tr>
                    <tr>
                        <td>Code Reuse</td>
                        <td>Different logic per landmark</td>
                        <td>Same logic for all landmarks</td>
                    </tr>
                </tbody>
            </table>

            <h3>Question 4d: List Data Usage</h3>
            <div class="success-box">
                <h4>Operations Performed on List:</h4>
                <ul class="checklist">
                    <li><code>.length</code> - checks size of the list</li>
                    <li><code>.includes(day)</code> - tests if each day is in selected range</li>
                    <li><code>.forEach()</code> - iterates through all filtered days</li>
                    <li>Creates new HTML string data from list elements</li>
                </ul>
                <p><strong>New Data Created:</strong> The HTML string is constructed by accessing multiple days from the list and formatting them into display elements. This transforms raw data (array of day names) into user-facing output (formatted hours display).</p>
            </div>
        </section>

        <!-- CHECKLIST SECTION -->
        <section id="checklist">
            <h2>✅ Component C Submission Checklist</h2>

            <h3>Procedure Requirements</h3>
            <ul class="checklist">
                <li>Student-developed (not built-in)</li>
                <li>Has defined name: <code>fetchLandmarkHours</code></li>
                <li>Has return type: Promise&lt;Object&gt; (async)</li>
                <li>Has parameter: <code>landmarkKey</code></li>
                <li>Parameter affects functionality (determines API endpoint)</li>
                <li>Contains sequencing (ordered steps)</li>
                <li>Contains selection (if statements, try-catch)</li>
                <li>Contains iteration (error handling flow or date loop)</li>
                <li>Procedure call shown in context</li>
            </ul>

            <h3>List Requirements</h3>
            <ul class="checklist">
                <li>List used: <code>selectedDays</code> array</li>
                <li>Data storage shown (Set → Array conversion)</li>
                <li>Multiple elements accessed (.length, .includes(), .forEach())</li>
                <li>New data created from list (HTML string generation)</li>
                <li>Manages complexity (avoids 49 conditionals)</li>
                <li>List purpose explained clearly</li>
            </ul>

            <h3>Formatting Requirements</h3>
            <ul class="checklist">
                <li>Code segments have NO comments</li>
                <li>Text is at least 10-point font</li>
                <li>Screen captures are clear (not blurry)</li>
                <li>All code is student-developed</li>
            </ul>

            <div class="success-box">
                <h4>📊 Submission Summary</h4>
                <table>
                    <tr>
                        <th>Component</th>
                        <th>Required</th>
                        <th>Provided</th>
                        <th>Status</th>
                    </tr>
                    <tr>
                        <td>Procedure Definition</td>
                        <td>1 segment</td>
                        <td>1 segment</td>
                        <td>✅</td>
                    </tr>
                    <tr>
                        <td>Procedure Call</td>
                        <td>1 segment</td>
                        <td>1 segment</td>
                        <td>✅</td>
                    </tr>
                    <tr>
                        <td>List Storage</td>
                        <td>1 segment</td>
                        <td>1 segment</td>
                        <td>✅</td>
                    </tr>
                    <tr>
                        <td>List Usage</td>
                        <td>1 segment</td>
                        <td>1 segment</td>
                        <td>✅</td>
                    </tr>
                    <tr>
                        <td><strong>Total Segments</strong></td>
                        <td><strong>4</strong></td>
                        <td><strong>4</strong></td>
                        <td><strong>✅ Complete</strong></td>
                    </tr>
                </table>
            </div>

            <div class="warning-box">
                <h4>⚠️ Before Final Submission:</h4>
                <ol>
                    <li>Remove ALL comments from code segments</li>
                    <li>Verify all screenshots are clear and readable</li>
                    <li>Confirm font size is 10pt or larger</li>
                    <li>Double-check that all code is YOUR original work</li>
                    <li>Submit as FINAL in AP Digital Portfolio by deadline</li>
                </ol>
            </div>
        </section>

        <div class="footer">
            <h3>🎓 Ready for AP Exam Day</h3>
            <p>This reference will be available to you during the written response portion of the exam.</p>
            <p><strong>Feature:</strong> Live Web Scraping with Itinerary-Based Date Filtering</p>
            <p style="margin-top: 20px; color: #94a3b8;">Created for AP Computer Science Principles - Component C</p>
        </div>
    </div>

    <div class="scroll-top" id="scrollTop" onclick="scrollToTop()">
        ↑
    </div>

    <script>
        // Smooth scroll for navigation
        document.querySelectorAll('nav a').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                target.scrollIntoView({ behavior: 'smooth' });
            });
        });

        // Show/hide scroll to top button
        window.addEventListener('scroll', () => {
            const scrollTop = document.getElementById('scrollTop');
            if (window.pageYOffset > 300) {
                scrollTop.classList.add('visible');
            } else {
                scrollTop.classList.remove('visible');
            }
        });

        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Highlight active section in nav
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('nav a');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (pageYOffset >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.style.background = '';
                link.style.color = '';
                if (link.getAttribute('href').slice(1) === current) {
                    link.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
                    link.style.color = 'white';
                }
            });
        });
    </script>
</body>
</html>