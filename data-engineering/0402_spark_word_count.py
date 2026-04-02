from pyspark import SparkContext

sc = SparkContext("local", "WordCount")

text = [
    "the quick brown fox",
    "the fox jumped over the lazy dog",
    "the dog barked at the fox"
]

rdd = sc.parallelize(text)
flat_list = rdd.flatMap(lambda line: line.split(" "))

flat_list = flat_list.map(lambda word:(word, 1))#创建一个tuple，tuple 里用逗号分隔，冒号是 dict 的语法

agg_words = flat_list.reduceByKey(lambda a,b:a+b)

words_order = agg_words.sortBy(lambda x: x[1], ascending=False)