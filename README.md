# Azure Subscription Switcher  

Problem: Switching between azure subscriptions via Azure CLI involves multiple commands. 


## What is `azure-subscription-switcher`?

`azsub` is a CLI tool to interactively select Azure subscriptions using **`fzf`** fuzzy search. Inspired by [az-account-switcher](https://github.com/abij/az-account-switcher/pull/2/files) and [kubectx](https://github.com/ahmetb/kubectx)


## 📦 Installation

```sh
pip install azure-subscription-switcher
# Or using Poetry
poetry add azure-subscription-switcher
```

## 🚀 Usage

```sh
azsub
```
-OR-
```sh
azsub -s <subscription_id>
```

## 🛠 Requirements

- **Azure CLI (**`az`**)** must be installed and logged in.
- **`fzf` (fuzzy finder)** is required:
  - **Mac**: `brew install fzf`
  - **Linux**: `sudo apt install fzf`
  - **Windows**: Install via Git Bash or Chocolatey (`choco install fzf`).

## 🧰 Features

✅ Fetches available Azure subscriptions  
✅ Interactive fuzzy search for selection  
✅ Automatically switches to the selected subscription  
✅ Switches to the subscription passed with -s,--subscription  

## 🛠 Development & Contribution

1. Clone the repository:
   ```sh
   git clone https://github.com/LahiruSenevirathne/azure-subscription-switcher.git
   cd azure-subscription-switcher
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Run the CLI locally:
   ```sh
   poetry run azsub
   ```

## 🤝 Contributing

Pull requests are welcome! If you'd like to make improvements, please fork the repository and open a PR


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---


