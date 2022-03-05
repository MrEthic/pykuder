from src.manager import Manager
from src.masks import ResultReport
import eel
import os

wdir = os.getcwd()

if __name__ == '__main__':
    client_name = input('Pseudo: ')
    client_gender = input('Genre (M ou F): ')
    client_gender = 0 if client_gender == 'M' else 1

    sentences_path = os.sep.join([wdir, 'ressources', 'sentences-FR.txt'])
    output_path = os.sep.join([wdir, 'results', f'results_{client_name}.txt'])
    statements = Manager(sentences_path, output_path)

    eel.init('web')

    s1, s2, s3 = statements.next_questions()
    eel.update_with_stmt(s1, s2, s3, statements.current, None, None, None)


    @eel.expose
    def next(a1, a2, a3):
        statements.save_current(a1, a2, a3)

        s1, s2, s3 = statements.next_questions()
        if s1 is not None:
            w1, w2, w3 = statements.get_current_ans()
            eel.update_with_stmt(s1, s2, s3, statements.current, w1, w2, w3)



    @eel.expose
    def prev():
        s1, s2, s3 = statements.get_previous()
        w1, w2, w3 = statements.get_current_ans()
        eel.update_with_stmt(s1, s2, s3, statements.current, w1, w2, w3)

    eel.start('index.html')

    result = ResultReport(client_name, client_gender, statements.ans)
    result.generate_results_from_masks()
    result.generate_weighted_results()
    result.generate_plot(wdir)



