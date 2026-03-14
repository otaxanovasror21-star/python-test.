"""
Testlar to'plami: Frontend, HTML, Python, Database
Jami: 100 ta test
"""

import unittest
import os
import re
import sqlite3
from html.parser import HTMLParser


# ============================================================================
# 1. FRONTEND VA HTML TESTLARI (1-25)
# ============================================================================

class TestHTMLBasics(unittest.TestCase):
    """HTML asosiy tushunchalari bo'yicha testlar"""
    
    def test_html_document_structure(self):
        """HTML hujjat tuzilmasini tekshirish"""
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><title>Test</title></head>
        <body><h1>Salom</h1></body>
        </html>
        """
        self.assertIn('<!DOCTYPE html>', html_content)
        self.assertIn('<html>', html_content)
        self.assertIn('</html>', html_content)
    
    def test_html_heading_tags(self):
        """HTML sarlavha teglarini tekshirish"""
        headings = ['<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>']
        for tag in headings:
            self.assertIn(tag, f'<{tag[1:]}>')
    
    def test_html_paragraph_tag(self):
        """P tegini tekshirish"""
        self.assertIn('<p>', '<p>Matn</p>')
        self.assertIn('</p>', '<p>Matn</p>')
    
    def test_html_link_tag(self):
        """Anchor (a) tegini tekshirish"""
        link = '<a href="https://example.com">Link</a>'
        self.assertIn('href=', link)
        self.assertTrue('<a ' in link or link.startswith('<a>'))
    
    def test_html_image_tag(self):
        """Img tegini tekshirish"""
        img = '<img src="rasm.jpg" alt="Rasm">'
        self.assertIn('src=', img)
        self.assertIn('alt=', img)
    
    def test_html_list_tags(self):
        """Ro'yxat teglarini tekshirish"""
        ul = '<ul><li>Element</li></ul>'
        ol = '<ol><li>Element</li></ol>'
        self.assertIn('<ul>', ul)
        self.assertIn('<ol>', ol)
        self.assertIn('<li>', ul)
    
    def test_html_table_tag(self):
        """Jadval teglarini tekshirish"""
        table = '<table><tr><td>Ma\'lumot</td></tr></table>'
        self.assertIn('<table>', table)
        self.assertIn('<tr>', table)
        self.assertIn('<td>', table)
    
    def test_html_form_tag(self):
        """Forma teglarini tekshirish"""
        form = '<form action="/submit" method="POST"><input type="text"></form>'
        self.assertIn('<form', form)
        self.assertIn('method=', form)
        self.assertIn('<input', form)
    
    def test_html_button_tag(self):
        """Button tegini tekshirish"""
        button = '<button type="submit">Jonatish</button>'
        self.assertIn('<button', button)
        self.assertIn('type=', button)
    
    def test_html_input_types(self):
        """Input turlarini tekshirish"""
        inputs = ['text', 'password', 'email', 'number', 'checkbox', 'radio']
        for input_type in inputs:
            self.assertIn(f'type="{input_type}"', f'<input type="{input_type}">')
    
    def test_html_div_tag(self):
        """Div tegini tekshirish"""
        div = '<div class="container"><p>Content</p></div>'
        self.assertIn('<div', div)
        self.assertIn('class=', div)
    
    def test_html_span_tag(self):
        """Span tegini tekshirish"""
        span = '<span class="highlight">Matn</span>'
        self.assertIn('<span', span)
    
    def test_html_meta_tags(self):
        """Meta teglarini tekshirish"""
        meta = '<meta charset="UTF-8"><meta name="viewport" content="width=device-width">'
        self.assertIn('charset=', meta)
        self.assertIn('name="viewport"', meta)
    
    def test_html_script_tag(self):
        """Script tegini tekshirish"""
        script = '<script src="script.js"></script>'
        self.assertIn('<script', script)
        self.assertIn('src=', script)
    
    def test_html_style_tag(self):
        """Style tegini tekshirish"""
        style = '<style>.class { color: red; }</style>'
        self.assertIn('<style>', style)
    
    def test_html_select_tag(self):
        """Select tegini tekshirish"""
        select = '<select><option>Option 1</option></select>'
        self.assertIn('<select>', select)
        self.assertIn('<option>', select)
    
    def test_html_textarea_tag(self):
        """Textarea tegini tekshirish"""
        textarea = '<textarea rows="4" cols="50"></textarea>'
        self.assertIn('<textarea', textarea)
    
    def test_html_br_tag(self):
        """BR tegini tekshirish (self-closing)"""
        br = '<br>'
        self.assertIn('<br>', br)
    
    def test_html_hr_tag(self):
        """HR tegini tekshirish"""
        hr = '<hr>'
        self.assertIn('<hr>', hr)
    
    def test_html_iframe_tag(self):
        """Iframe tegini tekshirish"""
        iframe = '<iframe src="page.html"></iframe>'
        self.assertIn('<iframe', iframe)
        self.assertIn('src=', iframe)
    
    def test_html_comment_syntax(self):
        """HTML izoh sintaksisini tekshirish"""
        comment = '<!-- Izoh matni -->'
        self.assertIn('<!--', comment)
        self.assertIn('-->', comment)
    
    def test_html_entity_references(self):
        """HTML entity-referencelarini tekshirish"""
        self.assertEqual('<', '<')
        self.assertEqual('>', '>')
        self.assertEqual('&', '&')
        self.assertEqual('"', '"')
    
    def test_html5_semantic_tags(self):
        """HTML5 semantik teglarini tekshirish"""
        semantic = ['<header>', '<nav>', '<main>', '<article>', '<section>', '<footer>']
        for tag in semantic:
            self.assertIn(tag, f'<{tag[1:]}></{tag[1:]}>')
    
    def test_html_attribute_quotes(self):
        """HTML atribut qo'shtirnoqlarini tekshirish"""
        element = '<div class="test" id="main"></div>'
        self.assertIn('class="test"', element)
        self.assertIn('id="main"', element)
    
    def test_html_doctype(self):
        """HTML DOCTYPE ni tekshirish"""
        doctype = '<!DOCTYPE html>'
        self.assertIn('!DOCTYPE', doctype)


