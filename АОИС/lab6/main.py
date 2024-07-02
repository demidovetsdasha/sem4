class HashTable:
    def __init__(self, size=20):
        self.hash_table_size = size
        self.hash_table = [None] * size

    def _get_hash(self, key):
        if len(key) < 2:
            raise ValueError("Ключ должен содержать как минимум 2 символа")

        alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        alphabet_size = len(alphabet)

        first_char_index = alphabet.index(key[0].upper())
        second_char_index = alphabet.index(key[1].upper())

        hash = first_char_index * alphabet_size + second_char_index
        return hash

    def _get_index_by_hash(self, hash):
        return hash % self.hash_table_size

    def insert(self, key, value):
        # мой вариант: линейное разрешение коллизий
        hash = self._get_hash(key)
        index = self._get_index_by_hash(hash)

        # обновление существующего значения для ключа либо поиск первого свободного
        start_index = index
        steps = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = (key, value)
                return
            steps += 1
            index = (start_index + steps) % self.hash_table_size
            if steps > self.hash_table_size:
                raise Exception("Хэш-таблица переполнена")

        self.hash_table[index] = (key, value)

    def search(self, key):
        # мой вариант: квадратичный поиск
        hash = self._get_hash(key)
        index = self._get_index_by_hash(hash)

        start_index = index
        steps = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
            steps += 1
            index = (start_index + steps ** 2) % self.hash_table_size
            if steps > self.hash_table_size:
                return None

        return None

    def delete(self, key):
        # мой вариант: 
        V = self._get_hash(key)
        index = self._get_index_by_hash(V)

        original_index = index
        steps = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = None
                return True
            steps += 1
            index = (original_index + steps) % self.hash_table_size
            if steps > self.hash_table_size:
                return False

        return False

    def display(self):
        print("Index | Key          | Value              ")
        print("--------------------------")
        for index, item in enumerate(self.hash_table):
            if item is not None:
                print(f"{index} | {item[0]} | {item[1]}                                             ")
            else:
                print(f"{index} | {'None'} | None")


#main()
hash_table = HashTable()
hash_table.insert("Антитеза", "стилистическая фигура контраста в художественной или ораторской речи, заключающаяся в резком противопоставлении понятий, положений, образов: волос длинный – ум короткий. Известными примерами противопоставления в литературе являются романы И. С. Тургенева и Л. Н. Толстого «Отцы и дети» и «Война и мир»")
hash_table.insert("Афоризм", "лаконичные изречения, содержащие глубокую мысль, основанную на житейском опыте, например: Есть еще порох в пороховницах (Н. В. Гоголь «Тарас Бульба»); «Есть, чтобы жить, а не жить, чтобы есть». (Сократ); Краткость – сестра таланта! (Чехов)")
hash_table.insert("Баллада","лиро-эпический жанр, стихотворение, в основе которого какой-либо остродраматический сюжет, необыкновенный случай. Ярким примером исторической литературной баллады является баллада А.С. Пушкина Песнь о вещем Олеге. Известны баллады В. А. Жуковского «Светлана», «Ахилл», «Эолова арфа».")
hash_table.insert("Верлибр","стихотворение, написанное не по правилам классического стихосложения. Такие стихотворения лишены рифмы и размера, но сохраняют целый ряд стихотворных признаков, таких как разбиение текста на строки, написание строк с заглавной буквы и других.")
hash_table.insert("Градация","расположение синонимов в порядке нарастания или ослабления: тлеть, гореть, пылать, взрываться")
hash_table.insert("Гротеск","подчеркнутое искажение каких-либо характеристик, их преувеличение и заострение, например, образы генералов в сказке М. Е. Салтыкова-Щедрина «Повесть о том, как один мужик двух генералов прокормил», образ одичавшего помещика в его сказке «Дикий помещик»")
hash_table.insert("Дактиль","трехсложная стопа в русском силлабо-тоническом стихосложении, содержащий ударный и два безударных слога.")
hash_table.insert("Завязка","событие, которое содержит противоречие, конфликт и завязывает действие.")
hash_table.insert("Инверсия","изменения порядка слов: Пришел он поздно (Он поздно пришел).")
hash_table.insert("Ирония","употребление слова или выражения в перевернутом смысле, насмешливом, например, обращение к Ослу в басне Крылова: «Отколе, умная, бредёшь ты, голова?»")
hash_table.insert("Классицизм","литературное направление (течение) XVII — нач. XIX вв. в России и Западной Европе, базировавшееся на подражании античным образцам и строгих стилистических нормативах.")
hash_table.insert("Кульминация","наивысшая точка напряжения в развитии действия, когда противоречие достигает предела.")
hash_table.insert("Лирика","один из основных родов литературы, отражающий жизнь при помощи изображения отдельных (единичных) состояний, мыслей, чувств, впечатлений и переживаний человека, вызванных теми или иными обстоятельствами.")
hash_table.insert("Лирический герой","субъект высказывания в лирическом произведении, я-персонаж лирики, художественный образ, источником-прототипом которого является автор. Лирический герой — это сложно организованная маска биографического автора, под которой тот выступает в поэтическом тексте или их совокупности, обладающая как чертами реального автора, так и сконструированными характеристиками.")
hash_table.insert("Литературная критика","сочинения, посвященные оценке, анализу и толкованию художественных произведений")
hash_table.insert("Ода","хвалебное стихотворение, посвященное торжественному событию или герою.")
hash_table.insert("Оксюморон","соединение противоречий: живой труп, честный вор.")
hash_table.insert("Очерк","литературное произведение, основанное на фактах, документах, наблюдениях автора.")
hash_table.insert("Притча","назидательный рассказ о человеческой жизни в иносказательной или аллегорической форме.")
hash_table.insert("Проза","художественное произведение, изложенное обычной (свободно организованной, а не стихотворной) речью.")
 
print("Хэш-таблица:")
hash_table.display()

print("\nПоиск элементов:")
print(f"Лирика: {hash_table.search('Лирика')}")
print(f"Оксюморон: {hash_table.search('Оксюморон')}")
print(f"Дактиль: {hash_table.search('Дактиль')}")

hash_table.delete("Кульминация")
print("\nПосле удаления 'Кульминация':")
hash_table.display()