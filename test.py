from manager.Database_Managers import DatabaseManager

from app import db

db_manager = DatabaseManager(db)

db_manager.add_lecturer(first_name='Timur', last_name='Fatkulin', patronymic='Djalilevich')
db_manager.add_lecturer(first_name='Natalia', last_name='Korolkova', patronymic='Nikolaevna')
db_manager.add_lecturer(first_name='Sergey', last_name='Gurikov', patronymic='Rostislavovic')
db_manager.add_lecturer(first_name='Leonid', last_name='Vorobeichikov', patronymic='Alexandrovich')
db_manager.add_lecturer(first_name="Vladimir", last_name="Vladimirov", patronymic="Lvovich")

db_manager.add_subject(name="AVS")

db_manager.add_interval(name="9:30 - 11:00")
