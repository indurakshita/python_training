import os
import shutil

class ChangeFolder:
    def __init__(self,source_dir,make_dir):
        self.source_dir = source_dir
        self.make_dir = make_dir
        self.images = None
    def create_dir(self):
        try:
            os.mkdir(self.make_dir)

            print("new directory created")
            return self.make_dir
        except FileExistsError:
            print("already file exists")
    
    # def get_images_only(self):
    #     try:
    #         self.images = [i  for i in os.listdir(self.source_dir) if '.jpg' in i.lower()]
    #         return self.images
    #     except FileNotFoundError:
    #         return f"jpg files not found"
     
#     def store_image_new_folder(self):
#         for image in self.images:
#             self.src_path = os.path.join(self.source_dir, image)
         
#             self.make_path = os.path.join(self.make_dir,image)

#             os.rename(self.src_path,self.make_path)

    def move_image(self):
        try:
            self.images = [image for image in os.listdir(self.source_dir) if image.lower().endswith('.jpg')]
            for image in self.images:
                src_path = os.path.join(self.source_dir, image)
                dst_path = os.path.join(self.make_dir, image)
                shutil.move(src_path, dst_path)
            print(f"file has been moved")
        except FileNotFoundError:
            print(f"jpg files not found")

            
change = ChangeFolder(source_dir = r"C:\Users\admin\Desktop",make_dir =r"C:\Users\admin\Desktop\image_folder" )
change.create_dir()
# change.get_images_only()
# change.store_image_new_folder()
change.move_image()


