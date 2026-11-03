# PrintSync

Printing Shop Order and Queue Management System, built with Python and PyQt6.

PrintSync has two screens that work together:

- **User Screen**: the customer fills in their details, picks the paper, print type and extras, sees an itemised price, and submits the order.
- **Admin Screen**: the shop owner sees all orders, updates their status, deletes or undoes a delete, views sales totals, and changes prices.

It runs fully offline. With two monitors, the User Screen opens on the first and the Admin Screen on the second.

---

## Installation

1. Go to the [**Releases**](../../releases) page.
2. Download either:
   - `PrintSync.exe`, or
   - `PrintSync.rar` (the same app, compressed)
3. If you downloaded the `.rar`, right-click it and extract it with [7-Zip](https://www.7-zip.org/) or WinRAR. Newer versions of Windows 11 can also open it directly.
4. Move `PrintSync.exe` to a normal folder like Desktop or Documents (not `Program Files`).
5. Double-click `PrintSync.exe`. That's it.

The first launch takes a few seconds while the app unpacks itself.
Saved prices and the `orders` folder are created next to the `.exe`.

> Windows may show "Windows protected your PC" because the app is unsigned. Click **More info > Run anyway**.
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
