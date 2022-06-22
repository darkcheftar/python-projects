# python-projects

Simple and Fun Python Projects

# Instructions to Sparse Checkout (Specific Folder)

```
git clone --filter=blob:none --sparse https://github.com/darkcheftar/python-projects.git
```
```
cd python-projects
```
```
git sparse-checkout init --cone
```
```
git sparse-checkout add {specific_folder_name}
```

Instructions taken from this [video](https://www.youtube.com/watch?v=hAxCYmeZosE)
