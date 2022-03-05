import datetime


class Manager:

    def __init__(self, path_to_file: str, saving_path: str):
        self.saving_path = saving_path
        with open(saving_path, 'w', encoding='UTF-8') as f:
            f.write(f'GEN {datetime.datetime.now().strftime("%Y-%m-%d:%H.%M")}\n')
        self.qu = [[None for _ in range(3)] for _ in range(134)]
        self.ans = [[None for _ in range(3)] for _ in range(134)]
        self.current = -1
        self.len = 134
        with open(path_to_file, 'r', encoding="UTF-8") as f:
            for i, line in enumerate(f.readlines()):
                qu_id = i // 3
                stmt_id = i % 3
                self.qu[qu_id][stmt_id] = line.strip()
        print(f'Sentences loaded...')

    def __getitem__(self, key):
        return self.qu[key]

    def next_questions(self):
        if self.current == self.len - 1:
            return None, None, None

        self.current += 1
        print(f'Currently handling question n°{self.current}...')
        return self.get_current()

    def get_current(self):
        return self.qu[self.current]

    def get_current_ans(self):
        if self.current > len(self.ans):
            return None, None, None
        return self.ans[self.current]

    def get_previous(self):
        if self.current == 0:
            return self.get_current()

        self.current -= 1
        return self.get_current()

    def save_current(self, a1, a2, a3):
        self.ans[self.current] = [a1, a2, a3]

        data = None

        with open(self.saving_path, 'r', encoding='UTF-8') as f:
            data = f.readlines()

        if len(data) <= self.current + 1:
            for _ in range(len(data), self.current + 2):
                data.append('\n')

        data[self.current + 1] = f'{a1},{a2},{a3}\n'

        with open(self.saving_path, 'w', encoding='UTF-8') as f:
            f.writelines(data)

        print(f'Answers saved to file...')