class TestHTMLValidation(unittest.TestCase):
    """HTML validatsiya testlari"""
    
    def test_self_closing_tags(self):
        """Self-closing teglarni tekshirish"""
        self_closing = ['<br>', '<hr>', '<img>', '<input>', '<meta>', '<link>']
        for tag in self_closing:
            self.assertIn('<', tag)
    
    def test_nested_tags(self):
        """Ichma-ich teglarni tekshirish"""
        nested = '<div><p><span>Matn</span></p></div>'
        self.assertEqual(nested.count('<div>'), 1)
        self.assertEqual(nested.count('</div>'), 1)


# ============================================================================
# 2. CSS TESTLARI (26-40)
# ============================================================================

class TestCSSBasics(unittest.TestCase):
    """CSS asosiy tushunchalari bo'yicha testlar"""
    
    def test_css_selector_syntax(self):
        """CSS selector sintaksisini tekshirish"""
        css = '.class { color: red; }'
        self.assertIn('.class', css)
        self.assertIn('{', css)
        self.assertIn('}', css)
    
    def test_css_id_selector(self):
        """ID selector ni tekshirish"""
        css = '#header { background: blue; }'
        self.assertIn('#header', css)
    
    def test_css_element_selector(self):
        """Element selector ni tekshirish"""
        css = 'p { margin: 10px; }'
        self.assertIn('p {', css)
    
    def test_css_multiple_selectors(self):
        """Ko'p selectorlarni tekshirish"""
        css = 'h1, h2, h3 { font-weight: bold; }'
        self.assertIn(',', css)
    
    def test_css_descendant_selector(self):
        """Avlod selector ni tekshirish"""
        css = 'div p { padding: 5px; }'
        self.assertIn(' ', css)
    
    def test_css_color_properties(self):
        """Rang xossalarini tekshirish"""
        colors = ['color: red;', 'background-color: #fff;', 'border-color: rgb(0,0,0);']
        for color in colors:
            self.assertIn('color', color)
    
    def test_css_box_model(self):
        """Box model xossalarini tekshirish"""
        box = 'margin: 10px; padding: 15px; border: 1px solid black;'
        self.assertIn('margin', box)
        self.assertIn('padding', box)
        self.assertIn('border', box)
    
    def test_css_flexbox(self):
        """Flexbox xossalarini tekshirish"""
        flex = 'display: flex; justify-content: center; align-items: center;'
        self.assertIn('display: flex', flex)
        self.assertIn('justify-content', flex)
    
    def test_css_grid(self):
        """CSS Grid xossalarini tekshirish"""
        grid = 'display: grid; grid-template-columns: 1fr 1fr; gap: 10px;'
        self.assertIn('display: grid', grid)
        self.assertIn('grid-template-columns', grid)
    
    def test_css_position(self):
        """Position xossalarini tekshirish"""
        positions = ['position: static;', 'position: relative;', 'position: absolute;', 'position: fixed;']
        for pos in positions:
            self.assertIn('position:', pos)
    
    def test_css_responsive_media_query(self):
        """Media query ni tekshirish"""
        media = '@media (max-width: 768px) { .class { display: none; } }'
        self.assertIn('@media', media)
        self.assertIn('max-width', media)
    
    def test_css_pseudo_classes(self):
        """Pseudo-classlarni tekshirish"""
        pseudo = ':hover, :focus, :active, :first-child'
        self.assertIn(':hover', pseudo)
    
    def test_css_pseudo_elements(self):
        """Pseudo-elementlarni tekshirish"""
        pseudo = '::before, ::after, ::first-line'
        self.assertIn('::before', pseudo)
    
    def test_css_important_keyword(self):
        """!important kalit so'zini tekshirish"""
        css = 'color: red !important;'
        self.assertIn('!important', css)
    
    def test_css_important_priority(self):
        """CSS muhimligi tartibini tekshirish"""
        # Inline > ID > Class > Element
        priorities = ['inline', 'id', 'class', 'element']
        self.assertEqual(len(priorities), 4)


