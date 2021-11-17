# CLARIAH Interest Group Contribution Guidelines

1. Each Interest Group has its own **Github repository** with associated **issue tracker**, all interests groups are
   part of the [CLARIAH organization](https://github.com/CLARIAH) on Github.
     - There is one [over-arching repository](https://github.com/CLARIAH/IG) that provides [an index to all individual interest groups](https://github.com/CLARIAH/IG/blob/main/README.md)
       and holds documents that transcend individual interest groups. Such as meeting notes and documents
       from the Technical Committee.
     - There is another central repository that holds all [use cases](https://github.com/CLARIAH/usecases) for all
       Work Packages and Interest Groups.
2. All relevant documents and other group output should be gathered in the relevant repository.
    - This ensures everything can be found in one place and is under proper version control and that everybody
      is free to use the tools they prefer to edit the contents.
    - This provides transparency, findability, and accountability.
    - If there are relevant resources on external platforms, such as a document on Google docs for instance,
      then that is of course fine, but make you **link to it** from one or more documents this repository, simply
      putting a URL in relevant document will do. Otherwise people will not know about the existence of your document.
    - If the output of the group consists of custom-made software then that will be hosted in its
      own separate repository and will be linked to from one of more documents in this repository.
    - Keep documents in **plain text** as much as possible, or more specifically: use
      [Markdown](https://guides.github.com/features/mastering-markdown/) syntax and always use the UTF-8 character
      encoding. Prevent proprietary closed formats and binary formats as much as possible, but if you can't avoid it,
      just commit them to the repository.
    - If your group gives presentations, please put the slides in the repository.
3. Group discussion can take place through the **issue tracker** associated with a repository.
    - If your group holds meetings (virtual or physical), please ensure to always put the meeting notes in the
      git repository afterwards. Or, preferably, try to
      summarize any actionable points in issues on your group's issue tracker.
    - All issues/tickets should ideally have a well-defined and limited scope; make multiple issues if you want to address multiple unrelated points.
    - Please contribute by adding issues and by commenting on existing issues.
    - Discussion in the issue tracker is **public** and **open** to group members and non-group members alike (including partners outside of CLARIAH).
      Please be conscious of any privacy-sensitive issues.
    - The issues can be used to track the progress and can be further categorized with labels/tags (thee can be configured by
      the group coordinator).
    - People who prefer to use their e-mail client can simply reply to the issue notifications received by mail (take
        note of point 4). You can optionally also use [Github's command-line client](https://cli.github.com/) or [Github's desktop client](https://desktop.github.com/).
4. Group members should make sure to **watch** this repository ([click the watch
   button](https://docs.github.com/en/github/getting-started-with-github/be-social#watching-a-repository)) to receive
   notifications on important activity. We have also set up links between GitHub and the slack channels (see point 7) so
   notifications of any activity land there as well. Whenever you post an issue, notifications should go out
   automatically to everybody who subscribed.
5. Group membership is **open** to anybody with an interest in what we are doing and with some relationship to CLARIAH.
   The ``README.md`` file in each interest group's repository should list all the current members of that group.
6. When adding documents that you want other to review, use [Pull Requests](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/creating-an-issue-or-pull-request). This automatically opens up a thread for **discussion and peer review** of your contributions and will notify all group members. It is just a special form of an issue. You can mark specific people as reviewer. The group coordinator can finally **approve and merge** your contributions.
    - This may be overkill for simple situations, feel free to push directly to the repository if needed.
    - This only applies to adding documents, you can use the issue tracker for normal proposals/comments/remarks/review requests.
7. Each interest group has a **Slack channel** on the [CLARIAH slack platform](https://clariah-workspace.slack.com),
   this is a text-based chat (also offers videoconferencing functionality) that allows us to gather and communicate in
   a more direct and informal manner. Everybody is welcome! Feel free to join all the channels you're interested in.
   All interest group members should be a member of the respective slack channels. In addition, there are some generic
   channels.
8. Each interest group has a ``README.md`` file in the root of its repository that describes the aims and scope of the
   interest group and lists the group members.

## Frequently asked questions

### I'm a beginner: How do I add a document to a git repository?

If you're new to git and github and this looks a bit daunting to you, then don't panic! You can simply edit directly from github's interface as follows:

1. Make sure you have a Github account and are logged in
2. Go to the github repository of your interest group  (or the general group or the use cases group), navigate to the directory where you want
   to add a document, and then either click **Upload files** if you want to upload an files from your local system, or click the **Add file** button on the top-right and select **Create new file** to start a document from scratch.
3. If you're starting from scratch, type your document using the very simple [Markdown syntax](https://guides.github.com/features/mastering-markdown/) (use the preview option to see how it looks). When done, enter a filename in the *Create* field, make sure it is a simple descriptive filename without no spaces, prerefably all lowercase and ends in ``.md``. You can optionally enter a short description in the field below.
5. In the **Commit Changes** section, choose the *Create a new branch for this commit and start a pull request.* option and press **Commit new file**,
6. Submit the pull request in the new form that appears

### Where can I find the issue trackers?

Go the repository for your interest group, and click the Issues tab (right under the title of the repository and to the
right of the Code tab that is opened by default). By default this will show you all issues that are open, meaning they
still have to be handled. There is an additional tab to show issues that have been dealt with and are closed. (you may
still reopen and comment on them)

### What counts as an issue?

Any question, proposal, comment, response or whatever you want to raise can be considered an issue. Don't hold back!  We
also encourage you to comment on any existing issues. Each issue forms a special thread for clearly delimited
discussion.

### How to raise an issue within an interest group?

Post your issue to the **issue tracker** pertaining to your interest group, or to the
[central](https://github.com/CLARIAH/IG/issues) group if it is more generic and spans multiple interest groups, or to
the [use cases](https://github.com/CLARIAH/usecases/issues) issues if it specifically deals with use case.

### How to add a use case?

See [https://github.com/CLARIAH/usecases/blob/master/CONTRIBUTING.md](here) .

### How to raise an issue about a use case?

Open an issue on the [issue tracker for use cases](https://github.com/CLARIAH/usecases/issues)

### Can we organize our documents in a DropBox/GoogleDrive/SURFdrive?

No, please don't do that and keep them in the proper git repository instead to facilitate transparency. Otherwise we
would have documents or copies of documents all over the place and we don't know where to look to find them or whether
they are the proper latest version. Git is purposefully designed to solve this exact issue. The whole idea of using git
and github for the interest groups is to consolidate version control and have a single public entry point.

If you do have the document elsewhere, at least put a link to the document in the git repository (see next point).

### We have a document on Google Docs/Office 365, can we link to it?

Yes, you can link to the document from the git repository by adding simple markdown document to the git repository
that contains a link to the document on the external platform. (be aware not to share a link with public write
permissions in that case).

Preferably, you can export the document and put it in the git repository itself. But you will have to repeat the
procedure every time the document on the external platform changes. The version in git should always be authoritative.

### Can't we just mail documents around to participants?

No, this does not facilitate transparency, findability, reusability. Please use the repository and mail links to the
document in the repository if needed.

The notable exception here is when it concerns privacy-sensitive material, in that case the git repositories are **NOT**
suitable.

### Does everything have to be in Markdown format?

No, we recommend to do as much as possible in Markdown because it is a very simple and accessible text-based format with
almost no learning curve. It can be very easily visualised and easily converted to richer formats (like LaTeX, PDF). If
Markdown is not sufficient for your needs because you deal for example with complex spreadsheets, matrices and/or
large tables, or you're writing a journal/conference paper, then feel free to use other formats.

Our recommendation in this latter case is to use LaTeX, the tex sources and all required assets can be maintained in the git
repository without issue.

Regardless of the format you use, the most important thing is that the documents are committed to the git repository.
