
### Kaggle project

The analysis were provide for data and project from Kaggle.com

The has following features:

- **Restaurant_id** 
- **City** 
- **Cuisine Style** 
- **Ranking** — the place of the restaurant in the city ranking
- **Rating** — target
- **Price Range** 
- **Number of Reviews**
- **Reviews** - two reviews from restaurant website
- **URL_TA** — URL on TripAdvisor
- **ID_TA** — id on TripAdvisor

The goal is to predict the rating of restaurants.


### Выводы:
Метрику удалось улучшить не очень сильно - в пределах 0.1. 

Среди возможных идей для дальнейшего улучшения значения метрики  можно было бы попробовать следующее:

- собрать данные о количестве ресторанов в каждом городе, чтобы признак **ranking** сделать более репрезентативным
- собрать больше комментариев с сайта и их дальнейшей сортировки на "плохие" и "хорошие"
- возможно, стоило бы еще сделать анализ комментариев по времени, то есть - тренд: "улучшение или "ухудшение"

Из менее важного, возможно:
- определить возраст ресторана
- определить удаленность от центра города
