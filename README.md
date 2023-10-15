# org-mode-monthly-html-calendar 

Welcome to the org-mode-monthly-html-calendar repository!
Here's a step-by-step guide on how to create a monthly Org mode file with events,
export it to an ICS file, and serve it locally using the provided Python server.

## Creating a Monthly Org Mode File with Events

1. Open Emacs and create a new Org mode file for the desired month:

   ```
   emacs october.org
   ```

2. Insert your events into the Org mode file in the following format:

   ```
   * Event title
     <YYYY-MM-DD Day>
   ```

   For example:

   ```
   * This is event one
     <2023-10-17 Tue>
   ```

3. To insert the date:

   - Invoke the calendar by pressing `C-c .` (That's Control-c followed by a dot).
   - Navigate to your desired date using arrow keys.
   - Press `RET` (Enter) to insert the selected date.

4. To save your Org mode file:

   - Press `C-x C-s` (That's Control-x followed by Control-s).

## Exporting the Org Mode File to an ICS File

1. With your Org mode file open in Emacs:

   - Press `M-x` (Meta key followed by 'x' key).
   - Type `org-icalendar-export-to-ics` and press `RET` (Enter).
   - This will generate an ICS file with the same name as your Org mode file in the same directory.

## Serving the ICS File Locally

1. Open a terminal and navigate to the repository directory.

2. Run the Python server provided in the repository:

   ```
   python3 server.py
   ```

   This will start a local server, and it will be accessible at http://localhost:8000.

3. Using your preferred web browser, navigate to:

   ```
   http://localhost:8000/october.html
   ```

   Replace "october" with the name of your Org mode file if it's different.

---

You've successfully set up a monthly HTML calendar based on your Org mode events!