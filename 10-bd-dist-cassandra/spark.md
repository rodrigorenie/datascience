Ações


iconv -f UTF-8 -t ASCII//TRANSLIT despesas_original.csv  > despesas.csv
sed -i '1s/^/ANO;ORGAO;CUSTO\n/' despesas.csv
hdfs dfs -put  despesas.csv /user/hadoopinho/data/despesas.csv
var despesas = spark.read.options(Map("header"->"true","delimiter"->";","inferSchema"->"true")).csv("/user/hadoopinho/data/despesas.csv")
despesas = despesas.where("ORGAO != 'GOVERNO MUNICIPAL'").groupBy("ANO", "ORGAO").agg(sum("CUSTOS").as("TOTAL")).sort("ORGAO")
despesas.write.options(Map("header"->"false","delimiter"->";")).csv("/user/hadoopinho/data/relatorios")

