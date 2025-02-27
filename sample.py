from pyspark.sql import *
from pyspark.sql.functions import *
spark=SparkSession.builder.master("local[*]").appName("test").getOrCreate()
data=r"C:\Users\murali\Desktop\details.csv"
df=spark.read.format("csv").option("header","true").option("inferSchema","true").load(data)
df.show(5)