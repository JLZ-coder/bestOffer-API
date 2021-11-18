import functools
import psycopg2
from psycopg2.extras import RealDictCursor
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/<int:id>', methods=('GET',))
def get_user(id):

    user_json = {}

    with psycopg2.connect("dbname=bestoffer user=juanliu password=1234", cursor_factory=RealDictCursor) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id=%s", (id,))
            user_data = cur.fetchall()
            user_json.update(
                {
                    "users" : user_data,
                    "total" : len(user_data)
                }
            )

    return jsonify(user_json)

@bp.route('/', methods=('GET',))
def get_all_users():

    user_json = {}

    with psycopg2.connect("dbname=bestoffer user=juanliu password=1234", cursor_factory=RealDictCursor) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            user_data = cur.fetchall()
            user_json.update(
                {
                    "users" : user_data,
                    "total" : len(user_data)
                }
            )

    return jsonify(user_json)


@bp.route('/', methods=('POST',))
def add_user():

    user_json = request.get_json()

    with psycopg2.connect("dbname=bestoffer user=juanliu password=1234") as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (email, password) VALUES(%s, %s)", 
                (
                    user_json["email"],
                    generate_password_hash(user_json["password"])
                )
            )
            conn.commit()

    return "", 201


@bp.route('/<int:id>', methods=('PUT',))
def update_user(id):

    user_json = request.get_json()

    with psycopg2.connect("dbname=bestoffer user=juanliu password=1234") as conn:
        with conn.cursor() as cur:
            cur.execute(
                """UPDATE users 
                SET email=%s,
                    password=%s  
                WHERE id=%s""",
                (
                    user_json["email"],
                    generate_password_hash(user_json["password"]),
                    id,
                )
            )
            conn.commit()
            

    return "", 200

@bp.route('/<int:id>', methods=('DELETE',))
def delete_user(id):

    with psycopg2.connect("dbname=bestoffer user=juanliu password=1234") as conn:
        with conn.cursor() as cur:
            cur.execute(
                """DELETE FROM users 
                WHERE id=%s""",
                (
                    id,
                )
            )
            conn.commit()
            

    return "", 204