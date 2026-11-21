# Forecasting next week's wholesale vegetable prices at Keppetipola

The executed Python notebook goes from the publisher CSV to a chronological test of bagging, boosting, stacking and a last-week baseline. Each example forecasts one vegetable for one target week. On the 176 held-out examples, the baseline led with an average error of Rs. 27.89/kg. Gradient Boosting and stacking both scored Rs. 28.26/kg, followed by Random Forest at Rs. 30.53/kg.

## Run locally

Extract the ZIP, open PowerShell in the directory containing this README, and use Python 3.12. The existing assignment environment can also run the dashboard with `..\.venv\Scripts\python.exe dashboard.py` from the Keppetipola directory.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe dashboard.py
```

Open <http://127.0.0.1:8766/>. Choose a vegetable and forecast week, compare the three estimates, then reveal the observed price. The application loads the saved models and checks their predictions against the notebook results.

## Reproduce the analysis

Open `market_forecast.ipynb` in VS Code with Jupyter support. Select the project environment and run all cells from this directory. The notebook rebuilds the models, predictions and error breakdown under `results/`. The MP4 is a separate submission file.

## Source and disclosure

Anton Jayakody compiled the Keppetipola wholesale price data from market bulletins. The publisher describes the dataset as Apache 2.0 licensed. The source CSV is preserved in `data/prices.csv`; the licence text is in the same folder. [Zenodo record](https://zenodo.org/records/24214018) · [Publisher's datasheet](https://github.com/tobijay666/Sri-Lankan-Agri-Food-Economic-Open-Data).

ChatGPT generated the notebook, analysis, dashboard and presentation materials. The supplied demonstration uses synthetic English narration.
