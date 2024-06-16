from db import cursor, conn 

class PriceRange:
    TABLE_NAME = 'price_ranges'

    def __init__(self, min_price, max_price):
        self.id = None
        self.min_price = min_price
        self.max_price = max_price

    def save(self):
        existing_price_range = self.find_by_prices(self.min_price, self.max_price)
        if existing_price_range:
            print(f"Price range ${self.min_price}-${self.max_price} already exists in the database")
            self.id = existing_price_range.id
        else:
            sql = f"""
                INSERT INTO {self.TABLE_NAME} (min_price, max_price)
                VALUES (?, ?)
            """
            cursor.execute(sql, (self.min_price, self.max_price))
            conn.commit()
            self.id = cursor.lastrowid
            print(f"Price range ${self.min_price}-${self.max_price} saved")

    def to_dict(self):
        return {
            "id": self.id,
            "min_price": self.min_price,
            "max_price": self.max_price
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

        price_range = cls(row[1], row[2])
        price_range.id = row[0]

        return price_range

    @classmethod
    def find_by_prices(cls, min_price, max_price):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE min_price = ? AND max_price = ?
        """
        result = cursor.execute(sql, (min_price, max_price)).fetchone()
        return cls.row_to_instance(result) if result else None

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                min_price REAL NOT NULL,
                max_price REAL NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"Price ranges table created")


price_ranges = [
    (80, 100), (101, 150), (151, 200), (201, 300), (301, 400),
    (401, 500), (501, 600), (601, 700), (701, 800), (801, 900),
    (901, 1000)
]

PriceRange.create_table()

for min_price, max_price in price_ranges:
    price_range = PriceRange(min_price, max_price)
    price_range.save()

