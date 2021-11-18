import psycopg2
from werkzeug.security import generate_password_hash

# Connect to an existing database
conn = psycopg2.connect("dbname=bestoffer user=juanliu password=1234")

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("DROP TABLE offers")
cur.execute("DROP TABLE products")
cur.execute("DROP TABLE users")

# Execute a command: this creates a new table
cur.execute("""CREATE TABLE users (
    id serial PRIMARY KEY,
    email varchar(150),
    password varchar(150)
    );""")

cur.execute(
    """CREATE TABLE products (
        id serial PRIMARY KEY,
        name varchar(150),
        description text
        );"""
)

cur.execute(
    """CREATE TABLE offers (
        id serial PRIMARY KEY,
        user_id int,
        product_id int,
        price money,
        site varchar(150),
        CONSTRAINT fk_user
            FOREIGN KEY(user_id) 
            REFERENCES users(id)
                ON DELETE SET NULL,
        CONSTRAINT fk_product
            FOREIGN KEY(product_id) 
            REFERENCES products(id)
                ON DELETE CASCADE
                );"""
)

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("insert into products (name, description) values ('Wine - Carmenere Casillero Del', 'ññññáéíóúñññññ¿?¡Caracteres raros!');")
cur.execute("insert into products (name, description) values ('Soup Campbells Beef With Veg', 'ññññáéíóúñññññ¿?¡Caracteres raros!');")
cur.execute("insert into products (name, description) values ('Cream - 10%', 'ññññáéíóúñññññ¿?¡Caracteres raros!');")
cur.execute("insert into products (name, description) values ('Momiji Oroshi Chili Sauce', 'ññññáéíóúñññññ¿?¡Caracteres raros!');")
cur.execute("insert into products (name, description) values ('Remy Red', 'ññññáéíóúñññññ¿?¡Caracteres raros!');")

cur.execute("insert into users (email, password) values (%s, %s)", ("lbreckon0@gmail.com", generate_password_hash("1234")))
cur.execute("insert into users (email, password) values (%s, %s)", ("juan@gmail.com", generate_password_hash("1234")))
cur.execute("insert into users (email, password) values (%s, %s)", ("ana@gmail.com", generate_password_hash("1234")))
cur.execute("insert into users (email, password) values (%s, %s)", ("pedro@gmail.com", generate_password_hash("1234")))
cur.execute("insert into users (email, password) values (%s, %s)", ("lebigmac@gmail.com", generate_password_hash("1234")))

cur.execute("insert into offers (user_id, product_id, price, site) values (%s, %s, %s, %s)",
    (1, 1, 10.00, "https://www.amazon.com/"))
cur.execute("insert into offers (user_id, product_id, price, site) values (%s, %s, %s, %s)",
    (2, 1, 35.56, "https://www.amazon.com/"))
cur.execute("insert into offers (user_id, product_id, price, site) values (%s, %s, %s, %s)",
    (3, 3, 35.56, "https://www.amazon.com/"))
cur.execute("insert into offers (user_id, product_id, price, site) values (%s, %s, %s, %s)",
    (1, 2, 35.56, "https://www.amazon.com/"))
cur.execute("insert into offers (user_id, product_id, price, site) values (%s, %s, %s, %s)",
    (4, 2, 35.56, "https://www.amazon.com/"))

# Query the database and obtain data as Python objects

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()