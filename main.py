import os
HZC1_MAGIC = b'hzc1'
NVSG_MAGIC = b'NVSG'

img_dir=''#此处写输入图片目录目录
output_dir=''#这里放输出目录
tlg2pngDir=''#tlg2png可执行文件路径
def get_file_names():
    files = os.listdir(img_dir)
    file_names = []
    for file in files:
        file_names.append(file)
    return file_names
fileList=get_file_names()
for i in fileList:
    print(1)
    with open(os.path.join(img_dir,i),"rb") as input_file:
        _=b''
        while _.count(b"TLG6.0") ==0:
            _+=input_file.read(1)
        data = b'TLG6.0'+input_file.read()
        print(i)
        with open(os.path.join(output_dir,"tmp.tlg"),"wb") as f:
            f.write(data)
        os.system(tlg2pngDir+" " + os.path.join(output_dir,"tmp"+i+".tlg") +' ' +os.path.join(output_dir,i+'.png'))
    print("ok")


