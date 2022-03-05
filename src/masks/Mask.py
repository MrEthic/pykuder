import numpy as np
import os

wdir = os.getcwd()


class Mask:
    masks = [
        os.sep.join([wdir, 'masks', 'masks_data', 'm0_plein-air.csv']),
        os.sep.join([wdir, 'masks', 'masks_data', 'm1_pratique.csv']),
        os.sep.join([wdir, 'masks', 'masks_data', 'm2_numerique.csv']),
        (os.sep.join([wdir, 'masks', 'masks_data', 'm3_scientifique_g.csv']),
         os.sep.join([wdir, 'masks', 'masks_data', 'm3_scientifique_f.csv'])),
        (os.sep.join([wdir, 'masks', 'masks_data', 'm4_persuasif_g.csv']),
         os.sep.join([wdir, 'masks', 'masks_data', 'm4_persuasif_f.csv'])),
        os.sep.join([wdir, 'masks', 'masks_data', 'm5_artistique.csv']),
        os.sep.join([wdir, 'masks', 'masks_data', 'm6_litteraire.csv']),
        os.sep.join([wdir, 'masks', 'masks_data', 'm7_musical.csv']),
        os.sep.join([wdir, 'masks', 'masks_data', 'm8_social.csv']),
        os.sep.join([wdir, 'masks', 'masks_data', 'm9_urbain.csv'])
    ]

    @classmethod
    def get_mask(cls, model_id, gender_id: int):
        mask = Mask.masks[model_id]
        if len(mask) == 2:
            return Mask(mask[gender_id])

        return Mask(mask)

    def __init__(self, path_to_model: str):
        self.model = np.loadtxt(path_to_model, delimiter=',')

    def compute_result(self, answers: np.array):
        return np.count_nonzero((self.model * answers) == 1)
