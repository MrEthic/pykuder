from src.masks import ResultReport
import numpy as np


def generate_result_from_answer_file(file_path, name, gender):
    ans = np.loadtxt(file_path, skiprows=1, delimiter=',', max_rows=134)
    r = ResultReport(name, gender, ans)
    r.generate_results_from_masks()
    r.generate_weighted_results()
    r.generate_plot(r'C:/Users/jerem/OneDrive/Bureau')


generate_result_from_answer_file(r'D:\Programation\Python\OrintaPy\results\results_maman.txt', 'Valérie', 1)
