# GarnetPassX
A simple CV project to automate the Hostel Signout Form filling process for Garnet Hostels in NITT (2024-25).

## How to Automate Your Hostel Sign Out Form Process:

### Step 0 (Only for Windows)  
- Install **Python 3.12.x**: [Download Here](https://www.python.org/downloads/release/python-3129/)  
- Enable **"Add to Path"** option while installing.  

### Step 0.5  
- **Right-click this folder** and select **"Open in Terminal"**  

### Prerequisite  
- **Add your Signature with Date** (as `signature.jpg`) in this folder.  

---

## Terminal Commands:

### Step 1: Create a Virtual Environment  
```sh
python3 -m venv env
```

### Step 2: Activate Virtual Environment  
- **Windows:**  
  ```sh
  env\Scripts\activate
  ```
- **Linux:**  
  ```sh
  source env/bin/activate
  ```

### Step 3: Install Dependencies  
```sh
pip install -r requirements.txt
```

### Step 4: Run the Automation Script  
```sh
python3 hostel_form.py
```

### Step 5: Download the Generated Form  
- Go into the folder and download **`out.jpg`**  

---

🚀 **Enjoy Automated Sign-Out!**
