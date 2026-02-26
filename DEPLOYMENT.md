# 🚀 How to Host Your Streamlit App on the Internet for Free

The best and easiest way to host a Streamlit app is using **Streamlit Community Cloud**, which is 100% free and connects directly to GitHub. 

Here is your step-by-step guide from scratch:

---

## Step 1: Install Git on your Computer
Since Git is not currently installed on your computer, you need to install it first to push your code to GitHub.

1. Go to the official Git website: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Click **"Click here to download"** to get the latest 64-bit setup.
3. Run the installer and just keep clicking **"Next"** (the default settings are perfectly fine).
4. *Important:* Once installed, close your terminal/command prompt and open a new one so it recognizes the `git` command.

---

## Step 2: Create a GitHub Account & Repository
1. Go to [https://github.com/](https://github.com/) and create a free account if you don't have one.
2. Once logged in, click the **"+"** icon in the top right corner and select **"New repository"**.
3. Name your repository (e.g., `fresher-salary-calculator`).
4. Make it **Public** (Streamlit Community Cloud is free for public repos).
5. **Do NOT** check "Add a README file" (you already have one locally).
6. Click **"Create repository"**.

---

## Step 3: Push Your Code to GitHub
1. Open your terminal (or command prompt) and navigate to your app folder:
   ```cmd
   cd "e:\My Apps"
   ```
2. Run these commands one by one to send your code to GitHub:
   ```cmd
   git init
   git add .
   git commit -m "Initial commit of ROI Calculator"
   ```
3. Now, go back to the GitHub page where you created your repository. Look for the section titled **"…or push an existing repository from the command line"**.
4. Copy those 3 lines of code provided by GitHub and paste them into your terminal. They will look something like this:
   ```cmd
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```
*(Note: If this is your first time using Git, it might ask you to log into GitHub in a pop-up window).*

---

## Step 4: Host it on Streamlit Community Cloud
Now that your code is on GitHub, hosting it takes 2 minutes!

1. Go to [https://share.streamlit.io/](https://share.streamlit.io/) and click **"Continue with GitHub"** to log in.
2. Click the **"New app"** button in the top right.
3. If it asks for authorization, allow Streamlit to access your GitHub repositories.
4. Fill in the details:
   - **Repository:** Select your `fresher-salary-calculator` repo from the dropdown.
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **"Deploy!"**

**🎉 Congratulations!** Streamlit will now build your app. In a couple of minutes, you will get a live public URL (e.g., `https://fresher-salary-calculator.streamlit.app`) that you can share with anyone in the world!
