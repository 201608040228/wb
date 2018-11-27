#生成训练数据
cat train.conll | python get_parser_train_test_input.py > train.data 

#生成测试数据
cat dev.conll | python get_parser_train_test_input.py > dev.data

#crf训练
crf_learn -f 3 -p 12 -c 4.0 template train.data model > train.rst  
#crf测试
crf_test -m model dev.data > dev.rst


