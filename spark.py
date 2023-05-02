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
                    
dp = spark.read.json("/Users/byronsun/Desktop/c2/twitter-huge.json")
#dp.printSchema()
#dp.show()

dp = dp.select(col("doc.data.author_id"), col("doc.data.text"), col("doc.data.sentiment"),
                            col("doc.includes"))
dp.show()
#df = dp.toPandas()
