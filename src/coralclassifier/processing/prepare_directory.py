import os
import shutil


class PrepareImageDirectory:
    def __init__(self, train_ratio, data_path, images_path, train_path, val_path):
        self.train_ratio = train_ratio
        self.data_path = data_path
        self.images_path = images_path
        self.train_path = train_path
        self.val_path = val_path


    def build_train_val_directory(self):
        '''
        Split images from original download into new train-validation split directory with paths:
        parent/train/class1, parent/train/class2
        parent/val/class1, parent/val/class2

        Inputs kept generic so directory names can be chosen higher up.
        '''
        paths = self.define_paths()

        # create directories
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)

        images_path, train_path, val_path = paths

        class_labels = os.listdir(images_path)

        self.populate_train_val_directory(class_labels, images_path, train_path, val_path)


    def define_paths(self):
        # image paths for train and validation split
        images_path = os.path.join(self.data_path, self.images_path)
        train_path = os.path.join(self.data_path, self.train_path)
        val_path = os.path.join(self.data_path, self.val_path)

        return [images_path, train_path, val_path]



    def populate_train_val_directory(self, classes, images_path, train_path, val_path):

        for c in classes:

            class_path = os.path.join(images_path, c)
            images = os.listdir(class_path)
            n_train = int(len(images) * self.train_ratio)

            train_images = images[:n_train]
            test_images = images[n_train:]

            os.makedirs(os.path.join(train_path, c), exist_ok = True)
            os.makedirs(os.path.join(val_path, c), exist_ok = True)

            for image in train_images:
                image_src = os.path.join(class_path, image)
                image_destination = os.path.join(train_path, c, image)
                shutil.copyfile(image_src, image_destination)

            for image in test_images:
                image_src = os.path.join(class_path, image)
                image_destination = os.path.join(val_path, c, image)
                shutil.copyfile(image_src, image_destination)
