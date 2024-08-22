from pyspark.testing import assertDataFrameEqual
from os.path import abspath
from pyspark.sql import SparkSession

from myfuncs import *

def test_transform_test():
    spark = SparkSession.builder.getOrCreate()
    indf = spark.read.option("header", True).csv(abspath("./tests/test_cases/test_myfuncs/test.csv"))
    exp = spark.read.option("header", True).csv(abspath("./tests/test_cases/test_myfuncs/exp.csv"))
    test = transform_test(spark, indf)
    assertDataFrameEqual(test, exp)