# ============================================================================
# 3. JAVASCRIPT TESTLARI (41-50)
# ============================================================================

class TestJavaScriptBasics(unittest.TestCase):
    """JavaScript asosiy tushunchalari bo'yicha testlar"""
    
    def test_js_variable_declaration(self):
        """O'zgaruvchi e'lon qilishni tekshirish"""
        js_code = 'let x = 5; const y = 10; var z = 15;'
        self.assertIn('let', js_code)
        self.assertIn('const', js_code)
        self.assertIn('var', js_code)
    
    def test_js_function_declaration(self):
        """Funksiya e'lon qilishni tekshirish"""
        func = 'function test() { return true; }'
        self.assertIn('function', func)
        self.assertIn('()', func)
    
    def test_js_arrow_function(self):
        """Arrow funksiyani tekshirish"""
        arrow = 'const add = (a, b) => a + b;'
        self.assertIn('=>', arrow)
    
    def test_js_array_methods(self):
        """Array metodlarini tekshirish"""
        methods = ['map', 'filter', 'reduce', 'forEach', 'find']
        for method in methods:
            self.assertIn(method, f'arr.{method}()')
    
    def test_js_dom_manipulation(self):
        """DOM manipulyatsiyasini tekshirish"""
        dom = "document.getElementById('id'); document.querySelector('.class');"
        self.assertIn('document.getElementById', dom)
        self.assertIn('document.querySelector', dom)
    
    def test_js_event_handling(self):
        """Event handlerlarni tekshirish"""
        event = "element.addEventListener('click', handler);"
        self.assertIn('addEventListener', event)
    
    def test_js_promise(self):
        """Promise ni tekshirish"""
        promise = 'new Promise((resolve, reject) => { });'
        self.assertIn('Promise', promise)
    
    def test_js_async_await(self):
        """Async/await ni tekshirish"""
        async_code = 'async function fetchData() { const data = await fetch(url); }'
        self.assertIn('async', async_code)
        self.assertIn('await', async_code)
    
    def test_js_json_operations(self):
        """JSON operatsiyalarini tekshirish"""
        json_ops = 'JSON.stringify(obj); JSON.parse(str);'
        self.assertIn('JSON.stringify', json_ops)
        self.assertIn('JSON.parse', json_ops)
    
    def test_js_error_handling(self):
        """Xatolarni qayta ishlashni tekshirish"""
        error = 'try { } catch (e) { } finally { }'
        self.assertIn('try', error)
        self.assertIn('catch', error)
        self.assertIn('finally', error)


