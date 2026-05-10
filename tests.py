import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('book_name',['Я', 'Горе от ума', 'Путешествие сквозь время и пространство!'])
    def test_add_new_book_len_name_from_1_to_40_characters_add_in_books_genre(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize('book_name', ['','Дорога сквозь туманы к далёким тихим гора','Тень ветра: тайна старинной библиотеки и потерянная душа'])
    def test_add_new_book_len_name_0_or_more40_characters_not_in_books_genre(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_new_book_readding_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Преступление и наказание')
        assert len(collector.books_genre) == 1
    
    def test_set_book_genre_book_in_books_genre_and_genre_in_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        collector.set_book_genre(name='Анна Каренина', genre='Ужасы')
        assert collector.books_genre['Анна Каренина'] == 'Ужасы'

    def test_set_book_genre_book_not_in_books_genre(self):
        collector = BooksCollector()
        collector.set_book_genre(name='Оно', genre='Ужасы')
        assert collector.books_genre == {}

    def test_set_book_genre_book_in_books_genre_genge_not_in_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Лолита')
        collector.set_book_genre(name='Лолита', genre='Роман')
        assert collector.books_genre ['Лолита']== ''

    def test_get_book_genre_returns_correct_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения электроника')
        collector.set_book_genre(name='Приключения электроника', genre='Фантастика')
        assert collector.get_book_genre('Приключения электроника') == 'Фантастика'

    def test_get_book_genre_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Бесы')
        assert collector.get_book_genre('Бесы') == ''

    def test_get_book_genre_without_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Дракула') == None     

    def test_get_books_with_specific_genre_returns_correct_books_for_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мэри Джейн')
        collector.set_book_genre(name='Мэри Джейн', genre='Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Мэри Джейн']

    def test_get_books_with_specific_genre_books_with_diffrend_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Замок')
        collector.set_book_genre(name='Замок', genre='Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_with_specific_genre_no_book_in_list(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Детективы') == []  

    def test_get_books_genre_return_dict_with_books_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оливер Твист')
        collector.set_book_genre(name='Оливер Твист', genre='Мультфильмы')
        assert collector.get_books_genre() == {'Оливер Твист':'Мультфильмы'}

    def test_get_books_for_children_returns_list_with_no_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Красная шапочка')
        collector.set_book_genre(name='Красная шапочка', genre='Мультфильмы')
        assert collector.get_books_for_children()==['Красная шапочка']
    
    def test_add_book_in_favorites_book_in_books_genre_append_in_list_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хоумс')
        collector.add_book_in_favorites('Шерлок Хоумс')
        assert 'Шерлок Хоумс' in collector.favorites

    def test_add_book_in_favorites_twiсe_adds_onese(self):
        collector = BooksCollector()
        collector.add_new_book('Яма')
        collector.set_book_genre(name='Яма',genre='Ужасы')
        collector.add_book_in_favorites('Яма')
        collector.add_book_in_favorites('Яма')
        assert len(collector.favorites) == 1
    
    
    def test_delete_book_from_favorites_if_book_in_list_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Бойцовский клуб')
        collector.set_book_genre(name='Бойцовский клуб',genre='Детективы')
        collector.add_book_in_favorites('Бойцовский клуб')
        collector.delete_book_from_favorites('Бойцовский клуб')
        assert 'Бойцовский клуб'  not in collector.favorites

    def test_get_list_of_favorites_books_book_in_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre(name='Убийство в восточном экспрессе',genre='Детективы')
        collector.add_book_in_favorites('Убийство в восточном экспрессе')
        assert collector.get_list_of_favorites_books() == ['Убийство в восточном экспрессе'] 
    
