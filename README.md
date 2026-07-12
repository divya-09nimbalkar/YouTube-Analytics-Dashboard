
---

```markdown
# 📊 YouTube Analytics Dashboard

A data engineering project that simulates a YouTube analytics pipeline.  
It demonstrates ETL (Extract → Transform → Load), model training, and an interactive Streamlit dashboard for visualizing video performance metrics.

---

## 🚀 Features
- **Extract**: Generates dummy YouTube video data (or fetches via API if configured).
- **Transform**: Cleans and processes raw CSVs into structured datasets.
- **Load**: Saves processed data into the `data/processed/` folder.
- **Train**: Builds a simple regression model to predict video engagement.
- **Predict**: Runs predictions on processed data.
- **Dashboard**: Interactive Streamlit app with charts for views, likes, and comments.

---

## 📂 Project Structure
```
YouTube_Analytics_Dashboard/
│
├── data/
│   ├── raw/              # raw YouTube API data
│   └── processed/        # cleaned/aggregated data
│
├── docs/                 # documentation
├── models/               # trained ML models (e.g., engagement prediction)
├── notebooks/            # Jupyter notebooks for exploration
│
├── src/                  # source code
│   ├── __init__.py
│   ├── main.py           # entry point
│   ├── extract.py        # fetch data from YouTube API
│   ├── transform.py      # clean/aggregate data
│   ├── load.py           # save to DB or CSV
│   ├── dashboard.py      # Streamlit dashboard
│   └── train.py          # ML model training
│
├── tests/                # unit tests
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_train.py
│
├── .gitignore
├── README.md
└── requirements.txt

```

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/YouTube_Analytics_Dashboard.git
   cd YouTube_Analytics_Dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

### Step 1: Extract dummy data
```bash
python -m src.extract
```
Creates `data/raw/youtube_sample.csv`.

### Step 2: Transform & Load
```bash
python -m src.transform
python -m src.load
```
Creates `data/processed/youtube_data.csv`.

### Step 3: Train model
```bash
python -m src.train
```
Saves model to `models/youtube_model.pkl`.

### Step 4: Run dashboard
```bash
streamlit run src/dashboard.py
```
Opens the interactive dashboard at `http://localhost:8501`.

---

## 📓 Jupyter Notebook
A demo notebook is included in `notebooks/pipeline_demo.ipynb` to run the full pipeline interactively:
- Extract dummy data
- Transform and save processed CSV
- Train model
- Predict values
- Visualize results

---

## 🔮 Future Improvements
- Integrate with **YouTube Data API v3** for real channel analytics.
- Add more advanced ML models (e.g., engagement prediction).
- Expand dashboard with subscriber growth, watch time, and trending analysis.

---

## 🏷️ License
This project is for educational purposes.  
Feel free to fork and adapt it for your own use.
```

