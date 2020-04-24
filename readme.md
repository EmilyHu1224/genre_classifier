# Partition & Preprocessing
```
python track_artist_map_generator.py > track_artist_map.json
python artist_genre_map_generator.py > artist_genre_map.json
python split.py
```
# Train
```
vw --csoaa 18 train.txt -f csoaa.model
```
# Test
```
vw -i csoaa.model -t test.txt -p predictions.txt
```
# Validate
```
python validate.py > eval.txt
```