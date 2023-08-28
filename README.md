# News_App_using_newsapi.org
The News API Project is a web application built with Django that allows users to search for and explore news articles from various sources. It provides a user-friendly interface for discovering up-to-date news on different topics and from different parts of the world.

## Features

- **Search and Filter:** Users can search for news articles using keywords, filter by language, category, and specific news sources, and even narrow down results by date range.

- **Detailed Information:** Each news article is displayed with its title, author, description, publication date, and a link to the full article for more information.

- **User Authentication:** The app features user registration and login functionality, ensuring a personalized experience for users.

## Why This Project?

In a world of information overload, staying informed is crucial. This project demonstrates how to leverage the power of the [News API](https://newsapi.org/) to provide a streamlined way for users to access news articles that matter to them.

## Setup and Usage

To run this project locally:

1. Clone the repository:
   git clone  https://github.com/pradip-bhadre/News_App_using_newsapi.git

2.Create a virtual environment and activate it:


  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
  
3.Install the required packages:
  pip install -r requirements.txt

4. Run migrations
  python manage.py migrate

5. start the developemnet server
  python manage.py runserver
