# Next week at Keppetipola · Recording guide

Open the local dashboard, select Beans and the week starting 9 March 2026, and keep the observed price hidden. Record the browser in landscape with your microphone. Rehearse once, check your audio, and finish within three minutes.

| Show | Say |
|---|---|
| Dashboard title | Can last week's wholesale vegetable prices help us plan for next week at Keppetipola market? I compared bagging, boosting and stacking with a simple rule: use the most recent week's price. The target is the average reported wholesale price per kilogram in the following week. |
| Vegetable and week selectors | The dataset covers sixteen vegetables. I used observed prices and excluded entries flagged as carried forward. To handle gaps, each example needs three consecutive weeks of historical prices and at least three observed days in every week used. The final eleven eligible weeks were held back for testing. |
| Beans forecasts | Consider beans for the week starting March ninth. The previous week averaged 270 rupees per kilogram. Random Forest averaged many trees and predicted about 269 rupees. Gradient Boosting added trees sequentially and predicted about 258. The stack made the same forecast because earlier validation weeks gave all the weight to boosting. |
| Reveal observed price | The observed average was about 234 rupees per kilogram. All three forecasts were high. Boosting came closer than repeating the last week's price on this occasion. |
| Overall comparison | Across 176 vegetable and week combinations, repeating the previous price had the smallest average absolute error, about 28 rupees per kilogram. Boosting and stacking were slightly behind, followed by Random Forest. The two trained models often missed in the same direction, limiting the benefit of combining them. |
| Movement table | Boosting improved on the baseline for the 63 larger moves. For the 113 smaller moves, keeping the price unchanged worked better. Those smaller moves were more frequent, which explains the overall ranking. These results describe one market and eleven test weeks. ChatGPT generated the project code, explanations and demo script. |

The supplied MP4 uses a synthetic English voice. For your own recording, pause after revealing the beans price and point to the two group counts as you explain the result.
