from db import cursor, conn 

class HouseType:
    TABLE_NAME = 'house_types'

    def __init__(self, name):
        self.id = None
        self.name = name

    def save(self):
       
        existing_house_type = self.find_by_name(self.name)
        if existing_house_type:
            print(f"{self.name} already exists in the database")
            self.id = existing_house_type.id
        else:
            sql = f"""
                INSERT INTO {self.TABLE_NAME} (name)
                VALUES (?)
            """
            cursor.execute(sql, (self.name,))
            conn.commit()
            self.id = cursor.lastrowid
            print(f"{self.name} saved")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def find_all(cls):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
        """
        rows = cursor.execute(sql).fetchall()

        return [
            cls.row_to_instance(row).to_dict() for row in rows
        ]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None

        house_type = cls(row[1])
        house_type.id = row[0]

        return house_type

    @classmethod
    def find_by_name(cls, name):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE name = ?
        """
        result = cursor.execute(sql, (name,)).fetchone()
        return cls.row_to_instance(result) if result else None

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"House types table created")


house_types = [
    "Ranch-style house", "Cottage", "Victorian", "Colonial", "Craftsman",
    "Tudor", "Mediterranean", "Cabin", "Modern", "Bungalow",
    "Log cabin", "Geodesic dome", "Townhouse", "Split-level", "Farmhouse",
    "Pueblo", "Treehouse", "Mobile home", "Castle", "Houseboat"
]


HouseType.create_table()


for name in house_types:
    house_type = HouseType(name)
    house_type.save()


all_house_types = HouseType.find_all()
print("All House Types:")
for house_type in all_house_types:
    print(house_type['name'])



