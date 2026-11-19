\<div align="center">

\<h1>🌾 PANGAN ALERT AI\</h1>

\<h3>Food Indicator Analysis & Machine Learning Clustering\</h3>

\<p>
\<strong>Turning Food Indicators Into Understandable Insights.\</strong>
\</p>

\<p>
An interactive web application for analyzing food indicators using
\<strong>Machine Learning, K-Means Clustering, and Data Visualization.\</strong>
\</p>

\<p>
\<img src="[https://img.shields.io/badge/Python-3.12-blue?logo=python](https://img.shields.io/badge/Python-3.12-blue?logo=python)" />
\<img src="[https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)" />
\<img src="[https://img.shields.io/badge/Machine_Learning-K--Means-orange](https://img.shields.io/badge/Machine_Learning-K--Means-orange)" />
\<img src="[https://img.shields.io/badge/Scikit--learn-ML-yellow?logo=scikitlearn](https://img.shields.io/badge/Scikit--learn-ML-yellow?logo=scikitlearn)" />
\<img src="[https://img.shields.io/badge/Status-Development-green](https://img.shields.io/badge/Status-Development-green)" />
\</p>

\</div>

---

\<h2>📌 About The Project\</h2>

\<p>
\<strong>PANGAN ALERT AI\</strong> is a web-based application designed to analyze and visualize food indicator data through Machine Learning.
\</p>

\<p>
The application utilizes the \<strong>K-Means Clustering\</strong> algorithm to identify patterns and group observations based on similarities in their food indicator values.
\</p>

\<p>
By combining data processing, machine learning, and interactive visualization, PANGAN ALERT AI transforms raw data into information that is easier to explore, understand, and interpret.
\</p>

\<h3>🎯 Project Objectives\</h3>

\<ul>
\<li>Explore patterns within food indicator datasets.\</li>
\<li>Group observations based on indicator similarities.\</li>
\<li>Present analytical results through interactive visualizations.\</li>
\<li>Make data exploration more accessible through a web interface.\</li>
\<li>Demonstrate the implementation of Machine Learning in web development.\</li>
\</ul>

---

\<h2>✨ Features\</h2>

\<table>
\<tr>
\<td width="50%">
\<h3>📊 Interactive Dashboard\</h3>
\<p>Displays dataset summaries, total commodities, cluster information, and the latest available observation period.\</p>
\</td>
\<td width="50%">
\<h3>🤖 AI Clustering Analysis\</h3>
\<p>Uses a trained K-Means model to group food indicator data based on similarities between QIPA, AIPA, and IFPA.\</p>
\</td>
\</tr>
\<tr>
\<td width="50%">
\<h3>🔎 Commodity Analysis\</h3>
\<p>Analyze specific commodities based on available monthly and yearly observations.\</p>
\</td>
\<td width="50%">
\<h3>📈 Data Visualization\</h3>
\<p>Explore indicator trends and status distributions through graphical representations.\</p>
\</td>
\</tr>
\<tr>
\<td width="50%">
\<h3>🧩 Cluster Profiling\</h3>
\<p>Understand the characteristics of each cluster through its indicator values.\</p>
\</td>
\<td width="50%">
\<h3>📋 Data Explorer\</h3>
\<p>Explore the dataset through a structured table containing the available observations.\</p>
\</td>
\</tr>
\</table>

---

\<h2>🧠 Machine Learning Approach\</h2>

\<h3>Algorithm: K-Means Clustering\</h3>

\<p>
K-Means is an unsupervised machine learning algorithm that groups data points into clusters based on their similarities.
\</p>

\<p>
In PANGAN ALERT AI, the model uses three main features:
\</p>

