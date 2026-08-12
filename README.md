# 📋 Django Todo List Web Application

A clean, responsive task management web application built using **Django** and styled with **Bootstrap 5**. This project allows users to create, update, organize, and track tasks with customizable categorization tags, deadlines, and direct toggle features.

---

## 🚀 Key Features

- **Dynamic Task Tracking**: Quickly mark tasks as completed (`Complete` / `Undo`) with instant home page status updates.
- **Strict Chronological Ordering**: Tasks are automatically sorted with active (not done) tasks first, arranged from newest to oldest.
- **Tag Management Framework**: Full CRUD implementation for classification tags to cross-reference tasks.
- **HTML5 Native Datepickers**: Forms securely bind to native interactive browser calendars for selecting task deadlines.
- **Django Crispy Forms Integration**: Sleek form designs built using `crispy-bootstrap5` layouts.
- **Robust Automation Controls**: Complete pre-configured suite of structural unit tests to verify sorting logic and view switches.

---

## 📂 Project Architecture

```text
First/
│
├── core/                           # Application core workspace directory
│   ├── fixtures/                   # Seed data snapshots
│   │   └── seed_data.json
│   ├── templates/                  # Base templates folder
│   │   └── core/
│   │       ├── base.html           # Main sidebar frame layout template
│   │       ├── index.html          # Task board list view template
│   │       ├── tag_list.html       # Tag management board template
│   │       ├── task_form.html      # Create/Update task form template
│   │       └── tag_form.html       # Create/Update tag form template
│   ├── admin.py                    # Advanced admin display configurations
│   ├── forms.py                    # Form widget structures (HTML5 bindings)
│   ├── models.py                   # Data relationship mappings (ManyToMany)
│   ├── tests.py                    # Automated functional unit test assertions
│   ├── urls.py                     # App url mapping definitions
│   └── views.py                    # Class-Based CRUD logic wrappers
│
├── todo_project/                   # Global configuration core setup
│   ├── settings.py                 # Engine control profiles (Crispy setups)
│   └── urls.py                     # Main project URL router
│
└── manage.py                       # Project execution control management utility
```

---

## 🛠️ Step-by-Step Installation & Local Execution

Follow these steps to launch the application workspace locally:

### 1. Clone the Project Repository
```bash
git clone <your-repository-url>
cd todo_project
```

### 2. Configure Dependencies
Ensure you have Python installed, then install the required layout helper packages:
```bash
pip install django django-crispy-forms crispy-bootstrap5
```

### 3. Run Database Migrations
Generate and execute system layout schemas to build your local SQLite database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load Pre-Configured Mock Seed Data
Instantly populate your application boards with mock tasks and tags without writing them by hand:
```bash
python manage.py loaddata seed_data
```

### 5. Launch the Local Application Server
```bash
python manage.py runserver
```
Open your browser and navigate directly to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧪 Testing and Verification

Verify workspace component logic by running the automated unit test suite:
```bash
python manage.py test core
```

---

## 📌 Submission Checklist Requirements

Per project specifications, ensure you complete the following steps on GitHub:
1. Work within the **`dev` branch** (`git checkout -b dev`).
2. Open a **Pull Request (PR)** going from the `dev` branch into the `main` branch.
3. Take screenshots of your workspace screens (Home board, Tag views, creation menus).
4. **Drag-and-drop the interface images directly into the PR description body text block** (do not embed external hosting or cloud links).
5. Paste the final GitHub Pull Request link inside your assignment solution input box.

![Home page](images/home_page.png)
![Tags page](images/tags_page.png)
