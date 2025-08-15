#!/usr/bin/env python3
"""
Script to create the alx_book_store database in MySQL server.
Creates database if it doesn't exist, handles connection errors gracefully.
"""

import mysql.connector


def create_database():
    """
    Creates the alx_book_store database if it doesn't already exist.
    Handles database connection and error management.
    """
    connection = None
    cursor = None

    try:
        # Establish connection to MySQL server
        # Note: Update these credentials according to your MySQL setup
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # MySQL username
            password="WAKHALE@CODing2023",  # MySQL password
            port=3306,  # Default MySQL port
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
