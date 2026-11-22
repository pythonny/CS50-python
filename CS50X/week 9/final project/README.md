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

** Design decisions & difficulties **.

To start with I'd like to inform the reader that this section is written in a more personal style. This is my first project of this size, and I did not start with a fully worked-out design beforehand. I initially underestimated the amount of work and structure needed to make everything function properly. Because of this, most - if not all - design choices were made and refined along the way. For this reason I will describe my design decisions in a similar manner; showing how this project evolved from a realistic point of view. I'll describe some of the difficulties that were most memorable, because this project consisted mainly off difficulties and it would be unrealistic to name them all.

I wanted to make this Python program object-oriented. I decided to write the back-end in a separate file called "pantry.py", to keep the main file called "project.py" easy to read. After finishing my project I discovered that one of the requirements was that at least 3 functions besides "main.py" had to be defined inside the "project.py" folder. This was a pretty stressful realization, which taught me to read the requirements more carefully next time. To meet this requirement without changing the overall structure of my code, I decided to create a few wrapper functions inside "project.py". In my personal opinion this makes "project.py" a bit less clean and readable, but this was the only way I could think of to meet the requirement.

When the user runs the Pantry manager the user gets shown the main menu. The main menu has a brief explanation of the program with 5 choices:

loading pantry
adding an item
deleting an item
empty the entire pantry
close the pantry. The initial idea was to add more functionality like meals, recipes etc. But the options above proved to be challenging enough.
We learned about "classes" in one of the weeks and it felt natural and relevant to use a class-based approach for this project. It was very important for me that this program could potentially be used in real life. A key design choice was that all stored data would stay persistent, even after exiting the program. In week 4 and 6 respectively we learned about JSON files and reading/writing to other files using "With open". I decided to use this knowledge to write all saved data to a JSON file.

I wanted the user to not have to worry about anything technical. One of the first design choices I made to successfully make this happen was to automatically create a JSON file without requiring any action from the user. The first function of the Pantry class, called "Load_from_file()" automatically creates new JSON file if there currently is none, but if there is, it will read the content and sync the content with "self.items". "self.items" is an attribute inside the Pantry class to read / write all pantry data to.

I used a dictionary {} for all the information inside self.items and the JSON file, because I need multiple keys per value. For example, for each consumable I wanted at least: quantity, expiry date and days left. Dictionaries are a lot more convenient for this compared to lists.

The next step was to create a function to add items, called "add_items" . The user is asked to enter the name of the consumable, expiry date and quantity. For each input except for the name of the consumable, I added validation loops to make sure the answers are valid. In one of the weeks I learned about "fromisoformat" . With this function I am able to confirm whether the information the user entered is valid. For quantity I kept it simple, as long as the quantity is greater than zero the user can end the loop. If any of the information is not valid, the user will get a guided message what he/she needs to change.

Early on, I decided to support multiple copies of the same consumable. This choice was based on real-life usage: I often buy a new pack of an item before the previous one is fully consumed. A good example is milk. If I buy a new pack of milk, before the last one is finished, the expiry date will be different. If I were to simply add quantities together, the different expiry dates would be lost in the Pantry class, which would make it impossible to know which batch should be consumed first. To avoid this, I designed add_items() to store each consumable as a list of batches. After adding “Milk”, the key Milk refers to a list containing multiple dictionaries, where each dictionary represents a single batch with its own quantity and expiry date. The expiry date is used to distinguish between batches.

One of the main motivators to create this pantry was reduce my food waste. This made it important to add a column "days left". The function that makes this possible is called "date_conversion" . I used the built-in module "datetime" to calculate the number of days before the item expires. I had to do a very similar exercise during the course, so this was one of the easier functions to create.

To show the current Pantry I made a function called show_items(). I wanted to use "Prettytable" for this, because I remembered this from when I followed some lessons from another course called "100 days of code" by Angela Yu. I had a lot of problems making this work properly because at this point, when looking at retrieving a single item; we need to first find the right dictionary batch that sits inside a list under the item name. That item itself lives inside the main Pantry dictionary ( Dictionary > list > dictionary). Writing a loop that reads and displays this cleanly was a real brain twister. For the days_left column I had to refer to the date_conversion function mentioned in the previous paragraph.

