# python-projects

Simple and Fun Python Projects

# Instructions to Sparse Checkout (Specific Folder)

```
path> git clone --file=blob:none --sparse https://github.com/darkcheftar/python-projects.git
path> cd python-projects
path> git sparse-checkout init --cone
path> git sparse-checkout add {specific_folder_name}
```
Instructions taken from this [video](https://www.youtube.com/watch?v=hAxCYmeZosE)
