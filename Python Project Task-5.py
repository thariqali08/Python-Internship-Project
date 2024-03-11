from PIL import Image,ImageFilter,ImageFont,ImageDraw

#Funtion to create a GIF file
def create_gif(img_file,output_file,fps=10,text=None,filter=None):
    images=[]
    for file in img_file:
        img=Image.open(file)
        images.append(img)
    if text:
        images=add_text(images,text)
    if filter:
         images=apply_filter(images,filter)

    images[0].save(output_file,save_all=True,append_images=images[1:],optimize=False,duration=int(1000/fps),loop=0)

#Function to add text to the images
def add_text(images,text):
    font=ImageFont.truetype('arial.ttf',size=40)

    modify_img=[]
    for img in images:
        draw=ImageDraw.Draw(img)
        draw.text((10,10),text,font=font,fill='white')
        modify_img.append(img)

    return modify_img

#Function to apply filter to the images
def apply_filter(images,filter):
    modify_img=[]
    for img in  images:
        if filter == 'gray':
            img=img.convert('L')
        else:
            img=img.filter(ImageFilter.BLUR)
        modify_img.append(img)

    return modify_img            

#User input for GIF creator
print("Welcome to the GIF Creator!")
print("Please provide the required information.")

#To get the image files
img_file=[]
while True:
    image_file=input("Enter the path to an image (or 'done' to finish):")
    if image_file == 'done':
        break
    img_file.append(image_file)

output_file=input("Enter the path to save GIF file:")

fps=int(input("Enter the frame rate(frames per second):"))

text=input("Enter the text to add (leave empty if not needed):")

filter=input("Enter the filter to apply (eg:'blur'or'gray') (leave empty if not needed):")

create_gif(img_file,output_file,fps,text,filter)

print("GIF creation completed. The GIF is saved at:",output_file)