使用utf-8编码
pysrfwork:
│  readme.txt
│  report.pdf
│
├─data
│      input.txt
│      output.txt
│
├─three
│      ch2_to_ch.json       两个字后面接一个字的统计
│      dp.py                输入输出到文件的版本
│      dpdirect.py          输入输出到命令行的版本
│      pinyin_to_char3.json 拼音对应汉字的统计
│      py2_to_ch2.json      两个拼音对应两个汉字的统计
│
└─two
        char_to_char.json    一个字后面接一个字的统计
        dp.py                输入输出到文件的版本
        dpdirect.py          输入输出到命令行的版本
        pinyin_to_char3.json 拼音对应汉字的统计

1.two是二元字模型，three是三元字模型。
2.dp.py是从data/input.txt读入，然后结果放在data/output.txt
3.dpdirect.py可以在命令行输入拼音，然后直接输出结果，方便手动测试。
4.二元模型统计数据较小，加载模型需要约1s，消耗50M内存。
5.三元模型统计数据较大，加载模型需要约20s，消耗4G内存，请耐心等待。

注：因为json太大，传不上来，使用者请自己按格式统计输出相应的json文件。