from src.masks import Mask, col_name, get_ref_from_abaque
import numpy as np
import matplotlib.pyplot as plt
import datetime
from fpdf import FPDF
import os


class ResultReport:

    def __init__(self, client_name: str, gender: str or int, ans: np.array):
        self.name = client_name
        if type(gender) == str:
            gender = 0 if gender == 'M' else 1
        self.gender = gender
        self.ans = ans
        self.result_values = []
        self.weighted_result = {}

    def generate_results_from_masks(self):
        for i in range(10):
            mask = Mask.get_mask(i, self.gender)
            self.result_values.append(mask.compute_result(self.ans))

    def generate_weighted_results(self):
        for i in range(len(self.result_values)):
            ans = self.result_values[i]
            self.weighted_result[col_name[i]] = get_ref_from_abaque(i, ans, self.gender)

    def generate_plot(self, save_dir: str):
        wdir = os.getcwd()

        fig, ax = plt.subplots(figsize=(16, 10))

        x = np.arange(len(col_name))
        width = 0.35

        plt.ylim(0, 100)
        ax.set_axisbelow(True)
        ax.set_yticks([5 * i for i in range(1, 21)])
        ax.grid(axis='y', linewidth=1, linestyle='--')

        # bars
        bars = list(self.weighted_result.values())
        rects1 = ax.bar(x, bars, width)
        ax.set_xticks(x, col_name, fontsize=16)
        # HLines
        ax.hlines((60, 75), -0.25, x[-1] + 0.25, linestyle='--', colors='r')

        ax.set_xlabel("Domaines d'intérets", labelpad=15, color='#333333')
        ax.set_title(f"Analyses du profil d'intérets de {self.name} ({self.gender})", pad=15, color='#333333',
                     weight='bold', fontsize=16)

        fig.tight_layout()
        dt = datetime.datetime.now().strftime('%Y%m%d%H%M')
        save_path = os.sep.join([wdir, 'results', f'{self.name}_{dt}.pdf'])

        tmp_path = os.sep.join([wdir, 'ressources', 'tmp.png'])
        fig.savefig(tmp_path, transparent=True)
        print(f'Temporary plot saved...')

        pdf = FPDF()
        pdf_w = 210
        pdf_h = 297
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        pdf.set_xy((pdf_w - 200*0.3)/2, 0)
        vba_path = os.sep.join([wdir, 'ressources', 'vba.jpg'])
        pdf.image(vba_path)

        pdf.set_xy(15, 60)
        pdf.cell(pdf_w, 10, txt=f'Prénom : {self.name}', ln=1, align='L')
        pdf.set_xy(15, 75)
        pdf.cell(pdf_w, 10, txt=f'Référentiel : {self.gender}', ln=1, align='L')
        pdf.set_xy(15, 90)
        pdf.cell(pdf_w, 10, txt=f'Date du test : {datetime.date.today().strftime("%d/%m/%Y")}', ln=1, align='L')
        pdf.set_xy(15, 110)
        pdf.set_font("Arial", 'B', size=20)
        pdf.cell(pdf_w-15, 10, txt=f"Profil d'intérets".upper(), ln=1, align='C')

        pdf.set_xy((pdf_w - (1600*0.3)/3)/2, 130)
        pdf.image(tmp_path,  link='', type='', w=(1600*0.3)/3, h=(1000*0.3)/3)
        pdf.set_author('VB Accompagnement')
        pdf.output(save_path)
        print(f'Result analysis saved to {save_path} !')
        print('Thanks...')
