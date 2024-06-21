from db import conn, cursor

class House:
    TABLE_NAME = "house"

    def __init__(self, name, type_id, location, price_range, image_url, description, year_of_birth):
        self.id = None
        self.name = name
        self.type_id = type_id
        self.location = location
        self.price_range = price_range
        self.image_url = image_url
        self.description = description
        self.year_of_birth = year_of_birth
        self.created_at = None
        self.house_type = None

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, type_id, location, price_range, image_url, description, year_of_birth)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.type_id, self.location, self.price_range, self.image_url, self.description, self.year_of_birth))
        conn.commit()
        self.id = cursor.lastrowid

        return self

    def update(self):
        sql = f"""
            UPDATE {self.TABLE_NAME}
            SET name = ?, type_id = ?, location = ?, price_range = ?, image_url = ?, description = ?, year_of_birth = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.type_id, self.location, self.price_range, self.image_url, self.description, self.year_of_birth, self.id))
        conn.commit()

        return self

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type_id": self.type_id,
            "location": self.location,
            "price_range": self.price_range,
            "image_url": self.image_url,
            "description": self.description,
            "year_of_birth": self.year_of_birth,
            "created_at": self.created_at,
            "house_type": self.house_type.to_dict() if self.house_type else None,
        }

    @classmethod
    def find_one(cls, id):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()

        return cls.row_to_instance(row)

    @classmethod
    def find_all(cls):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            ORDER BY created_at ASC
        """

        rows = cursor.execute(sql).fetchall()

        return [
            cls.row_to_instance(row).to_dict() for row in rows
        ]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None

        house = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        house.id = row[0]
        house.created_at = row[8]
        house.house_type = None

        return house

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type_id INTEGER NOT NULL,
                location TEXT NOT NULL,
                price_range TEXT NOT NULL,
                image_url TEXT NOT NULL,
                description TEXT NOT NULL,
                year_of_birth INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (type_id) REFERENCES house_types(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created successfully")

    @classmethod
    def alter_table(cls):
        sql = f"""ALTER TABLE {cls.TABLE_NAME} ADD COLUMN house_type TEXT"""  
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table altered")

if __name__ == "__main__":
    House.create_table()


