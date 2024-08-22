from pyspark.sql import (
    DataFrame,
    SparkSession
)

def transform_test(
    spark: SparkSession,
    df: DataFrame
):
    outdf = spark.sql(
        """
            select
                *,
                "hello_world" as new_column
            from {indf}
        """,
        indf=df
    )
    return outdf