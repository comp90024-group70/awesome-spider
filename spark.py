from pyspark.sql import *
import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType,BooleanType,DoubleType
from pyspark.sql.functions import get_json_object
from pyspark.sql.functions import to_json,col

def setLogLevel(self, logLevel):
        """
        Control our logLevel. This overrides any user-defined log settings.
        Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
        """
        self._jsc.setLogLevel(logLevel)
appName = "Spark - Setting Log Level"
master = "local"
# Create Spark session
spark = SparkSession.builder \
    .appName(appName) \
    .master(master) \
    .getOrCreate()
spark.sparkContext.setLogLevel("WARN")   
#spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
                    
dp_raw = spark.read.json("../Data/twitter-huge.json")
#dp.printSchema()
#dp.show()

dp = dp_raw.select(col("doc.data.author_id"), col("value.tokens"), col("doc.data.sentiment"),
                            col("doc.includes"))
dp = dp.na.drop()
# dp.count() = 3233513
dp.show()
#dp.write.csv("/Users/byronsun/Desktop/c2/zipcodes")
#dp.write.parquet("/Users/byronsun/Desktop/c2/twitter.parquet")
dp.coalesce(1).write.csv('../Data/twitter_raw.csv')