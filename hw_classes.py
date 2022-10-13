class CountVectorizer:
    def __init__(self):
        self.vocabulary = {}
        self.matrix = []

    def fit_transform(self, corpus: list) -> list:
        """
        Расчет матрицы на основе корпусных данных
        corpus – переменная с фразой

        Две части:
        1. Отбор всех уникальных слов по их порядку
        2. Подсчет использования каждого из слов в строке
        """
        for string in corpus:
            for word in string.split(" "):
                word = word.lower()
                if word not in self.vocabulary:
                    self.vocabulary[word] = 0

        for string in corpus:
            current_vocabulary = {key: 0 for key in self.vocabulary}
            for word in string.split(" "):
                word = word.lower()
                current_vocabulary[word] += 1
            self.matrix.append(list(current_vocabulary.values()))
        return self.matrix

    def get_feature_names(self) -> list:
        """
        Вывод всех слов, рассматриваемых в предложениях
        """
        return list(self.vocabulary.keys())


if __name__ == '__main__':
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(*count_matrix, sep="\n")
    
