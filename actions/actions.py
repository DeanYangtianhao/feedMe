# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions
#
#
# # This is a simple example for a custom action which utters "Hello World!"
# #
# # from rasa_sdk.types import DomainDict
# # from rasa_sdk.events import SlotSet
# import requests
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import sqlite3





# cursor = c.cursor()

# cursor.execute('create table if not exists food_order(ID integer primary key autoincrement)')
class QueryOrderDetails(Action):

    def name(self) -> Text:
        return "ask_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Runs a query using only the order ID column, outputs an utterance
        to the user w/ the relevent
        information for one of the returned rows.
        """
        c = sqlite3.connect('food.db')

        cursor = c.cursor()
        cursor.execute("insert into food_order(food) values(\' A \') ")
        print("success1")
        c.commit()
        res = cursor.execute("Select ID from food_order order by ID desc")
        result = res.fetchone()[0]
        print("success2")
        dispatcher.utter_message(text=f"You have successfully ordered a meal. The order number is {str(result)} ")
        c.close()
        # conn = DbQueryingMethods.create_connection(db_file="sarcdb/SarcbotDB.db")
        #
        # slot_value = tracker.get_slot("order_number")
        #
        # get_query_results = DbQueryingMethods.select_by_slot(conn=conn, slot_value=slot_value)
        #
        # dispatcher.utter_message(text=str(get_query_results))

        return


