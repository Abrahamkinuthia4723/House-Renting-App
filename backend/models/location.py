from db import cursor, conn  

class Location:
    TABLE_NAME = 'locations'

    def __init__(self, name):
        self.id = None
        self.name = name

    def save(self):
        existing_location = self.find_by_name(self.name)
        if existing_location:
            print(f"{self.name} already exists in the database")
            self.id = existing_location.id
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

        location = cls(row[1])
        location.id = row[0]

        return location

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
        print(f"{cls.TABLE_NAME} table created")


Location.create_table()

locations = [
    "Paris", "New York City", "Tokyo", "London", "Rome", "Dubai", "Sydney", "Moscow", 
    "Rio de Janeiro", "Cape Town", "Hong Kong", "Berlin", "Barcelona", "Mumbai", 
    "Bangkok", "Singapore", "Istanbul", "Toronto", "Los Angeles", "Florence", 
    "Amsterdam", "Prague", "Athens", "Seoul", "Mexico City", "Dublin", "Cairo", 
    "Venice", "San Francisco", "Edinburgh", "Buenos Aires", "Stockholm", "Vienna", 
    "Lisbon", "Beijing", "Madrid", "Warsaw", "Budapest", "Hanoi", "Kyoto", 
    "Osaka", "St. Petersburg", "Brussels", "Jakarta", "Nairobi", "Copenhagen", 
    "Zurich", "Munich", "Vancouver", "Melbourne", "Perth", "Auckland", 
    "Wellington", "Helsinki", "Dubrovnik", "Montreal", "Quebec City", "San Diego", 
    "Chicago", "Dallas", "Boston", "Seattle", "Denver", "Phoenix", 
    "Las Vegas", "Miami", "Orlando", "New Orleans", "Philadelphia", "Washington D.C.", 
    "San Jose", "Portland", "Atlanta", "Houston", "Austin", "Salt Lake City", 
    "Honolulu", "Anchorage", "Guatemala City", "San Salvador", "Panama City", "Lima", 
    "Santiago", "Bogota", "Caracas", "Lagos", "Johannesburg", "Casablanca", 
    "Marrakech", "Doha"
]


for location_name in locations:
    location = Location(location_name)
    location.save()

all_locations = Location.find_all()
print("All Locations:")
for location in all_locations:
    print(location['name'])