\<table>
\<thead>
\<tr>
\<th>Feature\</th>
\<th>Description\</th>
\</tr>
\</thead>
\<tbody>
\<tr>
\<td>\<strong>QIPA\</strong>\</td>
\<td>Food indicator variable included in the dataset.\</td>
\</tr>
\<tr>
\<td>\<strong>AIPA\</strong>\</td>
\<td>Food indicator variable included in the dataset.\</td>
\</tr>
\<tr>
\<td>\<strong>IFPA\</strong>\</td>
\<td>Food indicator variable included in the dataset.\</td>
\</tr>
\</tbody>
\</table>

\<h3>⚙️ Analytical Workflow\</h3>

\<ol>
\<li>Load the food indicator dataset.\</li>
\<li>Validate the required columns and data types.\</li>
\<li>Select QIPA, AIPA, and IFPA as model features.\</li>
\<li>Standardize the data using \<code>StandardScaler\</code>.\</li>
\<li>Process the standardized data using the trained K-Means model.\</li>
\<li>Assign each observation to its corresponding cluster.\</li>
\<li>Transform cluster centers back to their original scale for interpretation.\</li>
\<li>Display the analysis results through the web dashboard.\</li>
\</ol>

\<h3>Workflow Diagram\</h3>

\<pre>
┌──────────────────────────┐
│   Food Indicator Data   │
└────────────┬─────────────┘
&#x20;            ↓
┌──────────────────────────┐
│   Data Preprocessing    │
└────────────┬─────────────┘
&#x20;            ↓
┌──────────────────────────┐
│    StandardScaler       │
└────────────┬─────────────┘
&#x20;            ↓
┌──────────────────────────┐
│   K-Means Clustering    │
└────────────┬─────────────┘
&#x20;            ↓
┌──────────────────────────┐
│   Cluster Assignment    │
└────────────┬─────────────┘
&#x20;            ↓
┌──────────────────────────┐
│   Cluster Profiling     │
└────────────┬─────────────┘
&#x20;            ↓
┌──────────────────────────┐
│   Interactive Dashboard  │
└──────────────────────────┘
\</pre>

---

\<h2>📊 Dataset\</h2>

\<p>
The application uses a food indicator dataset containing observations by commodity and period.
\</p>

\<h3>Dataset Attributes\</h3>

\<table>
\<thead>
\<tr>
\<th>Column\</th>
\<th>Description\</th>
\</tr>
\</thead>
\<tbody>
\<tr>\<td>\<code>Tahun\</code>\</td>\<td>Observation year\</td>\</tr>
\<tr>\<td>\<code>Bulan\</code>\</td>\<td>Observation month\</td>\</tr>
\<tr>\<td>\<code>Komoditas\</code>\</td>\<td>Food commodity\</td>\</tr>
\<tr>\<td>\<code>QIPA\</code>\</td>\<td>Indicator value\</td>\</tr>
\<tr>\<td>\<code>AIPA\</code>\</td>\<td>Indicator value\</td>\</tr>
\<tr>\<td>\<code>IFPA\</code>\</td>\<td>Indicator value\</td>\</tr>
\<tr>\<td>\<code>Status\</code>\</td>\<td>Recorded dataset status\</td>\</tr>
\</tbody>
\</table>

\<p>
The dataset is processed locally by the application and used for dashboard visualizations and clustering analysis.
\</p>

---

\<h2>🖥️ Application Preview\</h2>

\<p align="center">
\<img src="docs/assets/dashboard.png" alt="PANGAN ALERT AI Dashboard Preview" width="100%" />
\</p>

\<p align="center">
\<em>Dashboard preview — replace this image with an actual screenshot of the application.\</em>
\</p>

---

\<h2>🛠️ Tech Stack\</h2>

