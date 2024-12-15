**Functionality with flow:**

1. Structure of application:

### **Top Navigation Bar (Header):**

- **Sign In / Sign Up Button** : Located in the top-left corner, this is where users can log in to their account or create a new account.
  - Action: \[When use click on, Sign In/Page, first open the Sign Up page \]
    - Sign In page: The page involves Sign In page which has fields like enter email and enter a password with their respective title There is another option called create and new account and in front of that there is a link of sign Up page if user click on Sign up page then open the sign up page In that page show the options entered Email and password and verify password with respective items and also the option to login with Google account directly or github account directly with their respective logo if user click on Google logo then it will redirect to Google auto sign up option and same with guihub/
    - In sign in page if user if user enter its Email and password then verify its credentials and if verify then then show the profile page if not then show the error and there is option sign in with Google or sign in with github account if there is account already sign in then directly logn Show its name at place of Sign in /Sign Up button with the profile Loin or directly go in a profile page
    - If use is sign igo.
    - validate an email with email format and password with universal password validator
    - Users can Log in with a registered email and password
- **Icons on the Right**:
  - **Settings (Gear Icon)**: Allows users to access and customize the application settings.
    - In settings button there is select the alarm tune there is options radio buttons with its title and their is if we click on a particular alarm tune then it's tune is set as default alarm tune of our appliation
    - There is four options to select tune Bell1, Bell2, Bell3, relax-tune when user opens the setting Trigger the API and download this for tunes from database and store in local storage and whenever the need take the data from local storage
    - Give option to add the Ultimate goal &lt;string&gt; (optional fild) default=backend data engineer
    - Also show the fields:with Progress-status (align with goal/good/average/not good) &lt;enum&gt; default = average, and Suggestion &lt;string&gt; default = complete tasks on time. This two fields are not editable for input based on some insights this filds are change,
  - **Notifications (Bell Icon)**: Displays alerts or updates related to tasks or deadlines.
  - **Analytics (Graph Icon)**: Provides insights or stats about the user's productivity (like task completion rate).

### **2\. Left-Side Panel (Navigation Menu):**

