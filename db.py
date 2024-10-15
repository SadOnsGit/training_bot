import aiosqlite


DATABASE = 'database.db'


class User:
    """Класс управления доступом пользователей в базе данных."""

    @staticmethod
    async def create_tables():
        """Создать таблицы, если они не существуют."""
        async with aiosqlite.connect(DATABASE) as conn:
            await conn.executescript('''
                CREATE TABLE IF NOT EXISTS user_access (
                    user_id INTEGER PRIMARY KEY
                );

                CREATE TABLE IF NOT EXISTS learns (
                    id_learn INTEGER PRIMARY KEY AUTOINCREMENT,
                    lesson_title TEXT NOT NULL,
                    lesson_text TEXT NOT NULL,
                    file_path TEXT
                );

                CREATE TABLE IF NOT EXISTS webinars (
                    id_webinar INTEGER PRIMARY KEY AUTOINCREMENT,
                    webinar_title TEXT NOT NULL,
                    webinar_description TEXT NOT NULL,
                    file_path TEXT
                );

                CREATE TABLE IF NOT EXISTS guides (
                    id_guide INTEGER PRIMARY KEY AUTOINCREMENT,
                    guide_title TEXT NOT NULL,
                    guide_content TEXT NOT NULL,
                    file_path TEXT
                );
            ''')
            await conn.commit()

    @staticmethod
    async def add_user(user_id: int):
        """Добавить пользователя в таблицу доступа."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                await conn.execute('INSERT OR IGNORE INTO user_access (user_id) VALUES (?)', (user_id,))
                await conn.commit()
            except Exception as e:
                print(f"Error adding user: {e}")

    @staticmethod
    async def user_access_exists(user_id: int) -> bool:
        """Проверить, существует ли доступ для пользователя."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                async with conn.execute('SELECT 1 FROM user_access WHERE user_id = ?', (user_id,)) as cursor:
                    exists = await cursor.fetchone() is not None
                return exists
            except Exception as e:
                print(f"Error checking user access existence: {e}")
                return False


class Webinar:
    """Класс управления вебинарами."""

    @staticmethod
    async def add_webinar(webinar_title: str, webinar_description: str, file_path):
        """Добавить новый вебинар в таблицу."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                await conn.execute(
                    'INSERT INTO webinars (webinar_title, webinar_description, file_path) VALUES (?, ?, ?)',
                    (webinar_title, webinar_description, file_path)
                )
                await conn.commit()
            except Exception as e:
                print(f"Error adding webinar: {e}")

    @staticmethod
    async def delete_webinar(title: str):
        """Удалить вебинар из таблицы по ID."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                await conn.execute('DELETE FROM webinars WHERE webinar_title = ?', (title,))
                await conn.commit()
            except Exception as e:
                print(f"Error deleting webinar: {e}")

    @staticmethod
    async def get_webinars():
        """Получить список всех вебинаров."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                async with conn.execute('SELECT id_webinar, webinar_title FROM webinars') as cursor:
                    webinars = await cursor.fetchall()
                return webinars
            except Exception as e:
                print(f"Error fetching webinars: {e}")
                return []

    @staticmethod
    async def get_webinar_by_id(webinar_id: int):
        """Получить вебинар по ID."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                async with conn.execute('SELECT webinar_description, file_path FROM webinars WHERE id_webinar = ?', (webinar_id,)) as cursor:
                    webinar = await cursor.fetchone()
                return {
                    'webinar_description': webinar[0],
                    'file_path': webinar[1]
                } if webinar else None
            except Exception as e:
                print(f"Error fetching webinar by ID: {e}")
                return None


class Lesson:
    """Класс управления уроками."""

    @staticmethod
    async def add_lesson(lesson_title: str, lesson_text: str):
        """Добавить новый урок в таблицу."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                await conn.execute('INSERT INTO learns (lesson_title, lesson_text) VALUES (?, ?)', (lesson_title, lesson_text))
                await conn.commit()
            except Exception as e:
                print(f"Error adding lesson: {e}")

    @staticmethod
    async def delete_lesson(title: str):
        """Удалить урок из таблицы по ID."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                await conn.execute('DELETE FROM learns WHERE lesson_title = ?', (title,))
                await conn.commit()
            except Exception as e:
                print(f"Error deleting lesson: {e}")

    @staticmethod
    async def get_lessons():
        """Получить список всех уроков."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                async with conn.execute('SELECT id_learn, lesson_title FROM learns') as cursor:
                    lessons = await cursor.fetchall()
                return lessons
            except Exception as e:
                print(f"Error fetching lessons: {e}")
                return []

    @staticmethod
    async def get_lesson_by_id(lesson_id: int):
        """Получить урок по ID."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                async with conn.execute('SELECT lesson_text FROM learns WHERE id_learn = ?', (lesson_id,)) as cursor:
                    lesson = await cursor.fetchone()
                return lesson[0] if lesson else None
            except Exception as e:
                print(f"Error fetching lesson by ID: {e}")
                return None


class Guide:
    """Класс управления гайдами."""

    @staticmethod
    async def add_guide(guide_title: str, guide_content: str, file_path):
        """Добавить новый гайд в таблицу."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                await conn.execute(
                    'INSERT INTO guides (guide_title, guide_content, file_path) VALUES (?, ?, ?)',
                    (guide_title, guide_content, file_path)
                )
                await conn.commit()
            except Exception as e:
                print(f"Error adding guide: {e}")

    @staticmethod
    async def delete_guide(title: str):
        """Удалить гайд из таблицы по ID."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                await conn.execute('DELETE FROM guides WHERE guide_title = ?', (title,))
                await conn.commit()
            except Exception as e:
                print(f"Error deleting guide: {e}")

    @staticmethod
    async def get_guides():
        """Получить список всех гайдов."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                async with conn.execute('SELECT id_guide, guide_title FROM guides') as cursor:
                    guides = await cursor.fetchall()
                return guides
            except Exception as e:
                print(f"Error fetching guides: {e}")
                return []

    @staticmethod
    async def get_guide_by_id(guide_id: int):
        """Получить гайд по ID."""
        async with aiosqlite.connect(DATABASE) as conn:
            try:
                async with conn.execute('SELECT guide_content, file_path FROM guides WHERE id_guide = ?', (guide_id,)) as cursor:
                    guide = await cursor.fetchone()
                return {
                    'guide_content': guide[0] if guide else None,
                    'file_path': guide[1] if guide else None
                }
            except Exception as e:
                print(f"Error fetching guide by ID: {e}")
                return None


user = User()
course = Lesson()
web = Webinar()
guide = Guide()
