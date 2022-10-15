# import sqlite3
# c = sqlite3.connect('food.db')
# c.close()
# cursor = c.cursor()
# cursor.execute("insert into food_order(food) values(\' A \') ")
# c.commit()
# res = cursor.execute("Select ID from food_order order by ID desc")
# result = res.fetchone()[0]
# print(result)
# # dispatcher.utter_message(text=f"You have successfully ordered a meal. The order number is " + str(result))
