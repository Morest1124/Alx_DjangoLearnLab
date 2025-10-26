
# Django Blog Comment System

This document provides an overview of the comment system implemented in the Django blog project.

## Features

*   Users can view comments on each blog post.
*   Authenticated users can add new comments to a blog post.
*   Authenticated users can edit their own comments.
*   Authenticated users can delete their own comments.

## How to Use

### 1. Viewing Comments

To view the comments on a blog post, simply navigate to the detail page of the post. The comments are displayed below the post content.

### 2. Adding a Comment

To add a comment, you must be logged in. If you are logged in, a form will be displayed below the comments section. Simply enter your comment in the text area and click the "Submit" button.

### 3. Editing a Comment

To edit a comment, you must be the author of the comment. If you are the author, you will see an "Edit" button next to your comment. Click this button to go to the edit page. On the edit page, you can modify your comment and click the "Update" button to save the changes.

### 4. Deleting a Comment

To delete a comment, you must be the author of the comment. If you are the author, you will see a "Delete" button next to your comment. Click this button to go to the delete confirmation page. Click the "Yes, Delete" button to permanently delete your comment.

## Permissions

*   Only authenticated users can add comments.
*   Only the author of a comment can edit or delete it.
