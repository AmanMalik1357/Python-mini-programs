import time
from plyer import notification
 
 
if __name__=="__main__":
   
    notification.notify(
        title = "Drink Water",
        message="Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones." ,
        app_name = "Water Remainder",
        app_icon = "D:\Work\VS Code program\Python\Mini Projects\Drink Water Notification\waterGlass.ico",
            # displaying time
        timeout=20
    )
        
    time.sleep(30)
        