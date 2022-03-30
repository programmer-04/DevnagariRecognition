from fastai import *
from pathlib import Path
from fastai.vision import *
from fastai.metrics import error_rate
from Config import pathtodataset

bs = 32
path = Path(pathtodataset)
tfms = get_transforms(do_flip=False)
data = ImageDataBunch.from_folder(path, ds_tfms=tfms, size=32)
learn = cnn_learner(data, models.resnet34, metrics=error_rate)

learn.load("stage-3")
learn.export("30Mar20_1513.pkl")