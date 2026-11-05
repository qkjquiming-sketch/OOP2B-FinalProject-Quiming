# PrintSync

Printing Shop Order and Queue Management System, built with Python and PyQt6.

PrintSync has two screens that work together:

- **User Screen**: the customer fills in their details, picks the paper, print type and extras, sees an itemised price, and submits the order.
- **Admin Screen**: the shop owner sees all orders, updates their status, deletes or undoes a delete, views sales totals, and changes prices.

It runs fully offline. With two monitors, the User Screen opens on the first and the Admin Screen on the second.

---

# Getting Started with PrintSync

This guide takes you from downloading PrintSync to completing your first order. No technical experience needed.

## Before you start

- A Windows PC (Windows 10 or 11)
- About a minute to download and set up

## Step-by-step

### 1. Download PrintSync
1. Go to the [Releases](https://github.com/qkjquiming-sketch/OOP2B-FinalProject-Quiming/releases) page.
2. Under **Assets**, download **`PrintSync.exe`**.
   *(Prefer a smaller download? `PrintSync.rar` is the same app, compressed.)*

![Screenshot: Releases page with PrintSync.exe highlighted](docs/images/01-releases.png)

### 2. Extract the file (only if you downloaded the .rar)
1. Right-click `PrintSync.rar` and choose **Extract here** with [7-Zip](https://www.7-zip.org/) or WinRAR.
2. Newer versions of Windows 11 can also open `.rar` files directly.

### 3. Move it to a normal folder
Move `PrintSync.exe` to your **Desktop** or **Documents** folder. Don't put it in `Program Files`.

> PrintSync saves your prices and an `orders` folder right next to the `.exe`, so it needs a folder you can write to.

### 4. Open PrintSync
1. Double-click **`PrintSync.exe`**.
2. Wait a few seconds. The first launch is slower while the app unpacks itself.

### 5. If Windows shows "Windows protected your PC"
This appears because the app isn't digitally signed. It's expected.
1. Click **More info**.
2. Click **Run anyway**.

![Screenshot: SmartScreen warning with "More info" circled](docs/images/02-smartscreen.png)
![Screenshot: "Run anyway" button circled](docs/images/03-run-anyway.png)

### 6. [Log in / start screen: describe what the user sees first]
1. [e.g., Enter your name or shop details, then click **Continue**.]

![Screenshot: main window on first launch](docs/images/04-main-window.png)

### 7. [Set your prices: if this is part of the setup]
1. [Open the prices section.]
2. [Enter the price for each item, e.g., per page, per size, or color vs. black & white.]
3. [Click **Save**. Prices are remembered next time you open the app.]

![Screenshot: prices screen](docs/images/05-prices.png)

### 8. [Create your first order: the main task]
1. [Click **New Order**.]
2. [Add the print job: choose the file, size, quantity, and color.]
3. [Check the total price shown on screen.]
4. [Click **Save / Confirm Order**.]

![Screenshot: order form filled in](docs/images/06-new-order.png)

### 9. Find your saved order
Open the **`orders`** folder next to `PrintSync.exe`. Your order is saved there.

![Screenshot: orders folder next to PrintSync.exe](docs/images/07-orders-folder.png)

## Troubleshooting

| Problem | Fix |
|---|---|
| Nothing happens after double-clicking | Wait a few seconds; the first launch is slow. |
| "Windows protected your PC" | Click **More info → Run anyway** (see Step 5). |
| Prices or orders won't save | Make sure the `.exe` isn't inside `Program Files`; move it to Desktop or Documents. |
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