# ============================================================================
# 4. PYTHON TESTLARI (51-75)
# ============================================================================

class TestPythonBasics(unittest.TestCase):
    """Python asosiy tushunchalari bo'yicha testlar"""
    
    def test_python_variable(self):
        """Python o'zgaruvchisini tekshirish"""
        x = 10
        self.assertIsInstance(x, int)
    
    def test_python_string(self):
        """Python stringni tekshirish"""
        s = "Hello, World!"
        self.assertIsInstance(s, str)
        self.assertEqual(len(s), 13)
    
    def test_python_list(self):
        """Python listni tekshirish"""
        lst = [1, 2, 3, 4, 5]
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 5)
    
    def test_python_tuple(self):
        """Python tupleni tekshirish"""
        t = (1, 2, 3)
        self.assertIsInstance(t, tuple)
        self.assertEqual(t[0], 1)
    
    def test_python_dictionary(self):
        """Python lug'atni tekshirish"""
        d = {'name': 'Ali', 'age': 25}
        self.assertIsInstance(d, dict)
        self.assertEqual(d['name'], 'Ali')
    
    def test_python_set(self):
        """Python setni tekshirish"""
        s = {1, 2, 3}
        self.assertIsInstance(s, set)
    
    def test_python_if_statement(self):
        """if qatorini tekshirish"""
        x = 5
        if x > 0:
            result = "musbat"
        self.assertEqual(result, "musbat")
    
    def test_python_for_loop(self):
        """for tsiklini tekshirish"""
        total = sum([1, 2, 3, 4, 5])
        self.assertEqual(total, 15)
    
    def test_python_while_loop(self):
        """while tsiklini tekshirish"""
        count = 0
        while count < 3:
            count += 1
        self.assertEqual(count, 3)
    
    def test_python_function(self):
        """Funksiyani tekshirish"""
        def greet(name):
            return f"Salom, {name}!"
        self.assertEqual(greet("Ali"), "Salom, Ali!")
    
    def test_python_lambda(self):
        """Lambda funksiyani tekshirish"""
        square = lambda x: x ** 2
        self.assertEqual(square(5), 25)
    
    def test_python_class(self):
        """Class ni tekshirish"""
        class Person:
            def __init__(self, name):
                self.name = name
        p = Person("Ali")
        self.assertEqual(p.name, "Ali")
    
    def test_python_inheritance(self):
        """Inheritance ni tekshirish"""
        class Animal:
            def speak(self):
                return "Sound"
        class Dog(Animal):
            def speak(self):
                return "Woof"
        dog = Dog()
        self.assertEqual(dog.speak(), "Woof")
    
    def test_python_exception_handling(self):
        """Exception handle qilishni tekshirish"""
        try:
            x = 1 / 0
        except ZeroDivisionError:
            result = "Xatolik"
        self.assertEqual(result, "Xatolik")
    
    def test_python_file_reading(self):
        """Fayl o'qishni tekshirish"""
        content = "Test matn"
        self.assertIsInstance(content, str)
    
    def test_python_list_comprehension(self):
        """List comprehension ni tekshirish"""
        squares = [x**2 for x in range(5)]
        self.assertEqual(squares, [0, 1, 4, 9, 16])
    
    def test_python_dict_comprehension(self):
        """Dict comprehension ni tekshirish"""
        d = {x: x**2 for x in range(3)}
        self.assertEqual(d, {0: 0, 1: 1, 2: 4})
    
    def test_python_map_function(self):
        """map funksiyasini tekshirish"""
        result = list(map(lambda x: x*2, [1, 2, 3]))
        self.assertEqual(result, [2, 4, 6])
    
    def test_python_filter_function(self):
        """filter funksiyasini tekshirish"""
        result = list(filter(lambda x: x > 2, [1, 2, 3, 4]))
        self.assertEqual(result, [3, 4])
    
    def test_python_string_methods(self):
        """String metodlarini tekshirish"""
        s = "  Hello World  "
        self.assertEqual(s.strip(), "Hello World")
        self.assertEqual(s.lower(), "  hello world  ")
        self.assertEqual(s.upper(), "  HELLO WORLD  ")
    
    def test_python_list_methods(self):
        """List metodlarini tekshirish"""
        lst = [1, 2, 3]
        lst.append(4)
        self.assertEqual(lst, [1, 2, 3, 4])
        lst.pop()
        self.assertEqual(lst, [1, 2, 3])
    
    def test_python_set_operations(self):
        """Set operatsiyalarini tekshirish"""
        a = {1, 2, 3}
        b = {2, 3, 4}
        self.assertEqual(a.union(b), {1, 2, 3, 4})
        self.assertEqual(a.intersection(b), {2, 3})
    
    def test_python_decorator(self):
        """Decorator ni tekshirish"""
        def decorator(func):
            def wrapper():
                return "Decorated"
            return wrapper
        self.assertIsNotNone(decorator)
    
    def test_python_generator(self):
        """Generator ni tekshirish"""
        def gen():
            yield 1
            yield 2
        g = gen()
        self.assertEqual(next(g), 1)
        self.assertEqual(next(g), 2)


