# The Motivation Behind LeetLog

## Making LeetCode Manageable
As a student preparing for my first round of technical interviews, I often felt unorganized and unsure of how to focus my study sessions. 
I had no system to track which problems I struggled with or which patterns I was weak on.
On top of that, I had never experienced a real technical interview before, so I didn’t know how to simulate the pressure or time constraints. 
That’s why I added Learn Mode and Warm-Up Mode, each with a built-in timer — to help simulate interview conditions

## Unfortunately, LeetCode Can Be a Discouraging Process
One of the hardest parts of interview prep isn’t the algorithms — it’s the feeling that you're not making progress.
That’s why I’m planning to build out analytics features that go beyond just tracking what you’ve solved. I want to help users:
See which problem patterns they’ve practiced most
Show how many problems they're averaging per day/week
Visualize growth over time
The goal isn’t just to collect stats — it’s to show that your work is paying off, even when it doesn’t always feel like it.

# LeetLog

A smart way to organize your LeetCode grinding journey. Track problems, patterns, and get AI-powered insights on your progress.

## Features

- 📝 Track LeetCode problems with problem numbers and patterns
- 🎯 Set priority levels for problems you need to focus on
- 🤖 AI Analysis of your problem-solving patterns
- 📊 Separate sections for detailed notes and analytics
- 🎨 Clean, dark-themed UI with Bootstrap

## Tech Stack

- **Backend**: Flask
- **Database**: SQLite with SQLAlchemy
- **Frontend**: HTML, SCSS, Bootstrap
- **AI Integration**: OpenAI GPT-3.5

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   - Create a `.env` file
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
4. Initialize the database:
   ```bash
   python app.py
   ```
5. Run the application:
   ```bash
   flask run
   ```

## Project Structure
LeetLog/
├── app.py # Main Flask application
├── static/
│ ├── styles.scss # SCSS styles
│ └── LeetLog2.png # Logo
├── templates/
│ └── index.html # Main template
└── database.db # SQLite database

## Future Improvements

- [ ] Add a dedicated Notes page for detailed problem solutions
- [ ] Implement Analytics dashboard
- [ ] Add user authentication
- [ ] Add problem categories and tags
- [ ] Export/Import functionality for problems
- [ ] Dark/Light theme toggle

## Contributing

This is a personal project, but suggestions and improvements are welcome! Feel free to fork and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

