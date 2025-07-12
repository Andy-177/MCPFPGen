from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class Segment_skin():
 def __init__(self, skin_path):
     self.skin_path = skin_path
 def cut_skin(self):
     skin = Image.open(self.skin_path).convert('RGBA')
     side_face = skin.crop((5, 9, 8, 16))
     side_face.save('cache/side_face.png')
     face = skin.crop((8, 9, 15, 16))
     face.save('cache/face.png')
     out_side_face = skin.crop((33, 9, 36, 16))
     out_side_face.save('cache/out_side_face.png')
     out_face = skin.crop((40, 9, 47, 16))
     out_face.save('cache/out_face.png')
     body = skin.crop((20, 20, 28, 29))
     body.save('cache/body.png')
     out_body = skin.crop((20, 36, 28,45))
     out_body.save('cache/out_body.png')
     rhand = skin.crop((45, 20, 47, 27))
     rhand.save('cache/rhand.png')
     out_rhand = skin.crop((45, 36, 47, 43))
     out_rhand.save('cache/out_rhand.png')
     lhand = skin.crop((37, 52, 39, 59))
     lhand.save('cache/lhand.png')
     out_lhand = skin.crop((53, 52, 55, 59))
     out_lhand.save('cache/out_lhand.png')
     self.edit_body()
 def edit_body(self):
     edit = Image.open('cache/body.png').convert('RGBA')
     edit.putpixel((0, 0), (0, 0, 0, 0))
     edit.putpixel((7, 0), (0, 0, 0, 0))
     edit.save('cache/body.png')
     edit = Image.open('cache/out_body.png')
     edit.putpixel((0, 0), (0, 0, 0, 0))
     edit.putpixel((7, 0), (0, 0, 0, 0))
     edit.save('cache/out_body.png')
class PFPGen():
    def __init__(self):
       pass
    def create_tbg(self):
     bg = Image.new(mode='RGBA', size=(20, 20), color=(0, 0, 0, 0))
     bg.save('cache/background.png')
    def create_bg(self,RGB:tuple):
     bg = Image.new(mode='RGBA', size=(20, 20), color=RGB)
     bg.save('cache/background.png')
     print('create_bg:OK')
    def gen_pfp(self):
        result = Image.open('cache/background.png').convert('RGBA')

        side_face = Image.open('cache/side_face.png').convert('RGBA')
        out_side_face = Image.open('cache/out_side_face.png').convert('RGBA')
        result.paste(side_face,(5,4))
        result.paste(out_side_face,(5,4),out_side_face)

        face = Image.open('cache/face.png').convert('RGBA')
        out_face = Image.open('cache/out_face.png').convert('RGBA')
        result.paste(face,(8,4))
        result.paste(out_face,(8,4),out_face)

        lhand = Image.open('cache/lhand.png').convert('RGBA')
        out_lhand = Image.open('cache/out_lhand.png').convert('RGBA')
        result.paste(lhand,(13,13))
        result.paste(out_lhand,(13,13),out_lhand)

        body = Image.open('cache/body.png').convert('RGBA')
        out_body = Image.open('cache/out_body.png').convert('RGBA')
        result.paste(body,(6,11),body)
        result.paste(out_body,(6,11),out_body)

        rhand = Image.open('cache/rhand.png').convert('RGBA')
        out_rhand = Image.open('cache/out_rhand.png').convert('RGBA')
        result.paste(rhand,(5,13))
        result.paste(out_rhand,(5,13),out_rhand)

        result.save('output/Template.png')

folder_names = ['cache','output']
for folder_name in folder_names:
   if not os.path.exists(folder_name):
      os.makedirs(folder_name)
      print('当前目录下文件夹有缺失，已自动创建')
p = input('请输入皮肤文件的路径，皮肤文件必须为64x64的png文件:\n')
if p == '':
   print('你没有选择文件')
   exit()
check = Image.open(f'{p}')
width, height = check.size
def cut():
   S = Segment_skin(skin_path=f'{p}')
   S.cut_skin()
if width ==64 and height == 64:
   cut()
else:
   print('图片不合规')
   exit()
class Sz():
 def __init__(self):
    pass
 def skin_shadow(self):
   Temp = Image.open('output/Template.png').convert('RGBA')
   shadow = Image.open('asset/skin_shadow.png').convert('RGBA')
   Temp.paste(shadow,(0,0),shadow)
   Temp.save('output/Template.png')
 def zoom(self):
   Temp = Image.open('output/Template.png').convert('RGBA')
   resized = Temp.resize((300,300),Image.NEAREST)
   resized.save('output/pfp.png')
 def shader(self):
   pfp = Image.open('output/pfp.png').convert('RGBA')
   shadow = Image.open('asset/shadow.png').convert('RGBA')
   pfp.paste(shadow,(0,0),shadow)
   pfp.save('output/pfp_shadow.png')
g = PFPGen()
qcc = input('是否选择透明背景，选择透明背景输入Y，不选择输入N:\n')
if qcc == 'Y':
 g.create_tbg()
 g.gen_pfp()
elif qcc == 'N':
   tg = PFPGen()
   cor = input('请输入背景的RGB值,格式：R,G,B\n')
   rgb_tuple = tuple(int(item.strip()) for item in cor.split(','))
   tg.create_bg(RGB=rgb_tuple)
   tg.gen_pfp()
sz = Sz()
qs = input('是否为头像添加skin_shadow，添加选Y，不添加选N:\n')
if qs == 'Y':
   sz.skin_shadow()
   sz.zoom()
elif qs == 'N':
   sz.zoom
qsd = input('是否为头像添加shadow，添加选Y，不添加选N:\n')
if qs == 'Y':
 sz.shader()
elif qs == 'N':
 exit()