I added color codes for days_left. Green for safe dates, yellow for items that are almost expiring and red when the item expires in 1 day or less. This was an important choice for me, because the textbased Prettytable is by default black and white. By adding some colors the user can immediately see which products are almost expiring and which products still have a lot of time left. Hopefully this reduces food waste. A problem I had was that the color of the "Days_left" would carry over to the table itself. For a while I couldn't find out why, but I found out that you had to {RESET} each time you "draw" with a new color, otherwise the table gets printed in either red/yellow/green as well.

After the user gets shown the table I needed a way to get the user back to the main menu. The easiest option was to prompt the user whether he wanted to return. However this unexpectedly caused a problem with the function delete_items() . Each time after I delete an item I want to show the user the new table. This way the user can immediately see the change of the Pantry, and the user will be able to delete another item if the user wishes to. I wanted to re-use show_items(), but when I did the user would get the prompt to return back to the main menu, which was only meant for when the user called the table from the main menu, not from deleting an item. I resolved this bug by adding a new loop inside show_items called "if main_menu == True" . By default I set main _menu == True, but inside the delete_items function I set main_menu == False .

The delete_items() function was by far the hardest part of the project. At one point, I even stepped away from the project entirely and focused on other things because I could not figure out how to make this work correctly. In the end, however, this is probably the function I am most proud of. When an item only had a single batch, the logic was relatively straightforward. I could compare the user input to the data stored in self. items, ask how much quantity should be deleted, and either reduce the quantity or remove the item entirely if the quantity reached zero. The real difficulties started when I had to support items with multiple batches. In this case, simply deleting based on the item name was no longer sufficient, because each batch could have a different expiry date and quantity. I needed a way for the user to clearly select which batch they wanted to delete or partially reduce.

I eventually solved this by using Python’s enumerate() function. This allowed me to assign a visible index number to each batch of an item, which could then be displayed to the user. The user will then select the correct batch by number, after which the same deleting progress will be repeated. For example, if an item like a banana had multiple batches, the user would see a numbered list showing the expiry date, quantity, and days left for each batch. This approach resulted in a clear and manageable user interface, even though the internal data structure was very complex for someone at my level. See the example below:

Banana has multiple batches, please choose which batch you'd like to (partly) delete:

Expiry: 2026-01-01 | Quantity: 5 | Days left: 14
Expiry: 2025-12-30 | Quantity: 8 | Days left: 12 Please type the number of the batch you want to delete:
The last option in the main menu is to empty the entire pantry. The function that is used for this is called: empty_pantry(self). It was important for me to add this because deleting item by item can become hideous if you want to start over. This function was also really easy to implement, because we could simply overwrite self.items and save this to the JSON file.

None of the functions mentioned above would work properly without the save_items(self) function. This function is called inside all functions that modify the pantry, such as delete_items(self), add_items(self), auto_expire(self), and empty_pantry(self). All of these functions update self.items, and save_items() is responsible for writing the latest state of self.items to the JSON file. This ensures that all changes are stored permanently and that the pantry data remains persistent between program runs.

One quality-of-life function I added is auto_expire(self). If an item has expired, it is automatically removed from the pantry. The function also informs the user whenever an item is removed, so the user stays aware of the changes inside the pantry. If a product expires today, the user will receive a warning. This was implemented to give the user a bigger chance to consume products in time and reduce food waste. This function runs automatically every time the pantry contents are loaded. There were a lot of difficulties creating this feature. To make auto_expire() work, I initially tried to loop through the data and delete items at the same time. Modifying a data structure while iterating over it can cause unexpected behavior and bugs, which I only learned after testing. To avoid this, I decided to create a new dictionary to rebuild the pantry state safely. For each product, I loop through its batches and compare the expiry date with today’s date using the datetime module. If an item is not expired, it is stored in a list called keep. If an item is already expired, it is not added to this list and instead a message is stored in removed_messages. When an item expires today, it is both kept and added to a list called warning_messages. At the end of this process, all non-expired items are stored in the keep lists and synced into a new dictionary called updated_pantry. Only after the entire process is finished do I replace self.items with updated_pantry. This approach prevents self.items from being modified while items are being deleted. If something goes wrong during the process, the original pantry data remains unaffected.

the functions delete_again(), return_to_menu(), pantry_empty(), delete_number(quantity,item) are all functions that contain texts or inputs that are re-used in multiple functions or multiple times in 1 function. This reduces code and text duplications.

This program was completed for a Python course called CS50P.
