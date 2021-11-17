# CLARIAH-PLUS WP3 Tasks: Contribution Guidelines

1. Each task is described by a Markdown file in directory pertainting to the institution, one file per task.
    - Choose a simple descriptive filename that starts with the task identifier (Txxx), avoid spaces, and mind that filenames are case-sensitive.
    - All documents should be plain text following [Markdown](https://guides.github.com/features/mastering-markdown/) syntax and always use the UTF-8 character encoding. Use the ``.md`` extension.
    - We recommend you use [this template](TEMPLATE.md) as a basis for your task description document.
    - You can use any text editor you like, or edit online through the interface offered by Github.
3. Submit your contributions by pushing directly to this repository if you  as a [Pull Requests](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/creating-an-issue-or-pull-request)A technical coordinator for your WP will **approve and merge** your contributions.


## Frequently asked questions

### I'm a beginner: How do I add a document to a git repository?

If you're new to git and github and this looks a bit daunting to you, then don't panic! You can simply edit directly from github's interface as follows:

1. Make sure you have a Github account and are logged in
2. Go your WP and possibly organization's directory in https://github.com/CLARIAH/clariah-plus-tasks, click the **Add file** button on the top-right and select **Create new file**.
3. Copy the contents from https://raw.githubusercontent.com/CLARIAH/clariah-plus-tasks/master/TEMPLATE.md , paste it into the text field and adapt it. Or if you're starting from scratch, type your document using the very simple [Markdown syntax](https://guides.github.com/features/mastering-markdown/) (use the preview option to see how it looks).
4. When done, enter a filename in the *Create* field, make sure it is a simple descriptive filename without spaces that ends ends in ``.md``. You can optionally enter a short description in the field below.
5. Choose the *Create a new branch for this commit and start a pull request.* option and press **Commit new file**,
6. Submit the pull request in the new form that appears

### And how do I edit existing documents as a beginner?

If you want to edit existing Markdown files on github, click the little pencil icon to the right, the res of the procedure is similar.

### Can we organize our documents in a DropBox/GoogleDrive/SURFdrive?

No, please don't do that and keep them in the proper git repository instead to facilitate transparency. Otherwise we
would have documents or copies of documents all over the place and we don't know where to look to find them or whether
they are the proper latest version. Git is purposefully designed to solve this exact issue. The whole idea of using git
and github for the interest groups is to consolidate version control and have a single public entry point.

If you do have the document elsewhere, at least put a link to the document in the git repository (see next point).

### We have a document on Google Docs/Office 365, can we link to it?

Only if having a simple Markdown document is not an option for you. You can link to the document from the git repository
by adding simple markdown document to the git repository that contains a link to the document on the external platform.
(be aware not to share a link with public write permissions in that case).

Preferably, you can export the document and put it in the git repository itself. But you will have to repeat the
procedure every time the document on the external platform changes. The version in git should always be authoritative.

### Can't we just mail documents around?

No, this does not facilitate transparency, findability, reusability. Please use the repository and mail links to the
document in the repository if needed.

The notable exception here is when it concerns privacy-sensitive material, in that case the git repositories are **NOT**
suitable.