# ============================================================================
# 5. DATABASE TESTLARI (76-100)
# ============================================================================

class TestDatabaseBasics(unittest.TestCase):
    """Database asosiy tushunchalari bo'yicha testlar"""
    
    def test_sqlite_connection(self):
        """SQLite bog'lanishini tekshirish"""
        conn = sqlite3.connect(':memory:')
        self.assertIsNotNone(conn)
        conn.close()
    
    def test_sqlite_create_table(self):
        """Jadval yaratishni tekshirish"""
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        result = cursor.fetchone()
        self.assertEqual(result[0], 'users')
        conn.close()
    
    def test_sqlite_insert_data(self):
        """Ma'lumot kiritishni tekshirish"""
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
        cursor.execute('INSERT INTO users (name) VALUES (?)', ('Ali',))
        conn.commit()
        cursor.execute('SELECT * FROM users')
        result = cursor.fetchone()
        self.assertEqual(result[1], 'Ali')
        conn.close()
    
    def test_sqlite_select_data(self):
        """Ma'lumot tanlashni tekshirish"""
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE test (id INTEGER, value TEXT)')
        cursor.execute('INSERT INTO test VALUES (1, "test")')
        cursor.execute('SELECT value FROM test WHERE id=1')
        self.assertEqual(cursor.fetchone()[0], 'test')
        conn.close()
    
    def test_sqlite_update_data(self):
        """Ma'lumot yangilashni tekshirish"""
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')
        cursor.execute('INSERT INTO users VALUES (1, "Ali")')
        cursor.execute('UPDATE users SET name=? WHERE id=?', ('Vali', 1))
        conn.commit()
        cursor.execute('SELECT name FROM users WHERE id=1')
        self.assertEqual(cursor.fetchone()[0], 'Vali')
        conn.close()
    
    def test_sqlite_delete_data(self):
        """Ma'lumot o'chirishni tekshirish"""
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')
        cursor.execute('INSERT INTO users VALUES (1, "Ali")')
        cursor.execute('DELETE FROM users WHERE id=1')
        conn.commit()
        cursor.execute('SELECT * FROM users')
        self.assertIsNone(cursor.fetchone())
        conn.close()
    
    def test_sql_select_keyword(self):
        """SELECT kalit so'zini tekshirish"""
        query = "SELECT name, age FROM users WHERE age > 18"
        self.assertIn('SELECT', query)
    
    def test_sql_insert_keyword(self):
        """INSERT kalit so'zini tekshirish"""
        query = "INSERT INTO users (name, age) VALUES ('Ali', 25)"
        self.assertIn('INSERT', query)
    
    def test_sql_update_keyword(self):
        """UPDATE kalit so'zini tekshirish"""
        query = "UPDATE users SET age=26 WHERE name='Ali'"
        self.assertIn('UPDATE', query)
    
    def test_sql_delete_keyword(self):
        """DELETE kalit so'zini tekshirish"""
        query = "DELETE FROM users WHERE age < 18"
        self.assertIn('DELETE', query)
    
    def test_sql_where_clause(self):
        """WHERE qatorchini tekshirish"""
        query = "SELECT * FROM users WHERE age > 18 AND city='Tashkent'"
        self.assertIn('WHERE', query)
    
    def test_sql_order_by(self):
        """ORDER BY ni tekshirish"""
        query = "SELECT * FROM users ORDER BY name ASC, age DESC"
        self.assertIn('ORDER BY', query)
    
    def test_sql_group_by(self):
        """GROUP BY ni tekshirish"""
        query = "SELECT COUNT(*), city FROM users GROUP BY city"
        self.assertIn('GROUP BY', query)
    
    def test_sql_join(self):
        """JOIN ni tekshirish"""
        query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id"
        self.assertIn('JOIN', query)
    
    def test_sql_left_join(self):
        """LEFT JOIN ni tekshirish"""
        query = "SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id"
        self.assertIn('LEFT JOIN', query)
    
    def test_sql_inner_join(self):
        """INNER JOIN ni tekshirish"""
        query = "SELECT * FROM A INNER JOIN B ON A.id = B.a_id"
        self.assertIn('INNER JOIN', query)
    
    def test_sql_count_function(self):
        """COUNT funksiyasini tekshirish"""
        query = "SELECT COUNT(*) FROM users"
        self.assertIn('COUNT', query)
    
    def test_sql_sum_function(self):
        """SUM funksiyasini tekshirish"""
        query = "SELECT SUM(price) FROM products"
        self.assertIn('SUM', query)
    
    def test_sql_avg_function(self):
        """AVG funksiyasini tekshirish"""
        query = "SELECT AVG(age) FROM users"
        self.assertIn('AVG', query)
    
    def test_sql_max_min_functions(self):
        """MAX/MIN funksiyalarini tekshirish"""
        queries = ["SELECT MAX(price) FROM products", "SELECT MIN(price) FROM products"]
        for q in queries:
            self.assertIn('MAX' if 'MAX' in q else 'MIN', q)
    
    def test_sql_like_operator(self):
        """LIKE operatorini tekshirish"""
        query = "SELECT * FROM users WHERE name LIKE 'A%'"
        self.assertIn('LIKE', query)
    
    def test_sql_in_operator(self):
        """IN operatorini tekshirish"""
        query = "SELECT * FROM users WHERE city IN ('Tashkent', 'Samarkand')"
        self.assertIn('IN', query)
    
    def test_sql_between_operator(self):
        """BETWEEN operatorini tekshirish"""
        query = "SELECT * FROM users WHERE age BETWEEN 18 AND 30"
        self.assertIn('BETWEEN', query)
    
    def test_sql_limit_keyword(self):
        """LIMIT kalit so'zini tekshirish"""
        query = "SELECT * FROM users LIMIT 10"
        self.assertIn('LIMIT', query)
    
    def test_sql_primary_key(self):
        """Primary Key ni tekshirish"""
        create = "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)"
        self.assertIn('PRIMARY KEY', create)
    
    def test_sql_foreign_key(self):
        """Foreign Key ni tekshirish"""
        create = "CREATE TABLE orders (id INTEGER, user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(id))"
        self.assertIn('FOREIGN KEY', create)


# Testlarni ishga tushirish uchun
if __name__ == '__main__':
    unittest.main()
