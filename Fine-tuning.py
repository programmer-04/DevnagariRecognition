from fastai import *
from pathlib import Path
from fastai.vision import *
from fastai.metrics import error_rate

path = Path('/run/media/chinmay/DATA/Chinmay/Chinmay/Passions/DeepLearning/Projects/DevanagariChars/DevanagariHandwrittenCharacterDataset/')
tfms = get_transforms(do_flip=False)
data = ImageDataBunch.from_folder(path, ds_tfms=tfms, size=32)
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.load('stage-1')
interp = ClassificationInterpretation.from_learner(learn)

losses,idxs = interp.top_losses()

print(len(data.valid_ds)==len(losses)==len(idxs))
interp.plot_top_losses(9, figsize=(15,11))