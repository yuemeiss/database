import jieba
# print(dir(jieba))
#  结巴　分词的３中基本模式
# jieba.cut ： 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
# 全模式
seg_list = jieba.cut('python开发工程师',cut_all=False,HMM=True)
print('/'.join(seg_list))

# jieba.cut_for_search ： 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
# 待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
# jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用jieba.lcut 以及jieba.lcut_for_search 直接返回 list
# jieba.Tokenizer(dictionary=DEFAULT_DICT) ： 新建自定义分词器，可用于同时使用不同词典。jieba.dt 为默认分词器，所有全局分词相关函数都是该分词器的映射。


