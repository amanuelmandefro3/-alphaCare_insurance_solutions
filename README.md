# AlphaCare Insurance Solutions - 10 Academy - Week 3

### Author: Amanuel Mandefrow 

## Task 1:
### Git and GitHub

- **Tasks:** 
  - Create a git repository for the week with a good Readme
  - Git version control 
  - CI/CD with Github Actions

- **Key Performance Indicators (KPIs):**
  - Dev Environment Setup.
  - Relevant skill in the area demonstrated.

### Project Planning - EDA & Stats

- **Tasks:**
  - Data Understanding
  - Exploratory Data Analysis (EDA)
  - Statistical thinking

- **KPIs:**
  - Proactivity to self-learn - sharing references.
  - EDA techniques to understand data and discover insights.
  - Demonstrating Stats understanding by using suitable statistical distributions and plots to provide evidence for actionable insights gained from EDA.

## Task 2:
### Data Version Control (DVC)

- **Tasks:**
  - Install DVC: 
    ```bash
    pip install dvc
    ```
  - Initialize DVC: In your project directory, initialize DVC
    ```bash
    dvc init
    ```
  - Set Up Local Remote Storage:
    - Create a Storage Directory:
      ```bash
      mkdir /path/to/your/local/storage
      ```
    - Add the Storage as a DVC Remote:
      ```bash
      dvc remote add -d localstorage /path/to/your/local/storage
      ```
  - Add Your Data: 
    - Place your datasets into your project directory and use DVC to track them:
      ```bash
      dvc add <data.csv>
      ```
  - Commit Changes to Version Control:
    - Create different versions of the data.
    - Commit the `.dvc` files (which include information about your data files and their versions) to your Git repository:
      ```bash
      git add <data.csv>.dvc
      git commit -m "Track dataset version with DVC"
      ```
  - Push Data to Local Remote:
    ```bash
    dvc push
    ```

