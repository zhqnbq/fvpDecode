# fvpDecode
一个极水的解包英文版Irotoridori的图片文件的脚本

用法:

1.用[garbro](https://github.com/morkt/GARbro)解压掉最外层的bin封包，解压出hzc文件

2.进入[tlg2png](https://github.com/vn-tools/tlg2png)仓库，下载/编译tlg2png的可执行文件

3.在main.py中标注位置填入解包出的hzc文件所在目录（最好只有这些hzc文件)，输出目录，tlg2png可执行文件路径

4.运行main.py

最后输出文件夹会有个tmp.hzc，没用，自行删除

已测试，在adult.bin上可用
