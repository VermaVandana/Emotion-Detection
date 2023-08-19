import sqlite3
import threading

# Create a threading.local object to store the SQLite connection and cursor
thread_local = threading.local()

# Function to get the SQLite connection and cursor
def get_db():
    if not hasattr(thread_local, "connection"):
        thread_local.connection = sqlite3.connect("C:\\Users\\vanda\\OneDrive\\Desktop\\New folder\\Emotion Detection\\data.db")
    if not hasattr(thread_local, "cursor"):
        thread_local.cursor = thread_local.connection.cursor()
    return thread_local.cursor

# Fxn
def create_page_visited_table():
    cursor = get_db()
    cursor.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')

def add_page_visited_details(pagename, timeOfvisit):
    cursor = get_db()
    cursor.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))
    thread_local.connection.commit()

def view_all_page_visited_details():
    cursor = get_db()
    cursor.execute('SELECT * FROM pageTrackTable')
    data = cursor.fetchall()
    return data

# Fxn To Track Input & Prediction
def create_emotionclf_table():
    cursor = get_db()
    cursor.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfvisit TIMESTAMP)')

def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    cursor = get_db()
    cursor.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES (?, ?, ?, ?)', (rawtext, prediction, probability, timeOfvisit))
    thread_local.connection.commit()

def view_all_prediction_details():
    cursor = get_db()
    cursor.execute('SELECT * FROM emotionclfTable')
    data = cursor.fetchall()
    return data

# Example usage
def main():
    create_page_visited_table()
    add_page_visited_details("Page 1", "2023-06-05 10:00:00")
    add_page_visited_details("Page 2", "2023-06-05 11:00:00")
    page_visited_data = view_all_page_visited_details()
    print(page_visited_data)

    create_emotionclf_table()
    add_prediction_details("Text 1", "Positive", 0.8, "2023-06-05 12:00:00")
    add_prediction_details("Text 2", "Negative", 0.6, "2023-06-05 13:00:00")
    prediction_data = view_all_prediction_details()
    print(prediction_data)

if __name__ == "__main__":
    main()
