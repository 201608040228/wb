#coding=utf-8
'''
词A依赖词B，A就是孩子，B就是父亲
'''

import sys 

sentence = ["Root"]

def do_parse(sentence):
  #with open('train.conll', 'r', encoding='utf-8') as f:
    if len(sentence) == 1:return
    for line in sentence[1:]:
        line_arr = line.strip().split("\t")
        #print line_arr
        c_id = int(line_arr[0])
        f_id = int(line_arr[6])
        #print c_id, f_id
        if f_id == 0:
            print("\t".join(line_arr[2:5])+"\t" + "0_Root")
            continue
        #print sentence[f_id].strip().split("\t")[3:5]
        f_post,f_detail_post = sentence[f_id].strip().split("\t")[3:5] #得到父亲节点的粗词性和详细词性
        c_edge_post = f_post #默认是依赖词的粗粒度词性，但是名词除外；名词取细粒度词性
        if f_post == "n":
            c_edge_post = f_detail_post
        #计算是第几个出现这种词行
        diff = f_id - c_id #确定要走几步
        step = 1 if f_id > c_id  else -1 #确定每一步方向
        same_post_num = 0 #中间每一步统计多少个一样的词性
        cmp_idx = 4 if f_post == "n" else 3  #根据是否是名词决定取的是粗or详细词性
        for i in range(0, abs(diff)):
            idx = c_id + (i+1)*step
            if sentence[idx].strip().split("\t")[cmp_idx] == c_edge_post:
                same_post_num += step

        print("\t".join(line_arr[2:5])+"\t" + "%d_%s"%(same_post_num, c_edge_post))
    print("")

for line in sys.stdin:
    line = line.strip()
    line_arr = line.split("\t")
    
    if  line == "" or line_arr[0] == "1":
        #print sentence
        do_parse(sentence)
        sentence = ["Root"]

    if line =="":continue 
    sentence.append(line)



