#coding=utf-8

import sys
da_correct, da_all =0,0
sa_correct, sa_all = 0,0
ra_correct, ra_all = 0,0

sentence=[]
line_num = 0
with open('dev.rst', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line_num += 1
        line = line.strip()
        if line =="" and len(sentence) > 0:
            sa_all += 1
            is_correct = 1
            has_root = 0
            for s in sentence:
                s_arr = s.split()
                r,p = s_arr[-2:]
                da_all += 1
                if r == p:
                    da_correct += 1

                if r.split("_")[-1] == "Root":
                    has_root = 1
                    ra_all += 1
                    if r == p :
                        ra_correct += 1
                if r != p:
                    is_correct = 0
            sa_correct += is_correct
            sentence = []

            if has_root == 0 :
                #print "没有找到Root,行号：",line_num
                pass
            continue

        sentence.append(line)

#开始统计效果
print("词的个数:%d, 句子的个数:%d"%(da_all, sa_all))
print("边正确的个数：%d，边的总数：%d,DA:%f"%(da_correct,da_all,da_correct/float(da_all)))
print("Root正确的个数：%d，Root的个数：%d, RA:%f"%(ra_correct,ra_all,ra_correct/float(ra_all)))
print("句子正确的个数：%d，句子的个数：%d,SA:%f"%(sa_correct, sa_all, sa_correct/float(sa_all)))



