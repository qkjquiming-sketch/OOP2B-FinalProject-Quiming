# PrintSync

Printing Shop Order and Queue Management System, built with Python and PyQt6.

PrintSync has two screens that work together:

- **User Screen**: the customer fills in their details, picks the paper, print type and extras, sees an itemised price, and submits the order.
- **Admin Screen**: the shop owner sees all orders, updates their status, deletes or undoes a delete, views sales totals, and changes prices.

It runs fully offline. With two monitors, the User Screen opens on the first and the Admin Screen on the second.

---

# Getting Started with PrintSync

## Installation

1. Go to the [Releases](https://github.com/qkjquiming-sketch/OOP2B-FinalProject-Quiming/releases) page and download `PrintSync.zip`.
2. Right-click the zip file and choose **Extract All...**. Pick a normal folder like Desktop or Documents (not `Program Files`).
3. Open the extracted folder and double-click `PrintSync.exe`.
4. Wait a few seconds. The first launch is slower while the app unpacks itself.
5. If Windows shows "Windows protected your PC", click **More info**, then **Run anyway**. This appears because the app is unsigned.

Your saved prices and the `orders` folder are created next to `PrintSync.exe`.

## Using PrintSync

6. [Set your prices.]
7. [Create a new order and fill in the details.]
8. [Save the order. Find it in the `orders` folder.]
   
---

## Project Structure

```
PrintSync/
├── assets/            # Extra resources
├── main.py            # Entry point: loads style, icon, and both windows
├── base_window.py     # BaseWindow: shared menu bar and close behaviour
├── user_screen.py     # User Screen (order form)
├── admin_screen.py    # Admin Screen (order table, totals, prices)
├── models.py          # Order class and CSV row conversion
├── dialogs.py         # Confirm, alert, and delete dialogs
├── config.py          # Prices, statuses, and loading of prices.json
├── prices.json        # Saved prices
├── style.qss          # Application stylesheet
├── customIcon.png     # Original icon image
├── icon.png           # Generated window icon
├── icon.ico           # Generated .exe icon
├── make_icon.py       # Converts customIcon.png into icon.png and icon.ico
├── PrintSync.spec     # PyInstaller build recipe
└── README.md
```

## Order Statuses

`Pending` > `Printing` > `Ready for Pickup` > `Completed` (or `Cancelled`)

Cancelled orders are not counted in total sales.
Orders are saved to a CSV file in the `orders` folder (next to the `.exe`) when the app closes.
