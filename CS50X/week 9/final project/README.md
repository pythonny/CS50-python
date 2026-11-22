# Pantry Manager
#### Video Demo: https://www.youtube.com/watch?v=lpfP2w28X1E
#### Description:

Pantry manager is a Python application that helps the user to track any consumable in their pantry.
The program runs in the terminal, and synchronizes all data to a JSON file.

** Features **:
- Add Item name, quantity and expiry date.
- Any item can have multiple batches. For example:
    Batch 1: 10 bottles of milk expiring on: 01-01-2026
    Batch 2: 6 bottles of milk expering on: 05-05-2026
- Warning message when an item is close to the expiry date.
- Items that are expired will be removed automatically, user will be informed.
- Delete individual items / batches, multiple items / batches, or everything.
- Pantry can always be displayed in a table, showing item name, quantity, expiry date and days left until expiry.
- "Days left" column is color-coded based on urgency (e.g. 1 day left = red, yellow for a few days left and green for safe dates).
- Data will be autosaved to .JSON file.

Technologies used:
- Python
- Prettytable
- datetime
- JSON

** Design choices **:


This program was completed for a Python course called CS50P.
