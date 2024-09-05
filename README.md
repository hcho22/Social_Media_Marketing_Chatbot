---
title: Social Media Marketing Chatbot

---

# Social Media Marketing Chatbot

![Chatbot](https://www.revechat.com/wp-content/uploads/2023/01/social-media-chatbot-jpg.webp)

This project aims to create a powerful social media marketing team using Language Models (LLMs) and CrewAI. The team automates content creation, scheduling, and strategy refinement, helping to drive engagement and boost growth across multiple social platforms.

## Project Overview
This repository demonstrates the integration of LLM with CrewAI to manage, optimize, and automate various aspects of social media marketing. By utilizing AI-based tools, it streamlines content generation, targeting, and performance measurement for social media marketers.

## Features
- Automated Content Creation: Leverage LLM to generate engaging and relevant content for posts, stories, and ads.
- Post Scheduling & Optimization: Schedule content at peak times for maximum engagement using CrewAI's team collaboration.

## Tech Stack
- Language Model: OpenAI's GPT (or any similar large language model)
- CrewAI: For building and managing the marketing team with automated workflows and collaboration tools.
- Backend: 
- Frontend: Streamlit


## Installation procedure


### Create new conda environment
Create a new conda environment by running the following command. 

conda create --name myenv python=3.10


### Clone repository
Clone the repository by running the following command.

git clone git@github.com:(your profile)/Social_Media_Marketing_Chatbot.git

cd social_media_marketing_chatbot

### Install dependencies
pip install -r requirements.txt

### Setup environment variables by creating a '.env' file:
CREWAI_API_KEY=your_crewai_api_key
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key

### Run the prject
streamlit run streamlit_app.py

### Usage
- Create Content: Use the LLM model to automatically generate tailored content for your target audience.
- Assign Roles: CrewAI will distribute tasks like market researcher, content strategist, and copywriter. 
- Optimize Strategy: Continuously refine your marketing strategy based on AI-driven insights.