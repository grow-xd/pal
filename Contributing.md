# Requirements for Contributions 💯

This documentation provides a series of instructions that will assist you in adding to this repository.

First of all, we want to thank you for your contribution in this project 😊 

Before contributing, do make sure you read the important section.

We eagerly anticipate your input. 👍

### Beginning the procedure of contributing? 🤔

- To learn the fundamentals of Git/GitHub and contributing to a repository, go to the articles below. 
- If you run into trouble when making a contribution, the project maintainers will be happy to assist you. 🤗

- [git and github fundamentals](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)
- [The GitHub Lab introduction](https://docs.github.com/en/get-started/quickstart/hello-world)
- [Making your first contribution to open source software?](https://www.youtube.com/watch?v=c6b6B9oN4Vg)

## Contibute to this project 

To contribute to this project, simply follow the procedure described below:

### 1. Find an issue

- Choose an issue from the ones already there or establish your own to begin contributing.
- You can start working on the issue once a maintainer assigns it to you!😎

### 2. Fork and clone the repository

- Fork the repository. It makes a copy of this repository and adds it to your personal GitHub repository.
- Create a copy of the forked repository on your machine. This will duplicate the repository on your personal computer. Run the following command after copying the forked repository link:
```bash
git clone <cloning URL>
```
- Change your current directory to the directory of the project repository.
```bash
cd <project_directory>
```
- To guarantee that your local copy is up to date, add a reference to the source repository.
```bash
git remote add upstream <source repository URL>
``` 

### 3. Create a new branch

- Make a fresh branch. Choose a name that accurately describes the issue you are resolving. The command that comes after will start a new branch and switch to it.

```bash
git checkout -b Branch_Name
```

### 4. Work on your chosen issue!!! 👨‍💻

- Work on the issue(s) that were given to you.
- When you're done, use the following to make modifications to your branch:

```bash  
# To add all new files to branch Branch_Name  
git add .  

# To add only a few files to Branch_Name
git add <some files>
```

### 5. Commit your changes

- Make your modifications and commit them to the repository. Don't forget to include a note that describes the changes you're making.

```bash 
git commit -m "message"  
```

### 6. Sync the fork with your local copy

- Before submitting changes, make sure your branch is synchronised with the source repository by using the following commands:

```bash
git fetch upstream
git checkout Branch_Name
git merge upstream/main
```

### 7. Push your changes

- Push your modifications to your repository when you believe your code is ready for review.

```bash
git push -u origin Branch_Name
```

### 8. Pull request

- Click on compare and pull requests after opening your repository in a browser.
Then provide a title description that describes your work in your pull request.

- Kudos! Your pull request has been submitted, and the moderators will examine it before merging.😍😍😍

## Keep contributing 😁😁😁