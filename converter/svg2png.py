# refer: https://qiita.com/umi_mori/items/7fdb522401c1f86e0487
# PDF作成部分は不要のため削除
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import sys
import os

args = sys.argv
filename = args[1]
filename_without_ext = os.path.splitext(os.path.basename(filename))[0]

drawing = svg2rlg(filename)
renderPM.drawToFile(drawing, filename_without_ext + ".png", fmt="PNG")
renderPM.drawToFile(drawing, filename_without_ext + ".jpg", fmt="JPG")