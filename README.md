# qa_python
Для тестирования класса BookCollector был создан класс TestBookCollector. Написаны тесты на все метода класса:add_new_book, set_book_genre, get_book_genre, get_books_with_specific_genre, get_books_genre, get_books_for_children, add_book_in_favorites, delete_book_from_favorites, get_list_of_favorites_books.

test_add_new_book_len_name_from_1_to_40_characters_add_in_books_genre
Проверяет, что книга с названием длиной от 1 до 40 символов успешно добавляется в словарь books_genre.

test_add_new_book_len_name_0_or_more40_characters_not_in_books_genre
Проверяет, что книга с пустым названием или названием длиннее 40 символов не добавляется в словарь books_genre.

test_add_new_book_readding_not_in_books_genre
Проверяет, что одну и ту же книгу нельзя добавить дважды — в словаре остаётся только одна запись.

test_set_book_genre_book_in_books_genre_and_genre_in_genre
Проверяет, что жанр устанавливается, если книга существует в books_genre, а жанр есть в списке допустимых жанров.

test_set_book_genre_book_not_in_books_genre
Проверяет, что если книги нет в словаре, попытка установить жанр не изменяет books_genre.

test_set_book_genre_book_in_books_genre_genge_not_in_genre
Проверяет, что если жанр отсутствует в списке допустимых, то жанр книге не присваивается (остаётся пустой строкой).

test_get_book_genre_returns_correct_genre_for_existing_book
Проверяет, что метод get_book_genre возвращает корректный жанр для существующей книги.

test_get_book_genre_book_without_genre
Проверяет, что метод возвращает пустую строку, если книга добавлена, но жанр ей не установлен.

test_get_book_genre_without_book
Проверяет, что метод возвращает None, если книги нет в словаре.

test_get_books_with_specific_genre_returns_correct_books_for_existing_genre
Проверяет, что метод возвращает список книг с указанным жанром.

test_get_books_with_specific_genre_books_with_diffrend_genre
Проверяет, что метод возвращает пустой список, если книг с указанным жанром нет.

test_get_books_with_specific_genre_no_book_in_list
Проверяет, что метод возвращает пустой список, если в словаре нет книг.

test_get_books_genre_return_dict_with_books_and_genre
Проверяет, что метод get_books_genre возвращает корректный словарь с книгами и их жанрами.

test_get_books_for_children_returns_list_with_no_genre_age_rating
Проверяет, что метод возвращает книги, жанр которых не входит в список возрастных ограничений.

test_add_book_in_favorites_book_in_books_genre_append_in_list_favorite
Проверяет, что книга добавляется в список favorites, если она есть в books_genre.

test_add_book_in_favorites_twiсe_add_one
Проверяет, что одну и ту же книгу нельзя добавить в избранное дважды.

test_delete_book_from_favorites_if_book_in_list_favorite
Проверяет, что книга удаляется из избранного, если она там присутствует.

test_get_list_of_favorites_books_book_in_favorite
Проверяет, что метод возвращает корректный список избранных книг.
