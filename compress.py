import os

from PIL import Image

from PIL import ImageFile


# 压缩图片文件
def compress(outfile, kb=600, quality=85, k=0.9):

    """不改变图片尺寸压缩到指定大小
    :param outfile: 压缩文件保存地址
    :param kb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """

    o_size = os.path.getsize(outfile) // 1024

    if o_size <= kb:

        return outfile

    ImageFile.LOAD_TRUNCATED_IMAGES = True

    while o_size > kb:

        im = Image.open(outfile)

        x, y = im.size

        out = im.resize((int(x * k), int(y * k)), Image.ANTIALIAS)

        try:

            out.save(outfile, quality=quality)

        except Exception as e:

            break

        o_size = os.path.getsize(outfile) // 1024

    return outfile