\<table>
\<thead>
\<tr>
\<th>Technology\</th>
\<th>Purpose\</th>
\</tr>
\</thead>
\<tbody>
\<tr>\<td>Python\</td>\<td>Core programming language\</td>\</tr>
\<tr>\<td>Flask\</td>\<td>Web application backend\</td>\</tr>
\<tr>\<td>Pandas\</td>\<td>Dataset processing\</td>\</tr>
\<tr>\<td>NumPy\</td>\<td>Numerical computation\</td>\</tr>
\<tr>\<td>Scikit-learn\</td>\<td>Machine Learning\</td>\</tr>
\<tr>\<td>Joblib\</td>\<td>Model serialization\</td>\</tr>
\<tr>\<td>HTML5\</td>\<td>Web page structure\</td>\</tr>
\<tr>\<td>CSS3\</td>\<td>Interface styling\</td>\</tr>
\<tr>\<td>JavaScript\</td>\<td>Frontend interactivity\</td>\</tr>
\<tr>\<td>Chart.js\</td>\<td>Data visualization\</td>\</tr>
\<tr>\<td>Git & GitHub\</td>\<td>Version control\</td>\</tr>
\<tr>\<td>Vercel\</td>\<td>Deployment platform\</td>\</tr>
\</tbody>
\</table>

---

\<h2>📂 Project Structure\</h2>

\<pre>
PANGAN-ALERT-AI/
│
├── app.py
├── requirements.txt
├── vercel.json
├── .python-version
├── .gitignore
│
├── data/
│   └── indikator_anomali_pangan_2026.csv
│
├── models/
│   └── pangan_alert_model.joblib
│
├── public/
│   ├── style.css
│   ├── script.js
│   └── images/
│
├── templates/
│   └── index.html
│
└── README.md
\</pre>

\<h3>Folder Description\</h3>

\<ul>
\<li>\<code>app.py\</code> — Main Flask application, data processing, and machine learning analysis.\</li>
\<li>\<code>data/\</code> — Stores the dataset used by the application.\</li>
\<li>\<code>models/\</code> — Stores the trained machine learning model and scaler.\</li>
\<li>\<code>public/\</code> — Contains CSS, JavaScript, and static assets.\</li>
\<li>\<code>templates/\</code> — Contains HTML templates rendered by Flask.\</li>
\<li>\<code>requirements.txt\</code> — Lists the Python dependencies.\</li>
\<li>\<code>vercel.json\</code> — Deployment configuration for Vercel.\</li>
\<li>\<code>.python-version\</code> — Specifies the Python runtime version.\</li>
\</ul>

---

\<h2>🚀 Getting Started\</h2>

\<p>
Follow these instructions to run PANGAN ALERT AI on your local machine.
\</p>

\<h3>Prerequisites\</h3>

\<ul>
\<li>Python 3.12\</li>
\<li>Git\</li>
\<li>Visual Studio Code (recommended)\</li>
\</ul>

\<h3>1. Clone the Repository\</h3>

