# LinkedIn Assistant

LinkedIn Assistant is an AI-powered agent designed to curate and generate insightful LinkedIn articles using data pulled from multiple sources. The project leverages Gemini API as the base LLM for all agents and consists of two main agents that work sequentially:

1. **Analyzer Agent**: Inspects curated data and identifies key insights.
2. **Writer Agent**: Generates well-structured LinkedIn articles based on the analyzed data.

---

## Features

### Data Sources

The assistant collects data from the following platforms:

- **Reddit**:
  - Subreddits:
    - [MachineLearning](https://www.reddit.com/r/MachineLearning/)
    - [Technology](https://www.reddit.com/r/technology/)
    - [Singularity](https://www.reddit.com/r/singularity/)
    - [ArtificialIntelligence](https://www.reddit.com/r/ArtificialIntelligence/)
  - Data is curated using `redditCurator.py`.

- **Twitter**:
  - Tweets related to AI and technology trends are pulled using `tweetCurator.py`.

### Workflow

1. **Data Collection**:
   - Reddit data is collected using `redditCurator.py`.
   - Twitter data is collected using `tweetCurator.py`.

2. **Data Analysis**:
   - The `main.py` script integrates the collected data.
   - The **Analyzer Agent** processes the curated content to extract key insights.

3. **Article Generation**:
   - The **Writer Agent** takes the insights from the Analyzer Agent.
   - Generates engaging and informative LinkedIn articles.

---

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`
- Gemini API access for LLM operations

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gowthambalachandhiran/LinkedInAssistant.git
   cd LinkedInAssistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Reddit Curator**:
   ```bash
   python redditCurator.py
   ```

4. **Run Twitter Curator**:
   ```bash
   python tweetCurator.py
   ```

5. **Generate LinkedIn Articles**:
   ```bash
   python main.py
   ```

---

## Project Files

- **`redditCurator.py`**: Fetches and curates data from Reddit subreddits.
- **`tweetCurator.py`**: Fetches and curates data from Twitter.
- **`main.py`**: Orchestrates the workflow of Analyzer and Writer agents.
- **`requirements.txt`**: Contains the list of dependencies.

---

## Technologies Used

- **Gemini API**: LLM used for both Analyzer and Writer agents.
- **Reddit API**: For fetching subreddit content.
- **Twitter API**: For fetching tweets.

---
## Final Output

![image](https://github.com/user-attachments/assets/a50b9151-944a-4cc2-b53a-656608426168)


## Contributing

Feel free to fork this repository and submit pull requests for any enhancements or bug fixes. Contributions are always welcome!

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For any questions or suggestions, reach out to [Gowtham Balachan]([https://www.linkedin.com/in/gowthambalachandhiran/](https://www.linkedin.com/in/gowtham-balachandhiran-47260273/).
