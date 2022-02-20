from PIL import Image, ImageDraw, ImageFont
import pandas as pd
form = pd.read_excel("Certificate_PCB.xlsx")
name_list = form['Name'].to_list()
output_path = 'C:/Users/Sihab Sahariar/Desktop/Certificate Generator/PCB/certificate/'
for i in name_list:
    im = Image.open("certificate.png")
    d = ImageDraw.Draw(im)
    location = (1160, 1050)
    text_color = (255, 255, 255)
    font = ImageFont.truetype("lcallig.ttf", 106)
    d.text(location, i, fill=text_color,font=font)
    print("Saving - "+i)
    im.save(output_path + "/certificate_"+ i + ".pdf")