- **Categories**:
  - **Today**: Displays tasks scheduled for today. When we clic on it, then Also give option to edit the task with fields Task deadline,Estimate time, Priority , Remainder time, Remainder sound, and status in the Main Content Area
  - **Tomorrow**: Shows tasks planned for the next day. Als give option to edit the task with fields as mentioned in Today categori
  - **This Week**: Contains tasks spanning the current week. Also give option to edit the task with fields as mentioned in Today categori
  - **This Month**: Tasks that are scheduled for month. Also give option to edit the task with fields as mentioned in Today categori
  - **Completed**: A log of finished tasks for review or record-keeping. Also give option to edit the task with fields as mentioned in Today categori
  - **Tasks**: A centralized list of all tasks created by the user. Also give option to edit the task with fields as mentioned in Today categori
  - **Add task:** form to fill the details with filds
    - Title &lt;string&gt;, Description &lt;long string&gt;,initial Task deadline&lt;date. time&gt; default = original task deadline date, Task deadline (today/tomorrow/day_after_tommrow/week) &lt;enum&gt; , Estimate time &lt;date.time&gt;, Priority (high/medium/low)&lt;enum&gt; default=medium, Remainder time interval &lt;date time&gt;, default=30Minute, Remainder sound (list of sounds)&lt;.mp3 file&gt; default=”double beep sound”, Delay_days (integer, default = 0), Status , (working/done/pending) &lt;enum&gt;, Start Time task &lt;date. time&gt; default = none
      - Action: Initial Task deadline is deside based on Task deadline value if its is today then Initial Task deadline value became today's date same with tomorrow/day_after_tommrow/week its value is not chnage one added in database by user.
    - When you add in database that time add the fild, current date and time and Task-complete-date &lt;epoch time&gt; default = None
    - To input the Remainder sound -> show the list of radio buttons with list as Bell1, Bell2, Bell3, relax-tune and its .mp3 files are download from API
    - When user click on save button the form is first validity all the fields as with its types and then and then send to add task API and send the payload in that API
    - Show the input filds with respective titles
    - When click on save button that time upload in database as well as synk with current state in application.
    - Add the filled with initial_task_deadline (in Django side)
      - Action: \[Initial Task deadline is decide based on Task deadline value if its is today then Initial Task deadline value became today's date same with tomorrow/day_after_tommrow/week its value is not change one added in the database by the user. Just validate this fild is it correct\]
- **Purpose**: Acts as a quick navigation menu to filter and find tasks based on the time frame or status.

### **3\. Main Content Area (Task Details):**

- **Header (Today)**:
  - Displays the active section (e.g., "Today").
- **Task Summary Metrics**:
  - **Estimated Time**: Total estimated time required to complete today's tasks.
  - **Tasks to be Completed**: The number of pending tasks.
  - **Elapsed Time**: The total time spent working on tasks.
  - **Completed Tasks**: Number of tasks finished for the day.

### **4\. Task List Section:**

- **Task Input Field**:
  - Allows users to add a new task by typing in the provided field.
    - Action: \[When use click on category then respected content as mentioned in Left-Side Panel (Navigation Menu) \]
- **Task List**:
  - Displays all tasks for the selected category (e.g., tasks for "Today").
  - Each task shows:
    - A checkbox or play button to mark as complete
      - Action: \[When mak as comple this task, update in database and also update in states of app also\]
    - A start button to start the task.
      - Action:\[When we clock on shart time and open the “Active Timer” section which is situated on bottom bar\]
    - Task title
    - Due date (e.g., "1 Dec"). In DD:MM format
  - Tasks can have icons or statuses (e.g., a red clock icon showing overdue tasks).
    - When we lick on it then open the Right Sidebar.

###

### **5\. Task Edit Panel (Right Sidebar):**

- Displays detailed information about the selected task with editable fild we can modify all the fields except created date:
  - **Task Name:** Matches the active task from the main list.
  - **Total Duration:** show the total duration from start task time to complet time means differ between two sounds.
  - Title, Description, initial Task deadline, Task deadline, Estimate time Priority , Remainder time interval, Remainder sound, Status

Entry-date, start date, Task-complete-date

1. Action: \[Show this all fields with edatable format, when we edit and click on save button, then save the updated task in database with API as well as in current states of application\]
   - **Due Date:** **Show the due date of task as shown task detail.**
   - **Show save button**
   - Back button at right side of right paner
   - Show the delete button
     - When we delete it show the confirmation pop-up if yes then only go ahead, update this in database as in application states
   - **Notes Section:** Space for adding custom notes.

- **Task Creation Timestamp:** "Created on 23 Nov" is shown at the bottom.

### **6\. Bottom Bar or Main Timer Section (Active Timer):**

### **Main Timer Section of timer**

- - **Circular Timer Display:** - The circular progress bar shows elapsed and remaining Pomodoro time visually. - Action: \[This Timer display shows the stop watch with seleted task reminder-time\] - The **current task** details is displayed above the timer: - Title, Description,Task deadline, Estimate time Priority , Remainder time interval - Action: \[In compact maner\] - **Pomodoro Cycles Remaining:** likely represents total cycles planned and those in progress
    - The timer is actively counting down, currently indicating the focus interval is underway.
    - **Pause Button:**
      - Prominently placed below the timer, enabling quick access to pause the current Pomodoro session.
        - Action: \[When we again click on pause button in it tourns into play button (and timer start ) if agin click play button, then clock start\]
- **Right Sidebar of Active Timer:**

#### **Focus Time of Today:**

- Tracks cumulative focus time for the day, displayed as in minutes. This metric helps users monitor their productivity.
  - Action: \[Evert time main the variable name with last update and when add when you update the cumulative focus time that time check the last updated time if is less than dayas date then rest cumulative focus time variable value, and padte the last updated cumated focus time variable pdated time\]

#### **Today Section:**

- Lists todays tasks with Pomodoro tracking details:
  - **First Task:**
    - **Name,** Estimate time Priority,Remainder time interval, total time to complete task (total time equal to differ of start time and finish time), status
  - **Other Tasks:**
    - Same with other tasks mentioned all details as mentioned above in firat task.
  - **Show this list in a compact manner**.

#### **Today's Focus Time Records:**

- - - 1. A horizontal progress bar at the bottom visualizes the time spent focusing. 2. A timeline (starting at **00:00**) suggests tracking intervals or cumulative Pomodoro durations for the day. 3. **Pomodoro Sessions**: 1. Start/Stop a session also List Pomodoro Sessions, and Pomodoro Analytics

Add the time in epoch time

Validations:

Calculate the Start and stop sessions based on Active-Timer

Action: \[when Pomodoro start, and add the end time as pomodoro ends, maximum time duration of single session is as Reminder_duration in minutes\]

Ensure task_id exists and belongs to the user.

Check if the task's status is "Pending" or "Working".

Prevent overlapping sessions.

- - - - 1. Track duration and associate with tasks

#### **Cosing buttons:** at at top left side give minimise option, after minimising it it visible In home page at middle on the bottom bar show the small bar with small size timer, title of selected task, and small option to play or pause the timer Action:\[at first opening of application show the current peinding task title and timer according to that\]

### **7\. Pomodoro reminder Activity(Pop-Up Activity):**

- **Pomodoro Reminder Pop-up Notification:**

  - When a reminder is done, cretae another pop-up and **ask, How are you feeling? →** align**/**stuck**/**distracted**/**feeling lazy

    - Show the buttons align**/**stuck**/**distracted**/**feeling lazy

      - And depending upon the feeling play music, play video, or audio format suggestions show the things based on the below conditions

        - Conditions for Play music, video, audio, Text format Text
        - If feeling = Align:

          - initial-2Minute-music-type = Align/background_music

          - Play the random music from the Motivational folder music list (file type is .mp3)
          -
          - Picture = Align/picture
          -
          - Show the random picture from above mentioned folder
          -
          - Text = Align/picture
          -
          - Show the random picture from abve mentioned folder
          -
          - Initial-2-minute-speech-folder-path = Align/background_speech
          -
          - Play random music from the above folder
          -
          - Core-speech-folder-path= Align/core_speetch
          -
          - Play the random music or video from the above folder
          -
          - Core-slot-time = 5 minutes
          -
          - Play the Core-speech-folder-path till Core-slot-time
          -
          - Post-break-gap =10 minutes
          -
          - Post-break-background-music-folder-path = Align/Post-break-background-music
          -
          - Play the music from after the Post-break-gap time
          -
          - Create a JSON file of this data and store the thing

- - - - If felling =Stuck:

        - initial-2Minute-music-type =Stuck/background_music
        -
        - Play the random music from the Motivational folder music list (
        -
        - Stuck/background_music)
        -
        - Picture = Stuck/picture
        -
        - Show the random picture from above mentioned folder
        -
        - Text = Stuck/picture
        -
        - Show the random picture from abve mentioned folder
        -
        - Initial-2-minute-speech-folder-path = Stuck/background_speech
        -
        - Play random music or video from the above folder
        -
        - Core-speech-folder-path= Stuck/core_speetch
        -
        - Play the random music or video from the above folder
        -
        - Core-slot-time = 10 minutes
        -
        - Play the Core-speech-folder-path till Core-slot-time
        -
        - Post-break-gap =0 minutes
        -
        - Post-break-background-music-folder-path = Stuck/Post-break-background-music
        -
        - Play the music from or video after the Post-break-gap time
        -
        - Create a JSON file of this data and store the thing

- - - - If felling = **distracted:**

        - initial-2Minute-music-type =**distracted**/background_music
        -
        - Play the random music from the Motivational folder music list (
        -
        - Stuck/background_music)
        -
        - Picture = **distracted**/picture
        -
        - Show the random picture from above mentioned folder
        -
        - Text = **distracted**/picture
        -
        - Show the random picture from abve mentioned folder
        -
        - Initial-2-minute-speech-folder-path = **distracted**/background_speech
        -
        - Play random music or video from the above folder
        -
        - Core-speech-folder-path= **distracted**/core_speetch
        -
        - Play the random music or video from the above folder
        -
        - Core-slot-time = 5 minutes
        -
        - Play the Core-speech-folder-path till Core-slot-time
        -
        - Post-break-gap =0 minutes
        -
        - Post-break-background-music-folder-path = **distracted**/Post-break-background-music
        -
        - Play the music from or video after the Post-break-gap time
        -
        - Create a JSON file of this data and store the thing

- - - - If felling = feeling lazy**:**

        - initial-2Minute-music-type =feeling-lazy/background_music
        -
        - Play the random music from mentioned folder path
        -
        - Picture = feeling-lazy/picture
        -
        - Show the random picture from above mentioned folder
        -
        - Text = feeling-lazy/picture
        -
        - Show the random picture from abve mentioned folder
        -
        - Initial-2-minute-speech-folder-path = feeling-lazy/background_speech
        -
        - Play random music or video from the above folder
        -
        - Core-speech-folder-path= feeling-lazy/core_speetch
        -
        - Play the random music or video from the above folder
        -
        - Core-slot-time = 10 minutes
        -
        - Play the Core-speech-folder-path till Core-slot-time
        -
        - Post-break-gap =5 minutes
        -
        - Post-break-background-music-folder-path = feeling-lazy/Post-break-background-music
        -
        - Play the music from or video after the Post-break-gap time

- - - - For all this conditions Create a one JSON and mentioned all the conditions of align**/ **stuck**/**distracted**/**feeling lazy in that as amntioned above
    -       Ask the current “Status of Task: → remain/doing/almost there”
      -     Store this value in a different table with task id, task status, time
    -     Ask “Food Taken? → Yes/No”
      -     Store the value in different Table with task ID, Food Taken, time
- Pop-up Structure:
  - 1\. Header Section
    - Text Prompt: "How are you feeling?" (likely a typo for "How are you feeling?")
    - The text is centred and serves as the title or main question for the pop-up.
  - 2\. First Question: Feeling Status
    - Question: "How are you feeling?"
      - Options (Buttons):
        - Align
        - Stuck
        - Distracted
        - Feeling lazy
    - Each option is displayed as a button with consistent styling (likely rounded with dark backgrounds and white text).
  - 3\. Second Question: Task Status
    - Question: "Status of Task?"
      - Includes an edit/pencil icon, suggesting the option to modify the question or input.
        - Options (Buttons):
        - Remain
        - Doing
        - Almost There
    - Options are displayed in a similar button style as above.
  - 4\. Third Question: Food Intake
    - Question: "Food Taken?"
      - Also includes an edit/pencil icon, indicating it may be customizable.
        - Options (Buttons):

Yes

No

- - Additional Food-related Emojis: - Includes food icons (e.g., cheese, carrot, water bottle, and plate), possibly used for emphasis or context.
    - 5\. Styling and Layout
      - Background: The pop-up has a light gray background with a subtle rounded border.
      - Spacing: Questions and buttons are evenly spaced for readability.
      - Font: Clean, sans-serif, likely used for clarity and modern appearance

### **8\. On load Pop-up(load-Pop Up):**

1. When we open the application that time, show the todays task, if not then say the user add the todays task.
2. Check every 5 minus is there is no task in today's task list then show a pop-up to user add Today's task.

### **9\. State Management**

- Use Redux or React Context for:
  - User Authentication.
  - Task Data (CRUD actions synced with API).
  - Timer states (active sessions, pauses).
  - Settings and Notifications.

### **10\. Validation Rules:**

- Ensure no overlapping start_time for tasks.
- Task deadline must be greater than created_on.
- Validate OAuth token uniqueness to avoid conflicts.
- For Pomodoro sessions:
  - Ensure task association is valid.
  - Prevent overlapping sessions.
  - Ensure proper status alignment.

#### **11\. Error Handling:**

- Implement structured error handling for:
  - Authentication issues (e.g., invalid credentials or token errors).
  - Task validation errors (e.g., invalid deadlines, overlapping schedules).
  - Pomodoro session constraints (e.g., duplicate or overlapping sessions).

### **10\. Edge Cases**

- **Task Management**:
  - Prevent creating duplicate tasks for the same title and date.
  - Notify user when a task deadline is near.
- **Pomodoro Timer**:
  - Handle timer reset if task status changes to "Done".
  - Pause timer if the application is minimized.
- **Error Messages**:
  - Display user-friendly messages (e.g., invalid fields).
  - Retry failed API calls for temporary network issues.

### **9\. UI Features**

- **Responsive Design**:
  - Desktop: Full sidebar and main content display.
  - Mobile: Collapsible sidebar, sticky bottom timer.
- **Analytics (Graph)**:
  - Track completed tasks, focus hours.
  - Chart.js or Recharts for visualizations.

Note:

1. In the Whole appliication add the code to handle the errors, and print the errors in log
