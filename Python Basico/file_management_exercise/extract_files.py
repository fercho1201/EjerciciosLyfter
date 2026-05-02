import os
from notion_client import Client

SECRET_KEY = os.getenv("NOTION_SECRET")
DATABASE_ID = "32188fc0bcdf806cbac2e7e085084b0a"


def get_sorted_songs(secret_key, database_id):
    notion = Client(auth=secret_key)
    response = notion.databases.query(database_id=database_id)

    songs = []
    for page in response["results"]:
        title_prop = page["properties"]["Song"]["title"]
        if title_prop:
            songs.append(title_prop[0]["plain_text"])

    songs.sort()
    return songs


def create_notion_table(secret_key, database_id, sorted_lines):
    if not sorted_lines:
        print("No songs found. Nothing to create.")
        return

    notion = Client(auth=secret_key)

   
    new_page = notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Song": {
                "title": [{"text": {"content": "Sorted Table"}}]
            }
        }
    )

    new_page_id = new_page["id"]

    children = [
        {
            "object": "block",
            "type": "table",
            "table": {
                "table_width": 1,
                "has_column_header": True,
                "has_row_header": False,
                "children": [
                    {
                        "object": "block",
                        "type": "table_row",
                        "table_row": {
                            "cells": [[{"type": "text", "text": {"content": line}}]]
                        }
                    }
                    for line in sorted_lines
                ]
            }
        }
    ]

    notion.blocks.children.append(block_id=new_page_id, children=children)
    print(f"Table created! Page ID: {new_page_id}")


sorted_lines = get_sorted_songs(SECRET_KEY, DATABASE_ID)
print("Songs found:", sorted_lines) 
create_notion_table(SECRET_KEY, DATABASE_ID, sorted_lines)