\<pre>\<code>git clone [https://github.com/USERNAME/PANGAN-ALERT-AI.git](https://github.com/USERNAME/PANGAN-ALERT-AI.git)
\</code>\</pre>

\<h3>2. Navigate to the Project Directory\</h3>

\<pre>\<code>cd PANGAN-ALERT-AI
\</code>\</pre>

\<h3>3. Create a Virtual Environment\</h3>

\<pre>\<code>python -m venv .venv
\</code>\</pre>

\<h3>4. Activate the Virtual Environment\</h3>

\<p>\<strong>Windows Command Prompt:\</strong>\</p>

\<pre>\<code>.venv\Scripts\activate
\</code>\</pre>

\<p>\<strong>Windows PowerShell:\</strong>\</p>

\<pre>\<code>.\\.venv\Scripts\Activate.ps1
\</code>\</pre>

\<h3>5. Install Dependencies\</h3>

\<pre>\<code>pip install -r requirements.txt
\</code>\</pre>

\<h3>6. Verify Dataset and Model\</h3>

\<p>Make sure the required files are available:\</p>

\<pre>\<code>data/indikator_anomali_pangan_2026.csv
models/pangan_alert_model.joblib
\</code>\</pre>

\<h3>7. Run the Application\</h3>

\<pre>\<code>python app.py
\</code>\</pre>

\<h3>8. Open the Application\</h3>

\<p>Open your browser and navigate to:\</p>

\<p align="center">
\<strong>\<a href="[http://127.0.0.1:5000](http://127.0.0.1:5000)">[http://127.0.0.1:5000](http://127.0.0.1:5000)\</a>\</strong>
\</p>

---

\<h2>📖 How to Use\</h2>

\<ol>
\<li>Open the PANGAN ALERT AI dashboard.\</li>
\<li>Select a food commodity from the available options.\</li>
\<li>Select the desired observation period.\</li>
\<li>Click the analysis button.\</li>
\<li>Wait for the clustering result to appear.\</li>
\<li>Review the cluster classification and indicator values.\</li>
\<li>Explore the charts and dataset table for additional information.\</li>
\</ol>

---

\<h2>📦 Requirements\</h2>

\<p>The application uses the following Python packages:\</p>

\<pre>\<code>Flask
pandas
numpy
scikit-learn
joblib
\</code>\</pre>

\<p>Install all packages with:\</p>

\<pre>\<code>pip install -r requirements.txt
\</code>\</pre>

---

\<h2>☁️ Deployment\</h2>

\<p>
PANGAN ALERT AI can be deployed using Vercel with the Flask backend and project dependencies.
\</p>

\<h3>Deployment Steps\</h3>

\<ol>
\<li>Push the project repository to GitHub.\</li>
\<li>Open the Vercel dashboard.\</li>
\<li>Select \<strong>Add New Project\</strong>.\</li>
\<li>Import the PANGAN ALERT AI GitHub repository.\</li>
\<li>Configure the project settings.\</li>
\<li>Deploy the application.\</li>
\<li>Open the deployment URL provided by Vercel.\</li>
\</ol>

\<h3>Deployment Configuration\</h3>

\<p>\<code>vercel.json\</code>\</p>

\<pre>\<code>{
&#x20; "$schema": "[https://openapi.vercel.sh/vercel.json](https://openapi.vercel.sh/vercel.json)",
&#x20; "framework": "flask"
}
\</code>\</pre>

\<p>\<code>.python-version\</code>\</p>

\<pre>\<code>3.12 \</code>\</pre>

\<p> Ensure the dataset, trained model, and required dependencies are available to the deployed application. \</p>

---

\<h2>⚠️ Limitations\</h2>

\<ul>
\<li>The analysis depends on the quality and completeness of the available dataset.\</li>
\<li>K-Means identifies similarities between observations; it does not predict future food prices.\</li>
\<li>Cluster assignments may change when the dataset or model is updated.\</li>
\<li>Machine Learning cluster classifications are analytical outputs, not official food status classifications.\</li>
\<li>Results should be interpreted alongside the original dataset and relevant context.\</li>
\</ul>

---

\<h2>🔮 Future Development\</h2>

\<ul>
\<li>Periodic dataset updates.\</li>
\<li>Additional historical data analysis.\</li>
\<li>Improved data visualization.\</li>
\<li>Cluster evaluation using appropriate metrics.\</li>
\<li>Commodity comparison across different periods.\</li>
\<li>Improved dashboard performance and accessibility.\</li>
\<li>Additional analytical features.\</li>
\</ul>

---

\<h2>👨‍💻 Developer\</h2>

\<p>
Developed as a learning and development project combining:
\</p>

\<ul>
\<li>Data Science\</li>
\<li>Machine Learning\</li>
\<li>Python Programming\</li>
\<li>Web Development\</li>
\<li>Data Visualization\</li>
\</ul>

---

\<h2>📜 Disclaimer\</h2>

\<p>
PANGAN ALERT AI is an educational and analytical application. Its clustering results are intended to support data exploration and understanding.
\</p>

\<p>
The application is not a substitute for official information, professional analysis, or government decision-making.
\</p>

---

\<div align="center">

\<h3>🌾 PANGAN ALERT AI\</h3>

\<p>\<em>Turning Food Indicators Into Understandable Insights.\</em>\</p>

\</div>
