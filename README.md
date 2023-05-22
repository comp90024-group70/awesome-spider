# awesome-spider, README.md
## GROUP 70

**Goal:** awesome-spider repository is for data extraction and data processing.
**Execution process:** Data extraction include the data of `twitter-huge.json`, Mastodon crawling, ADO API, "Greater Capital City" (GCC) and "Statistical Area Level 4" (SA4) shapefiles from Australia Bureau of Statistics (ABS). The part of data processing is mainly focusing on data cleansing and data aggregation to convert data format be readable and compatible on CouchDB. 

1. `spark.py`: Using PySpark to read `twitter-huge.json` file and save it as `twitter_raw.csv`.
2. `ADO.ipynb`: Extracting time series data (10/4/2022 - 10/6/2022) of topics with top30 topic key terms on the each day from ADO.
3. `shapefile.ipynb`: Web crawler for shapefiles from ABS.
4. `MAS_AU.py`,`MAS_NYC.py`,`MAS_UK.py`: Mastodon stream API for three servers.
5. `pre-processing.ipynb`: Twitter data cleansing, and save as `twitter_clean.csv`.
6. `LDA1.ipynb`: LDA model for Twitter topic selection converts `twitter_clean.csv` to the file of `Twitter_LDA.csv` involing the tweets related to our topic.
7. `Data_analysis.ipynb`: Including preliminary analysis of statistical distritions and geospatial visualizations.
8. `sudo_process.ipynb`: Basically merge and process SUDO data with shapefile.
10. `ADO_process.ipynb`: Basically merge and process ADO data with shapefile.

 **NB:** The geospatial visualizations in `Data_analysis.ipynb` will be shown as the main map on our website, just basic analysis for the report and `overview` on the web.
